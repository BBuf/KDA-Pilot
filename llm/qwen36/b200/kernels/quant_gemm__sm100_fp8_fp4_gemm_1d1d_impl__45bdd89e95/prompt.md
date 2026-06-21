# KDA Prompt: quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen36/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.87%`
- Kernel name: `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 240u, 128u, 128u, 1u, 128u, 128u, 128u, 6u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.94% GPU, calls=41, mean=171.29 us
- `random_high`: 4.87% GPU, calls=205, mean=86.67 us
- `sharegpt_mid`: 4.17% GPU, calls=164, mean=52.20 us

## Promoted Shape Samples

1. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=24995`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[11886,2048],[11886,4],[12288,2048],[12288,4],[11886,12288]],"Input Strides":[[2048,1],[1,11888],[2048,1],[1,12288],[12288,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`
2. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=53304`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[15434,2048],[15434,4],[12288,2048],[12288,4],[15434,12288]],"Input Strides":[[2048,1],[1,15436],[2048,1],[1,12288],[12288,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`
3. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=110239`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[8709,2048],[8709,4],[12288,2048],[12288,4],[8709,12288]],"Input Strides":[[2048,1],[1,8712],[2048,1],[1,12288],[12288,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
