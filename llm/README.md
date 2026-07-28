# KDA-Pilot LLM Kernel Interface Tasks

This subtree records SGLang LLM kernel optimization tasks discovered from live
B200 serving runs, then optimized as standalone single-GPU kernel tasks.

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

## Adding a model

`scripts/` holds the two capture stages and the task generator:

1. **Cookbook-aligned profile** — one torch-profiler trace per scenario, then
   `scripts/extract_kernel_shapes.py --trace <TP-0.trace.json.gz> --label
   <scenario> --out-dir <dir>` per label to get the per-kernel GPU-time shares
   with CPU-op provenance. Two practical notes: a CPU+GPU trace records
   continuously from arm until `num_steps` is reached, so arm it only once the
   workload is already in steady state (an idle gap makes the export large
   enough to trip the request watchdog), and a CUDA-graph replay has no
   per-kernel CPU launcher, so provenance needs one short `--disable-cuda-graph`
   window. `--provenance-from` merges that window's kernel -> interface mapping
   into per-scenario shares taken from small GPU-only traces.
2. **Kernel API shapes** — launch with `scripts/sglang_capture_shape_sitecustomize.py`
   on `PYTHONPATH` plus `KDA_CAPTURE_SHAPES_JSONL`, walk the scenarios with the
   model's `run_<model>_shape_capture_requests.py`, then
   `scripts/aggregate_sglang_shape_capture.py --records ... --markers ...
   --only <task slugs>` to write `docs/captured_kernel_api_shapes.json` and
   `bench/workloads.json`. Pass `--only`: a capture run covers one model, and
   without it every other model's task matches nothing.
3. **Task generation** — `scripts/build_e2e_tasks.py --shapes-dir ... --model ...
   --model-slug ... --threshold 3.0`. `--interface-map` supplies vendor
   exclusions and interface names for kernels whose launcher registers no torch
   op (JIT tvm-ffi modules); see `scripts/kimi_k3_kernel_interface_map.json`.
   `--provenance-note` records a capture host that differs from the
   optimization target.

Raw per-scenario shares land in `scripts/data/<model_slug>/` so a task's
selection can be re-derived without re-running the model.

The important rule is symmetry: copy the relevant upstream SGLang implementation
into `baseline/`, expose baseline and candidate through matching local
interfaces, and benchmark only task-local code on one idle target GPU. The live
SGLang server is used for shape discovery and target selection, not as the
correctness or benchmark baseline. Do not require `sglang serve`, `run_capture`,
TP/EP, or an all-GPU idle serving slot during the kernel optimization loop.
