# KDA Prompt: comm__comm__a12cdaa5b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `comm`
- Max observed GPU share: `2.80%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.80% GPU, calls=144, mean=57.36 us

## Promoted Shape Samples

1. `aten::view` via `external_id=4008`: `{"Concrete Inputs":["","[1]"],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
2. `aten::empty_like` via `external_id=4015`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[1],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["long int","","","","Scalar",""]}`
3. `aten::sum` via `external_id=4009`: `{"Concrete Inputs":["",""],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int",""]}`
4. `aten::empty_strided` via `external_id=4016`: `{"Concrete Inputs":["[1]","[1]","4","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
