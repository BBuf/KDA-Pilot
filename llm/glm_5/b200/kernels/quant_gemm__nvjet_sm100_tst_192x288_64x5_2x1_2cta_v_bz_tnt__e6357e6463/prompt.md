# KDA Prompt: quant_gemm__nvjet_sm100_tst_192x288_64x5_2x1_2cta_v_bz_tnt__e6357e6463

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/GLM-5-NVFP4`
- Model folder: `llm/glm_5/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.62%`
- Kernel name: `nvjet_sm100_tst_192x288_64x5_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 2.62% GPU, calls=312, mean=425.77 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=186891`: `{"Concrete Inputs":["",""],"Input Dims":[[20784,6144],[6144,2624]],"Input Strides":[[6144,1],[1,6144]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::permute` via `external_id=192497`: `{"Concrete Inputs":["","[1, 0]"],"Input Dims":[[1024,3072],[]],"Input Strides":[[3072,1],[]],"Input type":["unsigned char","ScalarList"]}`
3. `aten::view` via `external_id=189417`: `{"Concrete Inputs":["","[20784, 384]"],"Input Dims":[[20784,384],[]],"Input Strides":[[384,1],[]],"Input type":["c10::Float8_e4m3fn","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
