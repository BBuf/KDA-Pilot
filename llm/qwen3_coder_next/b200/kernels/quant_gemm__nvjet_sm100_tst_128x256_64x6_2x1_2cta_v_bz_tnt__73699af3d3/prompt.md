# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-Next`
- Model folder: `llm/qwen3_coder_next/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `6.21%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 5.20% GPU, calls=288, mean=106.43 us
- `random_high`: 6.21% GPU, calls=768, mean=115.78 us
- `sharegpt_high`: 4.51% GPU, calls=576, mean=106.11 us

## Promoted Shape Samples

1. `aten::arange` via `external_id=21219`: `{"Concrete Inputs":["0","14","1",""],"Input Dims":[[],[],[],[0]],"Input Strides":[[],[],[],[1]],"Input type":["Scalar","Scalar","Scalar","long int"]}`
2. `aten::t` via `external_id=21547`: `{"Concrete Inputs":[""],"Input Dims":[[32,2048]],"Input Strides":[[2048,1]],"Input type":["c10::BFloat16"]}`
3. `aten::mm` via `external_id=21071`: `{"Concrete Inputs":["",""],"Input Dims":[[16384,2048],[2048,6144]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::as_strided` via `external_id=25683`: `{"Concrete Inputs":["","[16384, 4096]","[4608, 1]","0"],"Input Dims":[[16384,4608],[],[],[]],"Input Strides":[[4608,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
