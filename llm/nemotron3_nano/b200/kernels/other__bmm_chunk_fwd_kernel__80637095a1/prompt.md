# KDA Prompt: other__bmm_chunk_fwd_kernel__80637095a1

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`
- Model folder: `llm/nemotron3_nano/b200`
- Kernel category: `other`
- Max observed GPU share: `2.20%`
- Kernel name: `_bmm_chunk_fwd_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.16% GPU, calls=69, mean=74.49 us
- `random_high`: 2.20% GPU, calls=115, mean=124.60 us

## Promoted Shape Samples

1. `sglang::nemotron_mamba2_with_output` via `external_id=9267`: `{"Concrete Inputs":["","","0"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
2. `sglang::nemotron_mamba2_with_output` via `external_id=11889`: `{"Concrete Inputs":["","","48"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
3. `sglang::nemotron_mamba2_with_output` via `external_id=10903`: `{"Concrete Inputs":["","","30"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
4. `sglang::nemotron_mamba2_with_output` via `external_id=9872`: `{"Concrete Inputs":["","","11"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
