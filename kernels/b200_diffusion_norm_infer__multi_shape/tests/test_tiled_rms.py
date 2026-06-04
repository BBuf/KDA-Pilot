"""Correctness for the tiled multi-row RMSNorm (D=128, bf16) huge-S candidate.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` (run on the remote B200 inside the
``sglang_bbuf`` container). The reference is the PINNED Triton baseline copy
under ``baseline/`` (bitwise-validated against installed sglang); the candidate
is ``src/register.py::tiled_rms_onepass`` called directly (no dispatcher, no
fallback — a broken build fails loudly).

Covers the two huge production row counts verbatim, the mid/small production
row counts, regression-small rows including non-multiple-of-16 tails, both
rows-per-CTA variants, both scheduling modes, and NaN/Inf parity.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None

KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 (on the remote B200) to run correctness.",
)


def _load_by_path(fq_name: str, path: Path):
    if fq_name in sys.modules:
        return sys.modules[fq_name]
    spec = importlib.util.spec_from_file_location(fq_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    sys.modules[fq_name] = module
    spec.loader.exec_module(module)
    return module


def _pinned():
    return _load_by_path("kda_pinned_baseline", KERNEL_DIR / "baseline" / "__init__.py")


def _register():
    return _load_by_path("kda_tiled_register", KERNEL_DIR / "src" / "register.py")


# Production row counts verbatim + regression rows; 650040 % 16 == 8 and the
# small rows exercise the partial-tile path (rows beyond S must be untouched).
# The odd counts force a half-warp-divergent tail (one row of a warp's pair
# valid, the other not) — the regime where the segmented reduction's shuffle
# mask must name only the executing half-warp's lanes.
ROW_COUNTS = [648720, 650040, 16384, 4096, 1320, 768, 64, 6, 1, 7, 15, 17, 31, 33]
D = 128


@pytest.mark.parametrize("rows_per_cta", [16, 32])
@pytest.mark.parametrize("scheduling", [0, 1])
@pytest.mark.parametrize("s", ROW_COUNTS)
def test_tiled_rms_matches_pinned_baseline(s, scheduling, rows_per_cta):
    torch.manual_seed(3000 + s % 9973)
    x = torch.randn(s, D, device="cuda", dtype=torch.bfloat16)
    w = torch.randn(D, device="cuda", dtype=torch.bfloat16)

    expected = _pinned().triton_one_pass_rms_norm(x, w, 1e-6).clone()
    got = _register().tiled_rms_onepass(x, w, 1e-6, rows_per_cta=rows_per_cta, scheduling=scheduling)
    torch.cuda.synchronize()

    assert not torch.isnan(got).any(), "tiled output contains NaN"
    assert not torch.isinf(got).any(), "tiled output contains Inf"
    torch.testing.assert_close(got.float(), expected.float(), atol=5e-2, rtol=5e-2)


@pytest.mark.parametrize("rows_per_cta", [16, 32])
def test_tiled_rms_nan_inf_parity(rows_per_cta):
    """Non-finite inputs must produce the same non-finite mask as the baseline
    (neither side hides NaN/Inf)."""
    torch.manual_seed(31337)
    x = torch.randn(4096, D, device="cuda", dtype=torch.bfloat16)
    x[7, 3] = float("nan")
    x[1234, 100] = float("inf")
    w = torch.randn(D, device="cuda", dtype=torch.bfloat16)

    expected = _pinned().triton_one_pass_rms_norm(x, w, 1e-6)
    got = _register().tiled_rms_onepass(x, w, 1e-6, rows_per_cta=rows_per_cta)
    torch.cuda.synchronize()

    assert torch.equal(torch.isfinite(got), torch.isfinite(expected)), "non-finite mask differs"


def test_dispatcher_alignment_gate_for_tiled_route():
    """The tiled large-S kernel uses 16-byte vector accesses; a contiguous view
    whose base is 8-byte- but not 16-byte-aligned must NOT take the CUDA route
    at huge S (it falls back to the baseline), while a 16-byte-aligned view
    stays eligible."""
    reg = _register()
    w = torch.randn(D, device="cuda", dtype=torch.bfloat16)
    base = torch.randn(648720 * D + 8, device="cuda", dtype=torch.bfloat16)

    x_8b = base[4: 4 + 648720 * D].view(648720, D)  # +8 bytes: 8B-aligned only
    assert x_8b.is_contiguous() and x_8b.data_ptr() % 16 == 8
    assert not reg._rms_onepass_supported(x_8b, w)

    x_16b = base[8: 8 + 648720 * D].view(648720, D)  # +16 bytes: 16B-aligned
    assert x_16b.is_contiguous() and x_16b.data_ptr() % 16 == 0
    assert reg._rms_onepass_supported(x_16b, w)


def test_tiled_rms_rejects_unsupported_signatures():
    """The direct entry must raise (not silently fall back) on inputs outside
    its contract — fp32 dtype, D != 128, non-contiguous rows."""
    reg = _register()
    w = torch.randn(D, device="cuda", dtype=torch.bfloat16)

    with pytest.raises(Exception):
        reg.tiled_rms_onepass(torch.randn(64, D, device="cuda", dtype=torch.float32), w.float(), 1e-6)
    with pytest.raises(Exception):
        reg.tiled_rms_onepass(
            torch.randn(64, 256, device="cuda", dtype=torch.bfloat16),
            torch.randn(256, device="cuda", dtype=torch.bfloat16),
            1e-6,
        )
    with pytest.raises(Exception):
        x_nc = torch.randn(64, 2 * D, device="cuda", dtype=torch.bfloat16)[:, ::2]
        reg.tiled_rms_onepass(x_nc, w, 1e-6)
    with pytest.raises(Exception):
        # contiguous offset view: is_contiguous() is True but the base pointer
        # is only 8-byte aligned — the 16-byte-vector kernel must NOT launch
        base = torch.randn(64 * D + 4, device="cuda", dtype=torch.bfloat16)
        x_8b = base[4: 4 + 64 * D].view(64, D)
        assert x_8b.is_contiguous() and x_8b.data_ptr() % 16 == 8
        reg.tiled_rms_onepass(x_8b, w, 1e-6)
