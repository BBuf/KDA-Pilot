# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x8_64x12_2x1_v_bz_tnt__da4bd0e0be

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`
- Model folder: `llm/nemotron3_nano/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `3.44%`
- Kernel name: `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 3.44% GPU, calls=9, mean=105.20 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=52928`: `{"Concrete Inputs":["",""],"Input Dims":[[1,2688],[2688,131072]],"Input Strides":[[2688,1],[1,2688]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
