"""Same-process interleaved A/B/C module-level benchmark for the continuation round.

Legs (all module-level, i.e. the raw tvm-ffi kernel entry, no python dispatch):
  A = SGLang baseline kernel module (from the pinned checkout on PYTHONPATH)
  B = incumbent candidate build (RKD/src_incumbent, pristine promoted source)
  C = variant candidate build   (RKD/src, the source under evaluation)

The three legs run in the same process on the same tensors, with the leg order rotated
across three blocks (A,B,C / C,A,B / B,C,A) so slow drift (clocks, thermals) cancels.
q/k are reset from pristine copies outside the timed region; CUDA events time each call.

Env: RKD (session dir), KDA_TAG, KDA_ITERS (total per leg, split across 3 blocks),
KDA_WARMUP (per leg per block), KDA_HOST, KDA_IDLE_BEFORE/AFTER (external readings).
Appends rows to RKD/benchmark.csv (level=module): one row set tagged "<TAG>" with
baseline=incumbent vs candidate=variant (the decision signal), and one tagged
"<TAG>-vs-sglang" with baseline=SGLang vs candidate=variant. Writes
RKD/abc_summary_<TAG>.json with per-shape medians and geomeans.
"""

import csv
import datetime
import hashlib
import importlib.util
import json
import math
import os
import statistics
import subprocess
import sys

RKD = os.environ["RKD"]

import torch  # noqa: E402

from sglang.jit_kernel.diffusion.qknorm_rope import _jit_qknorm_rope_module as up_mod_fn  # noqa: E402


def load_wrapper(subdir, modname):
    path = os.path.join(RKD, subdir, "wrapper.py")
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod
    spec.loader.exec_module(mod)
    return mod


B_DIR = os.environ.get("KDA_B_DIR", "src_incumbent")  # the reference build the variant must beat
wrap_inc = load_wrapper(B_DIR, "wrapper_incumbent")
wrap_var = load_wrapper("src", "wrapper_variant")

dev = "cuda"
GPU_NAME = torch.cuda.get_device_name(0)
GPU_PHYS = os.environ.get("CUDA_VISIBLE_DEVICES", "0")
HOST = os.environ.get("KDA_HOST", "ion8-h200")
TAG = os.environ.get("KDA_TAG", "abc")
ITERS = int(os.environ.get("KDA_ITERS", "300"))
WARMUP = int(os.environ.get("KDA_WARMUP", "10"))
ITERS_PER_BLOCK = max(1, ITERS // 3)

SHA_INC = hashlib.sha256(open(os.path.join(RKD, "src_incumbent/csrc/qknorm_rope_kernel.cuh"), "rb").read()).hexdigest()[:16]
SHA_VAR = hashlib.sha256(open(os.path.join(RKD, "src/csrc/qknorm_rope_kernel.cuh"), "rb").read()).hexdigest()[:16]
COMMAND = (
    f"CUDA_VISIBLE_DEVICES={GPU_PHYS} KDA_TAG={TAG} KDA_WARMUP={WARMUP} KDA_ITERS={ITERS} "
    f"PYTHONPATH={os.environ.get('PYTHONPATH', '')} python bench_abc.py  # @ REMOTE_KDA_DIR"
)

CAPTURED = [
    ("qwen_t4096", 4096, 24, 1e-6),
    ("qwen_t19", 19, 24, 1e-6),
    ("qwen_t47", 47, 24, 1e-6),
    ("qwenedit_t8424", 8424, 24, 1e-6),
    ("qwenedit_t195", 195, 24, 1e-6),
    ("qwenedit_t189", 189, 24, 1e-6),
    ("zimage_t4096", 4096, 30, 1e-5),
    ("zimage_t32", 32, 30, 1e-5),
    ("zimage_t4128", 4128, 30, 1e-5),
]
D = R = 128


def gpu_idle():
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits", "-i", GPU_PHYS],
            text=True, timeout=15).strip()
        return f"util={out.split(',')[0].strip()}% mem={out.split(',')[1].strip()}MiB"
    except Exception as exc:  # pragma: no cover - diagnostics only
        return f"n/a ({exc})"


def build(tokens, heads):
    gen = torch.Generator(device="cpu").manual_seed(tokens * 131 + heads)
    q = torch.randn(tokens, heads, D, generator=gen, dtype=torch.bfloat16).to(dev)
    k = torch.randn(tokens, heads, D, generator=gen, dtype=torch.bfloat16).to(dev)
    qw = torch.randn(D, generator=gen, dtype=torch.bfloat16).to(dev)
    kw = torch.randn(D, generator=gen, dtype=torch.bfloat16).to(dev)
    inv = 1.0 / (10000.0 ** (torch.arange(0, R, 2, device=dev, dtype=torch.float32) / R))
    tt = torch.arange(tokens, device=dev, dtype=torch.float32)
    csc = torch.cat([torch.outer(tt, inv).cos(), torch.outer(tt, inv).sin()], dim=-1)
    pos = torch.arange(tokens, device=dev, dtype=torch.int64)
    return q, k, qw, kw, csc, pos


def st(samples):
    ordered = sorted(samples)

    def pct(p):
        return ordered[min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))]

    return dict(median=statistics.median(ordered), mean=statistics.mean(ordered),
                std=(statistics.pstdev(ordered) if len(ordered) > 1 else 0.0),
                min=ordered[0], p10=pct(.1), p90=pct(.9))


def timed(call, reset, warmup, iters):
    for _ in range(warmup):
        reset(); call()
    torch.cuda.synchronize()
    ev0 = torch.cuda.Event(enable_timing=True)
    ev1 = torch.cuda.Event(enable_timing=True)
    out = []
    for _ in range(iters):
        reset(); torch.cuda.synchronize()
        ev0.record(); call(); ev1.record(); torch.cuda.synchronize()
        out.append(ev0.elapsed_time(ev1) * 1000.0)
    return out


def geomean(values):
    return math.exp(sum(math.log(v) for v in values) / len(values))


# Pre-build all three JIT modules so compile/load never lands in a timed region.
mod_a = up_mod_fn(128, 128, False, torch.bfloat16)
mod_b = wrap_inc._candidate_module(128, 128, False, torch.bfloat16)
mod_c = wrap_var._candidate_module(128, 128, False, torch.bfloat16)
torch.cuda.synchronize()

idle_before = os.environ.get("KDA_IDLE_BEFORE") or gpu_idle()
ts = datetime.datetime.now(datetime.timezone.utc).isoformat()

BLOCK_ORDERS = [["A", "B", "C"], ["C", "A", "B"], ["B", "C", "A"]]

rows = []
per_shape = {}
for name, tokens, heads, eps in CAPTURED:
    q, k, qw, kw, csc, pos = build(tokens, heads)
    q0, k0 = q.clone(), k.clone()

    def reset():
        q.copy_(q0); k.copy_(k0)

    calls = {
        "A": lambda: mod_a.qknorm_rope(q, k, qw, kw, csc, pos, eps),
        "B": lambda: mod_b.qknorm_rope(q, k, qw, kw, csc, pos, eps),
        "C": lambda: mod_c.qknorm_rope(q, k, qw, kw, csc, pos, eps),
    }
    samples = {"A": [], "B": [], "C": []}
    for order in BLOCK_ORDERS:
        for leg in order:
            samples[leg] += timed(calls[leg], reset, WARMUP, ITERS_PER_BLOCK)

    stats = {leg: st(samples[leg]) for leg in "ABC"}
    med = {leg: stats[leg]["median"] for leg in "ABC"}
    ratios = {
        "inc_vs_sglang": med["A"] / med["B"],
        "var_vs_sglang": med["A"] / med["C"],
        "var_vs_inc": med["B"] / med["C"],
    }
    per_shape[name] = {"median_us": med, "ratios": ratios, "tokens": tokens}
    rows.append((name, tokens, heads, eps, stats, med, ratios))
    print(
        f"{name:16s} A={med['A']:7.2f} B={med['B']:7.2f} C={med['C']:7.2f}"
        f" | var/inc={ratios['var_vs_inc']:.4f} var/sgl={ratios['var_vs_sglang']:.4f}"
        f" inc/sgl={ratios['inc_vs_sglang']:.4f}",
        flush=True,
    )

torch.cuda.synchronize()
idle_after = os.environ.get("KDA_IDLE_AFTER") or "PENDING_EXTERNAL"

g_all = {key: geomean([per_shape[n]["ratios"][key] for n in per_shape]) for key in
         ("inc_vs_sglang", "var_vs_sglang", "var_vs_inc")}
large = [n for n in per_shape if per_shape[n]["tokens"] >= 4096]
g_large = {key: geomean([per_shape[n]["ratios"][key] for n in large]) for key in
           ("inc_vs_sglang", "var_vs_sglang", "var_vs_inc")}

csv_path = os.path.join(RKD, "benchmark.csv")
newfile = (not os.path.exists(csv_path)) or os.path.getsize(csv_path) == 0
with open(csv_path, "a", newline="") as fh:
    writer = csv.writer(fh)
    if newfile:
        writer.writerow(["utc", "host", "gpu_id", "gpu_model", "level", "shape", "tokens", "heads", "eps",
                         "baseline_median_us", "candidate_median_us", "speedup_x", "baseline_full", "candidate_full",
                         "iters", "warmup", "cand_src_sha16", "tag", "command", "gpu_idle_before", "gpu_idle_after"])
    for name, tokens, heads, eps, stats, med, ratios in rows:
        writer.writerow([ts, HOST, GPU_PHYS, GPU_NAME, "module", name, tokens, heads, eps,
                         f"{med['B']:.3f}", f"{med['C']:.3f}", f"{ratios['var_vs_inc']:.4f}",
                         json.dumps(stats["B"]), json.dumps(stats["C"]),
                         ITERS, WARMUP, SHA_VAR, TAG, COMMAND, idle_before, idle_after])
        writer.writerow([ts, HOST, GPU_PHYS, GPU_NAME, "module", name, tokens, heads, eps,
                         f"{med['A']:.3f}", f"{med['C']:.3f}", f"{ratios['var_vs_sglang']:.4f}",
                         json.dumps(stats["A"]), json.dumps(stats["C"]),
                         ITERS, WARMUP, SHA_VAR, f"{TAG}-vs-sglang", COMMAND, idle_before, idle_after])

print(f"GEOMEAN all-9: var/inc={g_all['var_vs_inc']:.4f} var/sgl={g_all['var_vs_sglang']:.4f} "
      f"inc/sgl={g_all['inc_vs_sglang']:.4f}")
print(f"GEOMEAN large(T>=4096): var/inc={g_large['var_vs_inc']:.4f} var/sgl={g_large['var_vs_sglang']:.4f} "
      f"inc/sgl={g_large['inc_vs_sglang']:.4f}")
print(f"shas: incumbent={SHA_INC} variant={SHA_VAR}")
print(f"GPU idle before={idle_before} after={idle_after}")

json.dump({"utc": ts, "tag": TAG, "sha_incumbent": SHA_INC, "sha_variant": SHA_VAR,
           "geomean_all": g_all, "geomean_large": g_large, "per_shape": per_shape,
           "iters": ITERS, "warmup_per_block": WARMUP, "blocks": BLOCK_ORDERS,
           "gpu": GPU_NAME, "gpu_id": GPU_PHYS, "host": HOST, "command": COMMAND,
           "gpu_idle_before": idle_before, "gpu_idle_after": idle_after},
          open(os.path.join(RKD, f"abc_summary_{TAG}.json"), "w"), indent=2)
