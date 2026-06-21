# KDA Prompt: quant_gemm__nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_tnt__d6cc26eceb

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.72%`
- Kernel name: `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 4.72% GPU, calls=180, mean=450.31 us
- `sharegpt_high`: 2.03% GPU, calls=240, mean=493.85 us

## Promoted Shape Samples

1. `aten::linear` via `external_id=28529`: `{"Concrete Inputs":["","",""],"Input Dims":[[17070,4096],[1,4096],[]],"Input Strides":[[4096,1],[4096,1],[]],"Input type":["c10::BFloat16","c10::BFloat16",""]}`
2. `aten::arange` via `external_id=28169`: `{"Concrete Inputs":["0","10","1",""],"Input Dims":[[],[],[],[0]],"Input Strides":[[],[],[],[1]],"Input type":["Scalar","Scalar","Scalar","long int"]}`
3. `aten::view` via `external_id=159589`: `{"Concrete Inputs":["","[-1, 128]"],"Input Dims":[[1,20968,16,128],[]],"Input Strides":[[42942464,2048,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `aten::t` via `external_id=157219`: `{"Concrete Inputs":[""],"Input Dims":[[4096,2048]],"Input Strides":[[2048,1]],"Input type":["c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
