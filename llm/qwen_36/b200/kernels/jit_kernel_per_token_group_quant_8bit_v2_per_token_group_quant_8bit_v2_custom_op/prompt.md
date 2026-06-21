# KDA Prompt: jit_kernel_per_token_group_quant_8bit_v2_per_token_group_quant_8bit_v2_custom_op

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `jit_kernel.per_token_group_quant_8bit_v2._per_token_group_quant_8bit_v2_custom_op`

Goal: optimize or replace this interface for the Qwen/Qwen3.6-35B-A3B-FP8 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen_36/b200`
- Category: `quantization`
- Python interface: `jit_kernel.per_token_group_quant_8bit_v2._per_token_group_quant_8bit_v2_custom_op`
- Captured call count: `9545`
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

- `input: shape=[1, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[1, 4096], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[1, 512], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[103, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[103, 4096], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[103, 512], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[108, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[108, 4096], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[108, 512], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[11, 2048], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[11, 4096], dtype=bfloat16, device=cuda:0, contiguous=True`
- `input: shape=[11, 512], dtype=bfloat16, device=cuda:0, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`328`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  input=Tensor(\n      shape=(4, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_q=Tensor(\n      shape=(4, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_s=Tensor(\n      shape=(4, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  group_size=128\n  eps=1e-10\n  min_8bit=-448.0\n  max_8bit=448.0\n  scale_ue8m0=True\n  fuse_silu_and_mul=False\n  masked_m=None", "scalars": ["group_size=128", "eps=1e-10", "min_8bit=-448.0", "max_8bit=448.0", "scale_ue8m0=True", "fuse_silu_and_mul=False", "masked_m=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "i...`
   - kwargs: `{}`
2. label=`random_low`, calls=`164`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  input=Tensor(\n      shape=(4, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_q=Tensor(\n      shape=(4, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_s=Tensor(\n      shape=(4, 16)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  group_size=128\n  eps=1e-10\n  min_8bit=-448.0\n  max_8bit=448.0\n  scale_ue8m0=False\n  fuse_silu_and_mul=False\n  masked_m=None", "scalars": ["group_size=128", "eps=1e-10", "min_8bit=-448.0", "max_8bit=448.0", "scale_ue8m0=False", "fuse_silu_and_mul=False", "masked_m=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name...`
   - kwargs: `{}`
3. label=`random_low`, calls=`164`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  input=Tensor(\n      shape=(4, 4096)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_q=Tensor(\n      shape=(4, 4096)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_s=Tensor(\n      shape=(4, 8)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  group_size=128\n  eps=1e-10\n  min_8bit=-448.0\n  max_8bit=448.0\n  scale_ue8m0=True\n  fuse_silu_and_mul=False\n  masked_m=None", "scalars": ["group_size=128", "eps=1e-10", "min_8bit=-448.0", "max_8bit=448.0", "scale_ue8m0=True", "fuse_silu_and_mul=False", "masked_m=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "i...`
   - kwargs: `{}`
4. label=`random_low`, calls=`164`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  input=Tensor(\n      shape=(4, 512)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_q=Tensor(\n      shape=(4, 512)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_s=Tensor(\n      shape=(4, 1)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  group_size=128\n  eps=1e-10\n  min_8bit=-448.0\n  max_8bit=448.0\n  scale_ue8m0=True\n  fuse_silu_and_mul=False\n  masked_m=None", "scalars": ["group_size=128", "eps=1e-10", "min_8bit=-448.0", "max_8bit=448.0", "scale_ue8m0=True", "fuse_silu_and_mul=False", "masked_m=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "name": "inpu...`
   - kwargs: `{}`
5. label=`random_low`, calls=`82`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  input=Tensor(\n      shape=(103, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_q=Tensor(\n      shape=(103, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_s=Tensor(\n      shape=(103, 4)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  group_size=128\n  eps=1e-10\n  min_8bit=-448.0\n  max_8bit=448.0\n  scale_ue8m0=True\n  fuse_silu_and_mul=False\n  masked_m=None", "scalars": ["group_size=128", "eps=1e-10", "min_8bit=-448.0", "max_8bit=448.0", "scale_ue8m0=True", "fuse_silu_and_mul=False", "masked_m=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor", "nam...`
   - kwargs: `{}`
6. label=`random_low`, calls=`41`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  input=Tensor(\n      shape=(103, 2048)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_q=Tensor(\n      shape=(103, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  output_s=Tensor(\n      shape=(103, 16)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  group_size=128\n  eps=1e-10\n  min_8bit=-448.0\n  max_8bit=448.0\n  scale_ue8m0=False\n  fuse_silu_and_mul=False\n  masked_m=None", "scalars": ["group_size=128", "eps=1e-10", "min_8bit=-448.0", "max_8bit=448.0", "scale_ue8m0=False", "fuse_silu_and_mul=False", "masked_m=None"], "tensors": [{"device": "cuda:0", "dtype": "bfloat16", "is_contiguous": true, "kind": "tensor",...`
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
