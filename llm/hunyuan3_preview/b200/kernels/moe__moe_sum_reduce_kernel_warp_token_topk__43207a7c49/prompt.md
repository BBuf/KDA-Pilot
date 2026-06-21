# KDA Prompt: moe__moe_sum_reduce_kernel_warp_token_topk__43207a7c49

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.78%`
- Kernel name: `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, long, long, long, long, long, at::OpMathType<c10::Half>::type)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.78% GPU, calls=640, mean=224.76 us

## Promoted Shape Samples

1. `aten::matmul` via `external_id=37644`: `{"Concrete Inputs":["",""],"Input Dims":[[11225,4096],[4096,192]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`
2. `sgl_kernel::moe_sum_reduce` via `external_id=34810`: `{"Concrete Inputs":["","","1."],"Input Dims":[[11225,8,4096],[11225,4096],[]],"Input Strides":[[32768,4096,1],[4096,1],[]],"Input type":["c10::Half","c10::Half","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
