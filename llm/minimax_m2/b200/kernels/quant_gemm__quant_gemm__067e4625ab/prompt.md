# KDA Prompt: quant_gemm__quant_gemm__067e4625ab

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.72%`
- Kernel name: `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 4.72% GPU, calls=8928, mean=1.72 us
- `random_mid`: 2.21% GPU, calls=8928, mean=3.31 us
- `sharegpt_mid`: 2.09% GPU, calls=8928, mean=3.07 us

## Promoted Shape Samples

1. `aten::argmax` via `external_id=4300`: `{"Concrete Inputs":["","-1","False"],"Input Dims":[[1,200064],[],[]],"Input Strides":[[200064,1],[],[]],"Input type":["float","Scalar","Scalar"]}`
2. `aten::view` via `external_id=11100`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[9468,2,128],[]],"Input Strides":[[256,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
3. `aten::as_strided` via `external_id=44058`: `{"Concrete Inputs":["","[25357, 2, 64, 128]","[16384, 128, 256, 1]",""],"Input Dims":[[25357,64,2,128],[],[],[]],"Input Strides":[[16384,256,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
