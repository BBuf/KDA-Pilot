# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Model folder: `llm/ernie45/b200`
- Kernel category: `attention`
- Max observed GPU share: `4.48%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.35% GPU, calls=84, mean=39.83 us
- `random_high`: 4.39% GPU, calls=112, mean=38.40 us
- `sharegpt_mid`: 4.07% GPU, calls=140, mean=30.23 us
- `sharegpt_high`: 4.48% GPU, calls=140, mean=31.19 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=6177`: `{"Concrete Inputs":["","","","","True","27","","","","","","",""],"Input Dims":[[11264,2560],[11264,4,128],[11264,4,128],[11264,2560],[],[],[],[],[],[],[],[],[]],"Input Strides":[[3584,1],[3584,128,1],[3584,128,1],[2560,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
2. `sglang::unified_attention_with_output` via `external_id=6084`: `{"Concrete Inputs":["","","","","True","24","","","","","","",""],"Input Dims":[[11264,2560],[11264,4,128],[11264,4,128],[11264,2560],[],[],[],[],[],[],[],[],[]],"Input Strides":[[3584,1],[3584,128,1],[3584,128,1],[2560,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=6146`: `{"Concrete Inputs":["","","","","True","26","","","","","","",""],"Input Dims":[[11264,2560],[11264,4,128],[11264,4,128],[11264,2560],[],[],[],[],[],[],[],[],[]],"Input Strides":[[3584,1],[3584,128,1],[3584,128,1],[2560,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
4. `sglang::unified_attention_with_output` via `external_id=6053`: `{"Concrete Inputs":["","","","","True","23","","","","","","",""],"Input Dims":[[11264,2560],[11264,4,128],[11264,4,128],[11264,2560],[],[],[],[],[],[],[],[],[]],"Input Strides":[[3584,1],[3584,128,1],[3584,128,1],[2560,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
