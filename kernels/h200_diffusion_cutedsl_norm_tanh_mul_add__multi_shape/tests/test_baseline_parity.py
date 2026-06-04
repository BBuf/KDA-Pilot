"""Parity check: vendored baseline vs the sglang package entry points.

Asserts that the vendored copy under ``baseline/`` (pinned SGLang commit
0689ba84b88c991684b0f99ee9b50c3ce485b483, see docs/baseline_source.md)
produces bitwise-identical outputs to the real ``sglang`` package entry
points on the 4 captured production signatures, and that both sides agree
on out-of-domain ValueError behavior.

Run inside the sglang_bbuf container on an idle H200:

    python -m pytest tests/test_baseline_parity.py -v
    # or standalone:
    python tests/test_baseline_parity.py
"""

import os
import sys

import pytest
import torch

_KERNEL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _KERNEL_DIR not in sys.path:
    sys.path.insert(0, _KERNEL_DIR)

requires_cuda = pytest.mark.skipif(
    not torch.cuda.is_available(), reason="parity check needs a CUDA device"
)

# The 4 captured production signatures (docs/captured_shapes_h200.jsonl):
# bfloat16, rms, eps=1e-05, D=3840, weight=[D], bias=None,
# scale(/scale2)=[1,1,D], shift=[B,S,D], x=[1,S,3840] with S in {4096, 4128}.
PROD_SEQ_LENS = (4096, 4128)
PROD_D = 3840
PROD_DTYPE = torch.bfloat16
PROD_NORM = "rms"
PROD_EPS = 1e-5


def _make_prod_inputs(seq_len: int, *, dual: bool, seed: int):
    gen = torch.Generator(device="cuda").manual_seed(seed)

    def randn(*shape):
        return torch.randn(shape, generator=gen, device="cuda", dtype=PROD_DTYPE)

    x = randn(1, seq_len, PROD_D)
    weight = randn(PROD_D)
    scale = randn(1, 1, PROD_D)
    shift = randn(1, seq_len, PROD_D)
    args = [x, weight, None, scale, shift]
    if dual:
        weight2 = randn(PROD_D)
        scale2 = randn(1, 1, PROD_D)
        args += [weight2, None, scale2]
    args += [PROD_NORM, PROD_EPS]
    return args


def _import_pair():
    import baseline as vendored
    from sglang.jit_kernel.diffusion.cutedsl import (
        norm_tanh_mul_add_norm_scale as upstream,
    )

    return vendored, upstream


def _gpu_banner() -> str:
    idx = torch.cuda.current_device()
    return (
        f"host={os.uname().nodename} cuda_visible={os.environ.get('CUDA_VISIBLE_DEVICES', '<unset>')} "
        f"device_index={idx} name={torch.cuda.get_device_name(idx)}"
    )


@requires_cuda
@pytest.mark.parametrize("seq_len", PROD_SEQ_LENS)
def test_parity_single_norm(seq_len):
    vendored, upstream = _import_pair()
    args = _make_prod_inputs(seq_len, dual=False, seed=20260604 + seq_len)
    out_vendored = vendored.fused_norm_tanh_mul_add(*args)
    out_upstream = upstream.fused_norm_tanh_mul_add(*args)
    torch.cuda.synchronize()
    assert torch.isfinite(out_vendored.float()).all(), "vendored output has NaN/Inf"
    assert torch.equal(out_vendored, out_upstream), (
        f"vendored vs upstream mismatch (single norm, S={seq_len}): "
        f"max abs diff={(out_vendored.float() - out_upstream.float()).abs().max().item()}"
    )


@requires_cuda
@pytest.mark.parametrize("seq_len", PROD_SEQ_LENS)
def test_parity_dual_norm(seq_len):
    vendored, upstream = _import_pair()
    args = _make_prod_inputs(seq_len, dual=True, seed=20260604 + seq_len)
    y_v, y2_v = vendored.fused_norm_tanh_mul_add_norm_scale(*args)
    y_u, y2_u = upstream.fused_norm_tanh_mul_add_norm_scale(*args)
    torch.cuda.synchronize()
    assert torch.isfinite(y_v.float()).all(), "vendored y has NaN/Inf"
    assert torch.isfinite(y2_v.float()).all(), "vendored y2 has NaN/Inf"
    assert torch.equal(y_v, y_u), f"y mismatch (dual norm, S={seq_len})"
    assert torch.equal(y2_v, y2_u), f"y2 mismatch (dual norm, S={seq_len})"


@requires_cuda
def test_out_of_domain_d_matches():
    """Both sides must reject D % 256 != 0 and D > 8192 identically."""
    vendored, upstream = _import_pair()
    for bad_d in (3848, 8448):  # 3848 % 256 != 0; 8448 % 256 == 0 but > 8192
        x = torch.randn(1, 8, bad_d, device="cuda", dtype=PROD_DTYPE)
        scale = torch.randn(1, 1, bad_d, device="cuda", dtype=PROD_DTYPE)
        shift = torch.randn(1, 8, bad_d, device="cuda", dtype=PROD_DTYPE)
        for mod in (vendored, upstream):
            with pytest.raises(ValueError):
                mod.fused_norm_tanh_mul_add(x, None, None, scale, shift, "rms", 1e-5)


@requires_cuda
def test_non_3d_scale_rejected():
    """Recovered contract: scale/shift must be 3-D [1|B,1|S,D] at this public boundary."""
    vendored, upstream = _import_pair()
    x = torch.randn(1, 8, PROD_D, device="cuda", dtype=PROD_DTYPE)
    scale_1d = torch.randn(PROD_D, device="cuda", dtype=PROD_DTYPE)
    shift = torch.randn(1, 8, PROD_D, device="cuda", dtype=PROD_DTYPE)
    for mod in (vendored, upstream):
        with pytest.raises(ValueError):
            mod.fused_norm_tanh_mul_add(x, None, None, scale_1d, shift, "rms", 1e-5)


if __name__ == "__main__":
    if not torch.cuda.is_available():
        print("SKIP: no CUDA device available")
        sys.exit(0)
    print(_gpu_banner())
    vendored, upstream = _import_pair()
    for seq_len in PROD_SEQ_LENS:
        args = _make_prod_inputs(seq_len, dual=False, seed=20260604 + seq_len)
        assert torch.equal(
            vendored.fused_norm_tanh_mul_add(*args),
            upstream.fused_norm_tanh_mul_add(*args),
        ), f"single-norm parity FAILED (S={seq_len})"
        print(f"single-norm parity OK (S={seq_len})")
        args = _make_prod_inputs(seq_len, dual=True, seed=20260604 + seq_len)
        y_v, y2_v = vendored.fused_norm_tanh_mul_add_norm_scale(*args)
        y_u, y2_u = upstream.fused_norm_tanh_mul_add_norm_scale(*args)
        assert torch.equal(y_v, y_u) and torch.equal(y2_v, y2_u), (
            f"dual-norm parity FAILED (S={seq_len})"
        )
        print(f"dual-norm parity OK (S={seq_len})")
    print("PARITY PASS: vendored baseline == sglang package on all 4 captured signatures")
