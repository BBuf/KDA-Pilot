# KDA Prompt: memory_bound__cross_device_reduce_2stage__9697743b4f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`memory_bound` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `memory_bound`
- Max observed GPU share: `40.12%`
- Kernel name: `void sglang::cross_device_reduce_2stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 38.47% GPU, calls=1312, mean=530.62 us
- `random_high`: 40.12% GPU, calls=10784, mean=208.98 us

## Promoted Shape Samples

1. `sgl_kernel::all_reduce` via `external_id=245`: `{"Concrete Inputs":["597603008","","","140569036718080","8388608"],"Input Dims":[[],[38,4096],[38,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::Half","c10::Half","Scalar","Scalar"]}`
2. `sgl_kernel::all_reduce` via `external_id=69625`: `{"Concrete Inputs":["623900928","","","139661288669184","8388608"],"Input Dims":[[],[333,4096],[333,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::Half","c10::Half","Scalar","Scalar"]}`
3. `aten::as_strided` via `external_id=68815`: `{"Concrete Inputs":["","[50]","[1]","866"],"Input Dims":[[1210],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
