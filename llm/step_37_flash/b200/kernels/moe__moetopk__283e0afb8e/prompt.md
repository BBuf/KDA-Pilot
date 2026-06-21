# KDA Prompt: moe__moetopk__283e0afb8e

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Model folder: `llm/step_37_flash/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.94%`
- Kernel name: `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float const*)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.26% GPU, calls=3024, mean=9.20 us
- `random_mid`: 2.94% GPU, calls=3024, mean=26.25 us

## Promoted Shape Samples

1. `sgl_kernel::topk_sigmoid` via `external_id=5046`: `{"Concrete Inputs":["","","","True",""],"Input Dims":[[56,8],[56,8],[56,288],[],[288]],"Input Strides":[[8,1],[8,1],[288,1],[],[1]],"Input type":["float","int","float","Scalar","float"]}`
2. `sgl_kernel::topk_sigmoid` via `external_id=20679`: `{"Concrete Inputs":["","","","True",""],"Input Dims":[[12438,8],[12438,8],[12438,288],[],[288]],"Input Strides":[[8,1],[8,1],[288,1],[],[1]],"Input type":["float","int","float","Scalar","float"]}`
3. `aten::view` via `external_id=20605`: `{"Concrete Inputs":["","[12438]"],"Input Dims":[[12438],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
