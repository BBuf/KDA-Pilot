# KDA Prompt: comm__comm__515f5a341d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `comm`
- Max observed GPU share: `2.96%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.88% GPU, calls=4464, mean=4.28 us
- `sharegpt_low`: 2.96% GPU, calls=4464, mean=4.25 us

## Promoted Shape Samples

1. `aten::pad` via `external_id=254`: `{"Concrete Inputs":["","[1, 0]","",""],"Input Dims":[[1],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","",""]}`
2. `aten::empty_strided` via `external_id=4358`: `{"Concrete Inputs":["[]","[]","3","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
3. `aten::to` via `external_id=31546`: `{"Concrete Inputs":["","3","False","False",""],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
