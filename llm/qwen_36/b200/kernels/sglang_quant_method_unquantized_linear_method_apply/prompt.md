# KDA Prompt: sglang_quant_method_unquantized_linear_method_apply

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `sglang.quant_method.UnquantizedLinearMethod.apply`

Goal: optimize or replace this interface for the Qwen/Qwen3.6-35B-A3B-FP8 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen_36/b200`
- Category: `quantization`
- Python interface: `sglang.quant_method.UnquantizedLinearMethod.apply`
- Captured call count: `3259`
- Captured variants: `85`
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

- `arg[1]: shape=[1, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[103, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[108, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[11, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[112, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[12, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[12444, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[12655, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[128, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[14472, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[16, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `arg[1]: shape=[16543, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`164`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=ReplicatedLinear(\n      repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)\n    )\n  arg[1]=Tensor(\n      shape=(4, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=None", "scalars": ["arg[0]=ReplicatedLinear(", "repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)", "arg[2]=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [4, 2048]}]}]`
   - kwargs: `{}`
2. label=`random_low`, calls=`120`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=MergedColumnParallelLinear(\n      repr=MergedColumnParallelLinear(in_features=2048, output_features=64, bias=False, tp_size=1, gather_output=False)\n    )\n  arg[1]=Tensor(\n      shape=(4, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=None", "scalars": ["arg[0]=MergedColumnParallelLinear(", "repr=MergedColumnParallelLinear(in_features=2048, output_features=64, bias=False, tp_size=1, gather_output=False)", "arg[2]=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [4, 2048]}]}]`
   - kwargs: `{}`
3. label=`random_low`, calls=`41`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=ReplicatedLinear(\n      repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)\n    )\n  arg[1]=Tensor(\n      shape=(103, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=None", "scalars": ["arg[0]=ReplicatedLinear(", "repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)", "arg[2]=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [103, 2048]}]}]`
   - kwargs: `{}`
4. label=`random_low`, calls=`30`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=MergedColumnParallelLinear(\n      repr=MergedColumnParallelLinear(in_features=2048, output_features=64, bias=False, tp_size=1, gather_output=False)\n    )\n  arg[1]=Tensor(\n      shape=(103, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=None", "scalars": ["arg[0]=MergedColumnParallelLinear(", "repr=MergedColumnParallelLinear(in_features=2048, output_features=64, bias=False, tp_size=1, gather_output=False)", "arg[2]=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [103, 2048]}]}]`
   - kwargs: `{}`
5. label=`random_low`, calls=`8`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=ReplicatedLinear(\n      repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)\n    )\n  arg[1]=Tensor(\n      shape=(1, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=None", "scalars": ["arg[0]=ReplicatedLinear(", "repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)", "arg[2]=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [1, 2048]}]}]`
   - kwargs: `{}`
6. label=`random_mid`, calls=`41`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=ReplicatedLinear(\n      repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)\n    )\n  arg[1]=Tensor(\n      shape=(112, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=None", "scalars": ["arg[0]=ReplicatedLinear(", "repr=ReplicatedLinear(in_features=2048, output_features=256, bias=False)", "arg[2]=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "arg[1]", "requires_grad": false, "shape": [112, 2048]}]}]`
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
