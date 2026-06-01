"""Correctness harness for ``h200_diffusion_rotary_embedding__multi_shape``.

Gated by ``KDA_RUN_CORRECTNESS=1`` (needs CUDA + an importable SGLang). Run on the
remote H200 inside the ``sglang_bbuf`` container::

    KDA_RUN_CORRECTNESS=1 pytest tests/test_correctness.py -v

Oracle design (the named ``test_rope.py`` exercises a *different* API --
``apply_rope_inplace`` / FlashInfer -- so it is not a literal oracle here):

* Semantic oracle: the SGLang diffusion triton baselines pinned at SGLang
  HEAD ``6965fe0ee`` (``apply_rotary_embedding`` / ``apply_ltx2_split_rotary_emb``);
  a runtime provenance check enforces the pin (override with
  ``KDA_SGLANG_ORACLE_COMMIT`` only with justification).
* Independent cross-check: ``src/reference.py`` PyTorch FP32 references.

Workload = the 6 deduplicated production shapes (1 hunyuanvideo standard + 5 LTX-2),
asserted against an exact manifest so a dropped/extra/altered case fails loudly.
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "h200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"
KERNEL_DIR = Path(__file__).resolve().parents[1]
DEVICE = "cuda"
SGLANG_ORACLE_COMMIT = "6965fe0ee"

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on the remote H200 (CUDA + SGLang) to run.",
)


# ---------------------------------------------------------------------------
# Module loading
# ---------------------------------------------------------------------------
def _load_module(rel_path: str, mod_name: str):
    path = KERNEL_DIR / rel_path
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _register():
    return _load_module("src/register.py", f"kda_{KERNEL_SLUG}_register")


def _reference():
    return _load_module("src/reference.py", f"kda_{KERNEL_SLUG}_reference")


def _wrapper():
    # register.py inserts src/ on sys.path and imports `wrapper`.
    _register()
    import wrapper  # type: ignore

    return wrapper


REF = _reference()


# ---------------------------------------------------------------------------
# Exact production-case manifest (from docs/captured_shapes_h200.jsonl, deduped)
# ---------------------------------------------------------------------------
def _expected_cases():
    bf16 = torch.bfloat16
    f32 = torch.float32
    return {
        "hunyuanvideo__std__B1_T27030_H24_D128__bf16": dict(
            api="standard", nargs=4, x_shape=(1, 27030, 24, 128), x_dtype=bf16,
            cossin_shape=(27030, 64), cossin_dtype=f32, cossin_contig=True, interleaved=False,
        ),
        "ltx2__B1_S1536_H32_half64__bf16": dict(
            api="ltx2", nargs=3, x_shape=(1, 1536, 4096), x_dtype=bf16,
            cossin_shape=(1, 32, 1536, 64), cossin_dtype=bf16, cossin_contig=False,
        ),
        "ltx2__B1_S126_H32_half32__bf16": dict(
            api="ltx2", nargs=3, x_shape=(1, 126, 2048), x_dtype=bf16,
            cossin_shape=(1, 32, 126, 32), cossin_dtype=bf16, cossin_contig=False,
        ),
        "ltx2__B1_S1536_H32_half32__bf16": dict(
            api="ltx2", nargs=3, x_shape=(1, 1536, 2048), x_dtype=bf16,
            cossin_shape=(1, 32, 1536, 32), cossin_dtype=bf16, cossin_contig=False,
        ),
        "ltx2__B1_S6144_H32_half64__bf16": dict(
            api="ltx2", nargs=3, x_shape=(1, 6144, 4096), x_dtype=bf16,
            cossin_shape=(1, 32, 6144, 64), cossin_dtype=bf16, cossin_contig=False,
        ),
        "ltx2__B1_S6144_H32_half32__bf16": dict(
            api="ltx2", nargs=3, x_shape=(1, 6144, 2048), x_dtype=bf16,
            cossin_shape=(1, 32, 6144, 32), cossin_dtype=bf16, cossin_contig=False,
        ),
    }


# ---------------------------------------------------------------------------
# Input builders (deterministic; LTX-2 cos/sin are intentionally non-contiguous)
# ---------------------------------------------------------------------------
def _build_standard_inputs(B, T, H, D, dtype, *, seed):
    g = torch.Generator(device=DEVICE).manual_seed(seed)
    x = torch.randn(B, T, H, D, device=DEVICE, dtype=torch.float32, generator=g).to(dtype)
    angles = torch.randn(T, D // 2, device=DEVICE, dtype=torch.float32, generator=g)
    cos = torch.cos(angles).contiguous()
    sin = torch.sin(angles).contiguous()
    return (x, cos, sin, False), {}


def _build_ltx2_inputs(B, S, H, half, dtype, *, seed):
    g = torch.Generator(device=DEVICE).manual_seed(seed)
    D = half * 2
    x = (torch.randn(B, S, H * D, device=DEVICE, dtype=torch.float32, generator=g) * 1e-1).to(dtype)
    angles = torch.randn(B, S, H, half, device=DEVICE, dtype=torch.float32, generator=g)
    cos = torch.cos(angles).to(dtype).contiguous().permute(0, 2, 1, 3)  # (B,H,S,half) non-contig
    sin = torch.sin(angles).to(dtype).contiguous().permute(0, 2, 1, 3)
    assert not cos.is_contiguous() and not sin.is_contiguous()
    return (x, cos, sin), {}


def make_cases() -> list[dict[str, Any]]:
    """Return the 6 deduplicated production cases (tensors materialized once)."""
    if torch is None:
        return []
    cases: list[dict[str, Any]] = []
    args, kwargs = _build_standard_inputs(1, 27030, 24, 128, torch.bfloat16, seed=0)
    cases.append(dict(
        name="hunyuanvideo__std__B1_T27030_H24_D128__bf16", api="standard",
        args=args, kwargs=kwargs, atol=1e-2, rtol=1e-2, warmup=25, iters=100,
    ))
    ltx2_specs = [
        ("ltx2__B1_S1536_H32_half64__bf16", 1, 1536, 32, 64),
        ("ltx2__B1_S126_H32_half32__bf16", 1, 126, 32, 32),
        ("ltx2__B1_S1536_H32_half32__bf16", 1, 1536, 32, 32),
        ("ltx2__B1_S6144_H32_half64__bf16", 1, 6144, 32, 64),
        ("ltx2__B1_S6144_H32_half32__bf16", 1, 6144, 32, 32),
    ]
    for i, (name, B, S, H, half) in enumerate(ltx2_specs, start=1):
        args, kwargs = _build_ltx2_inputs(B, S, H, half, torch.bfloat16, seed=i)
        cases.append(dict(
            name=name, api="ltx2", args=args, kwargs=kwargs,
            atol=1e-2, rtol=1e-2, warmup=25, iters=100,
        ))
    return cases


# ---------------------------------------------------------------------------
# Oracle / reference / candidate
# ---------------------------------------------------------------------------
def baseline(case: dict[str, Any]) -> Any:
    args = case["args"]
    if case["api"] == "standard":
        from sglang.jit_kernel.diffusion.triton.rotary import apply_rotary_embedding

        return apply_rotary_embedding(*args)
    if case["api"] == "ltx2":
        from sglang.jit_kernel.diffusion.triton.ltx2_rotary import apply_ltx2_split_rotary_emb

        return apply_ltx2_split_rotary_emb(*args)
    raise ValueError(f"unknown api {case['api']!r}")


def reference(case: dict[str, Any]) -> Any:
    args = case["args"]
    x, cos, sin = args[0], args[1], args[2]
    if case["api"] == "standard":
        interleaved = args[3] if len(args) > 3 else case.get("kwargs", {}).get("interleaved", False)
        return REF.std_rope_ref_fp32(x, cos, sin, interleaved=interleaved)
    if case["api"] == "ltx2":
        return REF.ltx2_rope_ref_fp32(x, cos, sin)
    raise ValueError(f"unknown api {case['api']!r}")


def candidate(case: dict[str, Any]) -> Any:
    module = _register()
    return module.optimized_wrapper(*case.get("args", ()), **case.get("kwargs", {}))


# ---------------------------------------------------------------------------
# Assertions
# ---------------------------------------------------------------------------
def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    if torch is not None and isinstance(value, torch.Tensor):
        assert not torch.isnan(value).any(), f"{path} contains NaN"
        assert not torch.isinf(value).any(), f"{path} contains Inf"


def _assert_close(actual, expected, *, case, path="out", check_dtype=True) -> None:
    atol = case.get("atol", 1e-2)
    rtol = case.get("rtol", 1e-2)
    _assert_no_nan_inf(actual, path=path)
    assert isinstance(actual, torch.Tensor) and isinstance(expected, torch.Tensor)
    assert actual.shape == expected.shape, f"{path} shape {actual.shape} != {expected.shape}"
    if check_dtype:
        assert actual.dtype == expected.dtype, f"{path} dtype {actual.dtype} != {expected.dtype}"
    torch.testing.assert_close(actual.float(), expected.float(), atol=atol, rtol=rtol)


def assert_bf16_noise_bounded(actual, ref_fp32, *, mult=3.0, floor=1e-6) -> None:
    a = actual.float()
    ref_bf16 = ref_fp32.to(torch.bfloat16).float()
    err = (a - ref_fp32).abs()
    noise = (ref_bf16 - ref_fp32).abs()
    err_rms = torch.sqrt(torch.mean(err.square()))
    noise_rms = torch.sqrt(torch.mean(noise.square()))
    assert err.max().item() <= mult * noise.max().clamp_min(floor).item() + floor, (
        f"max abs error {err.max().item():.3e} exceeds {mult}x bf16 noise {noise.max().item():.3e}"
    )
    assert err_rms.item() <= mult * noise_rms.clamp_min(floor).item() + floor, (
        f"rms error {err_rms.item():.3e} exceeds {mult}x bf16 rms noise {noise_rms.item():.3e}"
    )


def _sglang_git_head() -> str | None:
    try:
        import sglang.jit_kernel.diffusion.triton.rotary as m
    except Exception:
        return None
    src = Path(m.__file__).resolve().parent
    root = subprocess.run(
        ["git", "-C", str(src), "rev-parse", "--show-toplevel"], capture_output=True, text=True
    )
    if root.returncode != 0:
        return None
    head = subprocess.run(
        ["git", "-C", root.stdout.strip(), "rev-parse", "--short=9", "HEAD"],
        capture_output=True, text=True,
    )
    return head.stdout.strip() if head.returncode == 0 else None


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_register_metadata() -> None:
    module = _register()
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])
    assert set(module.EXPORTS) == {"apply_rotary_embedding", "apply_ltx2_split_rotary_emb"}


def test_case_manifest() -> None:
    """The case set must be EXACTLY the 6 deduplicated production rows."""
    cases = make_cases()
    expected = _expected_cases()
    assert len(cases) == 6, f"expected 6 cases, got {len(cases)}"
    assert {c["name"] for c in cases} == set(expected), "case-name set drifted from the manifest"

    for case in cases:
        meta = expected[case["name"]]
        args = case["args"]
        assert case["api"] == meta["api"]
        assert len(args) == meta["nargs"], f"{case['name']}: arg count {len(args)} != {meta['nargs']}"
        x, cos, sin = args[0], args[1], args[2]
        assert tuple(x.shape) == meta["x_shape"] and x.dtype == meta["x_dtype"]
        assert x.is_contiguous()
        assert tuple(cos.shape) == meta["cossin_shape"] == tuple(sin.shape)
        assert cos.dtype == sin.dtype == meta["cossin_dtype"]
        if meta["api"] == "standard":
            assert args[3] is False, "standard production call is positional (x, cos, sin, False)"
            assert cos.is_contiguous() and sin.is_contiguous()
        else:
            half = meta["cossin_shape"][-1]
            num_heads = meta["cossin_shape"][1]
            for t in (cos, sin):
                assert not t.is_contiguous(), f"{case['name']}: LTX-2 cos/sin must be non-contiguous"
                assert t.stride(-1) == 1, "LTX-2 cos/sin last-dim stride must be 1"
                assert t.stride(1) == half, "LTX-2 cos/sin head stride must equal half"
                assert t.stride(2) == num_heads * half, "LTX-2 cos/sin seq stride must equal num_heads*half"


def test_sglang_oracle_pinned() -> None:
    override = os.environ.get("KDA_SGLANG_ORACLE_COMMIT")
    expected = override or SGLANG_ORACLE_COMMIT
    head = _sglang_git_head()
    if head is None:
        # Provenance must NOT silently pass: only accept a non-git-checkout oracle
        # when an override is explicitly set (and record it in the run output).
        if override is not None:
            print(f"[oracle-pin] imported SGLang is not a git checkout; honoring override KDA_SGLANG_ORACLE_COMMIT={override}")
            return
        pytest.fail(
            f"imported SGLang is not a git checkout; cannot verify the oracle pin {SGLANG_ORACLE_COMMIT}. "
            "Set KDA_SGLANG_ORACLE_COMMIT=<commit> to override and record it."
        )
    assert head.startswith(expected) or expected.startswith(head), (
        f"SGLang oracle commit {head!r} != expected {expected!r}; set KDA_SGLANG_ORACLE_COMMIT to override"
    )
    if override is not None:
        print(f"[oracle-pin] override KDA_SGLANG_ORACLE_COMMIT={override}; imported SGLang HEAD={head}")


def test_baseline_matches_reference() -> None:
    """Lock the contract: SGLang baseline must match the FP32 reference within bf16 noise."""
    cases = make_cases()
    assert cases
    for case in cases:
        base = baseline(case)
        ref = reference(case)
        _assert_no_nan_inf(base, path=case["name"] + ":baseline")
        assert_bf16_noise_bounded(base, ref, mult=3.0)


def test_correctness_cases() -> None:
    cases = make_cases()
    assert cases, "No correctness cases recovered. Fill make_cases() before optimizing."
    wrapper = _wrapper()
    for case in cases:
        x = case["args"][0]
        x_before = x.clone()
        base = baseline(case)
        ref = reference(case)
        cand = candidate(case)
        api = case["api"]
        # Supported production cases MUST take the native CUDA route -- a broken kernel
        # that silently falls back must NOT pass as correct (guards AC-2/AC-3).
        assert wrapper._LAST_DISPATCH[api] == "cuda", (
            f"{case['name']}: expected CUDA route, got {wrapper._LAST_DISPATCH[api]!r} "
            "(broken native kernel must not pass via fallback)"
        )
        # Functional contract: input not mutated; same dtype as input.
        assert torch.equal(x, x_before), f"{case['name']}: input x was mutated"
        assert cand.dtype == x.dtype, f"{case['name']}: candidate dtype {cand.dtype} != input {x.dtype}"
        _assert_no_nan_inf(cand, path=case["name"] + ":candidate")
        _assert_close(cand, base, case=case, path=case["name"])
        assert_bf16_noise_bounded(cand, ref, mult=3.0)


def test_fallback_routing() -> None:
    """Unsupported signatures must fall back non-recursively to the original baseline,
    or to the PyTorch reference if the baseline is unavailable -- never recurse."""
    wrapper = _wrapper()
    from sglang.jit_kernel.diffusion.triton.rotary import apply_rotary_embedding as sgl_std
    from sglang.jit_kernel.diffusion.triton.ltx2_rotary import apply_ltx2_split_rotary_emb as sgl_ltx2

    assert wrapper._BASELINES.get("standard") is sgl_std, "standard baseline must be the original SGLang symbol"
    assert wrapper._BASELINES.get("ltx2") is sgl_ltx2, "ltx2 baseline must be the original SGLang symbol"

    H, D = 24, 128
    angles = torch.randn(64, D // 2, device=DEVICE, dtype=torch.float32)
    cos2d, sin2d = torch.cos(angles), torch.sin(angles)

    def assert_not_cuda(x, cos, sin, interleaved, label):
        wrapper._LAST_DISPATCH["standard"] = None
        out = wrapper.apply_rotary_embedding(x, cos, sin, interleaved)
        assert wrapper._LAST_DISPATCH["standard"] != "cuda", f"{label}: must not take CUDA route"
        assert out.dtype == x.dtype, f"{label}: dtype changed"

    # Each unsupported standard signature must fall back (not CUDA):
    assert_not_cuda(torch.randn(1, 64, H, D, device=DEVICE, dtype=torch.float16), cos2d, sin2d, False, "fp16-standard")
    assert_not_cuda(torch.randn(1, 64, H, D, device=DEVICE, dtype=torch.bfloat16), cos2d, sin2d, True, "interleaved-true")
    assert_not_cuda(torch.randn(64, H, D, device=DEVICE, dtype=torch.bfloat16), cos2d, sin2d, False, "3d-standard")
    a64 = torch.randn(64, 32, device=DEVICE, dtype=torch.float32)
    assert_not_cuda(torch.randn(1, 64, H, 64, device=DEVICE, dtype=torch.bfloat16), torch.cos(a64), torch.sin(a64), False, "head64")
    # All-CPU (non-CUDA device) -> reference fallback, correct dtype.
    xc = torch.randn(1, 64, H, D, dtype=torch.bfloat16)
    wrapper._LAST_DISPATCH["standard"] = None
    oc = wrapper.apply_rotary_embedding(xc, torch.cos(angles).cpu(), torch.sin(angles).cpu(), False)
    assert wrapper._LAST_DISPATCH["standard"] != "cuda" and oc.dtype == xc.dtype

    # Standard non-recursion: baseline reached exactly once.
    calls = {"n": 0}
    orig = wrapper._BASELINES["standard"]
    wrapper._BASELINES["standard"] = lambda *a, **k: (calls.__setitem__("n", calls["n"] + 1) or orig(*a, **k))
    try:
        wrapper._LAST_DISPATCH["standard"] = None
        wrapper.apply_rotary_embedding(torch.randn(1, 64, H, D, device=DEVICE, dtype=torch.float16), cos2d, sin2d, False)
    finally:
        wrapper._BASELINES["standard"] = orig
    if wrapper._LAST_DISPATCH["standard"] == "baseline":
        assert calls["n"] == 1, "standard baseline reached exactly once (no recursion)"

    # LTX-2 non-bf16 -> fallback; ltx2 baseline non-recursion exactly once.
    xl = torch.randn(1, 128, 32 * 64, device=DEVICE, dtype=torch.float16)
    al = torch.randn(1, 128, 32, 32, device=DEVICE, dtype=torch.float16)
    cl, sl = torch.cos(al).permute(0, 2, 1, 3), torch.sin(al).permute(0, 2, 1, 3)
    lcalls = {"n": 0}
    lorig = wrapper._BASELINES["ltx2"]
    wrapper._BASELINES["ltx2"] = lambda *a, **k: (lcalls.__setitem__("n", lcalls["n"] + 1) or lorig(*a, **k))
    try:
        wrapper._LAST_DISPATCH["ltx2"] = None
        wrapper.apply_ltx2_split_rotary_emb(xl, cl, sl)
    finally:
        wrapper._BASELINES["ltx2"] = lorig
    assert wrapper._LAST_DISPATCH["ltx2"] != "cuda"
    if wrapper._LAST_DISPATCH["ltx2"] == "baseline":
        assert lcalls["n"] == 1, "ltx2 baseline reached exactly once (no recursion)"


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v", "-s"]))
