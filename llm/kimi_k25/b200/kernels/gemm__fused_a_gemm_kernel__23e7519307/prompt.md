# KDA Prompt: gemm__fused_a_gemm_kernel__23e7519307

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.5`
- Model folder: `llm/kimi_k25/b200`
- Kernel category: `gemm`
- Max observed GPU share: `19.70%`
- Kernel name: `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 19.70% GPU, calls=488, mean=856.80 us
- `sharegpt_mid`: 3.28% GPU, calls=488, mean=815.18 us
- `sharegpt_high`: 4.50% GPU, calls=488, mean=839.06 us

## Promoted Shape Samples

1. `sgl_kernel::dsv3_fused_a_gemm` via `external_id=74085`: `{"Concrete Inputs":["","",""],"Input Dims":[[15,2112],[15,7168],[7168,2112]],"Input Strides":[[2112,1],[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16"]}`
2. `aten::empty` via `external_id=77677`: `{"Concrete Inputs":["[384]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`
3. `aten::empty` via `external_id=86793`: `{"Concrete Inputs":["[0]","1","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`
4. `aten::empty` via `external_id=122169`: `{"Concrete Inputs":["[120]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
