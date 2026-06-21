# KDA Prompt: comm__comm__9dd2e02622

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-XS.2-FP8`
- Model folder: `llm/poolside_laguna_xs2/b200`
- Kernel category: `comm`
- Max observed GPU share: `12.60%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 4.15% GPU, calls=324, mean=52.42 us
- `sharegpt_high`: 12.60% GPU, calls=648, mean=86.61 us

## Promoted Shape Samples

1. `aten::cat` via `external_id=21160`: `{"Concrete Inputs":["","0"],"Input Dims":[[[704]],[]],"Input Strides":[[[1]],[]],"Input type":["TensorList","Scalar"]}`
2. `aten::narrow` via `external_id=51125`: `{"Concrete Inputs":["","0","320","41"],"Input Dims":[[361],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar"]}`
3. `aten::cat` via `external_id=55830`: `{"Concrete Inputs":["","0"],"Input Dims":[[[512]],[]],"Input Strides":[[[1]],[]],"Input type":["TensorList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
