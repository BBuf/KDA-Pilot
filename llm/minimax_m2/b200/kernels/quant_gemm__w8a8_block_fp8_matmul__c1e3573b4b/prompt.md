# KDA Prompt: quant_gemm__w8a8_block_fp8_matmul__c1e3573b4b

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `22.81%`
- Kernel name: `_w8a8_block_fp8_matmul`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 11.57% GPU, calls=4464, mean=34.62 us
- `random_high`: 9.63% GPU, calls=4464, mean=23.33 us
- `sharegpt_low`: 22.81% GPU, calls=4464, mean=17.10 us
- `sharegpt_mid`: 10.92% GPU, calls=4464, mean=32.03 us
- `sharegpt_high`: 10.03% GPU, calls=4464, mean=23.20 us

## Promoted Shape Samples

1. `aten::view` via `external_id=11100`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[9468,2,128],[]],"Input Strides":[[256,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
2. `aten::view` via `external_id=22811`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[2797,2,128],[]],"Input Strides":[[2048,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
3. `aten::as_strided` via `external_id=30046`: `{"Concrete Inputs":["","[64]","[1]","0"],"Input Dims":[[16384],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
4. `aten::as_strided` via `external_id=44058`: `{"Concrete Inputs":["","[25357, 2, 64, 128]","[16384, 128, 256, 1]",""],"Input Dims":[[25357,64,2,128],[],[],[]],"Input Strides":[[16384,256,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
