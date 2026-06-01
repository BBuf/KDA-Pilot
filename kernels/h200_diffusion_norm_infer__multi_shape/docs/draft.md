# Implementation / exploration log — h200_diffusion_norm_infer__multi_shape

Workspace KDA exploration notes. Records the recovered baseline, ranked candidate
directions, prior art, and keep/reject decisions. Selected host: `ion8-h200`
(`ion-h200-8`), container `sglang_omni_bbuf_kda` (privileged + ncu), idle GPU 7.
Pinned SGLang commit `c47f0e7cdde48ddc718e3c6ee8bc87bebee2e8ff`.

## Recovered baseline (oracle)

- `norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)` — out-of-place; one Triton program/row; `BLOCK_N=next_pow2(N)` (8192 for N=5120); loads whole row once; FP32 accumulation; biased variance (`/N`); LayerNorm `y=(x-mean)*rstd*w+b`.
- `triton_one_pass_rms_norm(x, w, eps=1e-6)` — out-of-place; tiled `BLOCK_SIZE_DIM=next_pow2(D)`, `BLOCK_SIZE_SEQ=min(16,next_pow2(max(1,S//512)))`; FP32 accumulation; `y=x*rsqrt(mean(x^2)+eps)*w`.
- Baseline import in the bare CUDA container needs a minimal `current_platform` shim (harness-only; `tests/_baseline_env.py`); kernels and `register_custom_op` are untouched. Verified: baseline runs on H200 and matches the FP32 reference (LN `max|err|≈2.4e-6`, RMS bf16 `max|err|≈0.013`).

## Roofline targets (H200 HBM3e peak ~4.8 TB/s; achievable ~3.5–4.0 TB/s)

| Shape | bytes (read x + write y) | SoL @4.8TB/s | SoL @3.5TB/s | Bound |
|---|---|---|---|---|
| RMS bf16 [650040,128] | 332.8 MB | ~69 µs | ~95 µs | HBM bandwidth |
| RMS bf16 [648720,128] | 332.3 MB | ~69 µs | ~95 µs | HBM bandwidth |
| RMS bf16 [16384,128] | 8.4 MB | ~1.7 µs | ~2.4 µs | launch/overhead |
| RMS bf16 [4096,128] | 2.1 MB | ~0.4 µs | ~0.6 µs | launch (likely no-go) |
| RMS bf16 [1320,128] | 0.68 MB | ~0.14 µs | ~0.2 µs | launch (clearest no-go) |
| LN fp32 [8640,5120] | 353.8 MB | ~74 µs | ~101 µs | HBM bandwidth |

## Ranked candidate directions (Codex task4 consult + Claude analysis)

1. **BF16 RMSNorm N=128 specialized CUDA kernel** (5/6 shapes; highest leverage).
   - First candidate: N=128 template, **16 lanes/row, 2 rows/warp** (each lane loads 8 bf16 = one 128-bit chunk), FP32 square accumulation, half-warp shuffle reduction, 4 warps/CTA = 8 rows/CTA, weight via cache (no shared preload first), vectorized bf16 load/store. Grid-stride over rows for huge-M.
   - Fallback design: one-warp-per-row (4 bf16/lane) if half-warp mapping underperforms.
   - Expected: 1.05–1.30× on huge-M; small on 16384/4096; 1320 launch-bound.
2. **FP32 LayerNorm N=5120 specialized one-CTA-per-row kernel** (helios).
   - First candidate: 256 threads/CTA, one CTA/row, 5 `float4`/thread, **retain x in registers**, compute mean then biased variance `sum((x-mean)^2)/N` from retained registers (NOT `E[x^2]-mean^2`), block reduction, `float4` stores, **no `--use_fast_math`** initially.
   - Expected: 1.10–1.40× if Triton's BLOCK_N=8192 masking/register pressure is costly.
3. **Cache-policy / operand-reuse tuning** (0–10%): treat x as streaming, w/weight/bias reused; test cache qualifiers only if profiling shows L1 pollution. Low priority.
4. **Shape-specific launch/config dispatch**: different rows/CTA for huge-M vs mid-M; document no-go for tiny-M.
5. **Fusion / CUDA Graph for tiny RMSNorm** — REJECTED for this task: changes the callsite contract / high scope risk. Out of scope (the captured callsite is norm-only).

## Rejected as design assumptions (memory-bound family)

- tcgen05 / TMEM / TMA / cluster MMA / warp specialization — REJECTED: these are simple streaming reductions; setup/sync overhead is the enemy (Codex + KernelWiki memory-bound guidance).
- Constant memory for RMS weight — REJECTED as default: lanes read different addresses (full-row vector reads), constant broadcast helps same-address reads only.
- `E[x^2]-mean^2` variance — REJECTED for FP32 LN: catastrophic-cancellation risk vs strict 1e-5.

## Prior art reviewed

- KernelWiki `patterns/memory-bound.md`, `techniques/vectorized-loads.md` (via Codex local KB) — confirm vectorized 128-bit loads + streaming + minimal sync for memory-bound norms; no MMA/TMA.
- SGLang baseline (`norm.py`, `rmsnorm_onepass.py`, commit c47f0e7cd) — tile/block choices, FP32 accumulation, biased variance, weight/bias handling (first-class reference).
- Repo precedent: `kda_kernels/diffusion/rotary_embedding/_impls/b200/wrapper.py` — JIT build (`cpp_extension.load`, `-O3 --use_fast_math -lineinfo`, `lru_cache`, `build()`), strict exact-shape dispatch gates, import-time baseline binding, 16-byte alignment, dispatch-path recorder.

## Next steps

- task5: implement BF16 N=128 RMSNorm CUDA kernel + wrapper + strict dispatcher.
- task6: implement FP32 N=5120 LayerNorm CUDA kernel + dispatcher gate.
- task7: remote build + correctness + same-card benchmarks (GPU 7).
- task8: NCU + roofline; decide keep/no-go per bucket (expect no-go for M=1320, maybe M=4096).
