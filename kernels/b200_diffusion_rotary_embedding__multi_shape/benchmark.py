#!/usr/bin/env python3
"""Benchmark harness for ``b200_diffusion_rotary_embedding__multi_shape``.

Parent/worker split so the idle evidence is trustworthy:
  * The PARENT validates GPU idleness with nvidia-smi BEFORE any CUDA work,
    spawns a `--worker` child, and — only after that child has fully exited —
    validates idleness AGAIN. Because the CUDA process is gone, the after-check
    genuinely shows `n_compute_procs=0`. The parent refuses to record promotion
    evidence unless both before and after pass the idle gate.
  * The WORKER imports CUDA, builds the cases, times all 11 signatures with CUDA
    events (median latency), and writes the timing rows to a temp JSON file.

Run inside the sglang_bbuf container on a verified-idle B200:
    CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --warmup 50 --iters 300 --candidate cuda-v4
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import os
import socket
import statistics
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_DIR = Path(__file__).resolve().parent


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    assert spec is not None and spec.loader is not None, test_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git_short_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=str(KERNEL_DIR), text=True
        ).strip()
    except Exception:
        return "nogit"


def _candidate_version() -> str:
    spec = importlib.util.spec_from_file_location(
        "kda_diffrope_wrapper_ver", str(KERNEL_DIR / "src" / "wrapper.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return f"src={module._SRC_HASH} pdl={module.USE_PDL}"


def _gpu_state(gpu_id: str) -> dict:
    """Query nvidia-smi for the physical GPU: utilization, memory, compute procs."""
    try:
        u = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits", "-i", str(gpu_id)],
            text=True,
        ).strip()
        procs = subprocess.check_output(
            ["nvidia-smi", "--query-compute-apps=pid,used_memory", "--format=csv,noheader,nounits", "-i", str(gpu_id)],
            text=True,
        ).strip()
        util, mem = (x.strip() for x in u.split(","))
        n = len([ln for ln in procs.splitlines() if ln.strip()])
        return {"util_pct": int(float(util)), "mem_used_mib": int(float(mem)), "n_compute_procs": n,
                "procs": procs.replace("\n", "|") or "none"}
    except Exception as e:  # pragma: no cover
        return {"error": repr(e)}


def _is_idle(state: dict) -> bool:
    # Idle == no compute process, <=2 GiB resident, <=10% util on the target GPU.
    if "error" in state:
        return False
    return state["n_compute_procs"] == 0 and state["mem_used_mib"] <= 2048 and state["util_pct"] <= 10


def _event_time(fn: Callable[[dict[str, Any]], Any], case: dict[str, Any], *, warmup: int, iters: int) -> list[float]:
    for _ in range(warmup):
        fn(case)
    torch.cuda.synchronize()
    starts = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    ends = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    for i in range(iters):
        starts[i].record()
        fn(case)
        ends[i].record()
    torch.cuda.synchronize()
    return [starts[i].elapsed_time(ends[i]) * 1000.0 for i in range(iters)]  # ms -> us


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[index]

    return {
        "median_us": statistics.median(ordered),
        "mean_us": statistics.mean(ordered),
        "std_us": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min_us": ordered[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
    }


def _geom_mean(values: list[float]) -> float:
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    if not cleaned:
        return float("nan")
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned))


def _load_compare_exports(src_dir: str):
    """Load a second wrapper module (e.g. a snapshot of the promoted candidate's
    src/) so two candidate generations can be timed in the SAME process through
    the identical wrapper/dispatch ABI. The wrapper resolves its csrc/ next to
    its own file, and its jit module name embeds that source hash, so the two
    builds never collide."""
    wrapper_py = Path(src_dir).resolve() / "wrapper.py"
    spec = importlib.util.spec_from_file_location("kda_diffrope_compare_wrapper", wrapper_py)
    assert spec is not None and spec.loader is not None, wrapper_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run_worker(tmp_path: str, warmup: int, iters: int, compare_src: str = "", sglang_path: str = "") -> int:
    """CUDA work happens in this child process; it exits before the parent's after-idle check."""
    if sglang_path:
        # Resolve `import sglang` (baseline kernels AND the jit build stack) from an
        # explicit checkout -- e.g. a task-owned worktree of sglang MAIN -- so the
        # recorded command alone pins the baseline source, independent of whatever
        # the container's default checkout happens to be.
        sys.path.insert(0, os.path.abspath(sglang_path))
    correctness = _load_correctness_module()
    cases = correctness.make_cases()
    if not cases:
        json.dump({"error": "no benchmark cases (need CUDA)"}, open(tmp_path, "w"))
        return 1
    compare_mod = _load_compare_exports(compare_src) if compare_src else None

    def compare_fn(case):
        return compare_mod.EXPORTS[case["entry"]](*case["args"])

    rows = []
    speedups = []
    cmp_speedups = []
    for case in cases:
        w = int(case.get("warmup", warmup))
        it = int(case.get("iters", iters))
        b = _summary(_event_time(correctness.baseline, case, warmup=w, iters=it))
        a = _summary(_event_time(compare_fn, case, warmup=w, iters=it)) if compare_mod else None
        c = _summary(_event_time(correctness.candidate, case, warmup=w, iters=it))
        sp = (b["median_us"] / c["median_us"]) if c["median_us"] > 0 else float("nan")
        speedups.append(sp)
        row = {"name": case["name"], "b": b, "c": c, "speedup": sp, "iters": it}
        if a is not None:
            csp = (a["median_us"] / c["median_us"]) if c["median_us"] > 0 else float("nan")
            cmp_speedups.append(csp)
            row["a"] = a
            row["speedup_vs_compare"] = csp
        rows.append(row)
    out = {
        "rows": rows,
        "geomean": _geom_mean(speedups),
        "gpu_model": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
    }
    if compare_mod is not None:
        out["geomean_vs_compare"] = _geom_mean(cmp_speedups)
        out["compare_version"] = f"src={compare_mod._SRC_HASH} pdl={compare_mod.USE_PDL}"
    json.dump(out, open(tmp_path, "w"))
    return 0


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--warmup", type=int, default=50)
    ap.add_argument("--iters", type=int, default=300)
    ap.add_argument("--candidate", type=str, default="cuda-v4", help="candidate id recorded in the CSV")
    ap.add_argument("--host", type=str, default="")
    ap.add_argument("--allow-busy", action="store_true", help="skip the idle-gate (NOT for promotion evidence)")
    ap.add_argument("--compare-src", type=str, default="",
                    help="path to an alternate src/ dir (e.g. a snapshot of the promoted candidate); "
                         "adds a third timing leg through the identical wrapper ABI in the same process")
    ap.add_argument("--compare-label", type=str, default="compare",
                    help="id recorded for the --compare-src leg (e.g. cuda-v4)")
    ap.add_argument("--sglang-path", type=str, default="",
                    help="python/ dir of an explicit sglang checkout (e.g. a task-owned worktree "
                         "of sglang MAIN) used for the baseline kernels and the jit build stack")
    ap.add_argument("--worker", action="store_true", help="internal: CUDA timing child process")
    ap.add_argument("--tmp", type=str, default="", help="internal: worker results path")
    args = ap.parse_args()

    if args.worker:
        return _run_worker(args.tmp, args.warmup, args.iters, compare_src=args.compare_src, sglang_path=args.sglang_path)

    # -------- parent: owns idle validation + CSV; never initializes CUDA --------
    visible = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    gpu_id = visible.split(",")[0] if visible else "0"

    pre = _gpu_state(gpu_id)
    if not args.allow_busy and not _is_idle(pre):
        raise SystemExit(f"GPU {gpu_id} not idle BEFORE run (refusing to benchmark): {pre}")

    tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False, dir=str(KERNEL_DIR))
    tmp.close()
    cmd = [
        sys.executable, os.path.abspath(__file__), "--worker", "--tmp", tmp.name,
        "--warmup", str(args.warmup), "--iters", str(args.iters), "--candidate", args.candidate,
    ]
    if args.compare_src:
        cmd += ["--compare-src", args.compare_src]
    if args.sglang_path:
        cmd += ["--sglang-path", args.sglang_path]
    rc = subprocess.run(cmd).returncode
    try:
        with open(tmp.name) as fh:
            data = json.load(fh)
    except Exception as e:
        data = {"error": f"could not read worker results: {e!r}"}
    finally:
        if os.path.exists(tmp.name):
            os.unlink(tmp.name)
    if rc != 0 or "rows" not in data:
        raise SystemExit(f"worker failed (rc={rc}): {data}")

    time.sleep(3)  # let the GPU settle after the CUDA worker process has exited
    post = _gpu_state(gpu_id)
    if not args.allow_busy and not _is_idle(post):
        raise SystemExit(
            f"GPU {gpu_id} not idle AFTER the worker exited (refusing to record promotion evidence): {post}"
        )

    host = args.host or socket.gethostname()
    gpu_model = data.get("gpu_model", "?")
    version = _candidate_version()
    sha = _git_short_sha()
    ver_id = f"git_sha={sha}" if sha != "nogit" else "git_sha=N/A(copied-dir); version-id=source-hash"
    cmdstr = f"CUDA_VISIBLE_DEVICES={visible} python benchmark.py --warmup {args.warmup} --iters {args.iters} --candidate {args.candidate}"
    if args.compare_src:
        # exact-command provenance: the paired rows must be reproducible verbatim
        cmdstr += f" --compare-src {args.compare_src} --compare-label {args.compare_label}"
    if args.sglang_path:
        cmdstr += f" --sglang-path {args.sglang_path}"
    prov = f"host={host} gpu_id={gpu_id} gpu={gpu_model} {ver_id} {version} cmd='{cmdstr}'"

    csv_path = KERNEL_DIR / "benchmark.csv"
    with csv_path.open("a", newline="") as f:
        wr = csv.writer(f)
        wr.writerow([_now(), args.candidate, "idle_check_before", "nvidia_smi", "", "", "", f"gpu_id={gpu_id} idle={_is_idle(pre)} {pre}"])
        for r in data["rows"]:
            b, c, sp = r["b"], r["c"], r["speedup"]
            wr.writerow([
                _now(), args.candidate, r["name"], "median_us",
                f"{b['median_us']:.4f}", f"{c['median_us']:.4f}",
                f"{sp:.4f}x" if math.isfinite(sp) else "",
                (
                    f"base[mean={b['mean_us']:.3f} std={b['std_us']:.3f} min={b['min_us']:.3f} "
                    f"p10={b['p10_us']:.3f} p90={b['p90_us']:.3f}] "
                    f"cand[mean={c['mean_us']:.3f} std={c['std_us']:.3f} min={c['min_us']:.3f} "
                    f"p10={c['p10_us']:.3f} p90={c['p90_us']:.3f}] iters={r['iters']} {prov}"
                ),
            ])
            print(f"{r['name']}: base={b['median_us']:.2f}us cand={c['median_us']:.2f}us speedup={sp:.4f}x")
        geo = data["geomean"]
        wr.writerow([_now(), args.candidate, "geomean_11_unique_signatures", "geomean_speedup_x", "", "", f"{geo:.4f}x", f"n={len(data['rows'])} {prov}"])
        # Paired-comparison rows: base columns carry the --compare-src leg (e.g. the
        # promoted cuda-v4 snapshot), cand columns the current candidate. Same
        # process, same case tensors, identical wrapper ABI on both legs.
        if args.compare_src and any("a" in r for r in data["rows"]):
            cmp_prov = f"compare[{data.get('compare_version', '?')} dir={args.compare_src}] {prov}"
            pair_label = f"{args.candidate}_vs_{args.compare_label}"
            for r in data["rows"]:
                if "a" not in r:
                    continue
                a, c, csp = r["a"], r["c"], r["speedup_vs_compare"]
                wr.writerow([
                    _now(), pair_label, r["name"], "median_us",
                    f"{a['median_us']:.4f}", f"{c['median_us']:.4f}",
                    f"{csp:.4f}x" if math.isfinite(csp) else "",
                    (
                        f"cmp[mean={a['mean_us']:.3f} std={a['std_us']:.3f} min={a['min_us']:.3f} "
                        f"p10={a['p10_us']:.3f} p90={a['p90_us']:.3f}] "
                        f"cand[mean={c['mean_us']:.3f} std={c['std_us']:.3f} min={c['min_us']:.3f} "
                        f"p10={c['p10_us']:.3f} p90={c['p90_us']:.3f}] iters={r['iters']} {cmp_prov}"
                    ),
                ])
                print(f"{r['name']}: {args.compare_label}={a['median_us']:.2f}us cand={c['median_us']:.2f}us vs_compare={csp:.4f}x")
            cgeo = data.get("geomean_vs_compare", float("nan"))
            wr.writerow([_now(), pair_label, "geomean_11_unique_signatures", "geomean_speedup_x", "", "", f"{cgeo:.4f}x", f"n={len(data['rows'])} {cmp_prov}"])
            print(f"GEOMEAN_VS_{args.compare_label.upper()} {cgeo:.4f}x")
        wr.writerow([_now(), args.candidate, "idle_check_after", "nvidia_smi", "", "", "", f"gpu_id={gpu_id} idle={_is_idle(post)} {post}"])
    print(f"GEOMEAN {geo:.4f}x | idle_before={_is_idle(pre)} {pre} | idle_after={_is_idle(post)} {post}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
