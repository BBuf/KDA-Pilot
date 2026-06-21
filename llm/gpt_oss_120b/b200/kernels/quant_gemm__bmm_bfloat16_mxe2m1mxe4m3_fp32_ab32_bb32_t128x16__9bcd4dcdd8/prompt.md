# KDA Prompt: quant_gemm__bmm_bfloat16_mxe2m1mxe4m3_fp32_ab32_bb32_t128x16__9bcd4dcdd8

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.21%`
- Kernel name: `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x16x256_s4_et128x16_m128x16x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.21% GPU, calls=612, mean=19.04 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=17822`: `{"Concrete Inputs":["","0","0","150","1"],"Input Dims":[[160,512],[],[],[],[]],"Input Strides":[[640,1],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
