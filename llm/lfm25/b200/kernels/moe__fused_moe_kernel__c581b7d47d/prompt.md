# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Model folder: `llm/lfm25/b200`
- Kernel category: `moe`
- Max observed GPU share: `50.52%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 32.96% GPU, calls=396, mean=16.85 us
- `random_mid`: 50.52% GPU, calls=396, mean=104.82 us
- `random_high`: 45.03% GPU, calls=396, mean=239.92 us
- `sharegpt_low`: 34.12% GPU, calls=396, mean=18.92 us
- `sharegpt_mid`: 47.66% GPU, calls=396, mean=105.68 us
- `sharegpt_high`: 42.22% GPU, calls=396, mean=174.82 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=743`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[103,2048],[32,3584,2048],[32,2048,1792],[103,4],[103,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2048,1],[7340032,2048,1],[3670016,1792,1],[4,1],[4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`
2. `sglang::inplace_fused_experts` via `external_id=8569`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[7505,2048],[32,3584,2048],[32,2048,1792],[7505,4],[7505,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2048,1],[7340032,2048,1],[3670016,1792,1],[4,1],[4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`
3. `sglang::inplace_fused_experts` via `external_id=32201`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[16384,2048],[32,3584,2048],[32,2048,1792],[16384,4],[16384,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2048,1],[7340032,2048,1],[3670016,1792,1],[4,1],[4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`
4. `sglang::inplace_fused_experts` via `external_id=43183`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False",""],"Input Dims":[[624,2048],[32,3584,2048],[32,2048,1792],[624,4],[624,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2048,1],[7340032,2048,1],[3670016,1792,1],[4,1],[4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
