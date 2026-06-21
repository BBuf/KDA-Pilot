# KDA Prompt: gemm__fused_a_gemm_kernel__23e7519307

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2`
- Model folder: `llm/deepseek_r1_fp4/b200`
- Kernel category: `gemm`
- Max observed GPU share: `10.78%`
- Kernel name: `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 10.78% GPU, calls=496, mean=469.60 us
- `sharegpt_mid`: 3.18% GPU, calls=496, mean=471.31 us
- `sharegpt_high`: 3.42% GPU, calls=496, mean=520.08 us

## Promoted Shape Samples

1. `sgl_kernel::dsv3_fused_a_gemm` via `external_id=90299`: `{"Concrete Inputs":["","",""],"Input Dims":[[16,2112],[16,7168],[7168,2112]],"Input Strides":[[2112,1],[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16"]}`
2. `aten::empty` via `external_id=110048`: `{"Concrete Inputs":["[16, 1024]","0","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
3. `aten::copy_` via `external_id=171860`: `{"Concrete Inputs":["","","False"],"Input Dims":[[16,8],[16,8],[]],"Input Strides":[[9,1],[8,1],[]],"Input type":["int","int","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
