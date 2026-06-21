# KDA Prompt: comm__comm__a12cdaa5b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Model folder: `llm/minimax_m3/b200`
- Kernel category: `comm`
- Max observed GPU share: `22.60%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 22.60% GPU, calls=8712, mean=34.57 us
- `random_high`: 8.77% GPU, calls=968, mean=281.34 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=294`: `{"Concrete Inputs":["","",""],"Input Dims":[[48,6144],[],[]],"Input Strides":[[6144,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::lift_fresh` via `external_id=96400`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
