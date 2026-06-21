# KDA Prompt: sgl_kernel_fast_topk_transform_fused

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `sgl_kernel.fast_topk_transform_fused`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `sampling`
- Python interface: `sgl_kernel.fast_topk_transform_fused`
- Captured call count: `4246`
- Captured variants: `247`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `cu_seqlens_q: shape=[11], dtype=int32, device=cuda:0, contiguous=True`
- `cu_seqlens_q: shape=[11], dtype=int32, device=cuda:3, contiguous=True`
- `cu_seqlens_q: shape=[11], dtype=int32, device=cuda:4, contiguous=True`
- `cu_seqlens_q: shape=[11], dtype=int32, device=cuda:6, contiguous=True`
- `cu_seqlens_q: shape=[11], dtype=int32, device=cuda:7, contiguous=True`
- `cu_seqlens_q: shape=[13], dtype=int32, device=cuda:2, contiguous=True`
- `cu_seqlens_q: shape=[13], dtype=int32, device=cuda:4, contiguous=True`
- `cu_seqlens_q: shape=[13], dtype=int32, device=cuda:5, contiguous=True`
- `cu_seqlens_q: shape=[13], dtype=int32, device=cuda:7, contiguous=True`
- `cu_seqlens_q: shape=[15], dtype=int32, device=cuda:0, contiguous=True`
- `cu_seqlens_q: shape=[15], dtype=int32, device=cuda:1, contiguous=True`
- `cu_seqlens_q: shape=[15], dtype=int32, device=cuda:2, contiguous=True`

## Captured Variants

1. label=`random_low`, calls=`22`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  score=Tensor(\n      shape=(2, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  lengths=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  page_table_size_1=Tensor(\n      shape=(2, 40)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  cu_seqlens_q=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  topk=2048\n  row_starts=None", "scalars": ["topk=2048", "row_starts=None"], "tensors": [{"device": "cuda:2", "dtype": "float32", "is_contiguous": false, "kind": "tensor", "name": "score", "requires_grad": false, "shape": [2, 64]}, {"device"...`
   - kwargs: `{}`
2. label=`random_low`, calls=`22`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  score=Tensor(\n      shape=(2, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  lengths=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  page_table_size_1=Tensor(\n      shape=(2, 42)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  cu_seqlens_q=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  topk=2048\n  row_starts=None", "scalars": ["topk=2048", "row_starts=None"], "tensors": [{"device": "cuda:2", "dtype": "float32", "is_contiguous": false, "kind": "tensor", "name": "score", "requires_grad": false, "shape": [2, 64]}, {"device"...`
   - kwargs: `{}`
3. label=`random_low`, calls=`22`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  score=Tensor(\n      shape=(2, 64)\n      dtype=torch.float32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  lengths=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  page_table_size_1=Tensor(\n      shape=(2, 44)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  cu_seqlens_q=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  topk=2048\n  row_starts=None", "scalars": ["topk=2048", "row_starts=None"], "tensors": [{"device": "cuda:2", "dtype": "float32", "is_contiguous": false, "kind": "tensor", "name": "score", "requires_grad": false, "shape": [2, 64]}, {"device"...`
   - kwargs: `{}`
4. label=`random_mid`, calls=`22`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  score=Tensor(\n      shape=(2, 192)\n      dtype=torch.float32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=False\n    )\n  lengths=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  page_table_size_1=Tensor(\n      shape=(2, 140)\n      dtype=torch.int32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  cu_seqlens_q=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:6\n      requires_grad=False\n      is_contiguous=True\n    )\n  topk=2048\n  row_starts=None", "scalars": ["topk=2048", "row_starts=None"], "tensors": [{"device": "cuda:6", "dtype": "float32", "is_contiguous": false, "kind": "tensor", "name": "score", "requires_grad": false, "shape": [2, 192]}, {"devi...`
   - kwargs: `{}`
5. label=`random_mid`, calls=`22`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  score=Tensor(\n      shape=(2, 256)\n      dtype=torch.float32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  lengths=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  page_table_size_1=Tensor(\n      shape=(2, 246)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  cu_seqlens_q=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:4\n      requires_grad=False\n      is_contiguous=True\n    )\n  topk=2048\n  row_starts=None", "scalars": ["topk=2048", "row_starts=None"], "tensors": [{"device": "cuda:4", "dtype": "float32", "is_contiguous": true, "kind": "tensor", "name": "score", "requires_grad": false, "shape": [2, 256]}, {"device...`
   - kwargs: `{}`
6. label=`random_mid`, calls=`22`
   - args: `[{"kind": "api_arguments", "raw": "Keyword input arguments:\n  score=Tensor(\n      shape=(2, 448)\n      dtype=torch.float32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=False\n    )\n  lengths=Tensor(\n      shape=(2,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  page_table_size_1=Tensor(\n      shape=(2, 409)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  cu_seqlens_q=Tensor(\n      shape=(3,)\n      dtype=torch.int32\n      device=cuda:0\n      requires_grad=False\n      is_contiguous=True\n    )\n  topk=2048\n  row_starts=None", "scalars": ["topk=2048", "row_starts=None"], "tensors": [{"device": "cuda:0", "dtype": "float32", "is_contiguous": false, "kind": "tensor", "name": "score", "requires_grad": false, "shape": [2, 448]}, {"devi...`
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
