# KDA Prompt: qwen38_nvfp4__sm120_fp8_gemv_multirow

Target GPU: NVIDIA RTX PRO 6000 Blackwell (SM120). Optimize the SGLang kernel
path behind:

- `sglang.kernels.ops.gemm.sm120_fp8_gemv.sm120_fp8_gemv`
- (fallback boundary) `sglang.srt.layers.quantization.fp8_utils.apply_fp8_linear`

**34.0% of bs=1 decode GPU time** on `RadixArk/Qwen3.8-27B-NVFP4` (4.77 ms of a
13.39 ms step, 128 calls/step; real torch-profiler capture on the target GPU,
see `docs/profile_evidence.md`). This is the per-tensor-static FP8 W8A8 skinny
GEMM serving all attention and GDN projections of the mixed-recipe checkpoint.

## Why this task

The existing `sm120_fp8_gemv_kernel` is a **M=1-only** weight-streaming GEMV
that runs within ~5% of copy-bandwidth. With DSpark speculative decoding the
decode step becomes a verify forward with `M = draft_block(+1) ∈ [4, 9]`, and
the whole family falls off the fast path onto cuBLAS `sm89_xmma` tiles
(64×128+ tiles at M≤16: heavily padded, measured ~2-3× off the weight-stream
optimum in the same regime on other models). Every point of verify-step time
converts directly into DSpark output throughput.

## Goal

One kernel (or a small tier family) covering `M ∈ [1, 16]` for the captured
`(K, N)` set, never slower than the M=1 baseline at M=1, and beating the
cuBLAS fallback at every M ∈ [2, 16] tier. Multi-row weight-streaming (each
weight tile read once, broadcast across the M rows in registers/smem) is the
expected shape of the solution; eviction-hint loads and the multirow recipe
from prior SM120 work apply.

## Contract

- Candidate API: `run(x_fp8, w_fp8, alpha, M) -> out_bf16` following the
  baseline callable in `baseline/`; per-tensor static scale folded into
  `alpha` exactly as the production path does.
- Weight layout: `[K, N]` column-major view of an `[N, K]`-contiguous buffer
  (the transposed view `apply` passes today). Do not repack weights at runtime;
  offline repack is allowed only if it is a pure view/one-time transform done
  in `prepare_benchmark`.
- Shapes: all rows in `bench/workloads.json` — K∈{5120, 6144} × N∈{16384,
  8192, 5120} × M∈{1, 2, 4, 6, 8, 16}.
- Numerics: bf16 output must match the baseline within the FP8 contract in
  `llm/docs/llm_correctness_contract.md` (bitwise vs same-order reference not
  required; per-element tolerance table applies).
- Standalone single-GPU task: optimize and validate via the task-local
  benchmark on one idle SM120 GPU. Follow
  `llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) and use
  `llm/docs/standalone_llm_benchmark_template.py`.

## Baseline

- M=1 rows: SGLang `sm120_fp8_gemv` (pinned upstream main at task creation).
- M≥2 rows: the production fallback (`apply_fp8_linear` → cuBLAS scaled_mm)
  with the same per-tensor scales.
- Score: geometric-mean speedup across all rows; any row slower than baseline
  fails the task gate.
