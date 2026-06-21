# KDA Prompt: moe__moetopk__283e0afb8e

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.5-Flash`
- Model folder: `llm/step35_flash/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.85%`
- Kernel name: `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float const*)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.79% GPU, calls=1512, mean=9.29 us
- `random_high`: 2.85% GPU, calls=1512, mean=9.30 us

## Promoted Shape Samples

1. `c10d::broadcast_` via `external_id=21726`: `{"Concrete Inputs":["","","0","0","False","-1"],"Input Dims":[[[1]],[],[],[],[],[]],"Input Strides":[[[1]],[],[],[],[],[]],"Input type":["TensorList","","Scalar","Scalar","Scalar","Scalar"]}`
2. `aten::detach_` via `external_id=25244`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`
3. `gloo:broadcast` via `external_id=22263`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`
4. `aten::empty` via `external_id=23753`: `{"Concrete Inputs":["[1]","4","0","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
