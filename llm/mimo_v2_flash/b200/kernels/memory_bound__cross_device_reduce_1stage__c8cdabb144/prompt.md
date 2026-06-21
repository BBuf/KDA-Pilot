# KDA Prompt: memory_bound__cross_device_reduce_1stage__c8cdabb144

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`memory_bound` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `XiaomiMiMo/MiMo-V2-Flash`
- Model folder: `llm/mimo_v2_flash/b200`
- Kernel category: `memory_bound`
- Max observed GPU share: `93.86%`
- Kernel name: `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 60.19% GPU, calls=6216, mean=954.56 us
- `random_mid`: 93.20% GPU, calls=6984, mean=889.49 us
- `random_high`: 93.13% GPU, calls=6984, mean=880.11 us
- `sharegpt_low`: 92.38% GPU, calls=6984, mean=787.32 us
- `sharegpt_mid`: 93.86% GPU, calls=6984, mean=997.28 us
- `sharegpt_high`: 92.61% GPU, calls=6984, mean=814.74 us

## Promoted Shape Samples

1. `sgl_kernel::all_reduce` via `external_id=1252353`: `{"Concrete Inputs":["892916160","","","140122326564864","8388608"],"Input Dims":[[],[4,4096],[4,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`
2. `aten::resolve_conj` via `external_id=1213867`: `{"Concrete Inputs":[""],"Input Dims":[[2]],"Input Strides":[[24]],"Input type":["long int"]}`
3. `sgl_kernel::all_reduce` via `external_id=1277498`: `{"Concrete Inputs":["846838800","","","139831778738176","8388608"],"Input Dims":[[],[4,4096],[4,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`
4. `c10d::_allgather_base_` via `external_id=1195113`: `{"Concrete Inputs":["","","","False","-1"],"Input Dims":[[48],[6],[],[],[]],"Input Strides":[[1],[1],[],[],[]],"Input type":["long int","long int","","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
