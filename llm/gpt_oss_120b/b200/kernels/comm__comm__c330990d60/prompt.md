# KDA Prompt: comm__comm__c330990d60

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss_120b/b200`
- Kernel category: `comm`
- Max observed GPU share: `8.07%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 8.07% GPU, calls=616, mean=87.75 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=41373`: `{"Concrete Inputs":["","[192, 1, 64]","[640, 64, 1]","0"],"Input Dims":[[192,1,64],[],[],[]],"Input Strides":[[640,64,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
2. `aten::as_strided` via `external_id=43867`: `{"Concrete Inputs":["","[2373, 512]","[512, 1]","0"],"Input Dims":[[2560,512],[],[],[]],"Input Strides":[[512,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
