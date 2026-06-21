# KDA Prompt: other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x16x128u2__fcc001e5b0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `other`
- Max observed GPU share: `2.99%`
- Kernel name: `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s4_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.99% GPU, calls=720, mean=15.41 us

## Promoted Shape Samples

1. `aten::expand` via `external_id=389`: `{"Concrete Inputs":["","[38]","False"],"Input Dims":[[38],[],[]],"Input Strides":[[1],[],[]],"Input type":["int","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
