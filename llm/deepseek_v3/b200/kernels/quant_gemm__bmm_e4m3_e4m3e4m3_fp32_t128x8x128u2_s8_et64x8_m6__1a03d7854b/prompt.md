# KDA Prompt: quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x8x128u2_s8_et64x8_m6__1a03d7854b

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V3`
- Model folder: `llm/deepseek_v3/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.00%`
- Kernel name: `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schedS_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 2.00% GPU, calls=2183, mean=24.51 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=87818`: `{"Concrete Inputs":["","","","","","","","","256","8","8","4","256","0","256","2.5","2","False","0","","16","1","3"],"Input Dims":[[16,256],[256],[16,7168],[56,16],[256,512,7168],[256,4,56],[256,7168,256],[256,56,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[1],[7168,1],[16,1],[3670016,7168,1],[224,56,1],[1835008,256,1],[112,2,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["float","c10::BFloat16","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::transpose` via `external_id=87810`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[16,56],[],[]],"Input Strides":[[56,1],[],[]],"Input type":["float","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
