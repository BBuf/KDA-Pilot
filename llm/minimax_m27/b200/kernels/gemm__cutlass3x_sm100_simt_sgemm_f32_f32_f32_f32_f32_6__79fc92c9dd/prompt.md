# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__79fc92c9dd

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `gemm`
- Max observed GPU share: `5.39%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.03% GPU, calls=496, mean=83.64 us
- `sharegpt_mid`: 5.39% GPU, calls=496, mean=222.20 us
- `sharegpt_high`: 2.56% GPU, calls=496, mean=83.79 us

## Promoted Shape Samples

1. `detach_` via `external_id=9124`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["int"]}`
2. `aten::as_strided` via `external_id=45892`: `{"Concrete Inputs":["","[5552, 768]","[768, 1]","0"],"Input Dims":[[5632,768],[],[],[]],"Input Strides":[[768,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `sglang::unified_attention_with_output` via `external_id=65416`: `{"Concrete Inputs":["","","","","True","6","","","","","","",""],"Input Dims":[[1536,768],[1536,1,128],[1536,1,128],[1536,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
