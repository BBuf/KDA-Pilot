# KDA Prompt: other__other__56d7fd43dd

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`other` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Model folder: `llm/lfm25/b200`
- Kernel category: `other`
- Max observed GPU share: `4.35%`
- Kernel name: `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.94% GPU, calls=216, mean=2.75 us
- `random_mid`: 3.54% GPU, calls=216, mean=13.46 us
- `random_high`: 4.35% GPU, calls=216, mean=42.52 us
- `sharegpt_low`: 3.16% GPU, calls=216, mean=3.21 us
- `sharegpt_mid`: 3.51% GPU, calls=216, mean=14.26 us
- `sharegpt_high`: 3.73% GPU, calls=216, mean=28.29 us

## Promoted Shape Samples

1. `sglang::_run_activation_inplace` via `external_id=662`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[412,3584],[412,1792]],"Input Strides":[[],[3584,1],[1792,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`
2. `sglang::_run_activation_inplace` via `external_id=8578`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[30020,3584],[30020,1792]],"Input Strides":[[],[3584,1],[1792,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`
3. `sglang::_run_activation_inplace` via `external_id=8485`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[7505,14336],[7505,7168]],"Input Strides":[[],[14336,1],[7168,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`
4. `sglang::_run_activation_inplace` via `external_id=30273`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[65536,3584],[65536,1792]],"Input Strides":[[],[3584,1],[1792,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
