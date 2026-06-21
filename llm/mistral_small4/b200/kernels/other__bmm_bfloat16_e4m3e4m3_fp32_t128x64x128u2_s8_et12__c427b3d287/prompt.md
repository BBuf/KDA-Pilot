# KDA Prompt: other__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s8_et12__c427b3d287

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `mistralai/Mistral-Small-4-119B-2603`
- Model folder: `llm/mistral_small4/b200`
- Kernel category: `other`
- Max observed GPU share: `9.05%`
- Kernel name: `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s8_et128x64_m256x64x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 9.05% GPU, calls=36, mean=518.11 us
- `random_high`: 2.86% GPU, calls=36, mean=171.26 us
- `sharegpt_mid`: 6.83% GPU, calls=36, mean=301.14 us
- `sharegpt_high`: 3.36% GPU, calls=36, mean=183.97 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=17791`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","16384","3"],"Input Dims":[[11179,128],[],[11179,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`
2. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=39474`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","2048","3"],"Input Dims":[[1215,128],[],[1215,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`
3. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=58744`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","8192","3"],"Input Dims":[[5519,128],[],[5519,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`
4. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=84975`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","2048","3"],"Input Dims":[[2012,128],[],[2012,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
