# KDA Prompt: moe__moe_sum_reduce_kernel_warp_token_topk__43207a7c49

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.83%`
- Kernel name: `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, long, long, long, long, long, at::OpMathType<c10::Half>::type)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.83% GPU, calls=496, mean=76.28 us
- `sharegpt_mid`: 2.72% GPU, calls=744, mean=47.79 us

## Promoted Shape Samples

1. `aten::view` via `external_id=11100`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[9468,2,128],[]],"Input Strides":[[256,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
2. `aten::as_strided` via `external_id=44058`: `{"Concrete Inputs":["","[25357, 2, 64, 128]","[16384, 128, 256, 1]",""],"Input Dims":[[25357,64,2,128],[],[],[]],"Input Strides":[[16384,256,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
