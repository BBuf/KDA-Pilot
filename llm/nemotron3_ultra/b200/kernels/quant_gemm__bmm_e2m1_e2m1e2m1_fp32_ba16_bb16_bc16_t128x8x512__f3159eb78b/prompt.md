# KDA Prompt: quant_gemm__bmm_e2m1_e2m1e2m1_fp32_ba16_bb16_bc16_t128x8x512__f3159eb78b

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Model folder: `llm/nemotron3_ultra/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.97%`
- Kernel name: `bmm_E2m1_E2m1E2m1_Fp32_bA16_bB16_bC16_t128x8x512u2_s5_et128x8_m128x8x64_c1x1x1_16dp256b_rM_TN_transOut_schPd2x1x2x3_biasFp32M_relu2_bN_ldgsts_ldgstsSf_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.97% GPU, calls=864, mean=21.84 us

## Promoted Shape Samples

1. `aten::view` via `external_id=3101`: `{"Concrete Inputs":["","[38, 2560]"],"Input Dims":[[38,2560],[]],"Input Strides":[[2560,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
2. `aten::pow` via `external_id=6222`: `{"Concrete Inputs":["","2"],"Input Dims":[[38,2,2048],[]],"Input Strides":[[4096,2048,1],[]],"Input type":["float","Scalar"]}`
3. `aten::empty` via `external_id=9343`: `{"Concrete Inputs":["[1, 1, 64, 64, 128]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
