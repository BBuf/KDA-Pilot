# Dispatch table + promote/no-go — normv5

Native-CUDA candidates (built via SGLang jit_kernel/tvm-ffi, no `--use_fast_math`)
behind a zero-overhead dispatcher (`src/norm_dispatch.py`) that preserves the two
public callable names and falls back to the SGLang baseline for any unsupported
signature.

## Decision table (ion8-h200 GPU7, NVIDIA H200, idle; wall-clock median; vs locked baseline)

| Bucket | shape | entry → variant | base (us) | cand (us) | speedup | active bound | decision |
|---|---|---|---|---|---|---|---|
| LN fp32 | [8640,5120] | norm_infer → layer_norm_block | 109.43 | 102.57 | 1.067x | HBM (cand 79.8% ≈ base 79.7% DRAM) | **promote** (at bound) |
| RMS huge | [648720,128] | triton_one_pass_rms_norm → rms_norm_warp | 107.83 | 103.63 | 1.041x | HBM (cand 77.5% vs base 83.2% DRAM) | **promote** (parity+, near bound) |
| RMS huge | [650040,128] | rms_norm_warp | 107.04 | 102.33 | 1.046x | HBM | **promote** (parity+) |
| RMS small | [16384,128] | rms_norm_warp | 31.81 | 16.63 | 1.912x | launch/dispatch | **promote** |
| RMS small | [1320,128] | rms_norm_warp | 31.93 | 16.43 | 1.944x | launch/dispatch | **promote** |
| RMS small | [4096,128] | rms_norm_warp | 31.48 | 16.41 | 1.918x | launch/dispatch | **promote** |
| **geomean** | | | | | **1.4223x** | | |

## Routing guards (exact; else fall back to SGLang baseline)
- `triton_one_pass_rms_norm` → `rms_norm_warp<128,false,bf16_t>` when: CUDA, dtype
  **bf16 only** (fp16 D=128 compiles but is outside the validated shape set → baseline),
  `x.is_contiguous()`, D==128, w is [128] bf16 contiguous.
- `norm_infer` → `layer_norm_block<5120,true,false,float>` when: CUDA, dtype float32,
  `is_rms_norm=False`, `out is None`, `x.is_contiguous()`, N==5120, weight & bias both [N] f32 contiguous.
- The full `x.is_contiguous()` requirement guarantees `reshape(-1,D)` and the fresh
  `empty_like(x)` output are kernel-writable views; merely last-dim-contiguous higher-rank
  inputs fall back to baseline (regression-tested).
- Everything else (CPU/MPS, non-contiguous, other dtype/N/D, is_rms_norm=True on
  norm_infer, missing weight/bias) → SGLang baseline (verified: candidate output ==
  baseline output for fallback cases).

## Promote/no-go rationale (user-confirmed policy: outcome metric; parity/no-go OK with bound evidence)
- **Promote normv5.** Correct on all 6 perf shapes + the full regression grid (201/201,
  incl. odd M) + the select01 modulation oracle, vs baseline and a PyTorch fp32 reference,
  with NaN/Inf checks. fp32 LN within 1e-5 (2.86e-6, == baseline error); bf16 within 5e-2.
- The 3 HBM-bandwidth-bound shapes are at/near the bound (LN at 79.8% DRAM = baseline;
  huge RMS at 77.5%, ~93% of baseline's 83%); they win on wall-clock via leaner launch.
- The 3 launch/dispatch-bound shapes win ~1.9x from the lean tvm-ffi dispatch (kernel ~3us;
  the baseline's register_custom_op path adds ~28us). Integrated path 14.93us vs 31.5us.
- **Residual / documented no-go-to-close:** the huge-RMS kernel bandwidth (77.5%) trails
  the baseline (83.2%). Closing the last ~5.6% would require a deeper multi-row tiling
  rewrite for diminishing return (baseline is itself only ~83% of the 4.8 TB/s peak), and
  the wall-clock is already parity+. Not pursued further per the don't-chase-a-number policy.
