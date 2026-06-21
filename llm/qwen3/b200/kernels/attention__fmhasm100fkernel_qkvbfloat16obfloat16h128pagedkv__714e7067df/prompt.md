# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507`
- Model folder: `llm/qwen3/b200`
- Kernel category: `attention`
- Max observed GPU share: `5.22%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 3.38% GPU, calls=3008, mean=23.13 us
- `sharegpt_mid`: 3.59% GPU, calls=3008, mean=22.48 us
- `sharegpt_high`: 5.22% GPU, calls=3760, mean=29.40 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=30213`: `{"Concrete Inputs":["","","","","False","0","","","","","","",""],"Input Dims":[[2560,1024],[2560,1,128],[2560,1,128],[2560,1024],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1280,1],[1280,128,1],[1280,128,1],[1024,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
2. `aten::as_strided` via `external_id=30443`: `{"Concrete Inputs":["","[2358, 1, 128]","[1280, 128, 1]","0"],"Input Dims":[[2560,1,128],[],[],[]],"Input Strides":[[1280,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `detach_` via `external_id=47525`: `{"Concrete Inputs":[""],"Input Dims":[[14]],"Input Strides":[[1]],"Input type":["int"]}`
4. `sglang::unified_attention_with_output` via `external_id=48085`: `{"Concrete Inputs":["","","","","False","17","","","","","","",""],"Input Dims":[[2560,1024],[2560,1,128],[2560,1,128],[2560,1024],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1280,1],[1280,128,1],[1280,128,1],[1024,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
