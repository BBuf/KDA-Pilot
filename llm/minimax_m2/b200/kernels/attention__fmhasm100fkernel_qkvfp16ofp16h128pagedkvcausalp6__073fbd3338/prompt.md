# KDA Prompt: attention__fmhasm100fkernel_qkvfp16ofp16h128pagedkvcausalp6__073fbd3338

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `attention`
- Max observed GPU share: `3.47%`
- Kernel name: `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.35% GPU, calls=744, mean=34.16 us
- `sharegpt_mid`: 2.83% GPU, calls=992, mean=37.29 us
- `sharegpt_high`: 3.47% GPU, calls=1240, mean=28.93 us

## Promoted Shape Samples

1. `aten::view` via `external_id=22813`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[1622848,2,128],[]],"Input Strides":[[256,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
2. `sglang::unified_attention_with_output` via `external_id=22613`: `{"Concrete Inputs":["","","","","True","0","","","","","","",""],"Input Dims":[[2816,1536],[2816,2,128],[2816,2,128],[2816,1536],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1536,1],[256,128,1],[2048,128,1],[1536,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","c10::Half","Scalar","Scalar","","","","","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=24039`: `{"Concrete Inputs":["","","","","True","46","","","","","","",""],"Input Dims":[[2816,1536],[2816,2,128],[2816,2,128],[2816,1536],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1536,1],[256,128,1],[2048,128,1],[1536,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","c10::Half","Scalar","Scalar","","","","","","",""]}`
4. `aten::empty_strided` via `external_id=44060`: `{"Concrete Inputs":["[5524, 12, 128]","[1536, 128, 1]","5","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
