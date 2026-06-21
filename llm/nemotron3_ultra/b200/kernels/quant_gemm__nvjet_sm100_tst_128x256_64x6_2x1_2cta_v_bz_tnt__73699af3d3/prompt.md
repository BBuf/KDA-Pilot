# KDA Prompt: quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Model folder: `llm/nemotron3_ultra/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.21%`
- Kernel name: `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.02% GPU, calls=308, mean=242.03 us
- `random_high`: 4.21% GPU, calls=752, mean=265.39 us
- `sharegpt_high`: 4.08% GPU, calls=500, mean=279.61 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=49384`: `{"Concrete Inputs":["",""],"Input Dims":[[12203,2560],[2560,8192]],"Input Strides":[[2560,1],[1,2560]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
2. `aten::linear` via `external_id=49290`: `{"Concrete Inputs":["","",""],"Input Dims":[[12203,16384],[2048,16384],[]],"Input Strides":[[16384,1],[16384,1],[]],"Input type":["c10::BFloat16","c10::BFloat16",""]}`
3. `aten::mm` via `external_id=49375`: `{"Concrete Inputs":["",""],"Input Dims":[[12203,8192],[8192,2560]],"Input Strides":[[8192,1],[1,8192]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `sglang::inplace_all_reduce` via `external_id=49281`: `{"Concrete Inputs":["",""],"Input Dims":[[12203,8192],[]],"Input Strides":[[8192,1],[]],"Input type":["c10::BFloat16",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
