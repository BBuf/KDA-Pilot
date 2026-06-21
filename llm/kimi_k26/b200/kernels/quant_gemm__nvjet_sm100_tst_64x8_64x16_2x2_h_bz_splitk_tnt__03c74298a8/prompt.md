# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitk_tnt__03c74298a8

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.6`
- Model folder: `llm/kimi_k26/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `13.13%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 13.13% GPU, calls=480, mean=516.93 us
- `random_mid`: 4.14% GPU, calls=480, mean=559.08 us
- `random_high`: 5.91% GPU, calls=480, mean=515.44 us
- `sharegpt_high`: 4.22% GPU, calls=480, mean=736.26 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=1588`: `{"Concrete Inputs":["",""],"Input Dims":[[38,7168],[7168,384]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `sglang::_run_activation_inplace` via `external_id=19934`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[38,512],[38,256]],"Input Strides":[[],[512,1],[256,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`
3. `aten::as_strided` via `external_id=44142`: `{"Concrete Inputs":["","[38, 8, 128]","[2048, 256, 1]","128"],"Input Dims":[[38,8,256],[],[],[]],"Input Strides":[[2048,256,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
4. `aten::mm` via `external_id=164456`: `{"Concrete Inputs":["",""],"Input Dims":[[65,7168],[7168,384]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
