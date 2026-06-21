# KDA Prompt: quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `internLM/Intern-S2-Preview`
- Model folder: `llm/intern_s2_preview/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `18.17%`
- Kernel name: `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 18.17% GPU, calls=320, mean=719.00 us
- `random_mid`: 8.60% GPU, calls=320, mean=743.71 us
- `sharegpt_low`: 18.06% GPU, calls=640, mean=347.02 us
- `sharegpt_mid`: 9.98% GPU, calls=320, mean=964.84 us
- `sharegpt_high`: 5.99% GPU, calls=640, mean=461.79 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=7386`: `{"Concrete Inputs":["",""],"Input Dims":[[38,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::mm` via `external_id=81785`: `{"Concrete Inputs":["",""],"Input Dims":[[17,2048],[2048,128]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::empty_like` via `external_id=88572`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[46,2048],[],[],[],[],[]],"Input Strides":[[2048,1],[],[],[],[],[]],"Input type":["c10::BFloat16","","","","Scalar",""]}`
4. `aten::empty_like` via `external_id=91495`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[1,46,4,128],[],[],[],[],[]],"Input Strides":[[23552,512,128,1],[],[],[],[],[]],"Input type":["c10::BFloat16","","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
