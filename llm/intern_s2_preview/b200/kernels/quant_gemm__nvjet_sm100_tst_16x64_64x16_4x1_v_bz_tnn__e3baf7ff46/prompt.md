# KDA Prompt: quant_gemm__nvjet_sm100_tst_16x64_64x16_4x1_v_bz_tnn__e3baf7ff46

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `internLM/Intern-S2-Preview`
- Model folder: `llm/intern_s2_preview/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `21.26%`
- Kernel name: `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 21.26% GPU, calls=8640, mean=31.15 us
- `random_mid`: 8.99% GPU, calls=2880, mean=86.43 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=3018`: `{"Concrete Inputs":["",""],"Input Dims":[[38,2048],[2048,1536]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
