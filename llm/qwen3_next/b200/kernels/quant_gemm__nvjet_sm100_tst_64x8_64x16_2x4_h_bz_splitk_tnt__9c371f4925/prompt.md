# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Model folder: `llm/qwen3_next/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `25.37%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 18.66% GPU, calls=384, mean=815.63 us
- `random_mid`: 7.73% GPU, calls=384, mean=856.03 us
- `random_high`: 25.37% GPU, calls=384, mean=5604.12 us
- `sharegpt_low`: 23.78% GPU, calls=384, mean=1749.47 us
- `sharegpt_mid`: 7.95% GPU, calls=384, mean=940.24 us
- `sharegpt_high`: 6.42% GPU, calls=384, mean=1394.37 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=2468`: `{"Concrete Inputs":["",""],"Input Dims":[[38,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::view` via `external_id=2458`: `{"Concrete Inputs":["","[-1]"],"Input Dims":[[38,2048],[]],"Input Strides":[[2048,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::matmul` via `external_id=41066`: `{"Concrete Inputs":["",""],"Input Dims":[[38,512],[512,2048]],"Input Strides":[[512,1],[1,512]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::mm` via `external_id=87651`: `{"Concrete Inputs":["",""],"Input Dims":[[17,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
