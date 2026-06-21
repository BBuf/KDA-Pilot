# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `moe`
- Max observed GPU share: `48.15%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 23.61% GPU, calls=4464, mean=17.26 us
- `random_mid`: 43.66% GPU, calls=4464, mean=130.68 us
- `random_high`: 48.15% GPU, calls=4464, mean=116.58 us
- `sharegpt_low`: 24.78% GPU, calls=4464, mean=18.57 us
- `sharegpt_mid`: 43.36% GPU, calls=4464, mean=127.11 us
- `sharegpt_high`: 47.91% GPU, calls=4464, mean=110.83 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=236`: `{"Concrete Inputs":["[2]","3","0","","","0"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","","Scalar"]}`
2. `aten::view` via `external_id=11100`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[9468,2,128],[]],"Input Strides":[[256,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
3. `aten::view` via `external_id=22811`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[2797,2,128],[]],"Input Strides":[[2048,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
4. `aten::as_strided` via `external_id=30046`: `{"Concrete Inputs":["","[64]","[1]","0"],"Input Dims":[[16384],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
