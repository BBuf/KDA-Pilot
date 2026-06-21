# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitk_tnt__a2d138c1c3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.7-Code`
- Model folder: `llm/kimi_k27_code/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `13.43%`
- Kernel name: `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 13.43% GPU, calls=488, mean=393.35 us
- `random_mid`: 5.62% GPU, calls=488, mean=705.91 us
- `random_high`: 6.91% GPU, calls=488, mean=662.02 us

## Promoted Shape Samples

1. `aten::view` via `external_id=8961`: `{"Concrete Inputs":["","[-1]"],"Input Dims":[[38,7168],[]],"Input Strides":[[7168,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
2. `aten::mm` via `external_id=8971`: `{"Concrete Inputs":["",""],"Input Dims":[[38,7168],[7168,2112]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::item` via `external_id=36663`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
