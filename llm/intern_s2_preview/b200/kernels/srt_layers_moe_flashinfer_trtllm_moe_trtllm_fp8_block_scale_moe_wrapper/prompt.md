# KDA Prompt: srt_layers_moe_flashinfer_trtllm_moe_trtllm_fp8_block_scale_moe_wrapper

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `srt.layers.moe.flashinfer_trtllm_moe.trtllm_fp8_block_scale_moe_wrapper`

Goal: optimize or replace this interface for the internlm/Intern-S2-Preview-FP8 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `internlm/Intern-S2-Preview-FP8`
- Model folder: `llm/intern_s2_preview/b200`
- Category: `moe`
- Python interface: `srt.layers.moe.flashinfer_trtllm_moe.trtllm_fp8_block_scale_moe_wrapper`
- Captured call count: `8800`
- Captured variants: `124`
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

- `gemm1_weights: shape=[256, 256, 2048], dtype=float8_e4m3fn, device=cuda:0, contiguous=True`
- `gemm1_weights: shape=[256, 256, 2048], dtype=float8_e4m3fn, device=cuda:1, contiguous=True`
- `gemm1_weights: shape=[256, 256, 2048], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `gemm1_weights: shape=[256, 256, 2048], dtype=float8_e4m3fn, device=cuda:3, contiguous=True`
- `gemm1_weights_scale: shape=[256, 2, 16], dtype=float32, device=cuda:0, contiguous=True`
- `gemm1_weights_scale: shape=[256, 2, 16], dtype=float32, device=cuda:1, contiguous=True`
- `gemm1_weights_scale: shape=[256, 2, 16], dtype=float32, device=cuda:2, contiguous=True`
- `gemm1_weights_scale: shape=[256, 2, 16], dtype=float32, device=cuda:3, contiguous=True`
- `gemm2_weights: shape=[256, 2048, 128], dtype=float8_e4m3fn, device=cuda:0, contiguous=True`
- `gemm2_weights: shape=[256, 2048, 128], dtype=float8_e4m3fn, device=cuda:1, contiguous=True`
- `gemm2_weights: shape=[256, 2048, 128], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `gemm2_weights: shape=[256, 2048, 128], dtype=float8_e4m3fn, device=cuda:3, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`160`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  routing_logits=Tensor(\n      shape=(1, 256)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  routing_bias=None\n  hidden_states=Tensor(\n      shape=(1, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  hidden_states_scale=Tensor(\n      shape=(16, 1)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights=Tensor(\n      shape=(256, 256, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights_scale=Tensor(\n      shape=(256, 2, 16)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  ...`
   - kwargs: `{}`
2. label=`random_low`, calls=`160`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  routing_logits=Tensor(\n      shape=(1, 256)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  routing_bias=None\n  hidden_states=Tensor(\n      shape=(1, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  hidden_states_scale=Tensor(\n      shape=(16, 1)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights=Tensor(\n      shape=(256, 256, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights_scale=Tensor(\n      shape=(256, 2, 16)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  ...`
   - kwargs: `{}`
3. label=`random_low`, calls=`160`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  routing_logits=Tensor(\n      shape=(1, 256)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  routing_bias=None\n  hidden_states=Tensor(\n      shape=(1, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  hidden_states_scale=Tensor(\n      shape=(16, 1)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights=Tensor(\n      shape=(256, 256, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights_scale=Tensor(\n      shape=(256, 2, 16)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  ...`
   - kwargs: `{}`
4. label=`random_low`, calls=`160`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  routing_logits=Tensor(\n      shape=(1, 256)\n      dtype=torch.bfloat16\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  routing_bias=None\n  hidden_states=Tensor(\n      shape=(1, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  hidden_states_scale=Tensor(\n      shape=(16, 1)\n      dtype=torch.float32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights=Tensor(\n      shape=(256, 256, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights_scale=Tensor(\n      shape=(256, 2, 16)\n      dtype=torch.float32\n      device=cuda:3\n      requires_grad=False\n      is_contiguous=True\n    )\n  ...`
   - kwargs: `{}`
5. label=`random_low`, calls=`40`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  routing_logits=Tensor(\n      shape=(103, 256)\n      dtype=torch.bfloat16\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  routing_bias=None\n  hidden_states=Tensor(\n      shape=(103, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  hidden_states_scale=Tensor(\n      shape=(16, 103)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights=Tensor(\n      shape=(256, 256, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights_scale=Tensor(\n      shape=(256, 2, 16)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n   ...`
   - kwargs: `{}`
6. label=`random_low`, calls=`40`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  routing_logits=Tensor(\n      shape=(103, 256)\n      dtype=torch.bfloat16\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  routing_bias=None\n  hidden_states=Tensor(\n      shape=(103, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  hidden_states_scale=Tensor(\n      shape=(16, 103)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights=Tensor(\n      shape=(256, 256, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n    )\n  gemm1_weights_scale=Tensor(\n      shape=(256, 2, 16)\n      dtype=torch.float32\n      device=cuda:1\n      requires_grad=False\n      is_contiguous=True\n   ...`
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
