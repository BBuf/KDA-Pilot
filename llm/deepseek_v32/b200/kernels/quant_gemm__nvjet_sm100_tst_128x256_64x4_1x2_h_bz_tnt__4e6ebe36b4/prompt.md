# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x4_1x2_h_bz_tnt__4e6ebe36b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.17%`
- Kernel name: `nvjet_sm100_tst_128x256_64x4_1x2_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 2.17% GPU, calls=244, mean=178.25 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=106472`: `{"Concrete Inputs":["",""],"Input Dims":[[8630,7168],[7168,2112]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
