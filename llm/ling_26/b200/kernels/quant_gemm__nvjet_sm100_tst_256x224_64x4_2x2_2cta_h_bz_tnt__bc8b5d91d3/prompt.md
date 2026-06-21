# KDA Prompt: quant_gemm__nvjet_sm100_tst_256x224_64x4_2x2_2cta_h_bz_tnt__bc8b5d91d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.14%`
- Kernel name: `nvjet_sm100_tst_256x224_64x4_2x2_2cta_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.14% GPU, calls=128, mean=143.23 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=18962`: `{"Concrete Inputs":["",""],"Input Dims":[[9780,4096],[4096,3072]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::as_strided` via `external_id=18890`: `{"Concrete Inputs":["","[22]","[0]",""],"Input Dims":[[22],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList",""]}`
3. `aten::transpose` via `external_id=19255`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[4096,1024],[],[]],"Input Strides":[[1024,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
