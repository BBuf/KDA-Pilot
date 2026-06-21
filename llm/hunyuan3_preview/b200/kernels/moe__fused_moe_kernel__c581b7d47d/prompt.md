# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `moe`
- Max observed GPU share: `34.73%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 15.84% GPU, calls=11776, mean=24.35 us
- `random_mid`: 34.73% GPU, calls=11744, mean=152.93 us
- `random_high`: 20.95% GPU, calls=11712, mean=100.46 us
- `sharegpt_low`: 12.37% GPU, calls=11776, mean=21.68 us
- `sharegpt_mid`: 21.16% GPU, calls=11680, mean=96.12 us
- `sharegpt_high`: 18.92% GPU, calls=11680, mean=89.67 us

## Promoted Shape Samples

1. `sglang::inplace_fused_experts` via `external_id=9354`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False"],"Input Dims":[[38,4096],[192,384,4096],[192,4096,192],[38,8],[38,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[1572864,4096,1],[786432,192,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar"]}`
2. `aten::empty` via `external_id=9346`: `{"Concrete Inputs":["[38, 192]","5","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
3. `aten::as_strided` via `external_id=36059`: `{"Concrete Inputs":["","[33056, 1, 64, 128]","[8192, 128, 128, 1]",""],"Input Dims":[[33056,64,1,128],[],[],[]],"Input Strides":[[8192,128,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList",""]}`
4. `sglang::inplace_fused_experts` via `external_id=64192`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","","","","False"],"Input Dims":[[1210,4096],[192,384,4096],[192,4096,192],[1210,8],[1210,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[4096,1],[1572864,4096,1],[786432,192,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::Half","c10::Half","c10::Half","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","","","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
