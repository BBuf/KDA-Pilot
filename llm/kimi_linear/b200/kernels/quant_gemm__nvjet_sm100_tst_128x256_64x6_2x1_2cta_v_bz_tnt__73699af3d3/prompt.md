# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Model folder: `llm/kimi_linear/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.88%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.88% GPU, calls=1008, mean=39.56 us
- `sharegpt_high`: 2.73% GPU, calls=632, mean=44.54 us

## Promoted Shape Samples

1. `aten::narrow` via `external_id=101675`: `{"Concrete Inputs":["","0","31","1"],"Input Dims":[[47],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar"]}`
2. `aten::as_strided` via `external_id=103211`: `{"Concrete Inputs":["","[2, 16384, 128]","[128, 3336, 1]",""],"Input Dims":[[16384,2,128],[],[],[]],"Input Strides":[[3336,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`
3. `aten::narrow` via `external_id=95183`: `{"Concrete Inputs":["","0","69","1"],"Input Dims":[[80],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar"]}`
4. `aten::copy_` via `external_id=96719`: `{"Concrete Inputs":["","","False"],"Input Dims":[[16384,8,64],[16384,8,64],[]],"Input Strides":[[1536,192,1],[1536,192,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
