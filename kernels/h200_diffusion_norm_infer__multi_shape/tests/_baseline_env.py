"""Test/benchmark harness helper: make the SGLang diffusion baseline importable.

The wrapped SGLang baselines live in
``sglang.jit_kernel.diffusion.triton.{norm,rmsnorm_onepass}`` (pinned commit
``c47f0e7cd``). Importing those modules pulls in
``sglang.multimodal_gen.runtime.platforms.current_platform`` only for the
``is_mps()/is_cpu()`` fallback selection at module bottom -- it is never used
inside the CUDA Triton kernels. In a bare CUDA container that lacks the heavy
diffusion extras (imageio, diffusers, ...), that import chain fails.

This helper installs a minimal ``sys.modules`` shim that fakes ONLY platform
detection (the real platform here is CUDA: ``is_mps()`` / ``is_cpu()`` -> False),
which selects exactly the CUDA Triton path -- identical to a real CUDA box. The
real ``register_custom_op`` and the real Triton kernels are left untouched.

This shim is a HARNESS concern only. The shippable wrapper (``src/register.py``)
binds the SGLang baseline with a normal ``try/except`` import; in a production
sglang checkout the diffusion deps are present and no shim is needed. The harness
calls ``install_platform_shim()`` BEFORE importing ``register`` so the wrapper's
import-time baseline binding also succeeds in this bare container.
"""

from __future__ import annotations

import sys
import types


def install_platform_shim() -> None:
    """Install a minimal CUDA platform shim so the diffusion baseline imports."""
    for pkg in ("sglang.multimodal_gen", "sglang.multimodal_gen.runtime"):
        if pkg not in sys.modules:
            mod = types.ModuleType(pkg)
            mod.__path__ = []  # mark as a package
            sys.modules[pkg] = mod
    name = "sglang.multimodal_gen.runtime.platforms"
    if name not in sys.modules:
        plat = types.ModuleType(name)

        class _CudaPlatform:
            @staticmethod
            def is_mps() -> bool:
                return False

            @staticmethod
            def is_cpu() -> bool:
                return False

            @staticmethod
            def is_cuda() -> bool:
                return True

        plat.current_platform = _CudaPlatform()
        sys.modules[name] = plat


def get_baselines():
    """Return ``(norm_infer, triton_one_pass_rms_norm)`` from the pinned SGLang.

    Requires ``PYTHONPATH`` to include the pinned sglang checkout's ``python``
    dir (set by the remote harness invocation). Raises ImportError if the
    baseline cannot be imported.
    """
    install_platform_shim()
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm,
    )

    return norm_infer, triton_one_pass_rms_norm


# Pinned SGLang commit the baseline contract was recovered against (see interface.md).
PINNED_SGLANG_COMMIT = "c47f0e7cdde48ddc718e3c6ee8bc87bebee2e8ff"
