# KDA Prompt: other__chunk_scan_fwd_kernel__e84657f454

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `other`
- Max observed GPU share: `12.59%`
- Kernel name: `_chunk_scan_fwd_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 6.96% GPU, calls=480, mean=248.39 us
- `random_high`: 12.59% GPU, calls=800, mean=604.50 us
- `sharegpt_mid`: 9.25% GPU, calls=480, mean=267.22 us

## Promoted Shape Samples

1. `sglang::nemotron_mamba2_with_output` via `external_id=19001`: `{"Concrete Inputs":["","","71"],"Input Dims":[[16384,4096],[16384,4096],[]],"Input Strides":[[4096,1],[4096,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
2. `sglang::nemotron_mamba2_with_output` via `external_id=19106`: `{"Concrete Inputs":["","","73"],"Input Dims":[[16384,4096],[16384,4096],[]],"Input Strides":[[4096,1],[4096,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
3. `aten::as_strided` via `external_id=17803`: `{"Concrete Inputs":["","[16384, 2, 128]","[2560, 128, 1]",""],"Input Dims":[[1,16384,2,128],[],[],[]],"Input Strides":[[41943040,2560,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`
4. `sglang::nemotron_mamba2_with_output` via `external_id=19771`: `{"Concrete Inputs":["","","86"],"Input Dims":[[16384,4096],[16384,4096],[]],"Input Strides":[[4096,1],[4096,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
