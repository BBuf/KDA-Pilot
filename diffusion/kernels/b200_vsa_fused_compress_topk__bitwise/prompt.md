# b200_vsa_fused_compress_topk__bitwise

Target GPU: NVIDIA B200.

## Objective

Replace the VSA block-compression and TopK mask construction subgraphs with
fewer, faster kernels while preserving the exact tensors consumed by SGLang's
sparse attention backend.

The research baselines are:

- SGLang `main`
  `86ee545388677733df8da4cf8726c13d7b445875`,
  `python/sglang/multimodal_gen/runtime/layers/attention/backends/video_sparse_attn.py`;
- FastVideo `1b2b2a0161bc6b3b80158d1fa6380a051c6530c7`,
  `fastvideo-kernel/python/fastvideo_kernel/triton_kernels/fused_compress_topk.py`;
- FastVideo PR 1421, merged as
  `31b719ae491972735f813c8e31a5287fadd534d1`;
- FastVideo padded-block fix PR 1517, merged as
  `00ec3e7388a43366b169b05fce10ced043ef0537`.

Both projects are Apache-2.0. Preserve required notices for any adapted code.
Resolve current SGLang `main` again at baseline-recovery time and record the
exact commit and copied files in `docs/baseline_source.md`.

Before implementation, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`
- `../../docs/diffusion_benchmark_shape_coverage.md`

## Baseline Semantics

The initial production layout is BHSD:

- Q/K/V: `[B, H, S, 128]`, contiguous BF16;
- `block_elements=64`;
- `variable_block_sizes=[num_blocks]`, CUDA int32 or int64, each value in
  `[1, 64]`;
- compressed tensors: `[B, H, num_blocks, 128]`, BF16;
- scores: `[B, H, q_blocks, kv_blocks]`;
- mask: same score shape, `torch.bool`, exactly `topk` true values per row.

Block compression must match this exact operation order:

```python
x_blocks = x.view(B, H, num_blocks, 64, 128)
out = (
    x_blocks.float().sum(dim=3)
    / variable_block_sizes.view(1, 1, -1, 1).float()
).to(torch.bfloat16)
```

The TopK baseline is:

```python
indices = torch.topk(scores, topk, dim=-1).indices
mask = torch.zeros_like(scores, dtype=torch.bool).scatter_(-1, indices, True)
```

The candidate outputs must pass `torch.equal`. Do not substitute
`torch.allclose`, cosine similarity, or row-count-only checks. In particular,
FastVideo's current bisection-based Triton TopK kernel does not prove identical
tie ordering; adapt or replace it so the task's exact contract passes.

## Required Workloads

Freeze these rows before tuning:

- `B=1`, `H=12`, `D=128`, BF16, block size 64;
- sequence lengths `10240`, `40960`, `49152`, `102400`, and `115200`;
- TopK ratios `0.1`, `0.25`, `0.5`, and the SGLang-requested production ratio;
- KV-block counts `160`, `640`, `768`, `1600`, `1800`, `2048`, and `4096`;
- partial final blocks from latent grids `(5, 32, 32)`, `(21, 30, 52)`, and
  `(21, 60, 104)`, retaining their exact `variable_block_sizes`;
- scores with `10%`, `30%`, `50%`, and `80%` `-inf` entries;
- deterministic tied-score rows, including an all-equal row and a tie at the
  TopK boundary.

Capture live SGLang shapes before tuning. If the current production model uses
different head counts, sequence lengths, strides, or sparsity ratios, add those
rows and keep the list above as the regression grid.

The padded-block TopK count is:

```python
num_kv_blocks = variable_block_sizes.numel()
cur_topk = math.ceil((1 - sparsity) * num_kv_blocks)
cur_topk = max(1, min(cur_topk, num_kv_blocks))
```

Do not derive it from unpadded sequence length.

## First Milestone

1. Recover the effective SGLang/VSA baseline locally without importing SGLang
   at benchmark runtime.
2. Create matching destination-passing baseline and candidate ABIs.
3. Populate `bench/workloads.json` from live capture plus the regression rows.
4. Make correctness reject dtype, shape, stride, NaN/Inf, masked-score,
   tie-order, partial-block, or output-buffer failures.
5. Benchmark block mean and TopK separately, then report their contribution to
   the full VSA preprocessing path.

Do not claim a B200 result from H100. H100 may validate task logic and a
portable candidate, but the final KDA result must run on an idle B200 and record
per-row statistics plus a roofline-style explanation.
