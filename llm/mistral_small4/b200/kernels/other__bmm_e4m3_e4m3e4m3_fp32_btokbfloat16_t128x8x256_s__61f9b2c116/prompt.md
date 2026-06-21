# KDA Prompt: other__bmm_e4m3_e4m3e4m3_fp32_btokbfloat16_t128x8x256_s__61f9b2c116

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `mistralai/Mistral-Small-4-119B-2603`
- Model folder: `llm/mistral_small4/b200`
- Kernel category: `other`
- Max observed GPU share: `7.00%`
- Kernel name: `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x8x256_s6_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 7.00% GPU, calls=36, mean=96.17 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_per_tensor_scale_moe_wrapper` via `external_id=44973`: `{"Concrete Inputs":["","","","","","","","","128","4","1","1","2048","0","128","1.","False","1","","32","3"],"Input Dims":[[18,128],[],[18,4096],[128,4096,4096],[128],[128],[128,4096,2048],[128],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[128,1],[],[4096,1],[16777216,4096,1],[1],[1],[8388608,2048,1],[1],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
