# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-XS.2-FP8`
- Model folder: `llm/poolside_laguna_xs2/b200`
- Kernel category: `comm`
- Max observed GPU share: `9.66%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 9.66% GPU, calls=324, mean=166.88 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=10066`: `{"Concrete Inputs":["","","","","True","4","","",""],"Input Dims":[[11264,1536],[11264,2,128],[11264,2,128],[11264,1536],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,128,1],[2048,128,1],[1536,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
