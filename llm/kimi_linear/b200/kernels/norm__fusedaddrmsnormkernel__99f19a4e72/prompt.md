# KDA Prompt: norm__fusedaddrmsnormkernel__99f19a4e72

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`norm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Model folder: `llm/kimi_linear/b200`
- Kernel category: `norm`
- Max observed GPU share: `25.98%`
- Kernel name: `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 25.98% GPU, calls=216, mean=501.91 us
- `sharegpt_mid`: 16.44% GPU, calls=432, mean=521.96 us

## Promoted Shape Samples

1. `aten::empty_like` via `external_id=113582`: `{"Concrete Inputs":["","","","","False",""],"Input Dims":[[1024,15],[],[],[],[],[]],"Input Strides":[[1,3336],[],[],[],[],[]],"Input type":["c10::BFloat16","","","","Scalar",""]}`
2. `aten::lift_fresh` via `external_id=129316`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["int"]}`
3. `aten::as_strided` via `external_id=130460`: `{"Concrete Inputs":["","[1, 257, 8, 128]","[263168, 1024, 128, 1]",""],"Input Dims":[[257,8,128],[],[],[]],"Input Strides":[[1024,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
