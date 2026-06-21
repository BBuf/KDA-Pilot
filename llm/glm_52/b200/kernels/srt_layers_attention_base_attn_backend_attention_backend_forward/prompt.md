# KDA Prompt: srt_layers_attention_base_attn_backend_attention_backend_forward

Target GPU: NVIDIA B200.

Target SGLang kernel Python interface to copy as local baseline:

- `srt.layers.attention.base_attn_backend.AttentionBackend.forward`

Goal: optimize or replace this interface for the GLM-5.2 serving shapes
captured on B200. The shapes below come from runtime SGLang kernel API
logging at the Python interface boundary; they are not torch profiler
CPU-op context shapes.

## Kernel Interface

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Category: `attention`
- Python interface: `srt.layers.attention.base_attn_backend.AttentionBackend.forward`
- Captured call count: `18091`
- Captured variants: `456`
- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.

## Workload Coverage

- `random_low`
- `random_mid`
- `random_high`
- `sharegpt_low`
- `sharegpt_mid`
- `sharegpt_high`

## Shape Summary

- `arg[0]: shape=[1055, 64, 256], dtype=bfloat16, device=cuda:5, contiguous=True`
- `arg[0]: shape=[1095, 64, 256], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[110, 64, 256], dtype=bfloat16, device=cuda:2, contiguous=True`
- `arg[0]: shape=[1167, 64, 256], dtype=bfloat16, device=cuda:6, contiguous=True`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:0, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:1, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:2, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:3, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:4, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:5, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:6, contiguous=False`
- `arg[0]: shape=[14, 64, 512], dtype=bfloat16, device=cuda:7, contiguous=False`

## Captured Variants

1. label=`random_low`, calls=`78`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 64, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=RadixAttention(\n      repr=RadixAttention()\n    )\n  arg[4]=ForwardBatch(\n      repr=ForwardBatch(forward_mode=<ForwardMode.TARGET_VERIFY: 5>, batch_size=1, input_ids=tensor([  279, 94424], device='cuda:2'), req_pool_indices=tensor([2], device='cuda:2'), seq_lens=tensor([42], device='\n    )\n  arg[5]=True\nKeyword input arguments:\n  q_rope=Tensor(\n      shap...`
   - kwargs: `{}`
2. label=`random_low`, calls=`78`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 64, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=RadixAttention(\n      repr=RadixAttention()\n    )\n  arg[4]=ForwardBatch(\n      repr=ForwardBatch(forward_mode=<ForwardMode.TARGET_VERIFY: 5>, batch_size=1, input_ids=tensor([  82, 3146], device='cuda:2'), req_pool_indices=tensor([2], device='cuda:2'), seq_lens=tensor([38], device='cu\n    )\n  arg[5]=True\nKeyword input arguments:\n  q_rope=Tensor(\n      shap...`
   - kwargs: `{}`
3. label=`random_low`, calls=`78`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 64, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=RadixAttention(\n      repr=RadixAttention()\n    )\n  arg[4]=ForwardBatch(\n      repr=ForwardBatch(forward_mode=<ForwardMode.TARGET_VERIFY: 5>, batch_size=1, input_ids=tensor([5492,  911], device='cuda:2'), req_pool_indices=tensor([2], device='cuda:2'), seq_lens=tensor([40], device='cu\n    )\n  arg[5]=True\nKeyword input arguments:\n  q_rope=Tensor(\n      shap...`
   - kwargs: `{}`
4. label=`random_low`, calls=`78`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(38, 64, 256)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[1]=Tensor(\n      shape=(38, 64, 256)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(38, 64, 256)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[3]=RadixAttention(\n      repr=RadixAttention(\n  (kv_b_proj): ColumnParallelLinear(in_features=512, output_features=28672, bias=False, tp_size=1, gather_output=False)\n)\n    )\n  arg[4]=ForwardBatch(\n      repr=ForwardBatch(forward_mode=<ForwardMode.EXTEND: 1>, batch_size=1, input_ids=tensor([ 7984,   264,   220, 98729,    19,    15,    82,  3146,  5492,   91...`
   - kwargs: `{}`
5. label=`random_low`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 64, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=RadixAttention(\n      repr=RadixAttention()\n    )\n  arg[4]=ForwardBatch(\n      repr=ForwardBatch(forward_mode=<ForwardMode.DRAFT_EXTEND_V2: 6>, batch_size=1, input_ids=tensor([3146, 5492], device='cuda:2'), req_pool_indices=tensor([2], device='cuda:2'), seq_lens=tensor([40], device='\n    )\n  arg[5]=True\nKeyword input arguments:\n  q_rope=Tensor(\n      shap...`
   - kwargs: `{}`
6. label=`random_low`, calls=`1`
   - args: `[{"kind": "api_arguments", "raw": "Positional input arguments:\n  arg[0]=Tensor(\n      shape=(2, 64, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=False\n    )\n  arg[1]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[2]=Tensor(\n      shape=(2, 1, 512)\n      dtype=torch.bfloat16\n      device=cuda:2\n      requires_grad=False\n      is_contiguous=True\n    )\n  arg[3]=RadixAttention(\n      repr=RadixAttention()\n    )\n  arg[4]=ForwardBatch(\n      repr=ForwardBatch(forward_mode=<ForwardMode.DRAFT_EXTEND_V2: 6>, batch_size=1, input_ids=tensor([911, 279], device='cuda:2'), req_pool_indices=tensor([2], device='cuda:2'), seq_lens=tensor([42], device='cu\n    )\n  arg[5]=True\nKeyword input arguments:\n  q_rope=Tensor(\n      shap...`
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
