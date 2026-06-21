# KDA Prompt: quant_gemm__bmm_bfloat16_e2m1e2m1_fp32_ab16_bb16_t128x32x512__5ea7167b72

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.54%`
- Kernel name: `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x32x512_s4_et128x32_m256x32x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 2.54% GPU, calls=522, mean=71.14 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=150807`: `{"Concrete Inputs":["","0","0","104","1"],"Input Dims":[[512],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
