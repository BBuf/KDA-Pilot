# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `3.02%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 3.02% GPU, calls=280, mean=115.92 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=63939`: `{"Concrete Inputs":["",""],"Input Dims":[[12199,4096],[4096,4608]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::detach_` via `external_id=63411`: `{"Concrete Inputs":[""],"Input Dims":[[31]],"Input Strides":[[1]],"Input type":["float"]}`
3. `aten::mm` via `external_id=64161`: `{"Concrete Inputs":["",""],"Input Dims":[[12199,4096],[4096,3072]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::empty_strided` via `external_id=63633`: `{"Concrete Inputs":["[31]","[1]","4","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
