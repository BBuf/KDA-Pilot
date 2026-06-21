# KDA Prompt: quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `2.14%`
- Kernel name: `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 240u, 128u, 128u, 1u, 128u, 128u, 128u, 6u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.14% GPU, calls=1467, mean=103.27 us

## Promoted Shape Samples

1. `aten::view` via `external_id=80800`: `{"Concrete Inputs":["","[8, 1, 19360]"],"Input Dims":[[8,19360],[]],"Input Strides":[[19360,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
2. `aten::record_stream` via `external_id=117132`: `{"Concrete Inputs":["",""],"Input Dims":[[92,6144],[]],"Input Strides":[[6144,1],[]],"Input type":["c10::Float8_e4m3fn",""]}`
3. `aten::new_zeros` via `external_id=81198`: `{"Concrete Inputs":["","[0]","","","","False"],"Input Dims":[[8],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["long int","ScalarList","","","","Scalar"]}`
4. `aten::to` via `external_id=80999`: `{"Concrete Inputs":["","","6","False","False",""],"Input Dims":[[8],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["float","","Scalar","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
