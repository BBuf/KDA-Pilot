# KDA Prompt: quant_gemm__nvjet_hsh_32x64_64x16_4x1_v_bz_splitk_tnn__be91d90e63

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `3.08%`
- Kernel name: `nvjet_hsh_32x64_64x16_4x1_v_bz_splitK_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 3.08% GPU, calls=10560, mean=5.28 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=14933`: `{"Concrete Inputs":["",""],"Input Dims":[[4,4096],[4096,1280]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::Half","c10::Half"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
