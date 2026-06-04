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
- normv5 (PROMOTE — historical overlay round, superseded by tilev1; see section 8): RMS → 2-rows-per-warp 128-bit (prior-art lever). huge-RMS DRAM 70.6%→77.5%; all shapes ≥1.04x; geomean **1.4223x**. 201/201 full-grid correctness. NCU bounds in profile/ncu_normv2/REPORT.md.

Active bound per bucket (normv5): LN at HBM bound (79.8% ≈ baseline); huge-RMS near bound (77.5%, ~93% of baseline's 83%, wall parity+); small-RMS launch/dispatch-bound (win = lean tvm-ffi dispatch, AC-9 14.93us vs 31.5us).

## 7. Remote run record (host / GPU id / GPU model / before-after idleness)

- Session `s20260601-232934`: host `ion8-h200` (`ion-h200-8`), container `sglang_bbuf`,
  GPU id `7` (NVIDIA H200), idle `0util/100MB` before+after baseline lock.
  `REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_norm_infer__multi_shape/s20260601-232934`.
  sglang `c47f0e7cd`, torch 2.11.0+cu130, ncu 2025.3.1.0. Harness validated:
  33/33 baseline-vs-FP32-reference correctness checks pass. Baseline locked.

---

## 8. Continuation round (PR #25 re-validation, RLCR 2026-06-04_18-46-16)

Trigger: kernel-pilot commit `cc17c1149` tightened the prompt AFTER the normv5
promotion (PR #18). New mandatory rules: symmetric shipping-integration
benchmark, registration preservation, device-vs-host decomposition. The prior
**1.4223x geomean is HISTORICAL OVERLAY EVIDENCE** (measured through the
`kda_kernels.install()` plain-callable monkey-patch) — not PR#25-admissible.
Plan: `.humanize/kernel-agent/refined-plan.md`. Lineage:
`solutions.jsonl` id `continuation_pr25_audit`.

### Missing-repo-docs note (audit)

`../../docs/standalone_diffusion_benchmark.md`, `../../docs/diffusion_kernel_rules.md`,
and `../../docs/diffusion_correctness_contract.md` do **not** exist in this worktree.
Binding repo-level rules: `../../docs/sglang_jit_kernel_export.md` and
`../../docs/tvm_ffi_benchmark_status.md` (listed this task as "Blocked: no
optimized tvm-ffi candidate is present in the SGLang checkout" at round start;
updated to Done by this round's in-tree arbiter).

### User decisions baked in (do not re-ask mid-loop)

- DEC-1 verify container sglang commit vs locked `c47f0e7cd`; re-lock only on drift.
- DEC-2 in-tree launcher savings admissible WITH device/host split (registration kept).
- DEC-3 huge-RMS: bounded multi-row-tile rewrite first, then fallback-by-M.
- DEC-4 geomean = outcome metric; honest-lower-than-1.4223x stands.

### Continuation candidate directions (ranked; refined by prior-art pass)

1. Huge-RMS multi-row tile (R rows/CTA, 128-bit loads, uncapped grid) — attacks
   the only device-level gap (77.5% vs 83.2% DRAM on [648720,128]). Risk: B200
   sibling no-go (memory-latency + SM-issue bound there).
2. Launch-policy retune for huge-M (rows-per-CTA sweep, `__launch_bounds__`).
3. Cache-policy hints (`ld.global.cg/.cs`) on streaming loads.
4. PDL re-validation on this workload (prior pilot: hurt isolated latency; keep
   only if it wins here).
5. LN headroom re-check only (expected none: at HBM bound, device-parity).

### Iteration context-refresh log (AC discipline)

- r0-audit: submodules initialized; KernelWiki + ncu-report-skill SKILL.md read.
  Arbiter pattern refreshed from k13 norm_tanh precedent: dispatch-symmetric
  env-toggled routes in ONE patched checkout; fallback probes assert gate False
  AND compare outputs to reference; idle gate = REMOTE_GPU_ID == first
  CUDA_VISIBLE_DEVICES entry + compute-app count before AND after.

### Continuation remote run record (r0 audit)

- Host `ion8-h200` (`ion-h200-8`), container `sglang_bbuf` (Up 13 days),
  `REMOTE_GPU_ID=0` (NVIDIA H200). Idle gate: `0util/0MB/0 compute apps` before,
  `0MB/0 apps` after the spot-check.
- `REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_norm_infer__multi_shape/r20260604-rlcr184616`.
- Container sglang: editable install of `/home/sglang-omni/bbuf/repos/sglang`,
  HEAD `84e1108312` (main, clean). Drift check vs locked `c47f0e7cd`:
  `norm.py` + `rmsnorm_onepass.py` + `custom_op.py` **byte-identical**; only
  `jit_kernel/utils.py` +7/−1 (MUSA guard in `is_arch_support_pdl()`, inert on CUDA).
  torch `2.11.0+cu130` (matches lock-time), triton `3.6.0`, tvm_ffi `0.1.9`.
- Baseline spot-check on GPU 0 (wall median, warmup 30 / iters 200):
  helios LN `109.71us` (locked 109.43), rms 4096x128 `31.15us` (locked 31.48),
  rms 648720x128 `107.20us` (locked 107.83) — all within ±1%.
- **DEC-1 outcome: locked baseline KEPT** (`docs/baseline_locked.json` stands);
  round pin = container HEAD `84e1108312` (baseline-relevant files identical to
  `c47f0e7cd`).

### r0 honest re-measurement (symmetric local legs, ion8-h200 GPU0, 2026-06-04)

Harness `benchmark_symmetric.py` (two-pass: per-call wall == locked methodology;
batched device rate = 1 event pair around 32 back-to-back enqueues). Leg A =
copied Triton baseline (`baseline/triton_norm_baseline.py` @ `84e1108312`),
leg B = normv5 dispatcher. Interleaved, order-swapped, idle-gated. Floors:
wall 4.82us, device 0.214us/call. A first per-call-event run was discarded
(event window captured the enqueue gap; never imported).

| shape | base wall | base dev | cand wall | cand dev | wall x | dev x |
|---|---|---|---|---|---|---|
| helios LN 8640x5120 f32 | 111.00 | 90.98 | 103.48 | 89.53 | 1.073 | 1.016 |
| hunyuan 648720x128 bf16 | 104.04 | 81.97 | 100.81 | 90.37 | 1.032 | **0.907** |
| hunyuan 1320x128 bf16 | 26.09 | 18.68 | 16.42 | 9.68 | 1.589 | 1.931 |
| hunyuan 650040x128 bf16 | 104.05 | 82.21 | 100.95 | 90.57 | 1.031 | **0.908** |
| zimage 16384x128 bf16 | 26.16 | 18.67 | 17.62 | 9.67 | 1.485 | 1.930 |
| zimage 4096x128 bf16 | 25.98 | 18.83 | 16.34 | 9.69 | 1.590 | 1.943 |
| **geomean** | | | | | **1.274** | **1.350** |

Reading: huge-RMS solo-call wall win is host-only (launcher 22.1→10.4us) while
the device rate REGRESSES ~9-10% — in a saturated back-to-back pipeline that is
a net loss → 16-row-tile rewrite (or fallback-by-M) decides the bucket.
Small-RMS: the Triton launcher is the bound even when saturated (18.7us/call
enqueue rate vs ~3.3us kernel); tvm-ffi enqueues at 9.7us/call → dev-rate x1.93
+ wall x1.49-1.59, admissible per DEC-2 (host delta, decomposed). Copied-baseline
leg is leaner than the production path (no custom-op shim, ~5us at small shapes),
so these speedups are conservative vs production.

### r0 outcome (round closed: PROMOTE tilev1)

- **tilev1 kernel** (`src/rms_norm_d128_tile16.cuh`): one 8x128 tile per
  128-thread CTA, 16 lanes/row, 128-bit loads, fp32 reduce, grid=ceil(M/8) —
  CUDA port of the Triton tile structure (prior-art D1). Sweep: tile8x128 beat
  tile16x128/16x256/32x256 and the normv5 warp kernel at EVERY captured M;
  streaming hints rejected (-0.6% device, +1.6% wall); PDL skipped (prior-art
  REJECT + qknorm pilot regression). Dispatcher routes ALL supported RMS
  shapes to it; LN kernel byte-unchanged.
- **NCU** (`profile/ncu_tilev1/REPORT.md`): tile vs Triton baseline on
  [648720,128] — IDENTICAL 77,664ns single-launch, 82.67% vs 82.17% DRAM
  (both at the practical HBM bound; normv5's 77.5% gap closed; diagnosis =
  CTA-count/memory-level parallelism, confirmed by the fix).
- **Correctness**: full regression grid 404/404 on ion8-h200 GPU0
  (KDA_RUN_CORRECTNESS=1 KDA_FULL_CORRECTNESS=1).
- **Promotion arbiter (in-SGLang, dispatch-symmetric env-toggle, PASS)**:
  ONE patched worktree @ 84e1108312; native paths inside the unchanged public
  bodies; 4 alternated off/on runs → **wall geomean 1.4458x** (dev-rate
  1.478x); oracle 288/288 with native ON and OFF; fallback probes (gate False
  + ref-equal) and torch.compile smoke (registered op present, bitwise) pass.
  Shipping patch: `docs/sglang_export.patch`.
- **Export**: kda_kernels `_impls/h200` refreshed (tile kernel);
  `validate_install.py` strict VALIDATE_OK (smoke 2.00x small / 1.14x huge);
  lineage stamps: export-source `76cd0a0de`, benchmarked anchor `b4f9b43aa`.
- Decision table + roofline: `docs/dispatch.md`. Evidence ledger:
  `benchmark.csv` (symmetric_* + intree_arbiter* + GEOMEAN row),
  `solutions.jsonl` (continuation lineage through `intree_arbiter_tilev1`).
