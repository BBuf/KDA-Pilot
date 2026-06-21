# KDA Prompt: jit_kernel_all_reduce_get_custom_all_reduce_cls_custom_all_reduce_obj_real_all_reduce

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `jit_kernel.all_reduce.get_custom_all_reduce_cls.CustomAllReduceObjReal.all_reduce`

Goal: optimize or replace this interface for the openai/gpt-oss-120b serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `openai/gpt-oss-120b`
- Model folder: `llm/gpt_oss/b200`
- Category: `comm`
- Python interface: `jit_kernel.all_reduce.get_custom_all_reduce_cls.CustomAllReduceObjReal.all_reduce`
- Captured call count: `30240`
- Captured variants: `208`
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

- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:3, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:4, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:6, contiguous=True`
- `arg[0]: shape=[1, 2880], dtype=bfloat16, device=cuda:7, contiguous=True`
- `arg[0]: shape=[102, 2880], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[0]: shape=[102, 2880], dtype=bfloat16, device=cuda:1, contiguous=True`
- `arg[0]: shape=[102, 2880], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[102, 2880], dtype=bfloat16, device=cuda:3, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`422`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2880)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=AllReduceAlgo(\n      repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>\n    )", "scalars": ["arg[1]=AllReduceAlgo(", "repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2880]}]}]`
   - kwargs: `{}`
2. label=`random_low`, calls=`422`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2880)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=AllReduceAlgo(\n      repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>\n    )", "scalars": ["arg[1]=AllReduceAlgo(", "repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>"], "tensors": [{"device": "cuda:1", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2880]}]}]`
   - kwargs: `{}`
3. label=`random_low`, calls=`422`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2880)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=AllReduceAlgo(\n      repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>\n    )", "scalars": ["arg[1]=AllReduceAlgo(", "repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>"], "tensors": [{"device": "cuda:2", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2880]}]}]`
   - kwargs: `{}`
4. label=`random_low`, calls=`422`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2880)\n      dtype=torch.bfloat16\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=AllReduceAlgo(\n      repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>\n    )", "scalars": ["arg[1]=AllReduceAlgo(", "repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>"], "tensors": [{"device": "cuda:3", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2880]}]}]`
   - kwargs: `{}`
5. label=`random_low`, calls=`422`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2880)\n      dtype=torch.bfloat16\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=AllReduceAlgo(\n      repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>\n    )", "scalars": ["arg[1]=AllReduceAlgo(", "repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>"], "tensors": [{"device": "cuda:4", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2880]}]}]`
   - kwargs: `{}`
6. label=`random_low`, calls=`422`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(1, 2880)\n      dtype=torch.bfloat16\n      device=cuda:5\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=AllReduceAlgo(\n      repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>\n    )", "scalars": ["arg[1]=AllReduceAlgo(", "repr=<AllReduceAlgo.ONE_SHOT_PUSH: 1>"], "tensors": [{"device": "cuda:5", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[0]", "requires_grad": false, "shape": [1, 2880]}]}]`
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
