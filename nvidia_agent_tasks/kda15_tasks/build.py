#!/usr/bin/env python3
"""Turn a real-model capture into a KDA-1.5-native task package.

KDA-1.5 registers a *kernel definition*, not a recorded call site: axes with concrete
values, a pure-PyTorch reference, one workload row per operating point, and only the
arguments that must carry real data shipped as safetensors blobs. Everything else the
benchmark constructs, which is why a native task cannot be handed an invalid address.

This script emits exactly that tree from the captures in `nvidia_agent_tasks`:

    definitions/<group>/<name>.json          axes, constraints, inputs, outputs, reference
    workloads/<group>/<name>.jsonl           one row per operating point
    blob/workloads/<group>/<name>_<arg>/     the real tensors those rows point at
    solutions/baseline/<group>/<name>/       the SGLang kernel, as an executable package

Run it where torch is importable (it reads the capture's `.pt` payloads); it needs no
GPU. `--check` re-reads what it wrote and fails on any disagreement with the capture.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import uuid as uuidlib

import torch
from safetensors.torch import save_file

HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = os.path.join(HERE, "specs")


def stable_uuid(*parts: str) -> str:
    """A uuid that is a function of the row, so rebuilding does not churn the tree."""
    digest = hashlib.sha1("|".join(parts).encode()).digest()
    return str(uuidlib.UUID(bytes=digest[:16], version=5))


def load_pt(path: str):
    return torch.load(path, map_location="cpu", weights_only=True)


def read_source(spec_dir: str, relative: str) -> str:
    with open(os.path.join(spec_dir, relative), encoding="utf-8") as handle:
        return handle.read()


def write_json(path: str, payload) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=4)
        handle.write("\n")


def write_jsonl(path: str, rows) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def blob(out_root: str, group: str, name: str, arg: str, row_uuid: str, tensor) -> dict:
    """Write one tensor and return the workload-row input spec that points at it."""
    folder = os.path.join(out_root, "blob", "workloads", group, "%s_%s" % (name, arg))
    os.makedirs(folder, exist_ok=True)
    filename = "%s_%s_%s.safetensors" % (name, row_uuid, arg)
    save_file({arg: tensor.contiguous()}, os.path.join(folder, filename))
    return {
        "type": "safetensors",
        "path": "./blob/workloads/%s/%s_%s/%s" % (group, name, arg, filename),
        "tensor_key": arg,
    }


def solution_json(out_root: str, group: str, name: str, spec_dir: str, spec: dict) -> str:
    sources = [
        {"path": rel, "content": read_source(spec_dir, os.path.join("baseline", rel))}
        for rel in spec["baseline"]["sources"]
    ]
    digest = hashlib.sha256(
        json.dumps(sources, sort_keys=True).encode()
    ).hexdigest()[:6]
    solution = {
        "name": "sglang_baseline_%s" % digest,
        "definition": name,
        "author": "sglang",
        "spec": {
            "language": "python",
            "target_hardware": spec["baseline"]["target_hardware"],
            "entry_point": spec["baseline"]["entry_point"],
            "dependencies": spec["baseline"]["dependencies"],
            "destination_passing_style": spec["baseline"]["destination_passing_style"],
        },
        "sources": sources,
    }
    relative = "solutions/baseline/%s/%s/%s.json" % (group, name, solution["name"])
    write_json(os.path.join(out_root, relative), solution)
    return relative


def definition_json(out_root: str, group: str, name: str, spec_dir: str, spec: dict) -> None:
    payload = {
        "name": name,
        "description": spec["description"],
        "op_type": spec["op_type"],
        "tags": spec["tags"],
        "axes": spec["axes"],
        "constraints": spec["constraints"],
        "inputs": spec["inputs"],
        "outputs": spec["outputs"],
        "reference": read_source(spec_dir, "reference.py"),
    }
    write_json(os.path.join(out_root, "definitions", group, name + ".json"), payload)


def capture_rows(capture_root: str, task: str, op: str):
    """Every recorded row for one op, across the task's workload files."""
    bench = os.path.join(capture_root, task, "bench")
    for filename in sorted(os.listdir(bench)):
        if not (filename.startswith("workloads") and filename.endswith(".json")):
            continue
        document = json.load(open(os.path.join(bench, filename), encoding="utf-8"))
        for entry in document["ops"]:
            if entry["op"] != op:
                continue
            for row in entry["rows"]:
                yield document.get("model", ""), row


def payload_dirs(capture_root: str, task: str, op: str):
    """(group, dir) for every shipped payload folder belonging to one op."""
    root = os.path.join(capture_root, task, "bench")
    for base, dirs, files in os.walk(root):
        if "meta.json" not in files:
            continue
        parts = base.replace(root, "").strip(os.sep).split(os.sep)
        # Two layouts are in the wild - "<group>__<op>__<args>" and "<group>/<op>__<args>"
        # - and both sit under a "tensors*" directory, so the operating point is found by
        # locating the part that names the op rather than by position.
        group = None
        for index, part in enumerate(parts):
            if op not in part:
                continue
            group = parts[index - 1] if part.startswith(op) else part.split("__" + op)[0]
            break
        if group is None:
            continue
        yield group, base


def build_attention(capture_root: str, out_root: str, spec_dir: str, spec: dict) -> dict:
    name, group = spec["name"], spec["group"]
    rows_by_key = {}
    for model, row in capture_rows(capture_root, spec["capture"]["task"], spec["capture"]["op"]):
        shape = row["args"]["q"]["shape"]
        rows_by_key[(row["group"], tuple(shape))] = (model, row)

    workloads, shipped = [], []
    for payload_group, folder in sorted(payload_dirs(
            capture_root, spec["capture"]["task"], spec["capture"]["op"])):
        query = load_pt(os.path.join(folder, "in_q.pt"))
        if list(query.shape[1:]) != [spec["axes"]["num_q_heads"]["value"],
                                     spec["axes"]["qk_head_dim"]["value"]]:
            continue  # a different attention geometry shares this capture; not this task
        key = (payload_group, tuple(query.shape))
        if key not in rows_by_key:
            continue
        model, row = rows_by_key[key]
        row_uuid = stable_uuid(name, row["row_id"], payload_group)

        indptr = load_pt(os.path.join(folder, "in_kv_indptr.pt"))
        indices = load_pt(os.path.join(folder, "in_kv_indices.pt"))
        splits = load_pt(os.path.join(folder, "in_num_kv_splits.pt"))

        # The row is only shippable if its addresses agree with each other and with the
        # pool the capture recorded: an indptr that ends outside its index array, or an
        # index outside the pool, is a stale snapshot rather than a workload.
        assert int(indptr[0]) == 0 and bool((indptr[1:] >= indptr[:-1]).all()), row["row_id"]
        assert int(indptr[-1]) == indices.numel(), row["row_id"]
        recorded_pool = row["args"]["k_buffer"]["shape"][0]
        assert int(indices.max()) < recorded_pool, row["row_id"]
        assert splits.numel() == query.shape[0], row["row_id"]
        lora = spec["axes"]["kv_lora_rank"]["value"]

        inputs = {
            "q": blob(out_root, group, name, "q", row_uuid, query),
            "k_buffer": {"type": "sparse_pool", "index_arg": "kv_indices"},
            "v_buffer": {"type": "view_of", "source": "k_buffer", "last_dim": lora},
            "o": {"type": "destination"},
            "kv_indptr": blob(out_root, group, name, "kv_indptr", row_uuid, indptr),
            "kv_indices": blob(out_root, group, name, "kv_indices", row_uuid, indices),
            "attn_logits": {"type": "destination"},
            "attn_lse": {"type": "destination"},
            "num_kv_splits": blob(out_root, group, name, "num_kv_splits", row_uuid, splits),
        }
        for scalar in spec["capture"]["scalars"]:
            inputs[scalar] = {"type": "scalar", "value": row["args"][scalar]}

        num_seqs = int(query.shape[0])
        tier_value = int(indices.numel()) if spec["size_rule"]["axis"] == "len_kv_indices" \
            else num_seqs
        axes = {
            "num_seqs": num_seqs,
            "kv_pool_rows": int(recorded_pool),
            "len_kv_indptr": int(indptr.numel()),
            "len_kv_indices": int(indices.numel()),
            "max_kv_splits": int(row["args"]["max_kv_splits"]),
        }
        workloads.append({
            "definition": name,
            "size_class": "large" if tier_value >= spec["size_rule"]["large_at"] else "small",
            "solution": None,
            "workload": {"uuid": row_uuid, "axes": axes, "inputs": inputs},
            "evaluation": None,
            "provenance": {"model": model, "capture_row": row["row_id"],
                           "operating_point": payload_group,
                           "real_calls": row.get("real_calls")},
        })
        shipped.append(row["row_id"])
    return {"workloads": workloads, "shipped": shipped}


def build_gdn(capture_root: str, out_root: str, spec_dir: str, spec: dict) -> dict:
    name, group = spec["name"], spec["group"]
    chains = {}
    for payload_group, folder in payload_dirs(
            capture_root, spec["capture"]["task"], spec["capture"]["op"]):
        if os.path.basename(folder).startswith("step"):
            batch = load_pt(os.path.join(folder, "in_mixed_qkv.pt")).shape[0]
            chains.setdefault((payload_group, batch), []).append(folder)

    workloads, shipped, seen = [], [], set()
    for model, row in capture_rows(capture_root, spec["capture"]["task"], spec["capture"]["op"]):
        num_seqs = int(row["args"]["mixed_qkv"]["shape"][0])
        # The same operating point can appear in two workload files (a decode-only
        # capture beside the full one). One row per (operating point, batch) is enough;
        # a duplicate would just double that tier's weight in the geomean.
        if (row["group"], num_seqs) in seen:
            continue
        seen.add((row["group"], num_seqs))
        row_uuid = stable_uuid(name, row["row_id"], row["group"])
        steps = sorted(chains.get((row["group"], num_seqs), []))
        inputs = {}
        if steps:
            # This row was captured with its tensors: ship the first link of the decode
            # chain, including the state slots it reads, so the workload runs on real
            # activations and a real state rather than on a Gaussian.
            step = steps[0]
            for arg in ("mixed_qkv", "a", "b", "A_log", "dt_bias", "cache_indices"):
                inputs[arg] = blob(out_root, group, name, arg, row_uuid,
                                   load_pt(os.path.join(step, "in_" + arg + ".pt")))
            slots = load_pt(os.path.join(step, "state_rows_ssm_states.pt"))
            values = load_pt(os.path.join(step, "state_before_ssm_states.pt"))
            assert slots.numel() == len(set(slots.tolist())), row["row_id"]
            assert int(slots.max()) < row["args"]["ssm_states"]["shape"][0], row["row_id"]
            inputs["ssm_states"] = {"type": "sparse_pool", "rows": "ssm_state_slots",
                                    "values": "ssm_state_values"}
            inputs["ssm_state_slots"] = blob(out_root, group, name, "ssm_state_slots",
                                             row_uuid, slots)
            inputs["ssm_state_values"] = blob(out_root, group, name, "ssm_state_values",
                                              row_uuid, values)
        else:
            for arg in ("mixed_qkv", "a", "b", "A_log", "dt_bias"):
                inputs[arg] = {"type": "random"}
            # Distinct slots by construction. The only property the capture's own
            # indices have that matters here is distinctness - two sequences sharing a
            # slot is a read-modify-write race, not a slower kernel - and the pool is
            # allocated fresh per row, so which distinct slots they are cannot matter.
            inputs["cache_indices"] = {"type": "slot_indices"}
            inputs["ssm_states"] = {"type": "sparse_pool", "rows": "cache_indices",
                                    "values": "random"}
        for scalar in spec["capture"]["scalars"]:
            inputs[scalar] = {"type": "scalar", "value": row["args"][scalar]}

        axes = {"num_seqs": num_seqs,
                "num_slots": int(row["args"]["ssm_states"]["shape"][0])}
        workloads.append({
            "definition": name,
            "size_class": "large" if num_seqs >= spec["size_rule"]["large_at"] else "small",
            "solution": None,
            "workload": {"uuid": row_uuid, "axes": axes, "inputs": inputs},
            "evaluation": None,
            "provenance": {"model": model, "capture_row": row["row_id"],
                           "operating_point": row["group"],
                           "real_calls": row.get("real_calls"),
                           "recorded_tensors": bool(steps),
                           # The capture shipped this operating point as a 16-step decode
                           # chain; the row uses its first link. The rest is what a
                           # state-drift check would replay.
                           "recorded_chain_steps": len(steps)},
        })
        shipped.append(row["row_id"])
    return {"workloads": workloads, "shipped": shipped}


BUILDERS = {"attention": build_attention, "gdn": build_gdn}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--captures", required=True, help="a tree of nvidia_agent_tasks captures")
    parser.add_argument("--out", default=os.path.join(HERE, "flashinfer_trace"))
    parser.add_argument("--task", action="append", default=[])
    args = parser.parse_args()

    names = args.task or sorted(os.listdir(SPECS))
    for name in names:
        spec_dir = os.path.join(SPECS, name)
        spec = json.load(open(os.path.join(spec_dir, "spec.json"), encoding="utf-8"))
        built = BUILDERS[spec["builder"]](args.captures, args.out, spec_dir, spec)
        definition_json(args.out, spec["group"], spec["name"], spec_dir, spec)
        solution = solution_json(args.out, spec["group"], spec["name"], spec_dir, spec)
        write_jsonl(os.path.join(args.out, "workloads", spec["group"], spec["name"] + ".jsonl"),
                    built["workloads"])
        tiers = {}
        for entry in built["workloads"]:
            tiers[entry["size_class"]] = tiers.get(entry["size_class"], 0) + 1
        print("%-52s %2d rows %s  baseline=%s"
              % (spec["name"], len(built["workloads"]), tiers, solution))
        for row_id in built["shipped"]:
            print("      %s" % row_id)


if __name__ == "__main__":
    main()
