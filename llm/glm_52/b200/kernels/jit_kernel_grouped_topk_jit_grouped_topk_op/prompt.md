# KDA Prompt: jit_kernel_grouped_topk_jit_grouped_topk_op

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `jit_kernel.grouped_topk._jit_grouped_topk_op`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `sampling`
- Python interface: `jit_kernel.grouped_topk._jit_grouped_topk_op`
- Captured call count: `17404`
- Captured variants: `131`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `arg[0]: shape=[1055, 256], dtype=float32, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1095, 256], dtype=float32, device=cuda:2, contiguous=True`
- `arg[0]: shape=[110, 256], dtype=float32, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1167, 256], dtype=float32, device=cuda:6, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:0, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:1, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:2, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:3, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:4, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:5, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:6, contiguous=True`
- `arg[0]: shape=[14, 256], dtype=float32, device=cuda:7, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`228`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 256)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(256,)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=True\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 8)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(2, 8)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=1\n  arg[5]=1\n  arg[6]=8\n  arg[7]=True\n  arg[8]=1.0", "scalars": ["arg[4]=1", "arg[5]=1", "arg[6]=8", "arg[7]=True", "arg[8]=1.0"], "tensors": [{"device": "cuda:2", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "arg...`
   - kwargs: `{}`
2. label=`random_low`, calls=`76`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(38, 256)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(256,)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=True\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(38, 8)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(38, 8)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=1\n  arg[5]=1\n  arg[6]=8\n  arg[7]=True\n  arg[8]=1.0", "scalars": ["arg[4]=1", "arg[5]=1", "arg[6]=8", "arg[7]=True", "arg[8]=1.0"], "tensors": [{"device": "cuda:2", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "...`
   - kwargs: `{}`
3. label=`random_mid`, calls=`152`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(6, 256)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(256,)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=True\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(6, 8)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6, 8)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=1\n  arg[5]=1\n  arg[6]=8\n  arg[7]=True\n  arg[8]=1.0", "scalars": ["arg[4]=1", "arg[5]=1", "arg[6]=8", "arg[7]=True", "arg[8]=1.0"], "tensors": [{"device": "cuda:0", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "arg...`
   - kwargs: `{}`
4. label=`random_mid`, calls=`152`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(6, 256)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(256,)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=True\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(6, 8)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6, 8)\n      dtype=torch.int32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=1\n  arg[5]=1\n  arg[6]=8\n  arg[7]=True\n  arg[8]=1.0", "scalars": ["arg[4]=1", "arg[5]=1", "arg[6]=8", "arg[7]=True", "arg[8]=1.0"], "tensors": [{"device": "cuda:1", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "arg...`
   - kwargs: `{}`
5. label=`random_mid`, calls=`152`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(6, 256)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(256,)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=True\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(6, 8)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6, 8)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=1\n  arg[5]=1\n  arg[6]=8\n  arg[7]=True\n  arg[8]=1.0", "scalars": ["arg[4]=1", "arg[5]=1", "arg[6]=8", "arg[7]=True", "arg[8]=1.0"], "tensors": [{"device": "cuda:2", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "arg...`
   - kwargs: `{}`
6. label=`random_mid`, calls=`152`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(6, 256)\n      dtype=torch.float32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(256,)\n      dtype=torch.float32\n      device=cuda:3\n      requires_grad=True\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(6, 8)\n      dtype=torch.float32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6, 8)\n      dtype=torch.int32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=1\n  arg[5]=1\n  arg[6]=8\n  arg[7]=True\n  arg[8]=1.0", "scalars": ["arg[4]=1", "arg[5]=1", "arg[6]=8", "arg[7]=True", "arg[8]=1.0"], "tensors": [{"device": "cuda:3", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "arg...`
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
