# KDA Prompt: other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x64x128u2__92e5ff29e3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `other`
- Max observed GPU share: `7.54%`
- Kernel name: `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 5.78% GPU, calls=160, mean=618.38 us
- `random_high`: 7.54% GPU, calls=480, mean=603.57 us
- `sharegpt_mid`: 4.73% GPU, calls=160, mean=409.79 us
- `sharegpt_high`: 6.72% GPU, calls=480, mean=444.09 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=16016`: `{"Concrete Inputs":["[1, 128, 2, 128, 128]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
2. `aten::as_strided` via `external_id=57208`: `{"Concrete Inputs":["","[5]","[1]","94"],"Input Dims":[[165],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`
3. `aten::item` via `external_id=46226`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["long int"]}`
4. `aten::remainder` via `external_id=89733`: `{"Concrete Inputs":["","128"],"Input Dims":[[],[]],"Input Strides":[[],[]],"Input type":["int","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
