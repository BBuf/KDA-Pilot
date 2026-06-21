# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h64pagedkvc__2d54ccf3a0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `attention`
- Max observed GPU share: `2.91%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.91% GPU, calls=1152, mean=7.45 us

## Promoted Shape Samples

1. `aten::view` via `external_id=4008`: `{"Concrete Inputs":["","[1]"],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
2. `aten::empty_like` via `external_id=4015`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[1],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["long int","","","","Scalar",""]}`
3. `aten::empty_strided` via `external_id=4016`: `{"Concrete Inputs":["[1]","[1]","4","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
