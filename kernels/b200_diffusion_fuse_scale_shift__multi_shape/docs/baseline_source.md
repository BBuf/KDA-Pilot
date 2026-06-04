# Baseline Source Provenance

## Upstream resolution

- Repository URL: https://github.com/sgl-project/sglang
- Branch: `main`
- Resolved commit SHA: `133254086bf1f5b887c8c99d311719102d58a7eb`
  - Commit date (UTC): 2026-06-04T13:46:36Z
  - Commit subject: "Plug mamba_extra_buffer ping-pong slot leaks (#26941)"
- Resolution time (UTC): 2026-06-04T14:59:05Z
- Resolution method: GitHub API `GET /repos/sgl-project/sglang/commits/main`,
  then raw file fetch pinned to the resolved SHA:
  `https://raw.githubusercontent.com/sgl-project/sglang/1332540.../python/sglang/jit_kernel/diffusion/triton/scale_shift.py`
- Upstream file sha256 (as fetched, 679 lines):
  `b51d0a25cc296b4dc1bb6e7c3c91c8c3f5f42d599b20a2a3d40d76cf96682838`

## Copied files

| Local file | Upstream source | Notes |
|------------|-----------------|-------|
| `baseline/scale_shift_triton.py` | `python/sglang/jit_kernel/diffusion/triton/scale_shift.py` @ `1332540` | Triton kernels + upstream wrappers; local edits below. sha256 `011647afb8607137cf81f41b9ca575df0920d74b53085018532ebe870105aef2` |
| `baseline/binding.py` | (task-local, new) | Destination-passing launchers used as the benchmark ABI |
| `baseline/__init__.py` | (task-local, new) | Empty package marker |

## Itemized local edits to the copied source (`baseline/scale_shift_triton.py`)

1. Added a 5-line provenance header comment at the top of the file.
2. Removed upstream line 5: `from sglang.multimodal_gen.runtime.platforms import current_platform`
   so the copy never imports `sglang` at benchmark runtime.
3. Removed upstream lines 659-679: the trailing non-CUDA platform fallback
   rebinding block (`if current_platform.is_npu(): ...`, `is_mps`, `is_musa`,
   `is_cpu`), which only re-binds `fuse_scale_shift_kernel` on non-CUDA
   platforms. This task targets CUDA (B200) only.

Everything else — the three `@triton.jit` kernels
(`_fused_layernorm_scale_shift_gate_select01_kernel`,
`_fused_residual_layernorm_scale_shift_gate_select01_kernel`,
`_fused_scale_shift_4d_kernel`, `fuse_scale_shift_kernel_blc_opt`) and the
three upstream public wrappers — is byte-identical to the upstream file at the
resolved commit.

## Local benchmark ABI (`baseline/binding.py`)

The benchmark does not call the upstream wrappers directly because they
allocate outputs via `torch.empty_like` inside the call; the standalone
benchmark contract preallocates outputs outside the timed region on both
sides. `baseline/binding.py` ports each upstream wrapper into a
destination-passing launcher with output tensors passed last:

- `fuse_scale_shift(x, scale, shift, scale_constant, output)`
- `fuse_layernorm_scale_shift_gate_select01(x, weight, bias, scale0, shift0,
  gate0, scale1, shift1, gate1, index, eps, output, gate_out)`
- `fuse_residual_layernorm_scale_shift_gate_select01(x, residual,
  residual_gate, weight, bias, scale0, shift0, gate0, scale1, shift1, gate1,
  index, eps, output, residual_out, gate_out)`

Faithfulness contract of the port:

- All upstream input validation, broadcast normalization (0D/2D/3D/4D scale
  and shift), `expand`/stride extraction, the 4D `.contiguous()` reshapes, the
  scalar-scalar all-zero fast path (including its GPU->CPU `.any().to("cpu")`
  sync and `output.copy_(x)`), grid shapes, `BLOCK_*` constants, `num_warps`,
  and `num_stages` are preserved verbatim.
- The only behavioral deltas are: (a) outputs are caller-provided instead of
  `empty_like` (matching the contract's preallocation policy on both sides),
  and (b) cheap host-side shape/dtype/contiguity assertions on the provided
  output tensors (the candidate performs equivalent validation on its side).
- The launchers call the copied Triton kernels from
  `baseline/scale_shift_triton.py` only; no `sglang` import anywhere in the
  runtime path.
