# KDA Prompt: moe__moe_sum_reduce_warp_per_token_vec_kernel__3fc4b40863

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Model folder: `llm/kimi_linear/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.47%`
- Kernel name: `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, long, long, long, long, long, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.47% GPU, calls=416, mean=82.16 us
- `sharegpt_high`: 2.35% GPU, calls=416, mean=58.17 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=101865`: `{"Concrete Inputs":["","[]","[]","9"],"Input Dims":[[1],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
2. `aten::as_strided` via `external_id=102167`: `{"Concrete Inputs":["","[1]","[1]",""],"Input Dims":[[],[],[],[]],"Input Strides":[[],[],[],[]],"Input type":["long int","ScalarList","ScalarList",""]}`
3. `aten::as_strided` via `external_id=95373`: `{"Concrete Inputs":["","[4864]","[1]","13"],"Input Dims":[[4865],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
4. `aten::view` via `external_id=96837`: `{"Concrete Inputs":["","[16384, 8, 128]"],"Input Dims":[[16384,1024],[]],"Input Strides":[[1024,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
