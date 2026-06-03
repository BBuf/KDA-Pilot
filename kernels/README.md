# Kernel Tasks

Diffusion task folders are clean standalone workspaces. They no longer contain
historical candidates, CSV ledgers, SGLang monkey-patch code, export scripts, or
captured-shape artifacts.

Each diffusion task contains:

```text
prompt.md
config.toml
baseline/.gitkeep
solution/.gitkeep
bench/.gitkeep
docs/.gitkeep
```

During a run, the agent fills:

- `baseline/` with copied upstream SGLang baseline source and a local baseline
  ABI wrapper.
- `solution/` with the optimized candidate using the same ABI.
- `bench/` with workload generation, correctness checks, and benchmark scripts.
- `docs/` with source provenance, run logs, benchmark tables, and profiling notes.

The required benchmark contract is in
[`../docs/standalone_diffusion_benchmark.md`](../docs/standalone_diffusion_benchmark.md).
