# KDA Prompt: other__other__00ff8f7a29

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/GLM-5-NVFP4`
- Model folder: `llm/glm_5/b200`
- Kernel category: `other`
- Max observed GPU share: `3.73%`
- Kernel name: `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 2.73% GPU, calls=5616, mean=11.44 us
- `sharegpt_high`: 3.73% GPU, calls=5616, mean=33.74 us

## Promoted Shape Samples

1. `sglang::hadamard_transform` via `external_id=146889`: `{"Concrete Inputs":["","0.088388347648318447"],"Input Dims":[[9962,32,128],[]],"Input Strides":[[4096,128,1],[]],"Input type":["c10::BFloat16","Scalar"]}`
2. `aten::as_strided` via `external_id=140705`: `{"Concrete Inputs":["","[9962, 16, 192]","[4096, 256, 1]","0"],"Input Dims":[[9962,16,256],[],[],[]],"Input Strides":[[4096,256,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `sglang::hadamard_transform` via `external_id=213671`: `{"Concrete Inputs":["","0.088388347648318447"],"Input Dims":[[20784,32,128],[]],"Input Strides":[[4096,128,1],[]],"Input type":["c10::BFloat16","Scalar"]}`
4. `aten::as_strided` via `external_id=211923`: `{"Concrete Inputs":["","[98]","[0]",""],"Input Dims":[[100],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
