# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.79%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.79% GPU, calls=488, mean=100.66 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=67849`: `{"Concrete Inputs":["","[32329, 32, 128]","[8192, 256, 1]","0"],"Input Dims":[[32329,32,256],[],[],[]],"Input Strides":[[8192,256,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
2. `aten::empty_strided` via `external_id=66856`: `{"Concrete Inputs":["[2121, 512]","[512, 1]","15","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
3. `aten::mm` via `external_id=64739`: `{"Concrete Inputs":["",""],"Input Dims":[[32329,512],[512,8192]],"Input Strides":[[512,1],[1,512]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
