# KDA Prompt: norm__fusedaddrmsnormkernel__99f19a4e72

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`norm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Model folder: `llm/minimax_m3/b200`
- Kernel category: `norm`
- Max observed GPU share: `11.68%`
- Kernel name: `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 11.68% GPU, calls=2880, mean=135.91 us
- `random_high`: 11.08% GPU, calls=2880, mean=119.46 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=22081`: `{"Concrete Inputs":["","0","0","48","1"],"Input Dims":[[8192],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar","Scalar"]}`
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
