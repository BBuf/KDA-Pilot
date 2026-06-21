# KDA Prompt: other__other__00ff8f7a29

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `other`
- Max observed GPU share: `4.04%`
- Kernel name: `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 4.04% GPU, calls=4392, mean=18.41 us

## Promoted Shape Samples

1. `sglang::hadamard_transform` via `external_id=109568`: `{"Concrete Inputs":["","0.088388347648318447"],"Input Dims":[[8630,64,128],[]],"Input Strides":[[8192,128,1],[]],"Input type":["c10::BFloat16","Scalar"]}`
2. `aten::as_strided` via `external_id=107608`: `{"Concrete Inputs":["","[8630, 10358]","[10616, 1]","0"],"Input Dims":[[8630,10616],[],[],[]],"Input Strides":[[10616,1],[],[],[]],"Input type":["float","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
