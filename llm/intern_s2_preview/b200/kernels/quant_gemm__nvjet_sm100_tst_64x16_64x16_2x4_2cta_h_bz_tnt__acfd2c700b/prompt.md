# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_tnt__acfd2c700b

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `internLM/Intern-S2-Preview`
- Model folder: `llm/intern_s2_preview/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.80%`
- Kernel name: `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 4.80% GPU, calls=640, mean=369.92 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=156174`: `{"Concrete Inputs":["",""],"Input Dims":[[632,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::transpose` via `external_id=157601`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[128,2048],[],[]],"Input Strides":[[2048,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
