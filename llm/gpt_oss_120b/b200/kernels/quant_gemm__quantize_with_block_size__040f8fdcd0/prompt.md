# KDA Prompt: quant_gemm__quantize_with_block_size__040f8fdcd0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `3.04%`
- Kernel name: `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationType)2, __nv_bfloat16, 32, true, false, false, false, std::integral_constant<bool, false> >(int, int, int, int, __nv_bfloat16 const*, float const*, void*, unsigned int*, flashinfer::QuantizationSFLayout)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 3.04% GPU, calls=2592, mean=3.47 us
- `random_mid`: 2.46% GPU, calls=2592, mean=7.58 us

## Promoted Shape Samples

1. `aten::empty_like` via `external_id=4015`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[1],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["long int","","","","Scalar",""]}`
2. `aten::_to_copy` via `external_id=9480`: `{"Concrete Inputs":["","3","0","","","True",""],"Input Dims":[[21],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[]],"Input type":["int","Scalar","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
