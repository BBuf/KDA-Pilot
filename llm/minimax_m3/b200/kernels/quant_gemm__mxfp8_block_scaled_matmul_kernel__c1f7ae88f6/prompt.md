# KDA Prompt: quant_gemm__mxfp8_block_scaled_matmul_kernel__c1f7ae88f6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Model folder: `llm/minimax_m3/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `5.85%`
- Kernel name: `_mxfp8_block_scaled_matmul_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 5.80% GPU, calls=9072, mean=19.85 us
- `sharegpt_mid`: 5.85% GPU, calls=9072, mean=19.68 us

## Promoted Shape Samples

1. `aten::select` via `external_id=114594`: `{"Concrete Inputs":["","0","0"],"Input Dims":[[1,1],[],[]],"Input Strides":[[1,1],[],[]],"Input type":["int","Scalar","Scalar"]}`
2. `aten::slice` via `external_id=228497`: `{"Concrete Inputs":["","0","15","9223372036854775807","1"],"Input Dims":[[16,128],[],[],[],[]],"Input Strides":[[128,1],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
