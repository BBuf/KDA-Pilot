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
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from payload_match import payload_conflicts  # noqa: E402  shared with the run-time harness


def _bytes_of(args: dict) -> int:
    n = 0
    for v in args.values():
        if isinstance(v, dict) and "bytes" in v:
            n += int(v["bytes"])
    return n


def _row_inputs(r: dict) -> dict:
    return {"in_" + k: tuple(v["shape"]) for k, v in r["args"].items()
            if isinstance(v, dict) and "shape" in v}


def _payload_hits(r: dict, payloads: list) -> int:
    """How many of this row's inputs a shipped payload can supply.

    A payload whose folder name records shapes that contradict this row is skipped, not
    scored: when the large tensors were too big to ship, two calls of very different
    sequence length match equally well on their small arguments, and the row would then
    silently run on another call's segment arrays. Same rule as `tools/payload_match.py`
    uses at run time.
    """
    want = _row_inputs(r)
    best = 0
    for path, shapes in payloads or []:
        if payload_conflicts(path, r):
            continue
        hits = sum(1 for k, sh in shapes.items() if want.get(k) == sh)
        best = max(best, hits)
    return best


def select(rows: list, top: int, with_payload: set = None, max_unbacked: int = 0) -> list:
    if not rows:
        return []
    if with_payload:
        # a row whose tensors we actually captured is worth more than a row we would have
        # to invent inputs for: rank by how much of it is real, then by call count
        ranked = sorted(rows, key=lambda r: (-_payload_hits(r, with_payload), -r["count"]))
    else:
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
    if max_unbacked:
        # A row with no payload of its own runs on tensors allocated to its shape. Those
        # rows still carry a real production shape, but they cannot show a candidate what
        # the real distribution looks like - so keep only a few of them per op, and keep
        # the ones that widen the shape range (smallest / largest footprint) first.
        backed = [r for r in keep if _payload_hits(r, with_payload)]
        unbacked = [r for r in keep if not _payload_hits(r, with_payload)]
        unbacked.sort(key=lambda r: (0 if any("footprint" in w for w in r["kept_because"]) else 1,
                                     -r["count"]))
        order = {id(r): i for i, r in enumerate(keep)}
        keep = sorted(backed + unbacked[:max_unbacked], key=lambda r: order[id(r)])
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
    ap.add_argument("--max-unbacked", type=int, default=0,
                    help="cap the rows per op that have no payload of their own (0 = no cap)")
    ap.add_argument("--payloads", default="",
                    help="tensors dir from the SAME capture: rows that have a payload are "
                         "kept first, so every shipped row runs on real tensors")
    args = ap.parse_args()

    man = json.load(open(args.manifest))
    have_payload = {}
    if args.payloads and os.path.isdir(args.payloads):
        import glob as _glob
        for meta_p in _glob.glob(os.path.join(args.payloads, "**", "meta.json"), recursive=True):
            meta = json.load(open(meta_p))
            # the same rule tools/workload.py uses at run time: a payload matches a row
            # when its input tensors agree on shape; oversized inputs (weights, pools) are
            # metadata in the payload and simply do not participate
            shapes = {k: tuple(v["shape"]) for k, v in meta.get("tensors", {}).items()
                      if k.startswith("in_")}
            have_payload.setdefault(meta.get("op"), []).append(
                (os.path.dirname(meta_p), shapes))
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
        kept = select(rows, args.top, have_payload.get(op), args.max_unbacked)
        out["ops"].append({
            "op": op,
            "total_real_calls": sum(r["count"] for r in rows),
            "distinct_real_signatures": len(rows),
            "rows_with_payload": sum(1 for k in kept if _payload_hits(k, have_payload.get(op))),
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
