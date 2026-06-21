# KDA Prompt: attention__fmhasm100fkernel_qkvfp16ofp16h128pagedkvcausalp6__073fbd3338

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.5`
- Model folder: `llm/minimax_m25/b200`
- Kernel category: `attention`
- Max observed GPU share: `5.20%`
- Kernel name: `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 3.61% GPU, calls=3472, mean=17.34 us
- `sharegpt_mid`: 2.70% GPU, calls=1984, mean=29.99 us
- `sharegpt_high`: 5.20% GPU, calls=2976, mean=29.82 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=32354`: `{"Concrete Inputs":["","","","","True","0","","","","","","",""],"Input Dims":[[768,768],[768,1,128],[768,1,128],[768,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","c10::Half","Scalar","Scalar","","","","","","",""]}`
2. `aten::to` via `external_id=31638`: `{"Concrete Inputs":["","4","False","True",""],"Input Dims":[[256],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar",""]}`
3. `aten::as_strided` via `external_id=31671`: `{"Concrete Inputs":["","[161]","[1]","68224364"],"Input Dims":[[196612],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`
4. `sglang::unified_attention_with_output` via `external_id=33311`: `{"Concrete Inputs":["","","","","True","29","","","","","","",""],"Input Dims":[[768,768],[768,1,128],[768,1,128],[768,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","c10::Half","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
