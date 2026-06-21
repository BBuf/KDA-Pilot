# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.5-Flash`
- Model folder: `llm/step35_flash/b200`
- Kernel category: `moe`
- Max observed GPU share: `16.13%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 14.66% GPU, calls=3024, mean=24.40 us
- `random_mid`: 16.13% GPU, calls=3024, mean=24.29 us
- `random_high`: 14.89% GPU, calls=3024, mean=24.29 us
- `sharegpt_low`: 13.63% GPU, calls=3024, mean=21.10 us
- `sharegpt_mid`: 13.10% GPU, calls=3024, mean=21.08 us
- `sharegpt_high`: 15.80% GPU, calls=3024, mean=22.35 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=425741`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","7.","False"],"Input Dims":[[38,4096],[288,640,4096],[288,4096,320],[38,8],[38,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[2621440,4096,1],[1310720,320,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","Scalar","Scalar"]}`
2. `sglang::inplace_fused_experts` via `external_id=425261`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False"],"Input Dims":[[38,4096],[288,640,4096],[288,4096,320],[38,8],[38,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[2621440,4096,1],[1310720,320,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar"]}`
3. `sglang::inplace_fused_experts` via `external_id=1030172`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False"],"Input Dims":[[16,4096],[288,640,4096],[288,4096,320],[16,8],[16,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[2621440,4096,1],[1310720,320,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar"]}`
4. `sglang::inplace_fused_experts` via `external_id=1030667`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","7.","False"],"Input Dims":[[16,4096],[288,640,4096],[288,4096,320],[16,8],[16,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[2621440,4096,1],[1310720,320,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
