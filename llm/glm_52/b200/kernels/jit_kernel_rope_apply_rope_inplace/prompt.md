# KDA Prompt: jit_kernel_rope_apply_rope_inplace

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `jit_kernel.rope.apply_rope_inplace`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `rope`
- Python interface: `jit_kernel.rope.apply_rope_inplace`
- Captured call count: `25181`
- Captured variants: `262`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `arg[0]: shape=[1055, 1, 64], dtype=bfloat16, device=cuda:5, contiguous=False`
- `arg[0]: shape=[1055, 64, 64], dtype=bfloat16, device=cuda:5, contiguous=False`
- `arg[0]: shape=[1095, 1, 64], dtype=bfloat16, device=cuda:2, contiguous=False`
- `arg[0]: shape=[1095, 64, 64], dtype=bfloat16, device=cuda:2, contiguous=False`
- `arg[0]: shape=[110, 1, 64], dtype=bfloat16, device=cuda:2, contiguous=False`
- `arg[0]: shape=[110, 64, 64], dtype=bfloat16, device=cuda:2, contiguous=False`
- `arg[0]: shape=[1167, 1, 64], dtype=bfloat16, device=cuda:6, contiguous=False`
- `arg[0]: shape=[1167, 64, 64], dtype=bfloat16, device=cuda:6, contiguous=False`
- `arg[0]: shape=[14, 32, 64], dtype=bfloat16, device=cuda:0, contiguous=False`
- `arg[0]: shape=[14, 32, 64], dtype=bfloat16, device=cuda:1, contiguous=False`
- `arg[0]: shape=[14, 32, 64], dtype=bfloat16, device=cuda:2, contiguous=False`
- `arg[0]: shape=[14, 32, 64], dtype=bfloat16, device=cuda:3, contiguous=False`

## Captured Variants

1. label=`random_low`, calls=`237`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 64, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(1048960, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  is_neox=False\n  rope_dim=0", "scalars": ["is_neox=False", "rope_dim=0"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": false, "kind": "tensor", "name": "arg[0]", "requires_grad": ...`
   - kwargs: `{}`
2. label=`random_low`, calls=`79`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(38, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(38, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(1048960, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(38,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  is_neox=False\n  rope_dim=0", "scalars": ["is_neox=False", "rope_dim=0"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": false, "kind": "tensor", "name": "arg[0]", "requires_grad"...`
   - kwargs: `{}`
3. label=`random_low`, calls=`79`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(38, 64, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(38, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(1048960, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(38,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  is_neox=False\n  rope_dim=0", "scalars": ["is_neox=False", "rope_dim=0"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": false, "kind": "tensor", "name": "arg[0]", "requires_grad...`
   - kwargs: `{}`
4. label=`random_low`, calls=`66`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 32, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(1048960, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  is_neox=False\n  rope_dim=0", "scalars": ["is_neox=False", "rope_dim=0"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": false, "kind": "tensor", "name": "arg[0]", "requires_grad": ...`
   - kwargs: `{}`
5. label=`random_mid`, calls=`158`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(6, 64, 64)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(6, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(1048960, 64)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6,)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  is_neox=False\n  rope_dim=0", "scalars": ["is_neox=False", "rope_dim=0"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": false, "kind": "tensor", "name": "arg[0]", "requires_grad": ...`
   - kwargs: `{}`
6. label=`random_mid`, calls=`158`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(6, 64, 64)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(6, 1, 64)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(1048960, 64)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6,)\n      dtype=torch.int64\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\nKeyword input arguments:\n  is_neox=False\n  rope_dim=0", "scalars": ["is_neox=False", "rope_dim=0"], "tensors": [{"device": "cuda:1", "dtype": "bfloat16", "is_contiguous": false, "kind": "tensor", "name": "arg[0]", "requires_grad": ...`
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
