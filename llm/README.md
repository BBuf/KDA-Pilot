# KDA-Pilot LLM Kernel Interface Tasks

This subtree records SGLang LLM kernel optimization tasks from live B200 serving
runs.

The current LLM task source is runtime SGLang kernel API logging:

```bash
SGLANG_KERNEL_API_LOGLEVEL=3
SGLANG_KERNEL_API_LOGDEST=/path/to/kernel_api_%i.log
```

The resulting task shapes are direct Python-interface arguments and return
metadata for SGLang kernel entry points. They are not torch-profiler CPU op
context rows.

For each model run, the capture matrix keeps the serving command fixed and
covers two datasets at three concurrency levels:

- `random_low`, `random_mid`, `random_high`
- `sharegpt_low`, `sharegpt_mid`, `sharegpt_high`

Each generated kernel task owns:

```text
prompt.md       task card for the agent
config.toml     task/build/benchmark defaults
baseline/       copied upstream SGLang baseline source
solution/       optimized candidate source
bench/          standalone benchmark and correctness harness
docs/           evidence.json and source notes
profile/        optional profiling notes for later optimization loops
ncu/            optional Nsight Compute reports
tests/          task-local correctness tests
```

Task directory names are the full Python kernel interface slugified with dots
and symbols converted to underscores, for example
`sgl_kernel_build_tree_kernel_efficient`.

The important rule is symmetry: copy the relevant upstream SGLang implementation
into `baseline/`, expose baseline and candidate through matching local
interfaces, and benchmark only task-local code. The live SGLang server is used
for shape discovery, not as the correctness or benchmark baseline.
