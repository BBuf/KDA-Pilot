# KDA Prompt: comm__comm__9cd2963a17

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.5`
- Model folder: `llm/minimax_m25/b200`
- Kernel category: `comm`
- Max observed GPU share: `9.65%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.08% GPU, calls=1000, mean=47.03 us
- `random_high`: 9.65% GPU, calls=6000, mean=26.83 us
- `sharegpt_high`: 8.28% GPU, calls=5000, mean=28.23 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=9120`: `{"Concrete Inputs":["","","","","True","2","","","","","","",""],"Input Dims":[[832,768],[832,1,128],[832,1,128],[832,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","c10::Half","Scalar","Scalar","","","","","","",""]}`
2. `aten::slice` via `external_id=31636`: `{"Concrete Inputs":["","0","0","256","1"],"Input Dims":[[277],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::permute` via `external_id=74327`: `{"Concrete Inputs":["","[0, 2, 1, 3]"],"Input Dims":[[64859,64,1,128],[]],"Input Strides":[[8192,128,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
4. `aten::view` via `external_id=63081`: `{"Concrete Inputs":["","[-1, 768]"],"Input Dims":[[386,6,128],[]],"Input Strides":[[768,128,1],[]],"Input type":["c10::Half","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
