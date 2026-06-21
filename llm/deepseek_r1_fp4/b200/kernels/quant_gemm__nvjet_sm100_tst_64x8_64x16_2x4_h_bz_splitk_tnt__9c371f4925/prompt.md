# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2`
- Model folder: `llm/deepseek_r1_fp4/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `5.18%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 5.18% GPU, calls=472, mean=826.90 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=207871`: `{"Concrete Inputs":["",""],"Input Dims":[[28,7168],[7168,256]],"Input Strides":[[7168,1],[1,7168]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::_to_copy` via `external_id=207637`: `{"Concrete Inputs":["","24","","","","False",""],"Input Dims":[[28,1,64],[],[],[],[],[],[]],"Input Strides":[[2112,576,1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
