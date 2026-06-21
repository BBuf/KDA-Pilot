# KDA Prompt: quant_gemm__per_token_quant_fp8_kernel__f9fa21beab

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.5-1T`
- Model folder: `llm/ring_25_1t/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.37%`
- Kernel name: `void per_token_quant_fp8_kernel<__nv_bfloat16, __nv_fp8_e4m3, 8, 16, false>(__nv_bfloat16 const*, __nv_fp8_e4m3*, float*, long, long)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.67% GPU, calls=4416, mean=44.07 us
- `random_high`: 4.37% GPU, calls=9440, mean=63.90 us
- `sharegpt_mid`: 3.23% GPU, calls=4416, mean=60.56 us

## Promoted Shape Samples

1. `sgl_kernel::sgl_per_token_quant_fp8` via `external_id=46909`: `{"Concrete Inputs":["","",""],"Input Dims":[[9780,8192],[9780,8192],[9780,1]],"Input Strides":[[8192,1],[8192,1],[1,1]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","float"]}`
2. `aten::reshape` via `external_id=41111`: `{"Concrete Inputs":["","[22]"],"Input Dims":[[22],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
3. `sgl_kernel::sgl_per_token_quant_fp8` via `external_id=84919`: `{"Concrete Inputs":["","",""],"Input Dims":[[16384,8192],[16384,8192],[16384,1]],"Input Strides":[[8192,1],[8192,1],[1,1]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","float"]}`
4. `aten::empty` via `external_id=84619`: `{"Concrete Inputs":["[16384, 1]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
