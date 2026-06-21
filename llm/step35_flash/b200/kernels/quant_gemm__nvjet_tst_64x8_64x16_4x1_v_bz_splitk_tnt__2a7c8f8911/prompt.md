# KDA Prompt: quant_gemm__nvjet_tst_64x8_64x16_4x1_v_bz_splitk_tnt__2a7c8f8911

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.5-Flash`
- Model folder: `llm/step35_flash/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.19%`
- Kernel name: `nvjet_tst_64x8_64x16_4x1_v_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.19% GPU, calls=1440, mean=7.65 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=23753`: `{"Concrete Inputs":["[1]","4","0","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","Scalar",""]}`
2. `c10d::broadcast_` via `external_id=21726`: `{"Concrete Inputs":["","","0","0","False","-1"],"Input Dims":[[[1]],[],[],[],[],[]],"Input Strides":[[[1]],[],[],[],[],[]],"Input type":["TensorList","","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::detach_` via `external_id=25244`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`
4. `gloo:broadcast` via `external_id=22759`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
