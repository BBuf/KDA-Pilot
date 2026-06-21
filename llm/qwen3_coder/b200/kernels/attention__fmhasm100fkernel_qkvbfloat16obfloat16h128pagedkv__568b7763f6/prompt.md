# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__568b7763f6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Model folder: `llm/qwen3_coder/b200`
- Kernel category: `attention`
- Max observed GPU share: `4.66%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP32VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 3.18% GPU, calls=1984, mean=28.41 us
- `sharegpt_mid`: 2.67% GPU, calls=1984, mean=25.69 us
- `sharegpt_high`: 4.66% GPU, calls=2480, mean=32.64 us

## Promoted Shape Samples

1. `aten::to` via `external_id=28956`: `{"Concrete Inputs":["","","4","False","False",""],"Input Dims":[[1],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["long int","","Scalar","Scalar","Scalar",""]}`
2. `sglang::unified_attention_with_output` via `external_id=29190`: `{"Concrete Inputs":["","","","","False","0","","","","","","",""],"Input Dims":[[1536,1536],[1536,1,128],[1536,1,128],[1536,1536],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1792,1],[1792,128,1],[1792,128,1],[1536,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=29218`: `{"Concrete Inputs":["","","","","False","1","","","","","","",""],"Input Dims":[[1536,1536],[1536,1,128],[1536,1,128],[1536,1536],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1792,1],[1792,128,1],[1792,128,1],[1536,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
4. `sglang::unified_attention_with_output` via `external_id=43697`: `{"Concrete Inputs":["","","","","False","0","","","","","","",""],"Input Dims":[[2560,1536],[2560,1,128],[2560,1,128],[2560,1536],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1792,1],[1792,128,1],[1792,128,1],[1536,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
