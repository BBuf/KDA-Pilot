# KDA Prompt: quant_gemm__nvjet_sm100_tst_384x32_64x4_2x1_2cta_v_bz_tnt__42776567a6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/LLaDA2.1-mini`
- Model folder: `llm/llada_21_mini/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.44%`
- Kernel name: `nvjet_sm100_tst_384x32_64x4_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.44% GPU, calls=112, mean=105.80 us

## Promoted Shape Samples

1. `aten::copy_` via `external_id=11759`: `{"Concrete Inputs":["","","True"],"Input Dims":[[2],[2],[]],"Input Strides":[[1],[1],[]],"Input type":["int","int","Scalar"]}`
2. `aten::copy_` via `external_id=28598`: `{"Concrete Inputs":["","","False"],"Input Dims":[[1],[1],[]],"Input Strides":[[1],[1],[]],"Input type":["long int","int","Scalar"]}`
3. `aten::copy_` via `external_id=16372`: `{"Concrete Inputs":["","","False"],"Input Dims":[[],[],[]],"Input Strides":[[],[],[]],"Input type":["int","long int","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
