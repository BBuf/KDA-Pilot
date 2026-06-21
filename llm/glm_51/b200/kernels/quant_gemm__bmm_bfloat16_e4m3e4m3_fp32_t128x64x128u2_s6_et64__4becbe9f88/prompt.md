# KDA Prompt: quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.1-FP8`
- Model folder: `llm/glm_51/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `3.95%`
- Kernel name: `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 3.95% GPU, calls=608, mean=505.99 us

## Promoted Shape Samples

1. `aten::reshape` via `external_id=62409`: `{"Concrete Inputs":["","[11247, 128]"],"Input Dims":[[11247,128],[]],"Input Strides":[[128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
