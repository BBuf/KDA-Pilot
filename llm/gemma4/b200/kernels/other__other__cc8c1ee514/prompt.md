# KDA Prompt: other__other__cc8c1ee514

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `google/gemma-4-26B-A4B-it`
- Model folder: `llm/gemma4/b200`
- Kernel category: `other`
- Max observed GPU share: `2.16%`
- Kernel name: `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)1, true, false>((anonymous namespace)::ActivationParams)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.16% GPU, calls=270, mean=13.29 us

## Promoted Shape Samples

1. `sglang::_run_activation_inplace` via `external_id=11396`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[90032,1408],[90032,704]],"Input Strides":[[],[1408,1],[704,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
