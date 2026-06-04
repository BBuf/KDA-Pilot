"""Correctness tests for ``h200_diffusion_fuse_scale_shift__multi_shape``.

Thin pytest delegation into the authoritative harness in ``bench/``:
- case enumeration: bench/cases.py (15 production rows + canonical grid + negative)
- validation: bench/correctness.py (NaN/Inf guards, fixed oracle tolerances,
  dynamic quantization-noise cross-check, route assertions)

Skipped unless ``KDA_RUN_CORRECTNESS=1`` (the real run needs a CUDA device in
the remote container). ``KDA_CI=1`` selects the upstream CI subsets.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

import pytest

KERNEL_SLUG = "h200_diffusion_fuse_scale_shift__multi_shape"
OP_TYPE = "fuse_scale_shift"
KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 to run (needs a CUDA device).",
)


def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_register_metadata() -> None:
    module = _load_register_module()
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])
    assert set(module.EXPORTS) == {
        "fuse_scale_shift_kernel",
        "fuse_layernorm_scale_shift_gate_select01_kernel",
        "fuse_residual_layernorm_scale_shift_gate_select01_kernel",
    }


def test_comparator_self_check() -> None:
    from bench.correctness import comparator_self_check

    comparator_self_check()


def _all_cases():
    from bench import cases as cases_mod

    return cases_mod.all_cases()


@pytest.mark.parametrize(
    "case", _all_cases() if os.environ.get("KDA_RUN_CORRECTNESS") == "1" else [],
    # pytest invokes the ids callback on its internal sentinel when the
    # parameter list is empty, so the id function must not assume a Case.
    ids=lambda c: getattr(c, "case_id", str(c)),
)
def test_case(case) -> None:
    import torch

    if not torch.cuda.is_available():
        pytest.skip("CUDA required")
    from bench.correctness import run_case

    run_case(case, torch.device("cuda"))
