# KDA Prompt: comm__comm__9dd2e02622

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `comm`
- Max observed GPU share: `18.50%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 18.50% GPU, calls=260, mean=447.14 us
- `sharegpt_high`: 7.02% GPU, calls=260, mean=364.92 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=42584`: `{"Concrete Inputs":["","",""],"Input Dims":[[334,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `sgl_kernel::moe_sum_reduce` via `external_id=41849`: `{"Concrete Inputs":["","","2.5"],"Input Dims":[[334,8,4096],[334,4096],[]],"Input Strides":[[32768,4096,1],[4096,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
3. `sglang::outplace_all_reduce` via `external_id=82116`: `{"Concrete Inputs":["","",""],"Input Dims":[[1160,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
