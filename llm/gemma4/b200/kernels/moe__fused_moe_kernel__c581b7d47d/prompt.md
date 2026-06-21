# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `google/gemma-4-26B-A4B-it`
- Model folder: `llm/gemma4/b200`
- Kernel category: `moe`
- Max observed GPU share: `50.81%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 22.87% GPU, calls=540, mean=17.39 us
- `random_mid`: 45.23% GPU, calls=540, mean=139.42 us
- `random_high`: 50.81% GPU, calls=540, mean=114.12 us
- `sharegpt_low`: 21.68% GPU, calls=540, mean=16.22 us
- `sharegpt_mid`: 43.37% GPU, calls=540, mean=102.90 us
- `sharegpt_high`: 50.02% GPU, calls=540, mean=102.71 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=457`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[38,2816],[128,1408,2816],[128,2816,704],[38,8],[38,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2816,1],[3964928,2816,1],[1982464,704,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`
2. `sglang::inplace_fused_experts` via `external_id=11287`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[11254,2816],[128,1408,2816],[128,2816,704],[11254,8],[11254,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2816,1],[3964928,2816,1],[1982464,704,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`
3. `sglang::inplace_fused_experts` via `external_id=23889`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[1902,2816],[128,1408,2816],[128,2816,704],[1902,8],[1902,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2816,1],[3964928,2816,1],[1982464,704,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`
4. `sglang::inplace_fused_experts` via `external_id=31812`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[17,2816],[128,1408,2816],[128,2816,704],[17,8],[17,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2816,1],[3964928,2816,1],[1982464,704,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
