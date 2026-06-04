# Baseline Source Provenance

## Upstream Resolution

- Repository URL: `https://github.com/sgl-project/sglang.git`
- Branch: `main`
- Resolved commit SHA: `133254086bf1f5b887c8c99d311719102d58a7eb`
- Resolution time: `2026-06-04T15:01:03Z` (UTC)
- Resolution command: `git ls-remote https://github.com/sgl-project/sglang.git refs/heads/main`
- Extraction method: `git show <SHA>:<path>` from a clone of the upstream
  repository (objects are content-addressed; the blob checksums below pin the
  copied content to the upstream commit).

## Copied Files

| Local path | Upstream path (at resolved SHA) | Verbatim blob `shasum` at copy time |
|---|---|---|
| `baseline/group_norm_silu.py` | `python/sglang/jit_kernel/diffusion/group_norm_silu.py` | `59ee7c7894f5f6c8aca8ec7aabae454baf1387f5` |
| `baseline/triton/group_norm_silu.py` | `python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py` | `d69d02fb6de23a0ed09c695bdd30e1fc5333377d` |

The checksums above were taken on the verbatim copies BEFORE the local edits
listed below; re-verify any time with:

```bash
git -C <sglang-clone> show 133254086bf1f5b887c8c99d311719102d58a7eb:python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py \
  | diff -u - baseline/triton/group_norm_silu.py
```

## Local Files (not copied from upstream)

- `baseline/_sglang_shims.py` — local no-op `register_custom_op` replacement.
- `baseline/__init__.py` — local package exports + `group_norm_silu_baseline`
  destination-passing benchmark entry.
- `baseline/triton/__init__.py` — local empty package marker mirroring the
  upstream package layout.

## Local Edit Log (complete)

`baseline/group_norm_silu.py` (1 edit):

1. Runtime isolation: the in-function import of `triton_group_norm_silu` now
   targets the copied local module (`from .triton.group_norm_silu import ...`)
   instead of `sglang.jit_kernel.diffusion.triton.group_norm_silu`. No
   behavioral change.

`baseline/triton/group_norm_silu.py` (6 edits, all marked `# local edit` inline):

1. Runtime isolation: `from sglang.srt.utils.custom_op import
   register_custom_op` → `from .._sglang_shims import register_custom_op`
   (no-op decorator; the upstream decorator does not change eager-call
   behavior).
2. Destination passing: `_launch_one_pass(..., out=None)` — when `out` is
   provided, the Triton kernel writes into a reshaped view of the preallocated
   contiguous output instead of `torch.empty_like(x_flat)`; allocating
   behavior preserved when `out is None`.
3. Destination passing: `_launch_one_pass` returns `out` when provided.
4. Destination passing: `_launch_chunked(..., out=None)` — `y = out` when
   provided instead of `torch.empty_like(x_contiguous)`.
5. Destination passing: `_triton_group_norm_silu_cuda(..., out=None)` — passes
   `out` to both launch paths; the eager fallback branch copies the native
   result into `out` when provided.
6. Destination passing: public `triton_group_norm_silu(..., out=None)` —
   forwards `out`.

Deliberately preserved upstream behavior (per user ruling DEC-1):

- `x.contiguous()` materialization inside the timed call (the full copy paid
  by channels-last inputs), allocator-inclusive.
- All internal scratch allocations of the chunked path (`partial_sum`,
  `partial_sq`, `stats`).
- Gating logic, branch thresholds (`2^18` one-pass/chunked crossover), block
  sizes, `num_warps`/`num_stages`, and kernel bodies — bit-for-bit upstream.
- Output layout: the baseline writes a contiguous output for every row
  (upstream returns a contiguous tensor even for channels-last inputs); the
  benchmark `out` buffer is therefore allocated contiguous on both sides.

## Why The Baseline Stays Triton

`config.toml` names `baseline/kernel.cu::group_norm_silu_baseline` as a
template default, but the upstream implementation for these entry points is
Triton/Python. Per `docs/diffusion_kernel_rules.md` ("If the copied SGLang
implementation is Triton, CuTe DSL, or Python, keep it inside `baseline/` and
build a local adapter that has the same call signature, argument ordering,
stream behavior, and output allocation policy as the candidate adapter") and
`docs/standalone_diffusion_benchmark.md` ("kernel.cu or binding.py exposing
the baseline ABI"), the baseline is the copied Triton source behind
`baseline/__init__.py::group_norm_silu_baseline`. A CUDA port would not be the
upstream baseline.
