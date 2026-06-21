# KDA Prompt: sgl_kernel_verify_tree_greedy

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `sgl_kernel.verify_tree_greedy`

Goal: optimize or replace this interface for the Qwen/Qwen3.6-35B-A3B-FP8 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen_36/b200`
- Category: `other`
- Python interface: `sgl_kernel.verify_tree_greedy`
- Captured call count: `32`
- Captured variants: `20`
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

- `accept_index: shape=[1, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[11, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[12, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[16, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[2, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[27, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[28, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[32, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[4, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[44, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[45, 4], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[69, 4], dtype=int32, device=cuda:0, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`4`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(4,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(1, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(1, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(1, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(1, 4)\n      dtype=torch.int64\n      device=cud...`
   - kwargs: `{}`
2. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(112,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(28, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(28,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(28, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(28, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(28, 4)\n      dtype=torch.int64\n      dev...`
   - kwargs: `{}`
3. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(128,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(32, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(32,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(32, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(32, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(32, 4)\n      dtype=torch.int64\n      dev...`
   - kwargs: `{}`
4. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(36,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(9, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(9,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(9, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(9, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(9, 4)\n      dtype=torch.int64\n      device=cu...`
   - kwargs: `{}`
5. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(64,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(16, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(16,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(16, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(16, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(16, 4)\n      dtype=torch.int64\n      devi...`
   - kwargs: `{}`
6. label=`random_high`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(176,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(44, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(44,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(44, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(44, 4)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(44, 4)\n      dtype=torch.int64\n      dev...`
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
