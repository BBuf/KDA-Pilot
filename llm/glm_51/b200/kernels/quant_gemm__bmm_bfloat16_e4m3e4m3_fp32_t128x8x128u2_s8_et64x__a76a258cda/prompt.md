# KDA Prompt: quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x8x128u2_s8_et64x__a76a258cda

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.1-FP8`
- Model folder: `llm/glm_51/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.13%`
- Kernel name: `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.13% GPU, calls=5472, mean=16.12 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=20249`: `{"Concrete Inputs":["","","","","","","","","256","8","1","1","256","0","256","2.5","2","False","0","","64","1","3"],"Input Dims":[[38,256],[256],[38,6144],[48,38],[256,512,6144],[256,4,48],[256,6144,256],[256,48,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[1],[6144,1],[38,1],[3145728,6144,1],[192,48,1],[1572864,256,1],[96,2,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sgl_kernel::sgl_per_token_group_quant_8bit_v2` via `external_id=16023`: `{"Concrete Inputs":["","","","128","1e-10","-448.","448.","False","False",""],"Input Dims":[[38,6144],[38,6144],[38,48],[],[],[],[],[],[],[]],"Input Strides":[[6144,1],[6144,1],[48,1],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
