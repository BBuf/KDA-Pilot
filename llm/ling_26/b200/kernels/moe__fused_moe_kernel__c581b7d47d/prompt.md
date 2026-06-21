# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `moe`
- Max observed GPU share: `32.32%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 9.39% GPU, calls=2232, mean=16.46 us
- `random_mid`: 32.32% GPU, calls=2232, mean=123.80 us
- `random_high`: 18.60% GPU, calls=2232, mean=52.36 us
- `sharegpt_low`: 9.27% GPU, calls=2232, mean=17.42 us
- `sharegpt_mid`: 26.15% GPU, calls=2232, mean=125.76 us
- `sharegpt_high`: 18.55% GPU, calls=2232, mean=112.26 us

## Promoted Shape Samples

1. `sgl_kernel::moe_sum_reduce` via `external_id=1979`: `{"Concrete Inputs":["","","2.5"],"Input Dims":[[39,8,4096],[39,4096],[]],"Input Strides":[[32768,4096,1],[4096,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
2. `sglang::inplace_fused_experts` via `external_id=1965`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","2.5","","","False",""],"Input Dims":[[39,4096],[256,512,4096],[256,4096,256],[39,8],[39,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[2097152,4096,1],[1048576,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","Scalar","","","Scalar",""]}`
3. `sglang::inplace_fused_experts` via `external_id=21855`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","2.5","","","False",""],"Input Dims":[[9780,4096],[256,512,4096],[256,4096,256],[9780,8],[9780,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[2097152,4096,1],[1048576,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","Scalar","","","Scalar",""]}`
4. `aten::zero_` via `external_id=36797`: `{"Concrete Inputs":[""],"Input Dims":[[64]],"Input Strides":[[1]],"Input type":["float"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
