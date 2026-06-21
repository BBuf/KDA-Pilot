# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `attention`
- Max observed GPU share: `5.38%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.07% GPU, calls=1488, mean=22.72 us
- `sharegpt_mid`: 2.85% GPU, calls=1984, mean=29.32 us
- `sharegpt_high`: 5.38% GPU, calls=2976, mean=29.41 us

## Promoted Shape Samples

1. `aten::view` via `external_id=25652`: `{"Concrete Inputs":["","[-1, 64, 1, 128]"],"Input Dims":[[4148736,1,128],[]],"Input Strides":[[128,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
2. `sglang::unified_attention_with_output` via `external_id=24179`: `{"Concrete Inputs":["","","","","True","0","","","","","","",""],"Input Dims":[[3072,768],[3072,1,128],[3072,1,128],[3072,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=26060`: `{"Concrete Inputs":["","","","","True","57","","","","","","",""],"Input Dims":[[3072,768],[3072,1,128],[3072,1,128],[3072,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
4. `aten::copy_` via `external_id=45894`: `{"Concrete Inputs":["","","False"],"Input Dims":[[5552,768],[5552,768],[]],"Input Strides":[[768,1],[768,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
