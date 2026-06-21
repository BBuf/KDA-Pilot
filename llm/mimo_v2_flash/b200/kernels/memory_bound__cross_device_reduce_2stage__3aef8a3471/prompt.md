# KDA Prompt: memory_bound__cross_device_reduce_2stage__3aef8a3471

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`memory_bound` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `XiaomiMiMo/MiMo-V2-Flash`
- Model folder: `llm/mimo_v2_flash/b200`
- Kernel category: `memory_bound`
- Max observed GPU share: `34.97%`
- Kernel name: `void sglang::cross_device_reduce_2stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 34.97% GPU, calls=768, mean=4489.03 us

## Promoted Shape Samples

1. `aten::lift_fresh` via `external_id=1216446`: `{"Concrete Inputs":[""],"Input Dims":[[0]],"Input Strides":[[1]],"Input type":["float"]}`
2. `aten::resolve_neg` via `external_id=1197002`: `{"Concrete Inputs":[""],"Input Dims":[[2]],"Input Strides":[[24]],"Input type":["long int"]}`
3. `sgl_kernel::all_reduce` via `external_id=1216651`: `{"Concrete Inputs":["892916160","","","140122326564864","8388608"],"Input Dims":[[],[40,4096],[40,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`
4. `aten::select` via `external_id=1177769`: `{"Concrete Inputs":["","1","0"],"Input Dims":[[2,2],[],[]],"Input Strides":[[24,1],[],[]],"Input type":["long int","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
