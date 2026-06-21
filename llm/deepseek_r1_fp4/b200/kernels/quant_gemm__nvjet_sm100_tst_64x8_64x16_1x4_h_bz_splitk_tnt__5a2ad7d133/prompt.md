# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitk_tnt__5a2ad7d133

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2`
- Model folder: `llm/deepseek_r1_fp4/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `18.41%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 18.41% GPU, calls=472, mean=982.41 us
- `random_mid`: 3.46% GPU, calls=472, mean=825.85 us
- `random_high`: 8.27% GPU, calls=472, mean=879.75 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=3550`: `{"Concrete Inputs":["",""],"Input Dims":[[39,7168],[7168,256]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::view` via `external_id=5322`: `{"Concrete Inputs":["","[-1]"],"Input Dims":[[39,7168],[]],"Input Strides":[[7168,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::transpose` via `external_id=24968`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[4096,512],[],[]],"Input Strides":[[512,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
