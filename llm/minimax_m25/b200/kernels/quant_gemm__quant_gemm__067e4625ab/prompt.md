# KDA Prompt: quant_gemm__quant_gemm__067e4625ab

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.5`
- Model folder: `llm/minimax_m25/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.16%`
- Kernel name: `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 4.16% GPU, calls=17856, mean=1.71 us
- `random_mid`: 3.61% GPU, calls=17856, mean=4.58 us
- `sharegpt_mid`: 3.48% GPU, calls=17856, mean=4.29 us
- `sharegpt_high`: 2.62% GPU, calls=17856, mean=2.50 us

## Promoted Shape Samples

1. `aten::_index_put_impl_` via `external_id=4339`: `{"Concrete Inputs":["","","","False","False"],"Input Dims":[[4097],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","","long int","Scalar","Scalar"]}`
2. `aten::as_strided` via `external_id=253`: `{"Concrete Inputs":["","[39, 1, 128]","[1024, 128, 1]","0"],"Input Dims":[[48,1,128],[],[],[]],"Input Strides":[[1024,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`
3. `aten::as_strided` via `external_id=11701`: `{"Concrete Inputs":["","[8943, 1, 128]","[1024, 128, 1]","0"],"Input Dims":[[9216,1,128],[],[],[]],"Input Strides":[[1024,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`
4. `aten::as_strided` via `external_id=54662`: `{"Concrete Inputs":["","[5524, 768]","[768, 1]","0"],"Input Dims":[[5632,768],[],[],[]],"Input Strides":[[768,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
