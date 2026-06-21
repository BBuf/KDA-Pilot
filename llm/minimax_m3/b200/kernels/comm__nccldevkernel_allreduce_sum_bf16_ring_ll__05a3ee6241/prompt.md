# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Model folder: `llm/minimax_m3/b200`
- Kernel category: `comm`
- Max observed GPU share: `21.06%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 19.65% GPU, calls=1936, mean=340.01 us
- `random_high`: 15.99% GPU, calls=1936, mean=256.60 us
- `sharegpt_mid`: 14.72% GPU, calls=968, mean=464.41 us
- `sharegpt_high`: 21.06% GPU, calls=1936, mean=368.06 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=39991`: `{"Concrete Inputs":["","[7168]","[1]","0"],"Input Dims":[[8192],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
2. `aten::fill_` via `external_id=39996`: `{"Concrete Inputs":["","971"],"Input Dims":[[],[]],"Input Strides":[[],[]],"Input type":["long int","Scalar"]}`
3. `sglang::outplace_all_reduce` via `external_id=40069`: `{"Concrete Inputs":["","",""],"Input Dims":[[7168,6144],[],[]],"Input Strides":[[6144,1],[],[]],"Input type":["c10::BFloat16","",""]}`
4. `sglang::outplace_all_reduce` via `external_id=67535`: `{"Concrete Inputs":["","",""],"Input Dims":[[5120,6144],[],[]],"Input Strides":[[6144,1],[],[]],"Input type":["c10::BFloat16","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
