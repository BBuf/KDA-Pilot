# KDA Prompt: quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x8x128u2_s8_et64x8_m6__499a6a5a0c

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen36/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `10.76%`
- Kernel name: `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 10.37% GPU, calls=369, mean=18.57 us
- `sharegpt_low`: 10.03% GPU, calls=369, mean=17.78 us
- `sharegpt_mid`: 10.76% GPU, calls=338, mean=65.42 us
- `sharegpt_high`: 3.32% GPU, calls=92, mean=60.50 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=626`: `{"Concrete Inputs":["","","","","","","","","256","8","","","512","0","256","1.","4","False","0","","64","1","3"],"Input Dims":[[38,256],[],[38,2048],[16,38],[256,1024,2048],[256,8,16],[256,2048,512],[256,16,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[],[2048,1],[38,1],[2097152,2048,1],[128,16,1],[1048576,512,1],[64,4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=85661`: `{"Concrete Inputs":["","","","","","","","","256","8","","","512","0","256","1.","4","False","0","","32","1","3"],"Input Dims":[[17,256],[],[17,2048],[16,17],[256,1024,2048],[256,8,16],[256,2048,512],[256,16,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[],[2048,1],[17,1],[2097152,2048,1],[128,16,1],[1048576,512,1],[64,4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
3. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=135786`: `{"Concrete Inputs":["","","","","","","","","256","8","","","512","0","256","1.","4","False","0","","512","1","3"],"Input Dims":[[264,256],[],[264,2048],[16,264],[256,1024,2048],[256,8,16],[256,2048,512],[256,16,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[],[2048,1],[264,1],[2097152,2048,1],[128,16,1],[1048576,512,1],[64,4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
4. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=126258`: `{"Concrete Inputs":["","","","","","","","","256","8","","","512","0","256","1.","4","False","0","","512","1","3"],"Input Dims":[[267,256],[],[267,2048],[16,267],[256,1024,2048],[256,8,16],[256,2048,512],[256,16,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[],[2048,1],[267,1],[2097152,2048,1],[128,16,1],[1048576,512,1],[64,4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
