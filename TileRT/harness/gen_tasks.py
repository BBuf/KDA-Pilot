"""Generate KDA task directories from the kernel registry (B1/B2/B6).

For each kernel in kernel_registry.REGISTRY, emits a task dir:
  kernels/b200_tilert_<k>/
    prompt.md         problem + shapes + TileRT ref + design levers (B6)
    config.toml       task meta + [reference] (B5 numbers filled by measure step)
    README.md
    bench/workloads.json   full (seq x ct) shape coverage from SASS (B2)
    bench/adapter.py       baseline/candidate ABI
    bench/correctness.py   candidate-vs-baseline per shape (B3)

baseline/<k>.py (golden_forward port) is written separately per op (validated by
the oracle). Existing hand-authored tasks (the original 4) are NOT clobbered
unless listed in --force.

Usage:  python gen_tasks.py [--only k1,k2] [--force k1,k2] [--dry]
"""
import argparse
import json
import os

from kernel_registry import REGISTRY, CT_NAME, mtp_note, MEASURED, INGRAPH

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KDIR = os.path.join(ROOT, "kernels")

LEVER_TXT = {
    "L1": "**Tile-level overlap (warp specialization + mbarrier double-buffer, §4/§13):** "
          "Prefetcher warps stream weights/acts GMEM->SMEM via TMA while Consumer warps run "
          "warpgroup MMA; an mbarrier ring overlaps tile t+1 load with tile t compute.",
    "L2": "**No-GMEM intermediates (§13.3):** keep intermediate activations in SMEM/TMEM "
          "across the fused stages; only the final result is written to GMEM.",
    "L3": "**Weight read once + occupancy=1 persistent grid (§4):** 148 CTAs (=SM count), "
          "1 CTA/SM (~168 reg x 384 thr), each weight tile streamed once via TMA. A generic "
          "tiled GEMM caps ~58% HBM at decode M; the persistent warp-spec GEMV reaches ~78%.",
    "L4": "**Comm fused into the op (flag-based NVLink allreduce, §7):** peer LL buffers + "
          "device-ptr exchange + a flag token; P2P read-modify-write over NVLink overlaps the "
          "GEMM tail at tile granularity (no separate NCCL launch).",
    "L5": "**Bandwidth levers (§16/§20):** FP4 (MXFP4) expert weights (~4x less HBM); DSA "
          "sparse top-2048 KV so decode KV-read scales with 2048, not seq_len; compressed MLA "
          "latent cache (kv_c 512 + pe 64).",
    "L6": "**tcgen05/TMEM only for DSA index (§16):** the index/topk path uses tcgen05 "
          "(UTCHMMA); everything else is warpgroup HMMA. Default to warpgroup HMMA.",
}


def prompt_md(k, v):
    cts = ", ".join(f"{c}={CT_NAME[c]}" for c in v["cts"])
    levers = "\n".join(f"- {LEVER_TXT[L]}" for L in v["levers"])
    mtp = mtp_note(v["seqs"])
    dec = f"\n**Decode share:** {v['decode_pct']}% of TileRT decode CUDA time.\n" if v.get("decode_pct") else ""
    comm = ("\n> NOTE: this is a **communication kernel** — the real `torch.ops.tilert."
            f"{v['op']}` needs multi-GPU NVLink peer_bufs/ll_buf + flag setup, so it is "
            "profiled **in-graph** (not isolatable on 1 GPU). The PyTorch baseline still "
            "captures the compute (down/unproj GEMM) + the allreduce-sum semantics.\n"
            if v["std"] == "comm" else "")
    return f"""# b200_tilert_{k}
Target GPU: NVIDIA B200 (sm_100).

## Problem
{v['role']}. Matches TileRT `{v['executor']}ExecutorImpl`.
{dec}{comm}
Math: see `baseline/{k}.py` (a faithful port of TileRT's own `golden_forward`,
validated against the real op by `../../harness/tilert_oracle.py`).

## Shapes (decode + MTP)
- kSeqLen (from SASS symbol table) = {v['seqs']}  (MTP q_len subset = {mtp}; decode=1, MTP verify=4)
- KeComputeType variants = [{cts}]
- model dims: dim=7168, q_lora=1536, kv_lora=512, qk_nope=128, qk_rope=64,
  v_head=128, n_local_heads=20 (7-worker padded), n_routed=256, moe_inter=2048,
  index_topk=2048, vocab/8=16160.
- Full per-shape list: `bench/workloads.json`.

## TileRT reference (the target to match)
Measured from the real `libtilert_dsv32.so` op via ncu, **median of >=3 runs**
(see `config.toml [reference]` and `../../docs/tilert_reference.md`). Method:
`../../docs/benchmark_method.md`.

## Design levers to exploit (TileRT blog + SASS)
{levers}

See `../../docs/tilert_design_levers.md` for the full lever catalog.

## Goal
A B200 CUDA kernel matching `baseline/{k}.py` on **every** workload shape
(tolerances in `../../docs/tilert_correctness_contract.md`: bf16 <2e-2,
fp8/fp4 <5e-2) and reaching TileRT's measured latency on each shape.
"""


def reference_block(k, v):
    m = MEASURED.get(k)
    if m:
        s1 = m.get(1) or next(iter(m.values()))
        per_seq = ", ".join(f"{s}={m[s][0]}us/{m[s][1]}%HBM" for s in sorted(m))
        return (f"# ≥3× isolated ncu medians (gpu__time_duration.avg) on idle B200.\n"
                f"# Per-seq (median us / HBM%): {per_seq}. See ../../docs/tilert_reference.md.\n"
                f"tilert_latency_us = {s1[0]}\n"
                f"tilert_hbm_pct = {s1[1]}\n"
                f'measurement = "isolated_ncu_median_n3"\n'
                f"measured = true")
    if k in INGRAPH:
        return (f"# Not isolatable as a single launch — in-graph profiler target (§16).\n"
                f"tilert_latency_us = {INGRAPH[k]}\n"
                f'measurement = "in_graph_profiler"\n'
                f"measured = true")
    return ("# Comm/▲ kernel — needs 8-GPU NVLink peer setup; profiled in-graph only.\n"
            "tilert_latency_us = 0.0\n"
            'measurement = "in_graph_only"\n'
            "measured = false")


def config_toml(k, v):
    cts = ",".join(str(c) for c in v["cts"])
    return f"""[task]
slug = "b200_tilert_{k}"
arch = "b200"
target_gpu = "NVIDIA B200"
family = "{k}"
tilert_op = "tilert::{v['op']}"
tilert_kernel = "{v['executor']}ExecutorImpl<DefaultSchedule, 4, ., 1, ., .>"
decode_share_pct = {v.get('decode_pct', 0.0)}
standalone_measurable = "{v['std']}"

[build]
language = "cuda"
baseline_entry_point = "baseline/{k}.py::{k}_baseline"
candidate_entry_point = "solution/kernel.cu::{k}_candidate"

[reference]
{reference_block(k, v)}
seqlens = {v['seqs']}
compute_types = [{cts}]   # 0=none 3=bf16 5/6/8=fp4 7=fp8

[benchmark]
warmup_runs = 10
iterations = 200
num_trials = 7
required_matched_ratio = 1.0
"""


def workloads_json(k, v):
    rows = []
    for ct in v["cts"]:
        for seq in v["seqs"]:
            rtol = 0.02 if ct == 3 else 0.05
            rows.append({
                "id": f"s{seq}_{CT_NAME[ct]}",
                "production": seq in (1, 2, 3, 4),
                "function": k,
                "shapes": {"seq": seq, "ct": ct, "ct_name": CT_NAME[ct]},
                "rtol": rtol,
                "source": {"op": f"tilert::{v['op']}", "arch": "b200",
                           "executor": v["executor"]},
            })
    return rows


ADAPTER = '''"""Benchmark adapter for b200_tilert_{k} (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_{k}."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.{k} import {k}_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import {k}_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    {k}_candidate = None

def call_baseline(inp):   return {k}_baseline(**inp)
def call_candidate(inp):
    assert {k}_candidate is not None, "solution/binding.py:{k}_candidate missing"
    return {k}_candidate(**inp)
'''

CORRECTNESS = '''#!/usr/bin/env python3
"""Correctness: candidate vs PyTorch baseline on every workload shape
(see ../../docs/tilert_correctness_contract.md). Generated."""
import json, os, sys, torch
BENCH = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, BENCH)
import adapter
from baseline.{k} import make_inputs  # noqa

def main():
    dev = torch.device("cuda")
    rows = json.load(open(os.path.join(BENCH, "workloads.json")))
    ok = True
    for r in rows:
        inp = make_inputs(r["shapes"], dev)
        ref = adapter.call_baseline(inp)
        out = adapter.call_candidate(inp)
        ref = ref[-1] if isinstance(ref, (tuple, list)) else ref
        out = out[-1] if isinstance(out, (tuple, list)) else out
        rel = (out.float() - ref.float()).norm() / (ref.float().norm() + 1e-9)
        passed = rel < r.get("rtol", 0.02)
        ok &= bool(passed)
        print(f"[{{r['id']}}] rel={{rel:.2e}} {{'OK' if passed else 'FAIL'}}")
    print("CORRECTNESS", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
if __name__ == "__main__": main()
'''


def write(path, content, dry, force_set, k):
    if os.path.exists(path) and k not in force_set and os.path.basename(path) != "workloads.json" \
            and os.path.basename(path) not in ("prompt.md",):
        # don't clobber existing hand-authored files except always-refresh prompt/workloads
        return f"skip(exists) {path}"
    if dry:
        return f"DRY {path}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(content)
    return f"wrote {path}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--force", default="", help="kernels to fully (re)generate, clobbering")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    only = set(a.only.split(",")) if a.only else set(REGISTRY)
    force = set(a.force.split(",")) if a.force else set()
    for k, v in REGISTRY.items():
        if k not in only:
            continue
        d = os.path.join(KDIR, f"b200_tilert_{k}")
        msgs = [
            write(os.path.join(d, "prompt.md"), prompt_md(k, v), a.dry, force, k),
            write(os.path.join(d, "config.toml"), config_toml(k, v), a.dry, force, k),
            write(os.path.join(d, "README.md"),
                  f"# b200_tilert_{k}\n\nTileRT `{v['executor']}` — {v['role']}.\n", a.dry, force, k),
            write(os.path.join(d, "bench", "workloads.json"),
                  json.dumps(workloads_json(k, v), indent=1), a.dry, force, k),
            write(os.path.join(d, "bench", "adapter.py"), ADAPTER.format(k=k), a.dry, force, k),
            write(os.path.join(d, "bench", "correctness.py"), CORRECTNESS.format(k=k), a.dry, force, k),
        ]
        print(f"== {k} ==")
        for m in msgs:
            print("  ", m)


if __name__ == "__main__":
    main()
