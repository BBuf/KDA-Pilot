# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Model folder: `llm/kimi_linear/b200`
- Kernel category: `moe`
- Max observed GPU share: `26.35%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 14.79% GPU, calls=1872, mean=12.31 us
- `random_high`: 25.03% GPU, calls=1872, mean=185.00 us
- `sharegpt_low`: 4.45% GPU, calls=1872, mean=9.92 us
- `sharegpt_mid`: 10.04% GPU, calls=1872, mean=73.54 us
- `sharegpt_high`: 26.35% GPU, calls=1872, mean=144.88 us

## Promoted Shape Samples

1. `aten::copy_` via `external_id=300`: `{"Concrete Inputs":["","","False"],"Input Dims":[[1],[1],[]],"Input Strides":[[1],[1],[]],"Input type":["int","int","Scalar"]}`
2. `sglang::inplace_fused_experts` via `external_id=106517`: `{"Concrete Inputs":["","","","","","","","","True","False","False","False","False","False","False","","","","","","","","2.4460000000000002","","","False",""],"Input Dims":[[16384,2304],[256,512,2304],[256,2304,256],[16384,8],[16384,8],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[2304,1],[1179648,2304,1],[589824,256,1],[8,1],[8,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","float","int","","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","","","","","","","Scalar","","","Scalar",""]}`
3. `aten::view` via `external_id=104706`: `{"Concrete Inputs":["","[-1, 512]"],"Input Dims":[[131072,512],[]],"Input Strides":[[512,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `aten::as_strided` via `external_id=102153`: `{"Concrete Inputs":["","[1]","[1]",""],"Input Dims":[[],[],[],[]],"Input Strides":[[],[],[],[]],"Input type":["long int","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
