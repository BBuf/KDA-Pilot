# KDA Prompt: other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x8x128u2__7b9748cb9a

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507`
- Model folder: `llm/qwen3/b200`
- Kernel category: `other`
- Max observed GPU share: `3.75%`
- Kernel name: `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 3.75% GPU, calls=470, mean=55.62 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=271`: `{"Concrete Inputs":["","0","1","2","1"],"Input Dims":[[2],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
