# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Model folder: `llm/qwen3_coder/b200`
- Kernel category: `comm`
- Max observed GPU share: `16.30%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 16.30% GPU, calls=1000, mean=562.30 us
- `sharegpt_mid`: 10.16% GPU, calls=1016, mean=190.72 us

## Promoted Shape Samples

1. `record_param_comms` via `external_id=10848`: `{"Concrete Inputs":["","","","4","","[]","[]","0","1","8"],"Input Dims":[[[11011,6144]],[],[],[],[],[],[],[],[],[]],"Input Strides":[[[6144,1]],[],[],[],[],[],[],[],[],[]],"Input type":["TensorList","","","Scalar","","ScalarList","ScalarList","Scalar","Scalar","Scalar"]}`
2. `aten::lift_fresh` via `external_id=43593`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["int"]}`
3. `aten::to` via `external_id=45901`: `{"Concrete Inputs":["","4","0","","","True","False",""],"Input Dims":[[1950],[],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[],[]],"Input type":["long int","Scalar","Scalar","","","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
