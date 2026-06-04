"""Apply the two public-op edits inside an isolated SGLang worktree.

Usage: python apply_worktree_edits.py <worktree_root>

Edit 1 — `python/sglang/jit_kernel/diffusion/triton/norm.py`: the public
`norm_infer` tries the CUDA path first (its hot path carries no custom op, so
the public contract is preserved exactly).

Edit 2 — `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py`: the
CUDA path goes INSIDE the registered custom-op body
(`_triton_one_pass_rms_norm_cuda`), so `@register_custom_op` semantics
(torch.compile / CUDA-graph registration) are preserved for every shape on both
sides of any A/B.

Idempotent: re-running detects the markers and leaves the files unchanged.
"""

from __future__ import annotations

import sys
from pathlib import Path

MARKER = "cuda_norm_infer"

NORM_ANCHOR = """def norm_infer(
    x: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    eps: float,
    is_rms_norm: bool = False,
    out: Optional[Tensor] = None,
):
"""
NORM_INSERT = """def norm_infer(
    x: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    eps: float,
    is_rms_norm: bool = False,
    out: Optional[Tensor] = None,
):
    from sglang.jit_kernel.diffusion.cuda_norm_infer import maybe_norm_infer_cuda

    _cuda_out = maybe_norm_infer_cuda(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
    if _cuda_out is not None:
        return _cuda_out
"""

RMS_ANCHOR = """@register_custom_op(op_name="triton_one_pass_rms_norm_cuda", out_shape="x")
def _triton_one_pass_rms_norm_cuda(
    x: torch.Tensor, w: torch.Tensor, eps: float = 1e-6
) -> torch.Tensor:
"""
RMS_INSERT = """@register_custom_op(op_name="triton_one_pass_rms_norm_cuda", out_shape="x")
def _triton_one_pass_rms_norm_cuda(
    x: torch.Tensor, w: torch.Tensor, eps: float = 1e-6
) -> torch.Tensor:
    from sglang.jit_kernel.diffusion.cuda_norm_infer import maybe_rms_onepass_cuda

    _cuda_out = maybe_rms_onepass_cuda(x, w, eps)
    if _cuda_out is not None:
        return _cuda_out
"""


def _patch(path: Path, anchor: str, insert: str) -> str:
    text = path.read_text()
    if MARKER in text:
        return "already-patched"
    if anchor not in text:
        raise SystemExit(f"anchor not found in {path} — upstream drifted, re-derive the edit")
    path.write_text(text.replace(anchor, insert, 1))
    return "patched"


def main() -> int:
    root = Path(sys.argv[1])
    base = root / "python" / "sglang" / "jit_kernel" / "diffusion"
    print("norm.py:", _patch(base / "triton" / "norm.py", NORM_ANCHOR, NORM_INSERT))
    print("rmsnorm_onepass.py:", _patch(base / "triton" / "rmsnorm_onepass.py", RMS_ANCHOR, RMS_INSERT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
