# KDA Prompt: quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen36/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `16.12%`
- Kernel name: `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 16.12% GPU, calls=1510, mean=6.98 us
- `sharegpt_mid`: 2.77% GPU, calls=871, mean=6.54 us

## Promoted Shape Samples

1. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=86072`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[17,2048],[17,4],[9216,2048],[9216,4],[17,9216]],"Input Strides":[[2048,1],[1,20],[2048,1],[1,9216],[9216,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`
2. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=100449`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[17,4096],[17,8],[2048,4096],[2048,8],[17,2048]],"Input Strides":[[4096,1],[1,20],[4096,1],[1,2048],[2048,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
