# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.6-1T`
- Model folder: `llm/inclusion_ring26/b200`
- Kernel category: `moe`
- Max observed GPU share: `28.29%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 11.14% GPU, calls=10944, mean=28.78 us
- `random_mid`: 28.22% GPU, calls=10944, mean=257.81 us
- `random_high`: 28.29% GPU, calls=10944, mean=474.35 us
- `sharegpt_low`: 8.52% GPU, calls=10944, mean=24.49 us
- `sharegpt_mid`: 24.71% GPU, calls=10944, mean=196.34 us
- `sharegpt_high`: 24.75% GPU, calls=10944, mean=383.66 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=3290`: `{"Concrete Inputs":["","","","","","","","","True","False","True","False","False","False","True","","","","","","","","2.5","","","False",""],"Input Dims":[[38,8192],[256,512,8192],[256,8192,256],[38,8],[38,8],[],[],[],[],[],[],[],[],[],[],[256,512,1],[256,8192,1],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[8192,1],[4194304,8192,1],[2097152,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[512,1,1],[8192,1,1],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","float","float","","","","","","Scalar","","","Scalar",""]}`
2. `aten::empty` via `external_id=3266`: `{"Concrete Inputs":["[38, 8192]","15","0","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","",""]}`
3. `sglang::inplace_fused_experts` via `external_id=33697`: `{"Concrete Inputs":["","","","","","","","","True","False","True","False","False","False","True","","","","","","","","2.5","","","False",""],"Input Dims":[[16384,8192],[256,512,8192],[256,8192,256],[16384,8],[16384,8],[],[],[],[],[],[],[],[],[],[],[256,512,1],[256,8192,1],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[8192,1],[4194304,8192,1],[2097152,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[512,1,1],[8192,1,1],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","float","float","","","","","","Scalar","","","Scalar",""]}`
4. `aten::empty` via `external_id=33103`: `{"Concrete Inputs":["[16384]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
