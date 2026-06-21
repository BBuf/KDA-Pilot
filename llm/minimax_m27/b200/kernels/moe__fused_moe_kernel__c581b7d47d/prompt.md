# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `moe`
- Max observed GPU share: `32.52%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 16.64% GPU, calls=8928, mean=12.35 us
- `random_mid`: 31.40% GPU, calls=8928, mean=71.91 us
- `random_high`: 32.52% GPU, calls=8928, mean=59.60 us
- `sharegpt_low`: 18.24% GPU, calls=8928, mean=13.10 us
- `sharegpt_mid`: 30.62% GPU, calls=8928, mean=70.11 us

## Promoted Shape Samples

1. `aten::pad` via `external_id=254`: `{"Concrete Inputs":["","[1, 0]","",""],"Input Dims":[[1],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","",""]}`
2. `aten::lift_fresh` via `external_id=11681`: `{"Concrete Inputs":[""],"Input Dims":[[19]],"Input Strides":[[1]],"Input type":["float"]}`
3. `aten::as_strided` via `external_id=23967`: `{"Concrete Inputs":["","[1]","[1]","447"],"Input Dims":[[448],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
4. `aten::to` via `external_id=31546`: `{"Concrete Inputs":["","3","False","False",""],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
