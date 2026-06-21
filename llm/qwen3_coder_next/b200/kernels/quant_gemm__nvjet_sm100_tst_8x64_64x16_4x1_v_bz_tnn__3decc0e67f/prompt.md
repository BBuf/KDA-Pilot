# KDA Prompt: quant_gemm__nvjet_sm100_tst_8x64_64x16_4x1_v_bz_tnn__3decc0e67f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-Next`
- Model folder: `llm/qwen3_coder_next/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.82%`
- Kernel name: `nvjet_sm100_tst_8x64_64x16_4x1_v_bz_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 2.82% GPU, calls=768, mean=49.80 us

## Promoted Shape Samples

1. `aten::empty_like` via `external_id=176542`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[118,2048],[],[],[],[],[]],"Input Strides":[[2048,1],[],[],[],[],[]],"Input type":["c10::BFloat16","","","","Scalar",""]}`
2. `aten::reshape` via `external_id=176704`: `{"Concrete Inputs":["","[-1, 128]"],"Input Dims":[[1,118,16,128],[]],"Input Strides":[[241664,2048,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
