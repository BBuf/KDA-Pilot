# Capture and selection tooling

| file | role |
| --- | --- |
| `nvcap.py` | the capture hook. Wraps the kernel entry points named in a target config, records every call's shapes/dtypes/strides/scalars into a per-process manifest, and saves budgeted real tensor payloads (inputs, outputs, and state rows before/after for state-carrying ops). Never raises into the serving stack. |
| `sitecustomize.py` | one-line shim so `PYTHONPATH=tools` arms the hook in the server process and in every TP / diffusion worker, with no change to the serving code. |
| `merge_manifests.py` | merges the per-process manifests and sums call counts. Required: SGLang runs TP ranks and diffusion workers in separate processes, and a process that never touched a wrapped op would otherwise clobber a busy process's manifest with an empty one. |
| `build_workloads.py` | turns a merged manifest into a task's `bench/workloads.json`: top-N signatures by real-traffic call count, plus the smallest and largest input footprint, plus one signature per operating point. Records why each row was kept. |
| `verify_state_chain.py` | proves a captured decode chain is a valid ground truth (step[n+1] state-before == step[n] state-after, byte for byte) and prints the per-step state change. |
| `check_hacks.py` | prints, on the shipped real tensors, the statistics that let three verifier shortcuts pass under synthetic Gaussian inputs (norm spread, energy in the smallest channels, gate/decay distribution). |
| `targets/*.json` | which entry points to wrap per task, plus per-op capture policy: `state_args` / `index_arg` (slice the touched state rows out of a pool), `gather_args` (store only the KV rows a call reads), `skip_args` (expert weights: metadata only), `chain` + `chain_key` (capture N consecutive steps of ONE layer instance). |

## Environment

```
NVCAP_DIR                output directory (required)
NVCAP_CONFIG             target list JSON (required)
NVCAP_NO_TENSORS=1       manifest only
NVCAP_GROUP_MB           tensor budget per capture group (default 80)
NVCAP_MAX_TENSOR_MB      per-tensor cap; larger tensors are recorded as metadata (default 96)
NVCAP_MAX_SHAPES_PER_OP  distinct shape folders per (group, op) (default 6)
NVCAP_OPS                comma-separated op allowlist
NVCAP_RANK               which local rank writes tensor payloads (default 0)
```

The active capture group is read from `$NVCAP_DIR/GROUP` on every call, so one
server process can be walked through a whole operating-point matrix; calls seen
with no GROUP file land in `warmup_only_shapes` and never enter a workload row.

## Gotchas we hit (all fixed here, worth knowing if you extend it)

* A pool tensor passed as both an argument and a state arg gets saved twice - once
  whole (tens of MB of unrelated slots). `index_arg` now demotes the full pool to
  metadata.
* Slicing the post-call state with a CPU index raises on a CUDA tensor, which
  silently dropped the `state_after` half of every payload. The index is kept on its
  original device now.
* `torch.compile` traces the wrapped Python entry once, so a compiled diffusion run
  shows ~1 step of calls. Capture with compile disabled.
* Editing a running bash driver script changes the behaviour of the *running*
  process (bash reads scripts incrementally). Restart the driver instead.
