# KDA Prompt: moe__fused_moe_kernel__c581b7d47d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-XS.2-FP8`
- Model folder: `llm/poolside_laguna_xs2/b200`
- Kernel category: `moe`
- Max observed GPU share: `20.20%`
- Kernel name: `fused_moe_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 11.76% GPU, calls=2808, mean=9.18 us
- `random_mid`: 20.20% GPU, calls=2808, mean=40.28 us
- `random_high`: 15.89% GPU, calls=2808, mean=23.14 us
- `sharegpt_high`: 13.91% GPU, calls=2808, mean=22.08 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=392`: `{"Concrete Inputs":["","[4097, 38]","[262148, 1]","0"],"Input Dims":[[4097,262148],[],[],[]],"Input Strides":[[262148,1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`
2. `sglang::unified_attention_with_output` via `external_id=10066`: `{"Concrete Inputs":["","","","","True","4","","",""],"Input Dims":[[11264,1536],[11264,2,128],[11264,2,128],[11264,1536],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,128,1],[2048,128,1],[1536,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","",""]}`
3. `aten::cat` via `external_id=21160`: `{"Concrete Inputs":["","0"],"Input Dims":[[[704]],[]],"Input Strides":[[[1]],[]],"Input type":["TensorList","Scalar"]}`
4. `aten::cat` via `external_id=55830`: `{"Concrete Inputs":["","0"],"Input Dims":[[[512]],[]],"Input Strides":[[[1]],[]],"Input type":["TensorList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
