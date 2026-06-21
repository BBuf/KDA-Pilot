# KDA Prompt: comm__nccldevkernel_allreduce_sum_f16_ring_ll__29d2bcd930

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `comm`
- Max observed GPU share: `9.78%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_f16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 9.78% GPU, calls=1312, mean=385.52 us

## Promoted Shape Samples

1. `sglang::inplace_all_reduce` via `external_id=29293`: `{"Concrete Inputs":["",""],"Input Dims":[[11225,4096],[]],"Input Strides":[[4096,1],[]],"Input type":["c10::Half",""]}`
2. `aten::empty` via `external_id=29489`: `{"Concrete Inputs":["[11225, 8]","3","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
