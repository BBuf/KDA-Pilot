# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__6dd18c84c0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.7-Code`
- Model folder: `llm/kimi_k27_code/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `8.16%`
- Kernel name: `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 8.16% GPU, calls=960, mean=460.18 us

## Promoted Shape Samples

1. `aten::empty_strided` via `external_id=139121`: `{"Concrete Inputs":["[51, 7168]","[7168, 1]","15","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
2. `aten::mm` via `external_id=140347`: `{"Concrete Inputs":["",""],"Input Dims":[[51,7168],[7168,384]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
