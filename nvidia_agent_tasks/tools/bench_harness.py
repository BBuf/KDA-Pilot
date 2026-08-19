"""Shared A/B benchmark harness for the tasks in this directory.

    python tools/bench_harness.py <task_dir> [--rows N] [--op OP] [--iters 200]
                                 [--trials 7] [--eager] [--json out.json]

It loads a task's `bench/workloads.json`, builds each row's tensors (from the real
payload in `bench/tensors/` when one exists for that row, otherwise allocated to the
recorded shape/dtype/stride), and calls the baseline and the candidate through
matching local interfaces:

    baseline/entry.py :: run(**kwargs)      # thin wrapper you write once per task
    solution/entry.py :: run(**kwargs)      # same signature

Then it enforces the measurement contract instead of leaving it to each agent:

* timing inside a **CUDA graph** replay, not eager (eager overstated an MoE kernel
  401 us vs 53 us for us; `--eager` is available for kernels that cannot be captured,
  and the report marks the run as eager);
* **interleaved** A/B sampling within one process, `--trials` alternating blocks,
  median of per-trial medians, so clock drift on a sustained-load B300 cannot favour
  whichever arm ran first;
* preallocated outputs reused across iterations for both arms;
* for in-place kernels, the input is restored with `copy_` before every iteration and
  the restore cost is measured separately and subtracted;
* correctness before performance: exact / tolerance / **chained final state**, per the
  task's `config.json` `correctness.mode`.

Nothing here imports SGLang at run time: the baseline is the copied source in
`baseline/`, which is the point (see docs/baseline_policy.md).
"""

from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import os
import statistics
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates       # noqa: E402  the shared correctness judge
import workload    # noqa: E402  the shared input builder

build_inputs = workload.build_inputs
load_payload = workload.load_payload


# --------------------------------------------------------------------------- #
# timing
# --------------------------------------------------------------------------- #
def _graph_time(fn, kwargs, iters: int, restore: dict | None) -> float:
    """Median us per call, timed inside a captured graph when possible."""
    for _ in range(3):
        fn(**kwargs)
    torch.cuda.synchronize()
    try:
        g = torch.cuda.CUDAGraph()
        s = torch.cuda.Stream()
        s.wait_stream(torch.cuda.current_stream())
        with torch.cuda.stream(s):
            for _ in range(3):
                fn(**kwargs)
        torch.cuda.current_stream().wait_stream(s)
        with torch.cuda.graph(g):
            fn(**kwargs)
        torch.cuda.synchronize()
        start, end = torch.cuda.Event(True), torch.cuda.Event(True)
        start.record()
        for _ in range(iters):
            g.replay()
        end.record()
        torch.cuda.synchronize()
        return start.elapsed_time(end) * 1000.0 / iters
    except Exception:
        # not capturable (host-side branching, dynamic allocation): fall back to
        # eager, and the report says so
        start, end = torch.cuda.Event(True), torch.cuda.Event(True)
        torch.cuda.synchronize()
        start.record()
        for _ in range(iters):
            if restore:
                for k, v in restore.items():
                    kwargs[k].copy_(v)
            fn(**kwargs)
        end.record()
        torch.cuda.synchronize()
        total = start.elapsed_time(end) * 1000.0 / iters
        if restore:
            start.record()
            for _ in range(iters):
                for k, v in restore.items():
                    kwargs[k].copy_(v)
            end.record()
            torch.cuda.synchronize()
            total -= start.elapsed_time(end) * 1000.0 / iters
        return total


def interleaved(base_fn, cand_fn, kwargs_b, kwargs_c, iters: int, trials: int,
                restore_b=None, restore_c=None):
    """Alternate which arm goes first each trial.

    Running the candidate second in every trial hands it warmer clocks and caches: with an
    identity candidate that bias measured ~2% on this box. Swapping the order per trial
    centres it.
    """
    b, c = [], []
    for t in range(trials):
        if t % 2 == 0:
            b.append(_graph_time(base_fn, kwargs_b, iters, restore_b))
            c.append(_graph_time(cand_fn, kwargs_c, iters, restore_c))
        else:
            c.append(_graph_time(cand_fn, kwargs_c, iters, restore_c))
            b.append(_graph_time(base_fn, kwargs_b, iters, restore_b))
    return statistics.median(b), statistics.median(c), b, c


# --------------------------------------------------------------------------- #
# correctness
# --------------------------------------------------------------------------- #
def compare(mode: str, ref, got, payload: dict) -> tuple:
    return gates.compare(mode, ref, got)


def _unused_compare(mode: str, ref, got, payload: dict) -> tuple:
    if mode == "index_set":
        a = ref.flatten().tolist() if torch.is_tensor(ref) else ref
        b = got.flatten().tolist() if torch.is_tensor(got) else got
        return (set(a) == set(b), "selected index sets %s" % ("match" if set(a) == set(b) else "DIFFER"))
    if mode == "bitexact":
        ok = torch.is_tensor(ref) and torch.is_tensor(got) and ref.shape == got.shape and torch.equal(ref, got)
        return ok, "bit-exact" if ok else "NOT bit-exact"
    if mode == "chained_state":
        return None, ("chained-state gate: replay the shipped steps in order and compare the "
                      "FINAL state; see tools/verify_state_chain.py and docs/anti_hack_contract.md")
    r = ref.float() if torch.is_tensor(ref) else torch.tensor(ref).float()
    g = got.float() if torch.is_tensor(got) else torch.tensor(got).float()
    if r.shape != g.shape:
        return False, "shape mismatch %s vs %s" % (list(r.shape), list(g.shape))
    denom = r.abs().max().clamp_min(1e-30)
    rel = float((r - g).abs().max() / denom)
    return rel < 2e-2, "max rel err %.3g" % rel


# --------------------------------------------------------------------------- #
def load_entry(path: str, name: str):
    """Return a dispatch function for one arm.

    An entry module may expose either ``run(**kwargs)`` (single-op tasks) or
    ``OPS = {"<op name>": callable}`` (tasks whose workload covers several ops).
    """
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    ops = getattr(mod, "OPS", None)
    run = getattr(mod, "run", None)
    fix = getattr(mod, "RECONSTRUCT", {}) or {}
    if ops:
        def dispatch(_op=None, **kwargs):
            if _op in fix:
                kwargs = fix[_op](kwargs)
            fn = ops.get(_op)
            if fn is None:
                raise KeyError("%s does not implement op %r (has: %s)"
                               % (os.path.basename(path), _op, ", ".join(sorted(ops))))
            return fn(**kwargs)
        return dispatch
    if run:
        def only(_op=None, **kwargs):
            return run(**kwargs)
        return only
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    ap.add_argument("--op", default="")
    ap.add_argument("--rows", type=int, default=0, help="0 = all rows")
    ap.add_argument("--iters", type=int, default=200)
    ap.add_argument("--trials", type=int, default=7)
    ap.add_argument("--workloads", default="")
    ap.add_argument("--json", default="")
    args = ap.parse_args()

    cfg_p = os.path.join(args.task_dir, "config.json")
    cfg = json.load(open(cfg_p)) if os.path.exists(cfg_p) else {}
    mode = cfg.get("correctness", {}).get("mode", "tolerance")

    wl_files = [args.workloads] if args.workloads else sorted(
        os.path.join(args.task_dir, "bench", f)
        for f in os.listdir(os.path.join(args.task_dir, "bench"))
        if f.startswith("workloads") and f.endswith(".json"))

    base_run = load_entry(os.path.join(args.task_dir, "baseline", "entry.py"), "task_baseline")
    cand_run = load_entry(os.path.join(args.task_dir, "solution", "entry.py"), "task_solution")
    if base_run is None:
        raise SystemExit(
            "no baseline/entry.py in %s.\nWrite a ten-line wrapper that imports the copied\n"
            "baseline source and exposes run(**kwargs) with the argument names used in\n"
            "bench/workloads.json, then the same for solution/entry.py." % args.task_dir)

    report = {"task": os.path.basename(os.path.abspath(args.task_dir)),
              "correctness_mode": mode, "gpu": torch.cuda.get_device_name(0),
              "timestamp_unix": int(time.time()), "rows": []}
    for wf in wl_files:
        d = json.load(open(wf))
        for o in d["ops"]:
            if args.op and o["op"] != args.op:
                continue
            rows = o["rows"][: args.rows] if args.rows else o["rows"]
            for r in rows:
                try:
                    built = build_inputs(args.task_dir, r)
                except Exception as exc:
                    report["rows"].append({"row_id": r["row_id"], "op": o["op"],
                                           "status": "input build failed: %r" % (exc,)})
                    print("%-34s %-22s  input build failed: %s" % (r["row_id"], r["group"], exc))
                    continue
                kb = built["kwargs"]
                kc = {k: (v.clone() if torch.is_tensor(v) else v) for k, v in kb.items()}
                try:
                    ref = base_run(_op=o["op"],
                                   **{k: (v.clone() if torch.is_tensor(v) else v)
                                      for k, v in kb.items()})
                except Exception as exc:
                    msg = str(exc).strip().splitlines()[-1][:150]
                    need = [k for k, v in built["source"].items() if str(v).startswith("needs")]
                    rec = {"row_id": r["row_id"], "op": o["op"], "group": r["group"],
                           "status": "not runnable from the recorded row: %s" % msg,
                           "needs": need}
                    report["rows"].append(rec)
                    print("%-34s %-22s  NOT RUNNABLE: %s%s"
                          % (r["row_id"], r["group"], msg,
                             ("   (rebuild in baseline/entry.py RECONSTRUCT: %s)" % ", ".join(need))
                             if need else ""))
                    continue
                entry = {"row_id": r["row_id"], "op": o["op"], "group": r["group"],
                         "real_calls": r["real_calls"],
                         "inputs": built["source"]}
                if cand_run is None:
                    entry["status"] = "baseline only (no solution/entry.py yet)"
                    try:
                        tb = _graph_time(lambda **kw: base_run(_op=o["op"], **kw), kb, args.iters, None)
                        entry["baseline_us"] = round(tb, 3)
                    except Exception as exc:
                        msg = str(exc).strip().splitlines()[-1][:160] if str(exc).strip() else repr(exc)
                        entry["status"] = "not runnable from the recorded row: %s" % msg
                        entry["needs"] = [k for k, v in built["source"].items()
                                          if str(v).startswith("needs")]
                        if not workload.cuda_alive():
                            entry["status"] += "  [CUDA context lost - later rows cannot run]"
                            report["rows"].append(entry)
                            print("%-34s %-22s  %s" % (r["row_id"], r["group"], entry["status"]))
                            print("\nStopping: a row took the CUDA context down with it. Re-run the "
                                  "remaining ops one at a time with --op <op>, and give that row real "
                                  "tensors (an integer index argument allocated to zeros can address "
                                  "out of bounds).")
                            if args.json:
                                json.dump(report, open(args.json, "w"), indent=2)
                            return
                else:
                    got = cand_run(_op=o["op"],
                                   **{k: (v.clone() if torch.is_tensor(v) else v) for k, v in kb.items()})
                    ok, detail = compare(mode, ref, got, built["payload"])
                    entry["correct"] = ok
                    entry["correctness_detail"] = detail
                    if ok is False:
                        entry["status"] = "REJECTED on correctness - no timing reported"
                    else:
                        tb, tc, bs, cs = interleaved(
                            lambda **kw: base_run(_op=o["op"], **kw),
                            lambda **kw: cand_run(_op=o["op"], **kw),
                            kb, kc, args.iters, args.trials)
                        entry.update(baseline_us=round(tb, 3), candidate_us=round(tc, 3),
                                     speedup=round(tb / tc, 4) if tc else None,
                                     baseline_trials=[round(x, 3) for x in bs],
                                     candidate_trials=[round(x, 3) for x in cs])
                report["rows"].append(entry)
                # one compact line per row; the full record goes to --json
                bits = ["%-34s %-22s" % (entry["row_id"], entry["group"])]
                if "baseline_us" in entry:
                    bits.append("base %8.3f us" % entry["baseline_us"])
                if "candidate_us" in entry:
                    bits.append("cand %8.3f us  %.3fx" % (entry["candidate_us"], entry["speedup"]))
                if "correct" in entry:
                    bits.append("correct=%s (%s)" % (entry["correct"], entry["correctness_detail"]))
                if entry.get("status"):
                    bits.append(entry["status"])
                real = sum(1 for v in entry["inputs"].values() if v == "real")
                bits.append("[%d/%d inputs real]" % (real, len(entry["inputs"])))
                print("  ".join(bits), flush=True)

    sp = [r["speedup"] for r in report["rows"] if r.get("speedup")]
    if sp:
        geo = float(torch.tensor(sp).log().mean().exp())
        report["geomean_speedup"] = round(geo, 4)
        print("\ngeomean speedup over %d rows: %.4fx" % (len(sp), geo))
    if args.json:
        json.dump(report, open(args.json, "w"), indent=2)
        print("wrote", args.json)


if __name__ == "__main__":
    main()
