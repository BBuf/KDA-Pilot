# KDA Prompt: comm__comm__0821f7c6e6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `comm`
- Max observed GPU share: `33.85%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 33.75% GPU, calls=2340, mean=56.43 us
- `random_mid`: 8.64% GPU, calls=2080, mean=35.52 us
- `random_high`: 20.78% GPU, calls=2080, mean=62.78 us
- `sharegpt_low`: 33.85% GPU, calls=2340, mean=60.70 us
- `sharegpt_mid`: 13.48% GPU, calls=2080, mean=69.58 us
- `sharegpt_high`: 26.01% GPU, calls=1820, mean=193.04 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=1785`: `{"Concrete Inputs":["","",""],"Input Dims":[[39,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::as_strided` via `external_id=1799`: `{"Concrete Inputs":["","[39, 1024]","[3072, 1]","2048"],"Input Dims":[[39,3072],[],[],[]],"Input Strides":[[3072,1],[],[],[]],"Input type":["float","ScalarList","ScalarList","Scalar"]}`
3. `aten::as_strided` via `external_id=1585`: `{"Concrete Inputs":["","[2304, 4096]","[1, 2304]",""],"Input Dims":[[4096,2304],[],[],[]],"Input Strides":[[2304,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`
4. `aten::transpose` via `external_id=1940`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[4096,256],[],[]],"Input Strides":[[256,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
