# Baseline Source Provenance

## Upstream resolution

- Repository URL: https://github.com/sgl-project/sglang
- Branch: `main`
- Resolved commit SHA: `67b2a9ed0cfba8ec625d3f26548e502646fd914d`
  - Commit date (UTC): 2026-06-25T01:14:32Z
  - Commit subject: "[NPU] Fix the DeepSeek-V2-Coder model accuracy issue (#29042)"
- Resolution time (UTC): 2026-06-25T01:28:34Z
- Resolution method: GitHub API `GET /repos/sgl-project/sglang/commits/main` to resolve
  the latest `main` HEAD, then raw file fetch pinned to the resolved SHA:
  `https://raw.githubusercontent.com/sgl-project/sglang/67b2a9e.../python/sglang/jit_kernel/diffusion/triton/causal_conv3d_pad.py`
- Upstream file sha256 (as fetched, 122 lines):
  `f2f0bdd7571ab72a0891d596f09b3d2eae211e4bb83654deeb8db5e7be004d50`

## Copied files

| Local file | Upstream source | Notes |
|------------|-----------------|-------|
| `baseline/causal_conv3d_pad_triton.py` | `python/sglang/jit_kernel/diffusion/triton/causal_conv3d_pad.py` @ `67b2a9e` | Triton kernel `_fused_cat_pad_5d_kernel` + public wrapper `fused_causal_conv3d_cat_pad`. Only a provenance header was prepended (see below). Local file sha256 `f1cf7c4f23158d23a3d54db43c5ca45cfd4a031f17511a76703ed528d4b5145a` |
| `baseline/binding.py` | (task-local, new) | Destination-passing launcher used as the benchmark ABI |
| `baseline/__init__.py` | (task-local, new) | Package marker |

## Itemized local edits to the copied source (`baseline/causal_conv3d_pad_triton.py`)

1. Prepended a provenance header comment block (the only change).

Everything else — the `@triton.jit` kernel `_fused_cat_pad_5d_kernel` and the public
wrapper `fused_causal_conv3d_cat_pad` — is byte-identical to the upstream file at the
resolved commit. The upstream file imports only `torch`, `triton`, and
`triton.language` (no `sglang` import), so nothing had to be removed for the
standalone no-`sglang`-at-runtime contract.

## Recovered semantics (ground truth for the oracle and candidate)

`fused_causal_conv3d_cat_pad(x, cache_x, padding)`:

- `padding = [width_left, width_right, height_top, height_bottom, depth_left, depth_right]`
  (PyTorch F.pad order for the trailing W, H, D dims of a 5D `[N, C, T, H, W]` tensor).
- `cache_x` is a **required tensor** (`[N, C, cache_t, H, W]`). "Cache-null" is therefore
  modeled as a depth-0 cache tensor (`cache_t == cache_x.shape[2] == 0`), not `None`.
- The wrapper does `depth_left -= cache_x.shape[2]`, then asserts `depth_left >= 0`
  (i.e. `D_left >= cache_t`), `depth_right == 0`, `width_left == width_right`,
  `height_top == height_bottom`. These are the exact rejection conditions.
- Output shape: `[N, C, t_size + cache_t + (D_left - cache_t) + D_right,
  H + height_top + height_bottom, W + width_left + width_right]`
  = `[N, C, t_size + D_left + D_right, H + 2*height_top, W + 2*width_left]`
  (output depth is independent of `cache_t`).

`_fused_cat_pad_5d_kernel` (one output element per program lane):

- Iterates a flat index over the contiguous output `[N, C, out_t, out_h, out_w]`.
- `iw = ow - width_left`, `ih = oh - height_top`, `src_t = od - (D_left - cache_t)`.
- A cell is valid (copied) iff `iw in [0, W)`, `ih in [0, H)`, `src_t in [0, cache_t + t_size)`.
- `from_cache = src_t < cache_t`; cache region is the innermost left-depth planes, the
  remaining `D_left - cache_t` left planes and all out-of-range cells are written as **constant 0**
  (masked loads use `other=0.0`, and every output cell is stored).
- Read offsets for `x` and `cache_x` use **hardcoded C-contiguous stride formulas** — the kernel
  therefore **assumes `x` and `cache_x` are C-contiguous**; it does not read tensor strides.

Independent torch oracle implied by the above:

- cache-present: `out = F.pad(torch.cat([cache_x, x], dim=2),
  [width_left, width_right, height_top, height_bottom, D_left - cache_t, D_right], value=0)`
- cache-null (`cache_t == 0`): `out = F.pad(x,
  [width_left, width_right, height_top, height_bottom, D_left, D_right], value=0)`
