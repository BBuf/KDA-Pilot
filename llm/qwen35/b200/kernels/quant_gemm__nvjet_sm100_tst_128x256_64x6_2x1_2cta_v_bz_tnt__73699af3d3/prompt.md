# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `11.81%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 5.49% GPU, calls=1020, mean=92.35 us
- `random_high`: 11.81% GPU, calls=1680, mean=256.00 us
- `sharegpt_mid`: 2.99% GPU, calls=240, mean=256.70 us
- `sharegpt_high`: 3.16% GPU, calls=1200, mean=153.55 us

## Promoted Shape Samples

1. `aten::matmul` via `external_id=35033`: `{"Concrete Inputs":["",""],"Input Dims":[[17070,4096],[4096,512]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=59274`: `{"Concrete Inputs":["",""],"Input Dims":[[30758,4096],[4096,5120]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::mm` via `external_id=122502`: `{"Concrete Inputs":["",""],"Input Dims":[[10501,4096],[4096,5120]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::empty` via `external_id=121868`: `{"Concrete Inputs":["[1, 183, 16, 128, 128]","15","0","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
