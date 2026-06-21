# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_tnt__78a391e355

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `5.55%`
- Kernel name: `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 5.55% GPU, calls=60, mean=2207.66 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=9825`: `{"Concrete Inputs":["",""],"Input Dims":[[38,4096],[4096,4608]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::narrow` via `external_id=9833`: `{"Concrete Inputs":["","-1","0","256"],"Input Dims":[[38,8,512],[],[],[]],"Input Strides":[[4608,512,1],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
