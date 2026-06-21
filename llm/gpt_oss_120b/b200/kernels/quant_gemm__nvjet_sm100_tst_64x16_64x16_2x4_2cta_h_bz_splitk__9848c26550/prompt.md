# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__9848c26550

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `9.46%`
- Kernel name: `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 9.46% GPU, calls=288, mean=96.98 us
- `random_mid`: 4.41% GPU, calls=288, mean=122.18 us

## Promoted Shape Samples

1. `aten::view` via `external_id=304`: `{"Concrete Inputs":["","[38]"],"Input Dims":[[38],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
2. `aten::zero_` via `external_id=5110`: `{"Concrete Inputs":[""],"Input Dims":[[10]],"Input Strides":[[1]],"Input type":["long int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
