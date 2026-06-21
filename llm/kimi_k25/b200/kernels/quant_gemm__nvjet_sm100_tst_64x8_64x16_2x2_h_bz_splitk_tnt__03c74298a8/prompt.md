# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitk_tnt__03c74298a8

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.5`
- Model folder: `llm/kimi_k25/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `12.90%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 12.90% GPU, calls=480, mean=473.19 us
- `random_mid`: 3.79% GPU, calls=480, mean=505.34 us
- `random_high`: 6.33% GPU, calls=480, mean=596.60 us
- `sharegpt_high`: 4.07% GPU, calls=480, mean=772.81 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=3106`: `{"Concrete Inputs":["",""],"Input Dims":[[38,7168],[7168,384]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::as_strided` via `external_id=20038`: `{"Concrete Inputs":["","[38, 8, 128]","[2048, 256, 1]","128"],"Input Dims":[[38,8,256],[],[],[]],"Input Strides":[[2048,256,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `aten::as_strided` via `external_id=56398`: `{"Concrete Inputs":["","[512, 2048]","[1, 512]",""],"Input Dims":[[2048,512],[],[],[]],"Input Strides":[[512,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`
4. `aten::empty` via `external_id=51706`: `{"Concrete Inputs":["[304]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
