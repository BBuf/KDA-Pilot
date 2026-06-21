# KDA Prompt: srt_layers_quantization_fp8_kernel_deep_gemm_fp8_fp8_bf16_nt

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `srt.layers.quantization.fp8_kernel.deep_gemm_fp8_fp8_bf16_nt`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `quant_gemm`
- Python interface: `srt.layers.quantization.fp8_kernel.deep_gemm_fp8_fp8_bf16_nt`
- Captured call count: `105613`
- Captured variants: `1365`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `arg[0]: shape=[1055, 16384], dtype=float8_e4m3fn, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1055, 2048], dtype=float8_e4m3fn, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1055, 6144], dtype=float8_e4m3fn, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1095, 16384], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1095, 2048], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1095, 512], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1095, 6144], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `arg[0]: shape=[110, 1536], dtype=float8_e4m3fn, device=cuda:0, contiguous=True`
- `arg[0]: shape=[110, 1536], dtype=float8_e4m3fn, device=cuda:1, contiguous=True`
- `arg[0]: shape=[110, 1536], dtype=float8_e4m3fn, device=cuda:2, contiguous=True`
- `arg[0]: shape=[110, 1536], dtype=float8_e4m3fn, device=cuda:3, contiguous=True`
- `arg[0]: shape=[110, 1536], dtype=float8_e4m3fn, device=cuda:4, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`237`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 16384)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(2, 32)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(6144, 16384)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6144, 32)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[4]=Tensor(\n      shape=(2, 6144)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": [], "tensors": [{"device": "cuda:2", "dtype": "float8_e4m3fn"...`
   - kwargs: `{}`
2. label=`random_low`, calls=`237`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(2, 4)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(16384, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(16384, 4)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[4]=Tensor(\n      shape=(2, 16384)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": [], "tensors": [{"device": "cuda:2", "dtype": "float8_e4m3fn",...`
   - kwargs: `{}`
3. label=`random_low`, calls=`237`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 6144)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(2, 12)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(2624, 6144)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(2624, 12)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[4]=Tensor(\n      shape=(2, 2624)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": [], "tensors": [{"device": "cuda:2", "dtype": "float8_e4m3fn", ...`
   - kwargs: `{}`
4. label=`random_low`, calls=`228`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(2, 4)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(6144, 2048)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6144, 4)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[4]=Tensor(\n      shape=(2, 6144)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": [], "tensors": [{"device": "cuda:2", "dtype": "float8_e4m3fn", "i...`
   - kwargs: `{}`
5. label=`random_low`, calls=`228`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 6144)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(2, 12)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(4096, 6144)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(4096, 12)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[4]=Tensor(\n      shape=(2, 4096)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": [], "tensors": [{"device": "cuda:2", "dtype": "float8_e4m3fn", ...`
   - kwargs: `{}`
6. label=`random_low`, calls=`79`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(38, 16384)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(38, 32)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[2]=Tensor(\n      shape=(6144, 16384)\n      dtype=torch.float8_e4m3fn\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=Tensor(\n      shape=(6144, 32)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[4]=Tensor(\n      shape=(38, 6144)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )", "scalars": [], "tensors": [{"device": "cuda:2", "dtype": "float8_e4m3...`
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
