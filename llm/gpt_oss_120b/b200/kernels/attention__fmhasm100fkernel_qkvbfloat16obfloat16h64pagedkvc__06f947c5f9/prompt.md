# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h64pagedkvc__06f947c5f9

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `attention`
- Max observed GPU share: `2.55%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 2.55% GPU, calls=576, mean=29.68 us

## Promoted Shape Samples

1. `aten::view` via `external_id=43902`: `{"Concrete Inputs":["","[-1, 64]"],"Input Dims":[[2373,1,64],[]],"Input Strides":[[640,64,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
2. `sglang::unified_attention_with_output` via `external_id=43362`: `{"Concrete Inputs":["","","","","True","1","","","","","","",""],"Input Dims":[[2560,512],[2560,1,64],[2560,1,64],[2560,512],[],[],[],[],[8],[],[],[],[]],"Input Strides":[[640,1],[640,64,1],[640,64,1],[512,1],[],[],[],[],[1],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","float","","","",""]}`
3. `aten::index_put_` via `external_id=44562`: `{"Concrete Inputs":["","","","False"],"Input Dims":[[4097],[],[81],[]],"Input Strides":[[1],[],[1],[]],"Input type":["long int","","long int","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
