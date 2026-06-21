# KDA Prompt: attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__6f150a74e8

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-XS.2-FP8`
- Model folder: `llm/poolside_laguna_xs2/b200`
- Kernel category: `attention`
- Max observed GPU share: `3.77%`
- Kernel name: `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.06% GPU, calls=360, mean=32.08 us
- `random_high`: 3.77% GPU, calls=480, mean=32.09 us
- `sharegpt_mid`: 2.77% GPU, calls=600, mean=23.49 us
- `sharegpt_high`: 3.44% GPU, calls=720, mean=21.28 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=10761`: `{"Concrete Inputs":["","[11042, 2048]","[2560, 1]","0"],"Input Dims":[[11264,2048],[],[],[]],"Input Strides":[[2560,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
2. `sglang::unified_attention_with_output` via `external_id=22341`: `{"Concrete Inputs":["","","","","True","19","","",""],"Input Dims":[[2560,2048],[2560,2,128],[2560,2,128],[2560,2048],[],[],[],[],[]],"Input Strides":[[2560,1],[2560,128,1],[2560,128,1],[2048,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=21780`: `{"Concrete Inputs":["","","","","True","2","","",""],"Input Dims":[[2560,2048],[2560,2,128],[2560,2,128],[2560,2048],[],[],[],[],[]],"Input Strides":[[2560,1],[2560,128,1],[2560,128,1],[2048,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","",""]}`
4. `sglang::unified_attention_with_output` via `external_id=21747`: `{"Concrete Inputs":["","","","","True","1","","",""],"Input Dims":[[2560,2048],[2560,2,128],[2560,2,128],[2560,2048],[],[],[],[],[]],"Input Strides":[[2560,1],[2560,128,1],[2560,128,1],[2048,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
