# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.5-1T`
- Model folder: `llm/ring_25_1t/b200`
- Kernel category: `moe`
- Max observed GPU share: `32.31%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 12.89% GPU, calls=10944, mean=29.26 us
- `random_mid`: 30.99% GPU, calls=10944, mean=206.41 us
- `random_high`: 32.31% GPU, calls=10944, mean=407.32 us
- `sharegpt_low`: 13.29% GPU, calls=10944, mean=29.72 us
- `sharegpt_mid`: 29.19% GPU, calls=10944, mean=220.81 us
- `sharegpt_high`: 30.42% GPU, calls=10944, mean=187.73 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=3282`: `{"Concrete Inputs":["","","","","","","","","True","False","True","False","False","False","True","","","","","","","","2.5","","","False",""],"Input Dims":[[39,8192],[256,512,8192],[256,8192,256],[39,8],[39,8],[],[],[],[],[],[],[],[],[],[],[256,512,1],[256,8192,1],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[8192,1],[4194304,8192,1],[2097152,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[512,1,1],[8192,1,1],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","float","float","","","","","","Scalar","","","Scalar",""]}`
2. `aten::copy_` via `external_id=3274`: `{"Concrete Inputs":["","","False"],"Input Dims":[[39,256],[39,256],[]],"Input Strides":[[256,1],[256,1],[]],"Input type":["c10::BFloat16","float","Scalar"]}`
3. `sglang::inplace_fused_experts` via `external_id=40397`: `{"Concrete Inputs":["","","","","","","","","True","False","True","False","False","False","True","","","","","","","","2.5","","","False",""],"Input Dims":[[9780,8192],[256,512,8192],[256,8192,256],[9780,8],[9780,8],[],[],[],[],[],[],[],[],[],[],[256,512,1],[256,8192,1],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[8192,1],[4194304,8192,1],[2097152,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[512,1,1],[8192,1,1],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","float","float","","","","","","Scalar","","","Scalar",""]}`
4. `aten::empty` via `external_id=40329`: `{"Concrete Inputs":["[9780, 1024]","15","0","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
