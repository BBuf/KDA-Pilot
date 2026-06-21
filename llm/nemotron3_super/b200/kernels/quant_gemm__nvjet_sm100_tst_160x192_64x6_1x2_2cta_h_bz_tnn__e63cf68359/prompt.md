# KDA Prompt: quant_gemm__nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_tnn__e63cf68359

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `3.48%`
- Kernel name: `nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_TNN`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 3.48% GPU, calls=160, mean=372.27 us
- `random_high`: 3.10% GPU, calls=320, mean=372.16 us
- `sharegpt_high`: 2.10% GPU, calls=320, mean=208.72 us

## Promoted Shape Samples

1. `aten::index_put_` via `external_id=18513`: `{"Concrete Inputs":["","","","False"],"Input Dims":[[1025,32,64,128],[],[30,32,64,128],[]],"Input Strides":[[262144,8192,128,1],[],[262144,8192,128,1],[]],"Input type":["float","","float","Scalar"]}`
2. `aten::slice` via `external_id=19493`: `{"Concrete Inputs":["","0","0","16384","1"],"Input Dims":[[16384,2560],[],[],[],[]],"Input Strides":[[2560,1],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::as_strided` via `external_id=20403`: `{"Concrete Inputs":["","[262148]","[1]","6029404"],"Input Dims":[[342,262148],[],[],[]],"Input Strides":[[262148,1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`
4. `aten::slice` via `external_id=20088`: `{"Concrete Inputs":["","0","0","1","1"],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
