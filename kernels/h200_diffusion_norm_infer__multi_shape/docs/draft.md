# Implementation Draft — h200_diffusion_norm_infer__multi_shape

Native-CUDA optimization of the two SGLang diffusion inference-only norm kernels,
built/exported via SGLang `jit_kernel` / tvm-ffi. Target: NVIDIA H200. GPU work
runs only on remote `ion8-h200` / `ion9-h200` (`sglang_bbuf` container).

## 1. Baseline recovery (see interface.md for the exact contract)

- `norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)` — Triton, one
  program per row, `BLOCK_N = next_pow2(N)`, full row to fp32 registers, mean(+LN)
  / var, `rstd`, weight then bias, store. helios uses it as **LayerNorm** fp32
  with weight+bias.
- `triton_one_pass_rms_norm(x, w, eps=1e-6)` — Triton, tiled
  `BLOCK_SEQ x next_pow2(D)`, `mean_square=sum(x^2)/D`, `rstd=rsqrt(ms+eps)`,
  `y=x*rstd*w`, no bias. All RMS shapes have `D=128`, bf16.

Both are pure memory-bound elementwise-with-reduction. The CUDA candidate is a
first-class re-implementation; the Triton baseline is one reference among many.

## 2. Roofline (H200 HBM3e ~4.8 TB/s peak; ~3.8 TB/s ~80% achievable)

Traffic = read(x) + write(y) (+ tiny weight/bias). Lower-bound latency at
4.8 / 3.8 TB/s:

| Shape | dtype | bytes (R+W) | LB @4.8TB/s | LB @3.8TB/s | active bound |
|---|---|---|---|---|---|
| helios `[8640,5120]` LN | f32 | ~354 MB | ~74 µs | ~93 µs | HBM bandwidth |
| hunyuan `[648720,128]` | bf16 | ~332 MB | ~69 µs | ~87 µs | HBM bandwidth |
| hunyuan `[650040,128]` | bf16 | ~333 MB | ~69 µs | ~88 µs | HBM bandwidth |
| zimage `[16384,128]` | bf16 | ~8.4 MB | ~1.7 µs | ~2.2 µs | bandwidth / occupancy ramp |
| zimage `[4096,128]` | bf16 | ~2.1 MB | ~0.44 µs | ~0.55 µs | launch / dispatch overhead |
| hunyuan `[1320,128]` | bf16 | ~0.68 MB | ~0.14 µs | ~0.18 µs | launch / dispatch overhead |

Implication: the two huge RMS shapes + helios LN are HBM-bound (win = saturate
bandwidth, good occupancy, no wasted masked traffic). The two tiny RMS shapes are
launch/dispatch-bound (win = low-overhead CUDA launch + zero-overhead dispatch).

## 3. Shape buckets + dispatcher

- **Bucket RMS-D128** (5/6 shapes): one templated bf16 `D=128` kernel; launch
  config differs huge vs small (grid-stride/occupancy vs tiny grid).
- **Bucket LN-F32-N5120** (helios): exact-`N=5120` fp32 LayerNorm + weight + bias.
- Dispatcher: exact guards, baseline fallback (see interface.md). Must be
  zero-overhead (cache_once module, no per-call Python tax — prior pilot ~5µs tax
  erased small-shape wins). The integrated install()-path is timed explicitly.

## 4. Candidate optimization directions (ranked)

| # | Direction | Target bucket | Expected benefit | Risk |
|---|---|---|---|---|
| D1 | bf16 `D=128` warp/half-warp per row, 128-bit vec loads, fp32 accum, warp-shuffle reduce, cached weight, grid-stride | RMS huge + small | High (matches/﹥ Triton; low launch overhead) | Low — mirrors qknorm_rope.cuh |
| D2 | Zero-overhead dispatcher (cache_once, prebuilt module, no per-call alloc) | small RMS | High on `[1320,128]`/`[4096,128]` | Med — the known dispatcher-tax pitfall |
| D3 | exact-`N=5120` fp32 LN, float4 vec, fp32 block reduction (2-moment), rows-per-CTA tuned for occupancy | helios LN | Med (avoid Triton 8192 masked over-read) | Med — fp32 1e-5 reduction-order sensitivity |
| D4 | rows-per-CTA / vector-width autotune for huge RMS occupancy + tail | RMS huge | Low–Med | Low |
| D5 | PDL (`enable_pdl`) — measured only | any | Unknown (hurt in qknorm pilot) | keep only if it wins |

Out of scope: TensorCore/TMA/TMEM (pure normalization, no inner matmul); fusing
select01 modulation (changes interface); the channels-last `.contiguous()`
skip-copy lever (all captured shapes are contiguous); any shape outside the six.

## 5. Prior-art notes (KernelWiki / upstream)

Analyze pass (Codex gpt-5.5:high + KernelWiki; full output in
`.humanize/skill/2026-06-02_00-08-20-94442-b639113c/output.md`). Note: the
`external/KernelWiki` submodule is NOT initialized in this worktree (run
`git submodule update --init --recursive` to populate it); Codex used a fallback
local clone.

Kept / applied:
- **RMS D=128 128-bit two-rows-per-warp** (KernelWiki `technique-vectorized-loads`;
  pytorch#150705, vllm#27931) — applied in normv5; lifted huge-RMS DRAM 70.65%→77.54%.
- **Separate launch policy** for bandwidth-bound vs launch-bound shapes
  (`pattern-memory-bound`) — applied: LN one-CTA-per-row, RMS persistent capped grid-stride.

Rejected / no-op for this workload:
- `cp.async` / TMA / shared-memory staging (`hw-tma`) — no tile reuse in a pure norm.
- Persistent/CLC scheduling — SM100-oriented, not a low-risk H200 lever.
- 256-bit loads — stricter alignment + more registers; 128-bit half-warp is cleaner for D=128.
- Fusion with allreduce/quant/RoPE (sglang#8731, trtllm#13033) — changes dataflow, out of scope.
- Clever reduction math — reductions are not the bottleneck at ~3.6 TB/s.

## 6. Exploration log (KDA search DAG; mirror entries into solutions.jsonl)

### Locked baseline (immutable) — sglang `c47f0e7cd`, ion8-h200 GPU7 (NVIDIA H200), idle 0util/100MB before+after

| Shape | wall median (µs) | GB/s (event*) | active bound |
|---|---|---|---|
| helios f32 `[8640,5120]` LN | 109.43 | ~3825 | HBM bandwidth (~80% of 4.8 TB/s) |
| hunyuan `[648720,128]` | 107.83 | ~3984 | HBM bandwidth (~83%) |
| hunyuan `[650040,128]` | 107.04 | ~4006 | HBM bandwidth (~83%) |
| hunyuan `[1320,128]` | 31.93 | ~20 | CPU launch/dispatch overhead |
| zimage `[16384,128]` | 31.81 | ~242 | CPU launch/dispatch overhead |
| zimage `[4096,128]` | 31.48 | ~61 | CPU launch/dispatch overhead |

**Key insight (drives strategy):**
- The three small shapes all cost ~31–32 µs *regardless of size* (1320 vs 16384
  rows → same latency). They are **CPU launch/dispatch-bound**, not GPU-bound —
  the SGLang `triton_one_pass_rms_norm` goes through `register_custom_op` (torch
  custom-op dispatch) + Triton launch, a fixed ~30 µs Python cost. A lean
  native-CUDA callable (tvm-ffi, no `register_custom_op`, no per-call alloc) can
  cut this dramatically → this is the dominant win lever for 3 of 6 shapes
  (validates AC-9 / the zero-overhead dispatcher emphasis).
- The two huge RMS shapes + helios LN already hit ~3825–4006 GB/s ≈ 80–83% of the
  ~4.8 TB/s H200 HBM bound. They are bandwidth-bound; a CUDA kernel can match or
  modestly beat (target ~85–90% of peak), but **parity is the honest ceiling** —
  expect a documented near-bound result rather than a large speedup.

\*event-based GB/s is **CPU-contaminated** for launch-bound shapes (per-iter
`cuda.Event` brackets include the CPU enqueue gap when the CPU is the
bottleneck). Authoritative kernel-only GPU time / bandwidth comes from NCU
(AC-6). The wall-clock median is the official, fair production latency (it is
the speedup denominator and legitimately includes dispatch cost).

### Candidate attempts (full detail in solutions.jsonl)
- rms_v1: 64-bit warp-per-row RMS + lean dispatch. Correct; geomean 1.39x (helios fell back). Superseded.
- normv2: + exact-N=5120 fp32 LN (capped grid-stride). Correct (LN 2.86e-6). geomean 1.392x. NCU: LN 74% / huge-RMS 70.6% DRAM (both capped → bandwidth starved).
- grid_experiments (normv3/v4): uncapping helped LN (one-CTA-per-row → 79.8% DRAM, 1.067x) but hurt huge-RMS (added launch/tail). Kept LN uncapped + RMS capped (normv4, all shapes ≥1.02x, 1.408x).
- normv5 (PROMOTE): RMS → 2-rows-per-warp 128-bit (prior-art lever). huge-RMS DRAM 70.6%→77.5%; all shapes ≥1.04x; geomean **1.4223x**. 201/201 full-grid correctness. NCU bounds in profile/ncu_normv2/REPORT.md.

Active bound per bucket (normv5): LN at HBM bound (79.8% ≈ baseline); huge-RMS near bound (77.5%, ~93% of baseline's 83%, wall parity+); small-RMS launch/dispatch-bound (win = lean tvm-ffi dispatch, AC-9 14.93us vs 31.5us).

## 7. Remote run record (host / GPU id / GPU model / before-after idleness)

- Session `s20260601-232934`: host `ion8-h200` (`ion-h200-8`), container `sglang_bbuf`,
  GPU id `7` (NVIDIA H200), idle `0util/100MB` before+after baseline lock.
  `REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_norm_infer__multi_shape/s20260601-232934`.
  sglang `c47f0e7cd`, torch 2.11.0+cu130, ncu 2025.3.1.0. Harness validated:
  33/33 baseline-vs-FP32-reference correctness checks pass. Baseline locked.
