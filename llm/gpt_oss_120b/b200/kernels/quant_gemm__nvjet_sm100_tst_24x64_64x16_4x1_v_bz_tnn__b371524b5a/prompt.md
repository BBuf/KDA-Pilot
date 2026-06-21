# KDA Prompt: quant_gemm__nvjet_sm100_tst_24x64_64x16_4x1_v_bz_tnn__b371524b5a

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.66%`
- Kernel name: `nvjet_sm100_tst_24x64_64x16_4x1_v_bz_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.66% GPU, calls=2016, mean=3.89 us

## Promoted Shape Samples

1. `aten::empty_strided` via `external_id=3368`: `{"Concrete Inputs":["[1]","[1]","4","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
2. `aten::sum` via `external_id=4009`: `{"Concrete Inputs":["",""],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
