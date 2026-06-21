# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `comm`
- Max observed GPU share: `10.41%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 8.01% GPU, calls=356, mean=385.19 us
- `random_high`: 10.41% GPU, calls=1068, mean=374.44 us
- `sharegpt_mid`: 6.24% GPU, calls=356, mean=242.91 us
- `sharegpt_high`: 9.41% GPU, calls=712, mean=419.61 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=15494`: `{"Concrete Inputs":["","",""],"Input Dims":[[16384,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::empty` via `external_id=16016`: `{"Concrete Inputs":["[1, 128, 2, 128, 128]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
3. `aten::empty` via `external_id=16116`: `{"Concrete Inputs":["[1, 32, 8192]","6","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
4. `aten::item` via `external_id=46226`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["long int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
