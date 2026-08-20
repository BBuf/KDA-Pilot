#!/usr/bin/env python3
"""Carve a single-op task out of an existing multi-op package.

A package that defines seven or nine entry points asks one agent to optimise a whole
subsystem. This copies the mechanical parts of one op into a new task - its workload
rows, only the payload folders that belong to it, only the baseline sources it needs -
and leaves the prose (prompt.md, config.json, docs/) to be written for the new scope.

    python tools/split_task_op.py --from <task-dir> --op <op> --slug <new-slug> \
        --keep-source kernels/ops/attention/decode_attention.py \
        [--row-filter q=20x576] [--dry-run]

`--row-filter <arg>=<d1>x<d2>...` keeps only rows whose `<arg>` has those trailing
dimensions, which is how a package that captured two head geometries under one op name
becomes two coherent tasks.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import shutil


def row_matches(row: dict, filters: list) -> bool:
    for arg, dims in filters:
        spec = row["args"].get(arg)
        if not (isinstance(spec, dict) and "shape" in spec):
            return False
        if list(spec["shape"])[-len(dims):] != dims:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from", dest="source", required=True)
    parser.add_argument("--op", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--keep-source", action="append", default=[])
    parser.add_argument("--row-filter", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    filters = []
    for raw in args.row_filter:
        arg, _, dims = raw.partition("=")
        filters.append((arg, [int(d) for d in dims.split("x")]))

    out = args.slug
    plan = []
    kept_rows = 0
    for path in sorted(glob.glob(os.path.join(args.source, "bench", "workloads*.json"))):
        document = json.load(open(path, encoding="utf-8"))
        ops = []
        for entry in document["ops"]:
            if entry["op"] != args.op:
                continue
            rows = [r for r in entry["rows"] if row_matches(r, filters)]
            if rows:
                ops.append(dict(entry, rows=rows))
                kept_rows += len(rows)
        if not ops:
            continue
        document["ops"] = ops
        document["task"] = out
        document["selection_rule"] = (
            "%s  Carved out of %s by tools/split_task_op.py: one op, %s."
            % (document.get("selection_rule", ""), os.path.basename(args.source),
               "all recorded rows" if not filters
               else "rows whose " + ", ".join("%s ends %s" % (a, "x".join(map(str, d)))
                                              for a, d in filters)))
        plan.append(("workloads", path, os.path.join(out, "bench", os.path.basename(path)),
                     document))

    # Only the payloads a kept row can actually use. A package that captured two head
    # geometries under one op name ships payloads for both, and carrying the other
    # geometry's folders into this task leaves files that every row rejects on shape -
    # `payload_conflicts` is the same check the loader uses.
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
    from payload_match import payload_conflicts

    kept = [r for _, _, _, document in plan for entry in document["ops"] for r in entry["rows"]]

    payloads = []
    for root in glob.glob(os.path.join(args.source, "bench", "tensors*")):
        for base, _, files in os.walk(root):
            if "meta.json" not in files:
                continue
            parts = base.replace(root, "").strip(os.sep).split(os.sep)
            if not any(args.op in part for part in parts):
                continue
            # A chain lives in <folder>/stepNNN: copy the folder that owns the steps.
            top = base
            while os.path.basename(top).startswith("step"):
                top = os.path.dirname(top)
            if not any(not payload_conflicts(base, row) for row in kept):
                continue
            payloads.append(top)
    payloads = sorted(set(payloads))

    sources = []
    for relative in args.keep_source:
        src = os.path.join(args.source, "baseline", relative)
        if not os.path.exists(src):
            raise SystemExit("baseline source not in the package: %s" % relative)
        sources.append((src, os.path.join(out, "baseline", relative)))

    print("op %s -> %s: %d rows, %d payload folders, %d baseline sources"
          % (args.op, out, kept_rows, len(payloads), len(sources)))
    if args.dry_run:
        for folder in payloads:
            print("   payload %s" % os.path.relpath(folder, args.source))
        return

    for kind, _, destination, document in plan:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        with open(destination, "w", encoding="utf-8") as handle:
            json.dump(document, handle, indent=2)
            handle.write("\n")
        print("   wrote %s" % destination)
    for folder in payloads:
        relative = os.path.relpath(folder, os.path.join(args.source, "bench"))
        destination = os.path.join(out, "bench", relative)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copytree(folder, destination, dirs_exist_ok=True)
    print("   copied %d payload folders" % len(payloads))
    for src, destination in sources:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy2(src, destination)
    for extra in ("bench/target_signatures.json",):
        src = os.path.join(args.source, extra)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(out, extra))
    for placeholder in ("bench/.gitkeep", "docs/.gitkeep", "solution/.gitkeep"):
        path = os.path.join(out, placeholder)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "a").close()
    print("   copied %d baseline sources" % len(sources))


if __name__ == "__main__":
    main()
