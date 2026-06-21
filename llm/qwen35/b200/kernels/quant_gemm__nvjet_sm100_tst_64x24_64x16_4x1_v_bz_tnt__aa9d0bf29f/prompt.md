# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x24_64x16_4x1_v_bz_tnt__aa9d0bf29f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `14.15%`
- Kernel name: `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 14.15% GPU, calls=180, mean=807.15 us
- `sharegpt_mid`: 5.40% GPU, calls=180, mean=618.64 us
- `sharegpt_high`: 2.10% GPU, calls=180, mean=681.44 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=92277`: `{"Concrete Inputs":["",""],"Input Dims":[[17,4096],[4096,5120]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `detach_` via `external_id=104579`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["int"]}`
3. `aten::empty_like` via `external_id=106353`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[17,4096],[],[],[],[],[]],"Input Strides":[[4096,1],[],[],[],[],[]],"Input type":["c10::BFloat16","","","","Scalar",""]}`
4. `aten::empty` via `external_id=149893`: `{"Concrete Inputs":["[1, 17, 4, 128]","15","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
