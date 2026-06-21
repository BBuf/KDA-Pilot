# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_1x2_h_bz_tnt__2857e52688

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `internLM/Intern-S2-Preview`
- Model folder: `llm/intern_s2_preview/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `9.04%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 9.04% GPU, calls=640, mean=437.06 us

## Promoted Shape Samples

1. `aten::transpose` via `external_id=89659`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[1,2048],[],[]],"Input Strides":[[2048,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`
2. `aten::empty` via `external_id=89823`: `{"Concrete Inputs":["[1]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
