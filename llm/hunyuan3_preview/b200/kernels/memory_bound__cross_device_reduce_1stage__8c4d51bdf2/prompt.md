# KDA Prompt: memory_bound__cross_device_reduce_1stage__8c4d51bdf2

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`memory_bound` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `memory_bound`
- Max observed GPU share: `44.46%`
- Kernel name: `void sglang::cross_device_reduce_1stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 44.46% GPU, calls=3936, mean=599.36 us
- `sharegpt_high`: 30.75% GPU, calls=2616, mean=650.68 us

## Promoted Shape Samples

1. `sgl_kernel::all_reduce` via `external_id=136597`: `{"Concrete Inputs":["434645568","","","139898115850240","8388608"],"Input Dims":[[],[6,4096],[6,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::Half","c10::Half","Scalar","Scalar"]}`
2. `aten::empty` via `external_id=135451`: `{"Concrete Inputs":["[768]","3","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
3. `aten::linear` via `external_id=185392`: `{"Concrete Inputs":["","",""],"Input Dims":[[31,1024],[4096,1024],[]],"Input Strides":[[1024,1],[1024,1],[]],"Input type":["c10::Half","c10::Half",""]}`
4. `sgl_kernel::all_reduce` via `external_id=187218`: `{"Concrete Inputs":["623900928","","","139661288669184","8388608"],"Input Dims":[[],[31,4096],[31,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::Half","c10::Half","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
