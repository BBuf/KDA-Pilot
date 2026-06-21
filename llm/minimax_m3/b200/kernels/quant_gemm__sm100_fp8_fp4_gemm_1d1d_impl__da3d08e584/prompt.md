# KDA Prompt: quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__da3d08e584

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Model folder: `llm/minimax_m3/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `8.05%`
- Kernel name: `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 6.50% GPU, calls=4104, mean=21.13 us
- `sharegpt_mid`: 8.05% GPU, calls=4104, mean=59.91 us

## Promoted Shape Samples

1. `aten::unsqueeze` via `external_id=289`: `{"Concrete Inputs":["","-1"],"Input Dims":[[48],[]],"Input Strides":[[1],[]],"Input type":["bool","Scalar"]}`
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
