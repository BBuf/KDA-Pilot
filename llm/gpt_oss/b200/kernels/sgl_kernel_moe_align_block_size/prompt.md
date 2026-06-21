# KDA Prompt: sgl_kernel_moe_align_block_size

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `sgl_kernel.moe_align_block_size`

Goal: optimize or replace this interface for the openai/gpt-oss-120b serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss/b200`
- Category: `moe`
- Python interface: `sgl_kernel.moe_align_block_size`
- Captured call count: `16360`
- Captured variants: `248`
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

- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:0, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:1, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:3, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:4, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:6, contiguous=True`
- `arg[0]: shape=[1, 4], dtype=int32, device=cuda:7, contiguous=True`
- `arg[0]: shape=[102, 4], dtype=int32, device=cuda:0, contiguous=True`
- `arg[0]: shape=[102, 4], dtype=int32, device=cuda:1, contiguous=True`
- `arg[0]: shape=[102, 4], dtype=int32, device=cuda:2, contiguous=True`
- `arg[0]: shape=[102, 4], dtype=int32, device=cuda:3, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`209`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=129\n  arg[2]=16\n  arg[3]=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[6]=Tensor(\n      shape=(130,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[7]=True", "scalars": ["arg[1]=129", "arg[2]=16", "arg[7]=True"], "tensors": [{"device...`
   - kwargs: `{}`
2. label=`random_low`, calls=`209`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=129\n  arg[2]=16\n  arg[3]=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[6]=Tensor(\n      shape=(130,)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[7]=True", "scalars": ["arg[1]=129", "arg[2]=16", "arg[7]=True"], "tensors": [{"device...`
   - kwargs: `{}`
3. label=`random_low`, calls=`209`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=129\n  arg[2]=16\n  arg[3]=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[6]=Tensor(\n      shape=(130,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[7]=True", "scalars": ["arg[1]=129", "arg[2]=16", "arg[7]=True"], "tensors": [{"device...`
   - kwargs: `{}`
4. label=`random_low`, calls=`209`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=129\n  arg[2]=16\n  arg[3]=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[6]=Tensor(\n      shape=(130,)\n      dtype=torch.int32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[7]=True", "scalars": ["arg[1]=129", "arg[2]=16", "arg[7]=True"], "tensors": [{"device...`
   - kwargs: `{}`
5. label=`random_low`, calls=`209`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=129\n  arg[2]=16\n  arg[3]=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[6]=Tensor(\n      shape=(130,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[7]=True", "scalars": ["arg[1]=129", "arg[2]=16", "arg[7]=True"], "tensors": [{"device...`
   - kwargs: `{}`
6. label=`random_low`, calls=`209`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=129\n  arg[2]=16\n  arg[3]=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[6]=Tensor(\n      shape=(130,)\n      dtype=torch.int32\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[7]=True", "scalars": ["arg[1]=129", "arg[2]=16", "arg[7]=True"], "tensors": [{"device...`
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
