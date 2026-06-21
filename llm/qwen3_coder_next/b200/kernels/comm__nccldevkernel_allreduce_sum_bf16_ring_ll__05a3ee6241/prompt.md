# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-Next`
- Model folder: `llm/qwen3_coder_next/b200`
- Kernel category: `comm`
- Max observed GPU share: `4.37%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 4.37% GPU, calls=388, mean=152.40 us

## Promoted Shape Samples

1. `aten::to` via `external_id=131294`: `{"Concrete Inputs":["","4","False","False",""],"Input Dims":[[16384],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar",""]}`
2. `sglang::store_cache` via `external_id=134384`: `{"Concrete Inputs":["","","","","","512","0","3528493"],"Input Dims":[[16384,256],[16384,256],[3528493,256],[3528493,256],[16384],[],[],[]],"Input Strides":[[256,1],[4608,1],[256,1],[256,1],[1],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","long int","Scalar","Scalar","Scalar"]}`
3. `aten::empty` via `external_id=131735`: `{"Concrete Inputs":["[1]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`
4. `aten::empty` via `external_id=144006`: `{"Concrete Inputs":["[0]","15","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
