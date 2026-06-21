# KDA Prompt: comm__comm__554010158e

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `comm`
- Max observed GPU share: `7.54%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 7.54% GPU, calls=4500, mean=5.47 us
- `random_mid`: 3.12% GPU, calls=4000, mean=10.42 us
- `random_high`: 3.18% GPU, calls=3500, mean=9.81 us
- `sharegpt_low`: 7.37% GPU, calls=4500, mean=5.48 us
- `sharegpt_high`: 3.53% GPU, calls=3500, mean=10.40 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=236`: `{"Concrete Inputs":["[2]","3","0","","","0"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","","Scalar"]}`
2. `aten::argmax` via `external_id=4300`: `{"Concrete Inputs":["","-1","False"],"Input Dims":[[1,200064],[],[]],"Input Strides":[[200064,1],[],[]],"Input type":["float","Scalar","Scalar"]}`
3. `aten::slice` via `external_id=8626`: `{"Concrete Inputs":["","0","0","253","1"],"Input Dims":[[256,2,128],[],[],[],[]],"Input Strides":[[2048,128,1],[],[],[],[]],"Input type":["c10::Half","Scalar","Scalar","Scalar","Scalar"]}`
4. `sglang::unified_attention_with_output` via `external_id=17618`: `{"Concrete Inputs":["","","","","True","6","","","","","","",""],"Input Dims":[[48,1536],[48,2,128],[48,2,128],[48,1536],[],[],[],[],[],[],[],[],[]],"Input Strides":[[1536,1],[256,128,1],[2048,128,1],[1536,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","c10::Half","Scalar","Scalar","","","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
