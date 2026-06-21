# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitk_tnt__5a2ad7d133

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V3`
- Model folder: `llm/deepseek_v3/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `14.14%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 14.14% GPU, calls=472, mean=824.39 us
- `random_mid`: 5.87% GPU, calls=472, mean=898.78 us
- `random_high`: 7.47% GPU, calls=472, mean=849.70 us
- `sharegpt_high`: 5.87% GPU, calls=472, mean=1265.73 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=13144`: `{"Concrete Inputs":["",""],"Input Dims":[[39,7168],[7168,256]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=216356`: `{"Concrete Inputs":["",""],"Input Dims":[[42,7168],[7168,256]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::split_with_sizes` via `external_id=216114`: `{"Concrete Inputs":["","[128, 64]","-1"],"Input Dims":[[42,16,192],[],[]],"Input Strides":[[3072,192,1],[],[]],"Input type":["c10::BFloat16","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
