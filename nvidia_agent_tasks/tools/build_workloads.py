"""Turn a captured shape manifest into a task-local workload set.

    python build_workloads.py --manifest cap/<slug>_shapes/shape_manifest.json \
        --ops mamba2_chunk_scan_combined_fwd,causal_conv1d_prefill \
        --out <task>/bench/workloads.json --top 10

Selection rule (documented in the emitted file so a reviewer can re-derive it):

* every distinct call signature is ranked by real-traffic call count;
* the top ``--top`` signatures per op are kept;
* the smallest and largest signature by total input bytes are always kept, so a
  candidate kernel cannot be tuned for the mid-range only;
* one signature per capture group is kept, so every (sequence length x
  concurrency x dataset) operating point stays represented;
* warmup-only signatures are never kept - they come from start-up, CUDA-graph
  capture and autotuning, not from production traffic.
"""

from __future__ import annotations

import argparse
import json
import os


def _bytes_of(args: dict) -> int:
    n = 0
    for v in args.values():
        if isinstance(v, dict) and "bytes" in v:
            n += int(v["bytes"])
    return n


def select(rows: list, top: int) -> list:
    if not rows:
        return []
    ranked = sorted(rows, key=lambda r: -r["count"])
    keep, seen = [], set()

    def add(r, why):
        key = r["signature"]
        if key in seen:
            for k in keep:
                if k["signature"] == key and why not in k["kept_because"]:
                    k["kept_because"].append(why)
            return
        seen.add(key)
        rec = dict(r)
        rec["kept_because"] = [why]
        keep.append(rec)

    for r in ranked[:top]:
        add(r, "top-%d by call count" % top)
    by_bytes = sorted(rows, key=lambda r: _bytes_of(r["args"]))
    add(by_bytes[0], "smallest input footprint")
    add(by_bytes[-1], "largest input footprint")
    groups = {}
    for r in ranked:
        groups.setdefault(r["group"], r)
    for g, r in groups.items():
        add(r, "operating-point coverage: %s" % g)
    return keep


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--ops", default="", help="comma separated; default = all ops")
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--task", default="")
    ap.add_argument("--model", default="")
    ap.add_argument("--provenance", default="", help="path to capture_provenance.json to embed")
    args = ap.parse_args()

    man = json.load(open(args.manifest))
    real = man["real_workload_shapes"]
    want = [o for o in args.ops.split(",") if o]
    ops = {}
    for r in real:
        if want and r["op"] not in want:
            continue
        ops.setdefault(r["op"], []).append(r)

    out = {
        "task": args.task,
        "model": args.model,
        "source_manifest": os.path.basename(args.manifest),
        "selection_rule": (
            "top-%d signatures per op by real-traffic call count, plus the "
            "smallest and largest input footprint, plus one signature per "
            "capture group; warmup-only signatures excluded" % args.top),
        "ops": [],
    }
    if args.provenance and os.path.exists(args.provenance):
        out["capture_provenance"] = json.load(open(args.provenance))

    for op, rows in sorted(ops.items(), key=lambda kv: -sum(r["count"] for r in kv[1])):
        kept = select(rows, args.top)
        out["ops"].append({
            "op": op,
            "total_real_calls": sum(r["count"] for r in rows),
            "distinct_real_signatures": len(rows),
            "rows": [{
                "row_id": "%s#%02d" % (op, i),
                "group": k["group"],
                "real_calls": k["count"],
                "kept_because": k["kept_because"],
                "args": k["args"],
                "output": k["output"],
                "signature": k["signature"],
            } for i, k in enumerate(kept)],
        })

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=2)
    print("wrote %s: %d ops, %d rows"
          % (args.out, len(out["ops"]), sum(len(o["rows"]) for o in out["ops"])))


if __name__ == "__main__":
    main()
