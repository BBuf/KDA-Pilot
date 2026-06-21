# KDA Prompt: other__fwd_kernel__d4406e9fc7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-4.7-Flash`
- Model folder: `llm/glm_47_flash/b200`
- Kernel category: `other`
- Max observed GPU share: `35.25%`
- Kernel name: `_fwd_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 35.25% GPU, calls=423, mean=151.44 us
- `sharegpt_low`: 6.51% GPU, calls=47, mean=101.75 us
- `sharegpt_high`: 26.43% GPU, calls=235, mean=257.35 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=35285`: `{"Concrete Inputs":["","","","","True","5","","","","","","",""],"Input Dims":[[24,20,576],[24,1,576],[24,1,512],[24,10240],[],[],[],[],[],[],[],[],[]],"Input Strides":[[11520,576,1],[576,576,1],[512,512,1],[10240,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
2. `sglang::unified_attention_with_output` via `external_id=35901`: `{"Concrete Inputs":["","","","","True","27","","","","","","",""],"Input Dims":[[24,20,576],[24,1,576],[24,1,512],[24,10240],[],[],[],[],[],[],[],[],[]],"Input Strides":[[11520,576,1],[576,576,1],[512,512,1],[10240,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=35173`: `{"Concrete Inputs":["","","","","True","1","","","","","","",""],"Input Dims":[[24,20,576],[24,1,576],[24,1,512],[24,10240],[],[],[],[],[],[],[],[],[]],"Input Strides":[[11520,576,1],[576,576,1],[512,512,1],[10240,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
4. `sglang::unified_attention_with_output` via `external_id=35257`: `{"Concrete Inputs":["","","","","True","4","","","","","","",""],"Input Dims":[[24,20,576],[24,1,576],[24,1,512],[24,10240],[],[],[],[],[],[],[],[],[]],"Input Strides":[[11520,576,1],[576,576,1],[512,512,1],[10240,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
