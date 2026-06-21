# KDA Prompt: memory_bound__cross_device_reduce_1stage__3aeea98c14

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`memory_bound` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.5-Flash`
- Model folder: `llm/step35_flash/b200`
- Kernel category: `memory_bound`
- Max observed GPU share: `49.34%`
- Kernel name: `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 4>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 48.64% GPU, calls=4788, mean=51.14 us
- `random_mid`: 43.33% GPU, calls=4788, mean=41.20 us
- `random_high`: 47.63% GPU, calls=4788, mean=49.07 us
- `sharegpt_low`: 47.27% GPU, calls=4788, mean=46.22 us
- `sharegpt_mid`: 49.34% GPU, calls=4788, mean=50.16 us
- `sharegpt_high`: 41.59% GPU, calls=4788, mean=37.15 us

## Promoted Shape Samples

1. `c10d::broadcast_` via `external_id=21726`: `{"Concrete Inputs":["","","0","0","False","-1"],"Input Dims":[[[1]],[],[],[],[],[]],"Input Strides":[[[1]],[],[],[],[],[]],"Input type":["TensorList","","Scalar","Scalar","Scalar","Scalar"]}`
2. `sgl_kernel::all_reduce` via `external_id=538411`: `{"Concrete Inputs":["567964400","","","139617332363264","8388608"],"Input Dims":[[],[38,4096],[38,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`
3. `sgl_kernel::all_reduce` via `external_id=951135`: `{"Concrete Inputs":["1067976048","","","140051157614592","8388608"],"Input Dims":[[],[38,4096],[38,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`
4. `sgl_kernel::all_reduce` via `external_id=786273`: `{"Concrete Inputs":["434008688","","","140625307500544","8388608"],"Input Dims":[[],[38,4096],[38,4096],[],[]],"Input Strides":[[],[4096,1],[4096,1],[],[]],"Input type":["Scalar","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
