# KDA Prompt: quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `11.68%`
- Kernel name: `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 11.02% GPU, calls=20287, mean=13.23 us
- `random_mid`: 3.61% GPU, calls=17863, mean=13.79 us
- `sharegpt_low`: 11.68% GPU, calls=20366, mean=13.22 us

## Promoted Shape Samples

1. `sglang::deep_gemm_fp8_fp8_bf16_nt` via `external_id=24504`: `{"Concrete Inputs":["","","","",""],"Input Dims":[[38,16384],[38,32],[6144,16384],[6144,32],[38,6144]],"Input Strides":[[16384,1],[1,40],[16384,1],[1,6144],[6144,1]],"Input type":["c10::Float8_e4m3fn","int","c10::Float8_e4m3fn","int","c10::BFloat16"]}`
2. `aten::empty` via `external_id=5712`: `{"Concrete Inputs":["[0, 6144]","15","0","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","",""]}`
3. `aten::as_strided` via `external_id=15432`: `{"Concrete Inputs":["","[]","[]","0"],"Input Dims":[[8],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
4. `aten::record_stream` via `external_id=1911`: `{"Concrete Inputs":["",""],"Input Dims":[[0,8],[]],"Input Strides":[[8,1],[]],"Input type":["bool",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
