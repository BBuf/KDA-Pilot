# KDA Prompt: comm__comm__e96ef2a99d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/LLaDA2.1-flash`
- Model folder: `llm/llada_21_flash/b200`
- Kernel category: `comm`
- Max observed GPU share: `4.02%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 2u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 4.02% GPU, calls=14430, mean=6.05 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=16153`: `{"Concrete Inputs":["","[]","[]","1"],"Input Dims":[[2],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`
2. `aten::empty` via `external_id=17110`: `{"Concrete Inputs":["[131072]","3","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
