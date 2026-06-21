# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_1x4_h_bz_tnt__52249c10de

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `20.78%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 20.78% GPU, calls=480, mean=1033.66 us
- `random_mid`: 5.42% GPU, calls=480, mean=193.74 us
- `random_high`: 4.97% GPU, calls=3360, mean=53.89 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=5473`: `{"Concrete Inputs":["",""],"Input Dims":[[38,4096],[4096,512]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::as_strided` via `external_id=5481`: `{"Concrete Inputs":["","[256, 4096]","[1, 256]",""],"Input Dims":[[4096,256],[],[],[]],"Input Strides":[[256,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`
3. `aten::copy_` via `external_id=22313`: `{"Concrete Inputs":["","","False"],"Input Dims":[[38,8,256],[38,8,256],[]],"Input Strides":[[2048,256,1],[4608,512,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
4. `aten::as_strided` via `external_id=25511`: `{"Concrete Inputs":["","[3072, 38]","[1, 3072]",""],"Input Dims":[[38,3072],[],[],[]],"Input Strides":[[3072,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
