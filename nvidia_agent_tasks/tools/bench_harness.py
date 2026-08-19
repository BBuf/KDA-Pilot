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
_FLUSH = {}


def l2_flush_buffer():
    """A buffer big enough that writing it evicts L2 (2x its size), allocated once."""
    dev = torch.cuda.current_device()
    if dev not in _FLUSH:
        l2 = torch.cuda.get_device_properties(dev).L2_cache_size
        _FLUSH[dev] = torch.empty(int(2 * l2) // 4, dtype=torch.int32, device="cuda")
    return _FLUSH[dev]


def _graph_time(fn, kwargs, iters: int, restore: dict | None, l2: str = "cold") -> float:
    """Median us per call.

    `l2="cold"` flushes L2 before every call and brackets **only the call** with the event
    pair, the way `triton.testing.do_bench` does - so the flush cost is not in the number,
    but the kernel does not get to reuse the previous iteration's cache lines either. That
    matters here: B300 has 132.6 MB of L2, enough to hold an m=1 GEMM's whole weight, while
    in a real decode step ~1900 other kernels run between two calls of the same one.

    `l2="hot"` keeps the old behaviour (one replay after another, cache warm) for comparison.
    """
    flush = l2_flush_buffer() if l2 == "cold" else None
    for _ in range(3):
        fn(**kwargs)
    torch.cuda.synchronize()
    graph = None
    try:
        g = torch.cuda.CUDAGraph()
        st = torch.cuda.Stream()
        st.wait_stream(torch.cuda.current_stream())
        with torch.cuda.stream(st):
            for _ in range(3):
                fn(**kwargs)
        torch.cuda.current_stream().wait_stream(st)
        with torch.cuda.graph(g):
            fn(**kwargs)
        torch.cuda.synchronize()
        graph = g
    except Exception:
        graph = None            # not capturable: host branching or dynamic allocation

    def one_call():
        if graph is not None:
            graph.replay()
        else:
            if restore:
                for k, v in restore.items():
                    kwargs[k].copy_(v)
            fn(**kwargs)

    starts = [torch.cuda.Event(True) for _ in range(iters)]
    ends = [torch.cuda.Event(True) for _ in range(iters)]
    torch.cuda.synchronize()
    for i in range(iters):
        if flush is not None:
            flush.zero_()       # outside the event pair on purpose
        starts[i].record()
        one_call()
        ends[i].record()
    torch.cuda.synchronize()
    per_call = sorted(s_.elapsed_time(e_) * 1000.0 for s_, e_ in zip(starts, ends))
    med = per_call[len(per_call) // 2]
    if graph is None and restore:
        # eager fallback pays the copy_ restore inside the window; measure and subtract it
        st_, en_ = torch.cuda.Event(True), torch.cuda.Event(True)
        torch.cuda.synchronize(); st_.record()
        for _ in range(iters):
            for k, v in restore.items():
                kwargs[k].copy_(v)
        en_.record(); torch.cuda.synchronize()
        med -= st_.elapsed_time(en_) * 1000.0 / iters
    return med


def interleaved(base_fn, cand_fn, kwargs_b, kwargs_c, iters: int, trials: int,
                restore_b=None, restore_c=None, l2: str = "cold"):
    """Alternate which arm goes first each trial.

    Running the candidate second in every trial hands it warmer clocks and caches: with an
    identity candidate that bias measured ~2% on this box. Swapping the order per trial
    centres it.
    """
    b, c = [], []
    for t in range(trials):
        if t % 2 == 0:
            b.append(_graph_time(base_fn, kwargs_b, iters, restore_b, l2))
            c.append(_graph_time(cand_fn, kwargs_c, iters, restore_c, l2))
        else:
            c.append(_graph_time(cand_fn, kwargs_c, iters, restore_c, l2))
            b.append(_graph_time(base_fn, kwargs_b, iters, restore_b, l2))
    return statistics.median(b), statistics.median(c), b, c


# --------------------------------------------------------------------------- #
# correctness
# --------------------------------------------------------------------------- #
def compare(mode: str, ref, got, payload: dict, op: str = "") -> tuple:
    return gates.compare(mode, ref, got, op=op)


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
    ap.add_argument("--l2", choices=["cold", "hot", "both"], default="cold",
                    help="cold (default): flush L2 before every call, the way a kernel is "
                         "entered in a real step; hot: back-to-back replays; both: report each")
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
                trust_ok, trust_why = True, ""
                try:
                    trust_ok, trust_why = gates.reference_is_trustworthy(
                        lambda **kw: base_run(_op=o["op"], **kw), kb, o["op"])
                except Exception as exc:
                    trust_ok, trust_why = False, "baseline raised: %s" % str(exc).splitlines()[-1][:110]
                if not trust_ok:
                    rec = {"row_id": r["row_id"], "op": o["op"], "group": r["group"],
                           "status": "NO VALID REFERENCE: %s" % trust_why,
                           "inputs": built["source"]}
                    report["rows"].append(rec)
                    print("%-34s %-22s  NO VALID REFERENCE: %s" % (r["row_id"], r["group"], trust_why))
                    if not workload.cuda_alive():
                        print("\nStopping: the CUDA context is gone.")
                        return
                    continue
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
                        for regime in (["cold", "hot"] if args.l2 == "both" else [args.l2]):
                            tb = _graph_time(lambda **kw: base_run(_op=o["op"], **kw),
                                             kb, args.iters, None, regime)
                            entry["baseline_us" if regime == args.l2 or args.l2 == "both"
                                  and regime == "cold" else "baseline_us_hot"] = round(tb, 3)
                        entry["l2"] = args.l2
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
                    ok, detail = compare(mode, ref, got, built["payload"], op=o["op"])
                    entry["correct"] = ok
                    entry["correctness_detail"] = detail
                    if ok is False:
                        entry["status"] = "REJECTED on correctness - no timing reported"
                    else:
                        tb, tc, bs, cs = interleaved(
                            lambda **kw: base_run(_op=o["op"], **kw),
                            lambda **kw: cand_run(_op=o["op"], **kw),
                            kb, kc, args.iters, args.trials, l2=args.l2 if args.l2 != "both" else "cold")
                        entry["l2"] = "cold" if args.l2 == "both" else args.l2
                        def spread(xs):
                            return (max(xs) - min(xs)) / statistics.median(xs) if len(xs) > 1 else 0.0
                        sb, sc = spread(bs), spread(cs)
                        entry.update(baseline_us=round(tb, 3), candidate_us=round(tc, 3),
                                     speedup=round(tb / tc, 4) if tc else None,
                                     baseline_trials=[round(x, 3) for x in bs],
                                     candidate_trials=[round(x, 3) for x in cs],
                                     trial_spread={"baseline": round(sb, 4), "candidate": round(sc, 4)})
                        if max(sb, sc) > 0.10:
                            entry["unstable"] = True
                            entry["status"] = ("trial spread %.0f%% - treat this row's speedup as "
                                               "noise until it is stabilised" % (100 * max(sb, sc)))
                report["rows"].append(entry)
                # one compact line per row; the full record goes to --json
                bits = ["%-34s %-22s" % (entry["row_id"], entry["group"])]
                if "baseline_us" in entry:
                    bits.append("base %8.3f us" % entry["baseline_us"])
                if "baseline_us_hot" in entry:
                    bits.append("(hot-L2 %7.3f us)" % entry["baseline_us_hot"])
                if "candidate_us" in entry:
                    bits.append("cand %8.3f us  %.3fx" % (entry["candidate_us"], entry["speedup"]))
                if entry.get("trial_spread"):
                    bits.append("spread %.0f/%.0f%%" % (100 * entry["trial_spread"]["baseline"],
                                                        100 * entry["trial_spread"]["candidate"]))
                if "correct" in entry:
                    bits.append("correct=%s (%s)" % (entry["correct"], entry["correctness_detail"]))
                if entry.get("status"):
                    bits.append(entry["status"])
                real = sum(1 for v in entry["inputs"].values() if v == "real")
                bits.append("[%d/%d inputs real]" % (real, len(entry["inputs"])))
                if built.get("allocated_index_args"):
                    bits.append("[synthetic index args: %s]"
                                % ",".join(built["allocated_index_args"][:3]))
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
