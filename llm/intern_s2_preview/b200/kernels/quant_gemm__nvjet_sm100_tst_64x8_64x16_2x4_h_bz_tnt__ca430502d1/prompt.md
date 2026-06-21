# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_tnt__ca430502d1

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `internLM/Intern-S2-Preview`
- Model folder: `llm/intern_s2_preview/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `17.09%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 5.37% GPU, calls=3520, mean=53.44 us
- `sharegpt_low`: 17.09% GPU, calls=320, mean=656.97 us
- `sharegpt_mid`: 5.44% GPU, calls=640, mean=262.84 us
- `sharegpt_high`: 10.91% GPU, calls=3200, mean=168.26 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=41145`: `{"Concrete Inputs":["",""],"Input Dims":[[274,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=82481`: `{"Concrete Inputs":["",""],"Input Dims":[[17,2048],[2048,1536]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::view` via `external_id=108518`: `{"Concrete Inputs":["","[-1]"],"Input Dims":[[267,2048],[]],"Input Strides":[[2048,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `aten::mm` via `external_id=109160`: `{"Concrete Inputs":["",""],"Input Dims":[[267,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
