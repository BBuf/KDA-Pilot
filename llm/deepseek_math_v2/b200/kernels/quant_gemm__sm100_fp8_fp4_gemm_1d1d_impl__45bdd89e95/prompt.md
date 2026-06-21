# KDA Prompt: quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-Math-V2`
- Model folder: `llm/deepseek_math_v2/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `5.81%`
- Kernel name: `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 240u, 128u, 128u, 1u, 128u, 128u, 128u, 6u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 5.81% GPU, calls=26872, mean=63.06 us
- `sharegpt_mid`: 3.08% GPU, calls=2440, mean=53.96 us

## Promoted Shape Samples

1. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=17787`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[11101,7168],[11101,14],[4608,7168],[4608,14],[11101,4608]],"Input Strides":[[7168,1],[1,11104],[7168,1],[1,4608],[4608,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`
2. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=84233`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[8661,7168],[8661,14],[4608,7168],[4608,14],[8661,4608]],"Input Strides":[[7168,1],[1,8664],[7168,1],[1,4608],[4608,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
