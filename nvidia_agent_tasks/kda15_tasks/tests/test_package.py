#!/usr/bin/env python3
"""CPU checks on the generated tree: run before shipping, no GPU and no SGLang.

Every check here is one that a hand-edited workload file has broken before: a row whose
axes disagree with the blob it points at, a blob path that does not resolve, a size
class that contradicts the declared rule, an input the definition never declared.
"""

from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRACE = os.environ.get("KDA15_TRACE", os.path.join(HERE, "..", "flashinfer_trace"))

EXPECTED = {
    "glm47_mla_decode_grouped_h20_ckv512_kpe64": {
        "group": "attention",
        "tier_axis": "len_kv_indices",
        "large_at": 8192,
        "blob_args": ("q", "kv_indptr", "kv_indices", "num_kv_splits"),
    },
    "qwen3next_gdn_packed_decode_hv4_d128": {
        "group": "gdn",
        "tier_axis": "num_seqs",
        "large_at": 8,
        "blob_args": (),
    },
}


def failures():
    try:
        from safetensors import safe_open
    except ModuleNotFoundError:  # path checks still run; shape checks need the reader
        safe_open = None
        print("note: safetensors is not installed, so blob shapes are not checked")

    problems = []
    for name, expected in EXPECTED.items():
        group = expected["group"]
        definition = json.load(open(
            os.path.join(TRACE, "definitions", group, name + ".json"), encoding="utf-8"))
        assert definition["name"] == name
        declared = set(definition["inputs"])
        consts = {axis: spec["value"] for axis, spec in definition["axes"].items()
                  if spec["type"] == "const"}
        if "run(" not in definition["reference"]:
            problems.append("%s: the definition ships no reference entry point" % name)

        rows = [json.loads(line) for line in open(
            os.path.join(TRACE, "workloads", group, name + ".jsonl"), encoding="utf-8")]
        if not rows:
            problems.append("%s: no workload rows" % name)
        seen_uuid = set()
        tiers = {"small": 0, "large": 0}
        for row in rows:
            workload = row["workload"]
            uuid = workload["uuid"]
            if uuid in seen_uuid:
                problems.append("%s: duplicate workload uuid %s" % (name, uuid))
            seen_uuid.add(uuid)
            tiers[row["size_class"]] = tiers.get(row["size_class"], 0) + 1

            tier_value = workload["axes"].get(expected["tier_axis"])
            if tier_value is None:
                problems.append("%s/%s: no %s axis to classify on"
                                % (name, uuid, expected["tier_axis"]))
            else:
                want = "large" if tier_value >= expected["large_at"] else "small"
                if row["size_class"] != want:
                    problems.append("%s/%s: size_class %s but %s=%s says %s"
                                    % (name, uuid, row["size_class"],
                                       expected["tier_axis"], tier_value, want))

            for arg, spec in workload["inputs"].items():
                if arg not in declared and not arg.endswith(("_rows", "_slots", "_values")):
                    problems.append("%s/%s: input %r is not declared by the definition"
                                    % (name, uuid, arg))
                if not isinstance(spec, dict) or spec.get("type") != "safetensors":
                    continue
                path = os.path.join(TRACE, spec["path"].lstrip("./"))
                if not os.path.exists(path):
                    problems.append("%s/%s: blob for %s does not resolve: %s"
                                    % (name, uuid, arg, spec["path"]))
                    continue
                if safe_open is None:
                    continue
                with safe_open(path, framework="pt") as handle:
                    if spec["tensor_key"] not in handle.keys():
                        problems.append("%s/%s: blob for %s has no key %r"
                                        % (name, uuid, arg, spec["tensor_key"]))
                        continue
                    shape = handle.get_slice(spec["tensor_key"]).get_shape()
                # The row's axes have to describe the tensor it points at, or the
                # benchmark allocates one geometry and reads another.
                declared_shape = definition["inputs"].get(arg, {}).get("shape")
                if not declared_shape:
                    continue
                for position, axis in enumerate(declared_shape):
                    if isinstance(axis, int):
                        wanted = axis
                    elif axis in consts:
                        wanted = consts[axis]
                    else:
                        wanted = workload["axes"].get(axis)
                    if wanted is not None and shape[position] != wanted:
                        problems.append(
                            "%s/%s: %s dim %d is %d, axes say %s=%s"
                            % (name, uuid, arg, position, shape[position], axis, wanted))
            for arg in expected["blob_args"]:
                if workload["inputs"].get(arg, {}).get("type") != "safetensors":
                    problems.append("%s/%s: %s must come from the capture, not a draw"
                                    % (name, uuid, arg))

        solutions = os.listdir(
            os.path.join(TRACE, "solutions/baseline", group, name))
        if len(solutions) != 1:
            problems.append("%s: expected one baseline package, found %s" % (name, solutions))
        print("%-46s %2d rows  small=%d large=%d  baseline=%s"
              % (name, len(rows), tiers["small"], tiers["large"], solutions[0]))
    return problems


if __name__ == "__main__":
    found = failures()
    for problem in found:
        print("FAIL " + problem)
    print("\n%s" % ("every check passed" if not found else "%d problems" % len(found)))
    sys.exit(1 if found else 0)
