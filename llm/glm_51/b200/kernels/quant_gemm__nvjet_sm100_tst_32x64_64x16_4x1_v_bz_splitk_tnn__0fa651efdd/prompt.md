# KDA Prompt: quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitk_tnn__0fa651efdd

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.1-FP8`
- Model folder: `llm/glm_51/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `18.18%`
- Kernel name: `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 18.18% GPU, calls=5600, mean=145.06 us
- `sharegpt_mid`: 13.60% GPU, calls=1312, mean=1082.02 us
- `sharegpt_high`: 5.86% GPU, calls=608, mean=1229.38 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=156611`: `{"Concrete Inputs":["",""],"Input Dims":[[16,6144],[6144,256]],"Input Strides":[[6144,1],[1,6144]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=224351`: `{"Concrete Inputs":["",""],"Input Dims":[[6,6144],[6144,256]],"Input Strides":[[6144,1],[1,6144]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::narrow` via `external_id=262195`: `{"Concrete Inputs":["","0","0","448"],"Input Dims":[[448],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar"]}`
4. `aten::alias` via `external_id=245832`: `{"Concrete Inputs":[""],"Input Dims":[[16,1]],"Input Strides":[[1,16]],"Input type":["int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
