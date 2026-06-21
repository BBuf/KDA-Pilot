# KDA Prompt: norm__rmsnormkernel__1f38514bcf

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`norm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.5-Flash`
- Model folder: `llm/step35_flash/b200`
- Kernel category: `norm`
- Max observed GPU share: `2.92%`
- Kernel name: `void flashinfer::norm::RMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.64% GPU, calls=4896, mean=2.71 us
- `random_mid`: 2.92% GPU, calls=4896, mean=2.71 us
- `random_high`: 2.69% GPU, calls=4896, mean=2.72 us
- `sharegpt_low`: 2.82% GPU, calls=4896, mean=2.69 us
- `sharegpt_mid`: 2.71% GPU, calls=4896, mean=2.70 us

## Promoted Shape Samples

1. `sgl_kernel::gemma_rmsnorm` via `external_id=538414`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","True"],"Input Dims":[[38,4096],[38,4096],[4096],[],[]],"Input Strides":[[4096,1],[4096,1],[1],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar"]}`
2. `c10d::broadcast_` via `external_id=24250`: `{"Concrete Inputs":["","","0","0","False","-1"],"Input Dims":[[[1]],[],[],[],[],[]],"Input Strides":[[[1]],[],[],[],[],[]],"Input type":["TensorList","","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::to` via `external_id=23256`: `{"Concrete Inputs":["","","4","False","False",""],"Input Dims":[[1],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["long int","","Scalar","Scalar","Scalar",""]}`
4. `gloo:broadcast` via `external_id=22263`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
