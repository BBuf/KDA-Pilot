# KDA Prompt: gemm__fused_a_gemm_kernel__23e7519307

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.6`
- Model folder: `llm/kimi_k26/b200`
- Kernel category: `gemm`
- Max observed GPU share: `19.27%`
- Kernel name: `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 19.27% GPU, calls=488, mean=824.46 us
- `sharegpt_mid`: 7.20% GPU, calls=488, mean=763.80 us
- `sharegpt_high`: 3.40% GPU, calls=488, mean=584.51 us

## Promoted Shape Samples

1. `sgl_kernel::dsv3_fused_a_gemm` via `external_id=67615`: `{"Concrete Inputs":["","",""],"Input Dims":[[15,2112],[15,7168],[7168,2112]],"Input Strides":[[2112,1],[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16"]}`
2. `aten::numpy_T` via `external_id=66571`: `{"Concrete Inputs":[""],"Input Dims":[[2112,7168]],"Input Strides":[[7168,1]],"Input type":["c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
