# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_tnt__ca430502d1

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Model folder: `llm/qwen3_next/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `18.35%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 18.35% GPU, calls=768, mean=675.14 us
- `sharegpt_mid`: 7.48% GPU, calls=768, mean=442.44 us
- `sharegpt_high`: 12.55% GPU, calls=2688, mean=389.52 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=87558`: `{"Concrete Inputs":["",""],"Input Dims":[[17,2048],[2048,8]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=87552`: `{"Concrete Inputs":["",""],"Input Dims":[[17,2048],[2048,1536]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::mm` via `external_id=117530`: `{"Concrete Inputs":["",""],"Input Dims":[[262,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::reshape` via `external_id=117504`: `{"Concrete Inputs":["","[262, -1]"],"Input Dims":[[262,4,128],[]],"Input Strides":[[512,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
