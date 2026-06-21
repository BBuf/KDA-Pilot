# KDA Prompt: moe__finalizekernel__6a7a068b8f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `mistralai/Mistral-Small-4-119B-2603`
- Model folder: `llm/mistral_small4/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.47%`
- Kernel name: `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.40% GPU, calls=324, mean=3.80 us
- `sharegpt_low`: 2.47% GPU, calls=324, mean=3.77 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=1859`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","64","3"],"Input Dims":[[38,128],[],[38,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`
2. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=45493`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","32","3"],"Input Dims":[[18,128],[],[18,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
