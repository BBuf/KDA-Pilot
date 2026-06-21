# KDA Prompt: quant_gemm__nvjet_sm100_tst_8x64_64x16_4x1_v_bz_tnn__3decc0e67f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/LLaDA2.1-mini`
- Model folder: `llm/llada_21_mini/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.81%`
- Kernel name: `nvjet_sm100_tst_8x64_64x16_4x1_v_bz_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.81% GPU, calls=2128, mean=6.42 us

## Promoted Shape Samples

1. `aten::copy_` via `external_id=11759`: `{"Concrete Inputs":["","","True"],"Input Dims":[[2],[2],[]],"Input Strides":[[1],[1],[]],"Input type":["int","int","Scalar"]}`
2. `aten::_local_scalar_dense` via `external_id=19157`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["long int"]}`
3. `aten::clamp` via `external_id=9374`: `{"Concrete Inputs":["","0",""],"Input Dims":[[1],[],[]],"Input Strides":[[1],[],[]],"Input type":["int","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
