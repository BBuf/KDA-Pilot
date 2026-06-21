# KDA Prompt: gemm__router_gemm_kernel__11c0c72e30

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V3`
- Model folder: `llm/deepseek_v3/b200`
- Kernel category: `gemm`
- Max observed GPU share: `7.28%`
- Kernel name: `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 6, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 7.28% GPU, calls=472, mean=1181.03 us

## Promoted Shape Samples

1. `aten::_to_copy` via `external_id=148860`: `{"Concrete Inputs":["","4","","","","False",""],"Input Dims":[[1,1],[],[],[],[],[],[]],"Input Strides":[[1,1],[],[],[],[],[],[]],"Input type":["int","Scalar","","","","Scalar",""]}`
2. `sglang::flashinfer_dsv3_router_gemm` via `external_id=148972`: `{"Concrete Inputs":["","",""],"Input Dims":[[6,256],[6,7168],[256,7168]],"Input Strides":[[256,1],[7168,1],[7168,1]],"Input type":["float","c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
