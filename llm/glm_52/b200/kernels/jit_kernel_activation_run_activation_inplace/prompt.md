# KDA Prompt: jit_kernel_activation_run_activation_inplace

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `jit_kernel.activation._run_activation_inplace`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `other`
- Python interface: `jit_kernel.activation._run_activation_inplace`
- Captured call count: `25876`
- Captured variants: `2448`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `arg[1]: shape=[10112, 4096], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[1]: shape=[10112, 4096], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[1]: shape=[10112, 4096], dtype=bfloat16, device=cuda:3, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:3, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:4, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:5, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:6, contiguous=True`
- `arg[1]: shape=[1024, 4096], dtype=bfloat16, device=cuda:7, contiguous=True`
- `arg[1]: shape=[10240, 4096], dtype=bfloat16, device=cuda:1, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`228`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]='silu'\n  arg[1]=Tensor(\n      shape=(2, 4096)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 2048)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": ["arg[0]='silu'"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [2, 4096]}, {"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[2]", "requires_grad": false, "shape": [2, 2048]}]}]`
   - kwargs: `{}`
2. label=`random_low`, calls=`76`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]='silu'\n  arg[1]=Tensor(\n      shape=(38, 4096)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(38, 2048)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": ["arg[0]='silu'"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [38, 4096]}, {"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[2]", "requires_grad": false, "shape": [38, 2048]}]}]`
   - kwargs: `{}`
3. label=`random_low`, calls=`14`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]='silu'\n  arg[1]=Tensor(\n      shape=(1280, 4096)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1280, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": ["arg[0]='silu'"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [1280, 4096]}, {"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[2]", "requires_grad": false, "shape": [1280, 2048]}]}]`
   - kwargs: `{}`
4. label=`random_low`, calls=`14`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]='silu'\n  arg[1]=Tensor(\n      shape=(1280, 4096)\n      dtype=torch.bfloat16\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1280, 2048)\n      dtype=torch.bfloat16\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": ["arg[0]='silu'"], "tensors": [{"device": "cuda:5", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [1280, 4096]}, {"device": "cuda:5", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[2]", "requires_grad": false, "shape": [1280, 2048]}]}]`
   - kwargs: `{}`
5. label=`random_low`, calls=`14`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]='silu'\n  arg[1]=Tensor(\n      shape=(1408, 4096)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1408, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": ["arg[0]='silu'"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [1408, 4096]}, {"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[2]", "requires_grad": false, "shape": [1408, 2048]}]}]`
   - kwargs: `{}`
6. label=`random_low`, calls=`14`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]='silu'\n  arg[1]=Tensor(\n      shape=(1664, 4096)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1664, 2048)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": ["arg[0]='silu'"], "tensors": [{"device": "cuda:1", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [1664, 4096]}, {"device": "cuda:1", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[2]", "requires_grad": false, "shape": [1664, 2048]}]}]`
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
