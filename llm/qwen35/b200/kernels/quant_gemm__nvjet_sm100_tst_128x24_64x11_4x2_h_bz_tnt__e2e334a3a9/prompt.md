# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x24_64x11_4x2_h_bz_tnt__e2e334a3a9

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `13.99%`
- Kernel name: `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 13.99% GPU, calls=180, mean=1855.62 us
- `random_mid`: 3.90% GPU, calls=180, mean=371.82 us
- `random_high`: 3.00% GPU, calls=180, mean=606.04 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=11788`: `{"Concrete Inputs":["[38, 16, 128]","15","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
2. `aten::mm` via `external_id=11780`: `{"Concrete Inputs":["",""],"Input Dims":[[38,4096],[4096,5120]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::transpose` via `external_id=22924`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[512,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`
4. `aten::empty` via `external_id=53438`: `{"Concrete Inputs":["[1, 38, 4, 128]","15","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
