# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-M.1-NVFP4`
- Model folder: `llm/laguna_m1/b200`
- Kernel category: `comm`
- Max observed GPU share: `11.71%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 8.18% GPU, calls=1128, mean=274.60 us
- `random_high`: 5.29% GPU, calls=1128, mean=124.41 us
- `sharegpt_mid`: 11.71% GPU, calls=3384, mean=177.13 us

## Promoted Shape Samples

1. `aten::to` via `external_id=12227`: `{"Concrete Inputs":["","","6","False","False",""],"Input Dims":[[17],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["float","","Scalar","Scalar","Scalar",""]}`
2. `aten::as_strided` via `external_id=28070`: `{"Concrete Inputs":["","[2774, 1, 128]","[1280, 128, 1]","0"],"Input Dims":[[2816,1,128],[],[],[]],"Input Strides":[[1280,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `aten::detach_` via `external_id=44327`: `{"Concrete Inputs":[""],"Input Dims":[[15]],"Input Strides":[[1]],"Input type":["float"]}`
4. `aten::_to_copy` via `external_id=47112`: `{"Concrete Inputs":["","29","0","","","True",""],"Input Dims":[[16],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[]],"Input type":["long unsigned int","Scalar","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
