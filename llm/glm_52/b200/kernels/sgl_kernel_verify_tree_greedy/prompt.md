# KDA Prompt: sgl_kernel_verify_tree_greedy

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `sgl_kernel.verify_tree_greedy`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `other`
- Python interface: `sgl_kernel.verify_tree_greedy`
- Captured call count: `187`
- Captured variants: `95`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `accept_index: shape=[1, 2], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[1, 2], dtype=int32, device=cuda:2, contiguous=True`
- `accept_index: shape=[1, 2], dtype=int32, device=cuda:3, contiguous=True`
- `accept_index: shape=[1, 2], dtype=int32, device=cuda:4, contiguous=True`
- `accept_index: shape=[1, 2], dtype=int32, device=cuda:5, contiguous=True`
- `accept_index: shape=[1, 2], dtype=int32, device=cuda:6, contiguous=True`
- `accept_index: shape=[1, 2], dtype=int32, device=cuda:7, contiguous=True`
- `accept_index: shape=[10, 2], dtype=int32, device=cuda:0, contiguous=True`
- `accept_index: shape=[10, 2], dtype=int32, device=cuda:1, contiguous=True`
- `accept_index: shape=[10, 2], dtype=int32, device=cuda:2, contiguous=True`
- `accept_index: shape=[10, 2], dtype=int32, device=cuda:3, contiguous=True`
- `accept_index: shape=[10, 2], dtype=int32, device=cuda:4, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`3`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(1, 2)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cud...`
   - kwargs: `{}`
2. label=`random_mid`, calls=`3`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(1, 2)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cud...`
   - kwargs: `{}`
3. label=`random_mid`, calls=`3`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(1, 2)\n      dtype=torch.int32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(1,)\n      dtype=torch.int32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cud...`
   - kwargs: `{}`
4. label=`random_mid`, calls=`3`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(6,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(3, 2)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cud...`
   - kwargs: `{}`
5. label=`random_mid`, calls=`3`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(6,)\n      dtype=torch.int32\n      device=cuda:7\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(3, 2)\n      dtype=torch.int32\n      device=cuda:7\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:7\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cuda:7\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cuda:7\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cud...`
   - kwargs: `{}`
6. label=`random_mid`, calls=`2`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  predicts=Tensor(\n      shape=(6,)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_index=Tensor(\n      shape=(3, 2)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  accept_token_num=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  candidates=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_index=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  retrive_next_token=Tensor(\n      shape=(3, 2)\n      dtype=torch.int64\n      device=cud...`
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
