# KDA Prompt: comm__comm__2f32ca6996

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.5`
- Model folder: `llm/minimax_m25/b200`
- Kernel category: `comm`
- Max observed GPU share: `13.92%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 13.92% GPU, calls=9000, mean=11.33 us
- `sharegpt_mid`: 3.22% GPU, calls=6000, mean=11.80 us
- `sharegpt_high`: 3.99% GPU, calls=4000, mean=17.00 us

## Promoted Shape Samples

1. `aten::_index_put_impl_` via `external_id=4339`: `{"Concrete Inputs":["","","","False","False"],"Input Dims":[[4097],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","","long int","Scalar","Scalar"]}`
2. `aten::view` via `external_id=4337`: `{"Concrete Inputs":["","[]"],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
3. `aten::as_strided` via `external_id=46792`: `{"Concrete Inputs":["","[64859, 1, 64, 128]","[8192, 8192, 128, 1]",""],"Input Dims":[[64859,1,64,128],[],[],[]],"Input Strides":[[8192,128,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList",""]}`
4. `aten::permute` via `external_id=60632`: `{"Concrete Inputs":["","[0, 2, 1, 3]"],"Input Dims":[[64859,64,1,128],[]],"Input Strides":[[8192,128,128,1],[]],"Input type":["c10::Half","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
