# KDA Prompt: srt_distributed_parallel_state_outplace_all_reduce

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `srt.distributed.parallel_state.outplace_all_reduce`

Goal: optimize or replace this interface for the internlm/Intern-S2-Preview-FP8 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `internlm/Intern-S2-Preview-FP8`
- Model folder: `llm/intern_s2_preview/b200`
- Category: `comm`
- Python interface: `srt.distributed.parallel_state.outplace_all_reduce`
- Captured call count: `16200`
- Captured variants: `104`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Executed Workload Matrix

The capture run executed all workload labels below for this model.
A specific interface may still be absent from a workload when the
serving path does not call it for that dataset/concurrency level.

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Observed Workloads For This Interface

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Not Observed For This Interface

- none

## Shape Summary

- `arg[0]: shape=[1, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[0]: shape=[1, 2048], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[0]: shape=[1, 2048], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1, 2048], dtype=bfloat16, device=cuda:3, contiguous=True`
- `arg[0]: shape=[103, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[0]: shape=[103, 2048], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[0]: shape=[103, 2048], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[103, 2048], dtype=bfloat16, device=cuda:3, contiguous=True`
- `arg[0]: shape=[11, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[0]: shape=[11, 2048], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[0]: shape=[11, 2048], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[11, 2048], dtype=bfloat16, device=cuda:3, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`324`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  group_name='tp:0'\n  outplace_all_reduce_method='ca'", "scalars": ["group_name='tp:0'", "outplace_all_reduce_method='ca'"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2048]}]}]`
   - kwargs: `{}`
2. label=`random_low`, calls=`324`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2048)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  group_name='tp:0'\n  outplace_all_reduce_method='ca'", "scalars": ["group_name='tp:0'", "outplace_all_reduce_method='ca'"], "tensors": [{"device": "cuda:1", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2048]}]}]`
   - kwargs: `{}`
3. label=`random_low`, calls=`324`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2048)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  group_name='tp:0'\n  outplace_all_reduce_method='ca'", "scalars": ["group_name='tp:0'", "outplace_all_reduce_method='ca'"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2048]}]}]`
   - kwargs: `{}`
4. label=`random_low`, calls=`324`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2048)\n      dtype=torch.bfloat16\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  group_name='tp:0'\n  outplace_all_reduce_method='ca'", "scalars": ["group_name='tp:0'", "outplace_all_reduce_method='ca'"], "tensors": [{"device": "cuda:3", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2048]}]}]`
   - kwargs: `{}`
5. label=`random_low`, calls=`81`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(103, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  group_name='tp:0'\n  outplace_all_reduce_method='ca'", "scalars": ["group_name='tp:0'", "outplace_all_reduce_method='ca'"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [103, 2048]}]}]`
   - kwargs: `{}`
6. label=`random_low`, calls=`81`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(103, 2048)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  group_name='tp:0'\n  outplace_all_reduce_method='ca'", "scalars": ["group_name='tp:0'", "outplace_all_reduce_method='ca'"], "tensors": [{"device": "cuda:1", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [103, 2048]}]}]`
   - kwargs: `{}`

Full structured args/kwargs/result records are in `docs/evidence.json`.

## Required First Milestone

1. Copy the upstream SGLang source files needed for this exact interface into `baseline/`.
2. Record upstream URL, commit, and copied files in `docs/baseline_source.md`.
3. Expose the copied baseline through a local low-overhead ABI.
4. Expose the candidate through the exact same ABI in `solution/`.
5. Build correctness tests for every retained captured variant or an explicitly justified representative subset.
6. Benchmark baseline and candidate on an idle B200 with the same shapes, dtypes, devices, contiguity, and scalar parameters.
- Unsupported shapes or parameter combinations must fall back to the recovered SGLang baseline.

Do not import, patch, or monkey-patch a live SGLang server during correctness or benchmark runs.
