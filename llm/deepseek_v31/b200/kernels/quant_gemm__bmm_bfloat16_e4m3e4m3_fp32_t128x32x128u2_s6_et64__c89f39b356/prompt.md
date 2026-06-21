# KDA Prompt: quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x32x128u2_s6_et64__c89f39b356

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V3.1`
- Model folder: `llm/deepseek_v31/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `6.73%`
- Kernel name: `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 6.73% GPU, calls=3776, mean=91.66 us
- `sharegpt_high`: 2.92% GPU, calls=2832, mean=95.12 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=77821`: `{"Concrete Inputs":["","","","","","","","","256","8","8","4","256","0","256","2.5","2","False","0","","2048","1","3"],"Input Dims":[[1427,256],[256],[1427,7168],[56,1427],[256,512,7168],[256,4,56],[256,7168,256],[256,56,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[1],[7168,1],[1427,1],[3670016,7168,1],[224,56,1],[1835008,256,1],[112,2,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=167202`: `{"Concrete Inputs":["","","","","","","","","256","8","8","4","256","0","256","2.5","2","False","0","","2048","1","3"],"Input Dims":[[1502,256],[256],[1502,7168],[56,1502],[256,512,7168],[256,4,56],[256,7168,256],[256,56,2],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[1],[7168,1],[1502,1],[3670016,7168,1],[224,56,1],[1835008,256,1],[112,2,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
