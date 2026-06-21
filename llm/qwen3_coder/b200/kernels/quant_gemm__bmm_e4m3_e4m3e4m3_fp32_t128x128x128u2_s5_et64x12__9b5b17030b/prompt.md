# KDA Prompt: quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x128x128u2_s5_et64x12__9b5b17030b

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Model folder: `llm/qwen3_coder/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `5.78%`
- Kernel name: `bmm_E4m3_E4m3E4m3_Fp32_t128x128x128u2_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 4.96% GPU, calls=496, mean=177.51 us
- `sharegpt_mid`: 5.78% GPU, calls=558, mean=197.60 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=28954`: `{"Concrete Inputs":["","[1]","[1]","447"],"Input Dims":[[448],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
2. `aten::to` via `external_id=45901`: `{"Concrete Inputs":["","4","0","","","True","False",""],"Input Dims":[[1950],[],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[],[]],"Input type":["long int","Scalar","Scalar","","","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
