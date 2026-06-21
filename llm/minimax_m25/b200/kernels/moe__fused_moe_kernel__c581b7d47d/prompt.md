# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.5`
- Model folder: `llm/minimax_m25/b200`
- Kernel category: `moe`
- Max observed GPU share: `31.73%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 15.14% GPU, calls=8928, mean=12.43 us
- `random_mid`: 28.50% GPU, calls=8928, mean=72.30 us
- `random_high`: 31.73% GPU, calls=8928, mean=59.30 us
- `sharegpt_mid`: 28.53% GPU, calls=8928, mean=70.36 us
- `sharegpt_high`: 30.75% GPU, calls=8928, mean=58.74 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=253`: `{"Concrete Inputs":["","[39, 1, 128]","[1024, 128, 1]","0"],"Input Dims":[[48,1,128],[],[],[]],"Input Strides":[[1024,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`
2. `aten::as_strided` via `external_id=11701`: `{"Concrete Inputs":["","[8943, 1, 128]","[1024, 128, 1]","0"],"Input Dims":[[9216,1,128],[],[],[]],"Input Strides":[[1024,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`
3. `aten::slice` via `external_id=28435`: `{"Concrete Inputs":["","0","192","9223372036854775807","1"],"Input Dims":[[192],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar","Scalar"]}`
4. `aten::as_strided` via `external_id=54662`: `{"Concrete Inputs":["","[5524, 768]","[768, 1]","0"],"Input Dims":[[5632,768],[],[],[]],"Input Strides":[[768,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
