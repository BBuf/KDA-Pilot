# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `6.24%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 3.29% GPU, calls=512, mean=110.11 us
- `random_high`: 6.24% GPU, calls=1888, mean=127.04 us
- `sharegpt_mid`: 5.51% GPU, calls=704, mean=108.50 us
- `sharegpt_high`: 5.74% GPU, calls=1376, mean=132.52 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=19203`: `{"Concrete Inputs":["",""],"Input Dims":[[16384,2048],[2048,4096]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::empty` via `external_id=18250`: `{"Concrete Inputs":["[1, 128, 32, 8192]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
3. `aten::reshape` via `external_id=20490`: `{"Concrete Inputs":["","[1, 1, 1, 1]"],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
4. `aten::split_with_sizes` via `external_id=17900`: `{"Concrete Inputs":["","[16384, 0]","0"],"Input Dims":[[16384,32],[],[]],"Input Strides":[[4640,1],[],[]],"Input type":["c10::BFloat16","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
