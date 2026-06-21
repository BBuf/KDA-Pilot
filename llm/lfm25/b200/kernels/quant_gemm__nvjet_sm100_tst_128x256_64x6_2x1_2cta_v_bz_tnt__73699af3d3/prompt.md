# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Model folder: `llm/lfm25/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `11.24%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 5.08% GPU, calls=44, mean=94.86 us
- `random_high`: 11.24% GPU, calls=200, mean=118.60 us
- `sharegpt_mid`: 5.65% GPU, calls=52, mean=95.46 us
- `sharegpt_high`: 6.59% GPU, calls=78, mean=138.52 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=8407`: `{"Concrete Inputs":["",""],"Input Dims":[[7505,2048],[2048,14336]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=8358`: `{"Concrete Inputs":["",""],"Input Dims":[[7505,2048],[2048,6144]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::mm` via `external_id=30085`: `{"Concrete Inputs":["",""],"Input Dims":[[16384,2048],[2048,14336]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::mm` via `external_id=23723`: `{"Concrete Inputs":["",""],"Input Dims":[[14750,2048],[2048,14336]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
