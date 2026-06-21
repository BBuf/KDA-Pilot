# KDA Prompt: comm__comm__9dd2e02622

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `comm`
- Max observed GPU share: `6.93%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 6.93% GPU, calls=356, mean=333.22 us
- `random_high`: 2.60% GPU, calls=356, mean=280.70 us
- `sharegpt_mid`: 6.12% GPU, calls=356, mean=238.15 us
- `sharegpt_high`: 6.13% GPU, calls=1068, mean=182.19 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=22919`: `{"Concrete Inputs":["","[2, 1, 1]","[1, 1, 1]",""],"Input Dims":[[2,1],[],[],[]],"Input Strides":[[1,1],[],[],[]],"Input type":["bool","ScalarList","ScalarList",""]}`
2. `sglang::outplace_all_reduce` via `external_id=22295`: `{"Concrete Inputs":["","",""],"Input Dims":[[683,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
3. `sglang::outplace_all_reduce` via `external_id=68932`: `{"Concrete Inputs":["","",""],"Input Dims":[[694,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
4. `aten::as_strided` via `external_id=69921`: `{"Concrete Inputs":["","[694, 2048]","[4640, 1]","0"],"Input Dims":[[694,4640],[],[],[]],"Input Strides":[[4640,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
