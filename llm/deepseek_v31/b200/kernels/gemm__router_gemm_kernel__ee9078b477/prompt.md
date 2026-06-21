# KDA Prompt: gemm__router_gemm_kernel__ee9078b477

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V3.1`
- Model folder: `llm/deepseek_v31/b200`
- Kernel category: `gemm`
- Max observed GPU share: `14.68%`
- Kernel name: `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 14.68% GPU, calls=472, mean=887.56 us
- `sharegpt_mid`: 6.06% GPU, calls=472, mean=894.98 us
- `sharegpt_high`: 4.08% GPU, calls=472, mean=798.60 us

## Promoted Shape Samples

1. `sglang::flashinfer_dsv3_router_gemm` via `external_id=98716`: `{"Concrete Inputs":["","",""],"Input Dims":[[16,256],[16,7168],[256,7168]],"Input Strides":[[256,1],[7168,1],[7168,1]],"Input type":["float","c10::BFloat16","c10::BFloat16"]}`
2. `aten::_to_copy` via `external_id=115484`: `{"Concrete Inputs":["","6","","","","False",""],"Input Dims":[[1,129280],[],[],[],[],[],[]],"Input Strides":[[129280,1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","","","","Scalar",""]}`
3. `aten::transpose` via `external_id=105496`: `{"Concrete Inputs":["","-1","-2"],"Input Dims":[[3,16],[],[]],"Input Strides":[[16,1],[],[]],"Input type":["int","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
