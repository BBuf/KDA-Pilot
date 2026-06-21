# KDA Prompt: other__chunk_scan_fwd_kernel__e84657f454

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`
- Model folder: `llm/nemotron3_nano/b200`
- Kernel category: `other`
- Max observed GPU share: `20.57%`
- Kernel name: `_chunk_scan_fwd_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 13.76% GPU, calls=69, mean=475.04 us
- `random_high`: 19.38% GPU, calls=115, mean=1095.25 us
- `sharegpt_mid`: 17.50% GPU, calls=92, mean=395.82 us
- `sharegpt_high`: 20.57% GPU, calls=138, mean=802.62 us

## Promoted Shape Samples

1. `sglang::nemotron_mamba2_with_output` via `external_id=11777`: `{"Concrete Inputs":["","","46"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
2. `sglang::nemotron_mamba2_with_output` via `external_id=10522`: `{"Concrete Inputs":["","","23"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
3. `sglang::nemotron_mamba2_with_output` via `external_id=10791`: `{"Concrete Inputs":["","","28"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
4. `sglang::nemotron_mamba2_with_output` via `external_id=9267`: `{"Concrete Inputs":["","","0"],"Input Dims":[[9216,2688],[9216,2688],[]],"Input Strides":[[2688,1],[2688,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
