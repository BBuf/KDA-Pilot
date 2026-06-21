# KDA Prompt: comm__comm__510fc180fc

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `comm`
- Max observed GPU share: `3.47%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 3.08% GPU, calls=500, mean=66.67 us
- `sharegpt_high`: 3.47% GPU, calls=1000, mean=35.83 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=19904`: `{"Concrete Inputs":["","[352, 2, 128]","[2048, 128, 1]","0"],"Input Dims":[[352,2,128],[],[],[]],"Input Strides":[[2048,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`
2. `aten::slice` via `external_id=57540`: `{"Concrete Inputs":["","0","-1","9223372036854775807","1"],"Input Dims":[[256],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
