# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `google/gemma-4-26B-A4B-it`
- Model folder: `llm/gemma4/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `6.05%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 6.05% GPU, calls=65, mean=155.06 us
- `sharegpt_mid`: 2.45% GPU, calls=30, mean=104.49 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=11313`: `{"Concrete Inputs":["",""],"Input Dims":[[11254,2816],[2816,10240]],"Input Strides":[[2816,1],[1,2816]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=11354`: `{"Concrete Inputs":["",""],"Input Dims":[[11254,8192],[8192,2816]],"Input Strides":[[8192,1],[1,8192]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::mm` via `external_id=44264`: `{"Concrete Inputs":["",""],"Input Dims":[[7081,2816],[2816,4224]],"Input Strides":[[2816,1],[1,2816]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
