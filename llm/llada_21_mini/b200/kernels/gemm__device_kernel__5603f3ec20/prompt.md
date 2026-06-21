# KDA Prompt: gemm__device_kernel__5603f3ec20

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/LLaDA2.1-mini`
- Model folder: `llm/llada_21_mini/b200`
- Kernel category: `gemm`
- Max observed GPU share: `7.38%`
- Kernel name: `void cutlass::device_kernel<cutlass::fmha::kernel::Sm100FmhaFwdKernelTmaWarpspecialized<cute::tuple<cutlass::fmha::collective::VariableLength, cutlass::fmha::collective::VariableLength, int, cute::tuple<cute::tuple<int, int>, int> >, cutlass::fmha::collective::Sm100FmhaFwdMainloopTmaWarpspecialized<cutlass::bfloat16_t, float, float, cute::tuple<cute::C<256>, cute::C<128>, cute::C<128> >, cute::tuple<cute::C<256>, cute::C<128>, cute::C<128> >, cute::tuple<int, cute::C<1>, cute::tuple<int, int> >, cute::tuple<int, cute::C<1>, cute::tuple<cute::C<0>, int> >, cute::tuple<cute::C<1>, int, cute::tuple<cute::C<0>, int> >, cutlass::fmha::collective::ResidualMask, cute::tuple<cute::C<2>, cute::C<1>, cute::C<1> > >, cutlass::fmha::collective::Sm100FmhaFwdEpilogueTmaWarpspecialized<cutlass::bfloat16_t, float, cute::tuple<cute::C<128>, cute::C<128>, cute::C<128> > >, cutlass::fmha::kernel::HostPrecomputedTileScheduler, cutlass::fmha::kernel::Sm100FmhaCtxKernelWarpspecializedSchedule> >(cutlass::fmha::kernel::Sm100FmhaFwdKernelTmaWarpspecialized<cute::tuple<cutlass::fmha::collective::VariableLength, cutlass::fmha::collective::VariableLength, int, cute::tuple<cute::tuple<int, int>, int> >, cutlass::fmha::collective::Sm100FmhaFwdMainloopTmaWarpspecialized<cutlass::bfloat16_t, float, float, cute::tuple<cute::C<256>, cute::C<128>, cute::C<128> >, cute::tuple<cute::C<256>, cute::C<128>, cute::C<128> >, cute::tuple<int, cute::C<1>, cute::tuple<int, int> >, cute::tuple<int, cute::C<1>, cute::tuple<cute::C<0>, int> >, cute::tuple<cute::C<1>, int, cute::tuple<cute::C<0>, int> >, cutlass::fmha::collective::ResidualMask, cute::tuple<cute::C<2>, cute::C<1>, cute::C<1> > >, cutlass::fmha::collective::Sm100FmhaFwdEpilogueTmaWarpspecialized<cutlass::bfloat16_t, float, cute::tuple<cute::C<128>, cute::C<128>, cute::C<128> > >, cutlass::fmha::kernel::HostPrecomputedTileScheduler, cutlass::fmha::kernel::Sm100FmhaCtxKernelWarpspecializedSchedule>::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 7.38% GPU, calls=2240, mean=16.01 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=10331`: `{"Concrete Inputs":["","0","1","2","1"],"Input Dims":[[2],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`
2. `aten::slice` via `external_id=20071`: `{"Concrete Inputs":["","0","0","32","1"],"Input Dims":[[32,157184],[],[],[],[]],"Input Strides":[[157184,1],[],[],[],[]],"Input type":["float","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::slice` via `external_id=4675`: `{"Concrete Inputs":["","0","0","1","1"],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
