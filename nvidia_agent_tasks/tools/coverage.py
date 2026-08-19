"""How much of each task's workload runs on real captured tensors?

    python tools/coverage.py [task ...]

For every row it matches the shipped payloads by tensor shape (the same rule
`workload.build_inputs` uses at run time) and reports, per op:

    rows            how many workload rows the task ships
    with payload    rows that find a payload folder
    real inputs     of the arguments that carry data, how many come from the capture
                    (weights and whole state/KV pools are excluded by design - the first
                     would mean shipping model weights, the second ships as the touched
                     rows; both are recorded as metadata)

A row with no payload runs on allocated tensors, which is exactly the situation the
anti-hack contract warns about: a Gaussian-shaped input can be satisfied by a shortcut.
"""

from __future__ import annotations

import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from payload_match import payload_conflicts  # noqa: E402  same rule the harness uses

# Not shipped by design, and recorded as metadata instead:
#   * weights - shipping them would mean shipping model weights (one 6016x7168 bf16 is 86 MB)
#   * whole state/KV pools - the touched rows ship instead (state_before_*/__rows)
NOT_SHIPPED = ("weight", "w_q_t", "w_k_t", "w_v_t", "w1", "w2", "kvcache", "freq", "freqs",
               "ssm_state", "conv_state", "k_buffer", "v_buffer", "initial_state")


def is_weighty(name: str) -> bool:
    n = name.replace("in_", "")
    return any(w in n for w in NOT_SHIPPED)


def payload_index(task: str) -> list:
    out = []
    for root in glob.glob(os.path.join(task, "bench", "tensors*")):
        for dirpath, _, files in os.walk(root):
            if "meta.json" not in files:
                continue
            meta = json.load(open(os.path.join(dirpath, "meta.json")))
            shapes = {k: tuple(v["shape"]) for k, v in meta.get("tensors", {}).items()}
            out.append((dirpath, meta.get("op"), shapes))
    return out


def report(task: str) -> dict:
    idx = payload_index(task)
    per_op = {}
    for wf in sorted(glob.glob(os.path.join(task, "bench", "workloads*.json"))):
        for o in json.load(open(wf))["ops"]:
            st = per_op.setdefault(o["op"], {"rows": 0, "with_payload": 0, "real": 0, "data_args": 0})
            for r in o["rows"]:
                st["rows"] += 1
                want = {k: tuple(v["shape"]) for k, v in r["args"].items()
                        if isinstance(v, dict) and "shape" in v}
                data_args = [k for k in want if not is_weighty(k)]
                best, best_hits = None, 0
                for dirpath, op, shapes in idx:
                    if op and op != o["op"]:
                        continue
                    if payload_conflicts(dirpath, r):
                        continue
                    hits = sum(1 for k in data_args if shapes.get("in_" + k) == want[k])
                    if hits > best_hits:
                        best, best_hits = dirpath, hits
                st["data_args"] += len(data_args)
                st["real"] += best_hits
                st["with_payload"] += 1 if best_hits else 0
    return per_op


def line(task: str, per_op: dict) -> str:
    """The one-line summary used by the CLI and by each task's bench/README.md."""
    rows = sum(v["rows"] for v in per_op.values())
    wp = sum(v["with_payload"] for v in per_op.values())
    real = sum(v["real"] for v in per_op.values())
    args = sum(v["data_args"] for v in per_op.values())
    return ("%-44s %3d rows, %3d with payload (%3.0f%%), %4d/%4d data args real (%3.0f%%)"
            % (os.path.basename(os.path.normpath(task)), rows, wp, 100 * wp / max(rows, 1),
               real, args, 100 * real / max(args, 1)))


def main() -> None:
    tasks = sys.argv[1:] or sorted(
        d for d in os.listdir(".")
        if os.path.isdir(d) and os.path.exists(os.path.join(d, "prompt.md")))
    grand = [0, 0, 0, 0]
    for t in tasks:
        per_op = report(t)
        rows = sum(v["rows"] for v in per_op.values())
        wp = sum(v["with_payload"] for v in per_op.values())
        real = sum(v["real"] for v in per_op.values())
        args = sum(v["data_args"] for v in per_op.values())
        grand = [grand[0] + rows, grand[1] + wp, grand[2] + real, grand[3] + args]
        print(line(t, per_op))
        for op, v in sorted(per_op.items(), key=lambda kv: -kv[1]["rows"]):
            print("      %-40s %3d rows  %3d payload  %4d/%4d args"
                  % (op, v["rows"], v["with_payload"], v["real"], v["data_args"]))
    print("\nTOTAL: %d rows, %d with payload (%.0f%%), %d/%d data args real (%.0f%%)"
          % (grand[0], grand[1], 100 * grand[1] / max(grand[0], 1), grand[2], grand[3],
             100 * grand[2] / max(grand[3], 1)))


if __name__ == "__main__":
    main()
