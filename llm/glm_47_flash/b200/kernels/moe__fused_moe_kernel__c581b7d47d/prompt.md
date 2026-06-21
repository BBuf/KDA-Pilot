# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-4.7-Flash`
- Model folder: `llm/glm_47_flash/b200`
- Kernel category: `moe`
- Max observed GPU share: `30.39%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 30.39% GPU, calls=828, mean=169.99 us
- `sharegpt_mid`: 12.17% GPU, calls=828, mean=152.24 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=16135`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","1.8","","","False",""],"Input Dims":[[5102,2048],[65,3072,2048],[65,2048,1536],[5102,5],[5102,5],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2048,1],[6291456,2048,1],[3145728,1536,1],[5,1],[5,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","Scalar","","","Scalar",""]}`
2. `sglang::inplace_fused_experts` via `external_id=55392`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","1.8","","","False",""],"Input Dims":[[5528,2048],[65,3072,2048],[65,2048,1536],[5528,5],[5528,5],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2048,1],[6291456,2048,1],[3145728,1536,1],[5,1],[5,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
