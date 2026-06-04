"""Pinned SGLang Triton baseline lane for the local A/B benchmark.

Exposes the two public baseline callables from the pinned copies in this
directory, loaded WITHOUT importing the installed sglang package:

- ``norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)``
- ``triton_one_pass_rms_norm(x, w, eps=1e-6)``

Lineage: see ``docs/baseline_source.md``. Both files are byte-identical to the
upstream sglang commit ``edb1b3f8f`` (== round-1 pin ``0b65588c1`` for these
files) except for the documented import-shim edit. The custom-op registration
layer is intentionally stripped symmetrically in this lane; the registered-op
shipping comparison happens in an SGLang worktree at export time.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent

UPSTREAM_REPO = "https://github.com/sgl-project/sglang"
UPSTREAM_COMMIT = "edb1b3f8f"  # container-installed editable checkout (round-2 pin)
ROUND1_COMMIT = "0b65588c1"  # round-1 provenance pin; files identical across both
PRE_EDIT_MD5 = {
    "norm.py": "c3f6955e842f2cb9c0a9f14f64764511",
    "rmsnorm_onepass.py": "4c034f804c88b90a6deb6b758791d003",
}


def _load(name: str, filename: str):
    fq = f"kda_pinned_baseline_{name}"
    if fq in sys.modules:
        return sys.modules[fq]
    spec = importlib.util.spec_from_file_location(fq, _HERE / filename)
    assert spec is not None and spec.loader is not None, filename
    module = importlib.util.module_from_spec(spec)
    sys.modules[fq] = module
    spec.loader.exec_module(module)
    return module


# The pinned copies do ``from _sglang_shims import ...`` (bare import); register
# the shim module under that exact name before executing them.
if "_sglang_shims" not in sys.modules:
    _shims = _load("shims", "_sglang_shims.py")
    sys.modules["_sglang_shims"] = _shims

_norm = _load("norm", "norm.py")
_rms = _load("rmsnorm_onepass", "rmsnorm_onepass.py")

norm_infer = _norm.norm_infer
triton_one_pass_rms_norm = _rms.triton_one_pass_rms_norm

__all__ = [
    "norm_infer",
    "triton_one_pass_rms_norm",
    "UPSTREAM_REPO",
    "UPSTREAM_COMMIT",
    "ROUND1_COMMIT",
    "PRE_EDIT_MD5",
]
