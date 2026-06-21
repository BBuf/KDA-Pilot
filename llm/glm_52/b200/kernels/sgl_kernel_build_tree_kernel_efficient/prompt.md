# KDA Prompt: sgl_kernel_build_tree_kernel_efficient

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `sgl_kernel.build_tree_kernel_efficient`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `other`
- Python interface: `sgl_kernel.build_tree_kernel_efficient`
- Captured call count: `187`
- Captured variants: `187`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:0, contiguous=True`
- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:3, contiguous=True`
- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:4, contiguous=True`
- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:6, contiguous=True`
- `arg[0]: shape=[1, 0], dtype=int64, device=cuda:7, contiguous=True`
- `arg[0]: shape=[10, 0], dtype=int64, device=cuda:0, contiguous=True`
- `arg[0]: shape=[10, 0], dtype=int64, device=cuda:1, contiguous=True`
- `arg[0]: shape=[10, 0], dtype=int64, device=cuda:2, contiguous=True`
- `arg[0]: shape=[10, 0], dtype=int64, device=cuda:3, contiguous=True`
- `arg[0]: shape=[10, 0], dtype=int64, device=cuda:4, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 0)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(1, 1)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(80,)\n      dtype=torch.bool\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is...`
   - kwargs: `{}`
2. label=`random_low`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 0)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(1, 1)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(84,)\n      dtype=torch.bool\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is...`
   - kwargs: `{}`
3. label=`random_low`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 0)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(1, 1)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(88,)\n      dtype=torch.bool\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:2\n      requires_grad=False\n      is...`
   - kwargs: `{}`
4. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 0)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(1, 1)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1,)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(818,)\n      dtype=torch.bool\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:0\n      requires_grad=False\n      i...`
   - kwargs: `{}`
5. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 0)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(1, 1)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1,)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(484,)\n      dtype=torch.bool\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      i...`
   - kwargs: `{}`
6. label=`random_mid`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 0)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(1, 1)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(1,)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(488,)\n      dtype=torch.bool\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[4]=Tensor(\n      shape=(2,)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[5]=Tensor(\n      shape=(1, 2)\n      dtype=torch.int64\n      device=cuda:4\n      requires_grad=False\n      i...`
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
