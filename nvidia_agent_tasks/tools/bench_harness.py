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

DTYPES = {
    "bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32,
    "float64": torch.float64, "int64": torch.int64, "int32": torch.int32,
    "int16": torch.int16, "int8": torch.int8, "uint8": torch.uint8, "bool": torch.bool,
    "float8_e4m3fn": getattr(torch, "float8_e4m3fn", torch.uint8),
    "complex64": torch.complex64,
}


# --------------------------------------------------------------------------- #
# building a row's inputs
# --------------------------------------------------------------------------- #
def _alloc(info: dict, device: str = "cuda") -> torch.Tensor:
    dt = DTYPES.get(info["dtype"], torch.float32)
    shape = tuple(info["shape"])
    if dt.is_floating_point:
        t = torch.randn(shape, device=device, dtype=torch.float32).to(dt)
    elif dt == torch.bool:
        t = torch.zeros(shape, device=device, dtype=dt)
    elif dt.is_complex:
        t = torch.randn(shape, device=device, dtype=torch.float32).to(torch.complex64)
    else:
        t = torch.zeros(shape, device=device, dtype=dt)
    stride = info.get("stride")
    if stride and not info.get("contiguous", True):
        # reproduce a non-contiguous view over a larger buffer, because several of
        # these kernels really are fed slices of a fused buffer
        try:
            numel = 1
            for s, st in zip(shape, stride):
                numel = max(numel, (s - 1) * st + 1)
            base = torch.zeros(numel, device=device, dtype=dt)
            base[: t.numel()] = t.reshape(-1)[: min(numel, t.numel())]
            t = base.as_strided(shape, tuple(stride))
        except Exception:
            pass
    return t


def _row_shapes(row: dict) -> dict:
    return {k: tuple(v["shape"]) for k, v in row["args"].items()
            if isinstance(v, dict) and "shape" in v}


def load_payload(task_dir: str, row: dict) -> dict:
    """Real tensors for this row: the payload folder whose shapes match it.

    Matching matters - a task ships several payload folders and the wrong one silently
    feeds a candidate the wrong shapes.
    """
    roots = [d for d in glob.glob(os.path.join(task_dir, "bench", "tensors*")) if os.path.isdir(d)]
    if not roots:
        return {}
    want = row.get("payload_dir")
    cands = []
    for root in roots:
        if want and os.path.isdir(os.path.join(root, want)):
            cands.append(os.path.join(root, want))
        for grp in sorted(os.listdir(root)):
            gp = os.path.join(root, grp)
            if not os.path.isdir(gp):
                continue
            if os.path.exists(os.path.join(gp, "meta.json")) or glob.glob(os.path.join(gp, "step*")):
                cands.append(gp)
            for sd in sorted(os.listdir(gp)):
                p = os.path.join(gp, sd)
                if os.path.isdir(p):
                    cands.append(p)
    want_shapes = _row_shapes(row)
    scored = []
    for c in cands:
        meta_p = os.path.join(c, "meta.json")
        if not os.path.exists(meta_p):
            sub = sorted(d for d in os.listdir(c) if d.startswith("step")) if os.path.isdir(c) else []
            if sub:
                meta_p = os.path.join(c, sub[0], "meta.json")
        if not os.path.exists(meta_p):
            continue
        meta = json.load(open(meta_p))
        base = os.path.dirname(meta_p)
        got = {}
        for name, info in meta["tensors"].items():
            f = os.path.join(base, info["file"])
            if os.path.exists(f):
                got[name] = torch.load(f, map_location="cuda")
        if not got:
            continue
        score = sum(1 for k, sh in want_shapes.items()
                    if torch.is_tensor(got.get("in_" + k)) and tuple(got["in_" + k].shape) == sh)
        got["__meta__"] = meta
        got["__dir__"] = c
        scored.append((score, c, got))
    if not scored:
        return {}
    scored.sort(key=lambda x: -x[0])
    best_score, best_dir, best = scored[0]
    if best_score == 0:
        return {}
    return best


def _holds_tensor_meta(x) -> bool:
    if isinstance(x, dict):
        if "shape" in x and "dtype" in x:
            return True
        return any(_holds_tensor_meta(v) for v in x.values())
    if isinstance(x, list):
        return any(_holds_tensor_meta(v) for v in x)
    return False


def build_inputs(task_dir: str, row: dict) -> dict:
    payload = load_payload(task_dir, row)
    kwargs, source = {}, {}
    for name, info in row["args"].items():
        if isinstance(info, dict) and "shape" in info:
            real = payload.get("in_" + name)
            if real is not None and list(real.shape) == list(info["shape"]):
                kwargs[name] = real.clone()
                source[name] = "real"
            else:
                kwargs[name] = _alloc(info)
                source[name] = "allocated"
        elif isinstance(info, dict) and "repr" in info:
            # an object the capture could not serialize (a triton dtype, a plan struct).
            # baseline/entry.py's RECONSTRUCT hook is where a task rebuilds it.
            source[name] = "needs RECONSTRUCT (%s)" % info["repr"]
        elif isinstance(info, (dict, list)) and _holds_tensor_meta(info):
            # e.g. a plan / namedtuple whose fields include tensors: the capture recorded
            # their metadata, not the object. RECONSTRUCT rebuilds it.
            source[name] = "needs RECONSTRUCT (structured arg with tensors)"
        elif isinstance(info, dict):
            kwargs[name] = info          # plain config dict of scalars
            source[name] = "config"
        elif isinstance(info, list):
            kwargs[name] = info
            source[name] = "list"
        else:
            kwargs[name] = info
            source[name] = "scalar"
    return {"kwargs": kwargs, "source": source, "payload": payload}


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
    b, c = [], []
    for _ in range(trials):
        b.append(_graph_time(base_fn, kwargs_b, iters, restore_b))
        c.append(_graph_time(cand_fn, kwargs_c, iters, restore_c))
    return statistics.median(b), statistics.median(c), b, c


# --------------------------------------------------------------------------- #
# correctness
# --------------------------------------------------------------------------- #
def compare(mode: str, ref, got, payload: dict) -> tuple:
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
