# KDA Prompt: comm__comm__c330990d60

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `comm`
- Max observed GPU share: `10.87%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.31% GPU, calls=1000, mean=47.26 us
- `sharegpt_high`: 10.87% GPU, calls=5000, mean=35.36 us

## Promoted Shape Samples

1. `detach_` via `external_id=9124`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["int"]}`
2. `sglang::unified_attention_with_output` via `external_id=65416`: `{"Concrete Inputs":["","","","","True","6","","","","","","",""],"Input Dims":[[1536,768],[1536,1,128],[1536,1,128],[1536,768],[],[],[],[],[],[],[],[],[]],"Input Strides":[[768,1],[128,128,1],[1024,128,1],[768,1],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","","","","","",""]}`
3. `aten::slice` via `external_id=54271`: `{"Concrete Inputs":["","0","0","334","1"],"Input Dims":[[352,768],[],[],[],[]],"Input Strides":[[768,1],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
