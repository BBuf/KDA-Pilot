"""Correctness harness for ``b200_diffusion_qknorm_rope__multi_shape``.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` is set (the real run owns the CUDA
environment on the remote NVIDIA B200 box via the ``ion-b200`` skill).

Semantics recovered from the SGLang baseline
(``sglang/jit_kernel/diffusion/qknorm_rope.py`` +
``csrc/diffusion/qknorm_rope.cuh``):

- ``fused_inplace_qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions,
  *, is_neox, eps=1e-6, head_dim=0, rope_dim=0) -> None`` mutates ``q`` and ``k``
  IN PLACE (per-head RMS norm with weight, then RoPE by ``positions``).
- The semantic oracle is the SGLang split path:
  ``fused_inplace_qknorm`` (bf16) followed by
  ``flashinfer.rope.apply_rope_with_cos_sin_cache_inplace``, compared at
  ``ATOL=8e-2, RTOL=1e-2`` (identical to
  ``python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py``).

Case sets:
- ``make_cases()`` — the 10 fixed production rows (used for primary benchmarking).
- ``make_ci_grid_cases()`` — the SGLang CI grid (correctness-or-fallback). The full
  grid is the default; set ``KDA_CI_GRID_SUBSET=1`` for the reduced developer subset.

Inputs follow the SGLang test/benchmark convention (cos/sin cache sized to
``MAX_SEQ_LEN`` with randomized positions) so the comparison is fair against
SGLang's own harnesses and exercises arbitrary RoPE positions rather than the
identity mapping.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"
KERNEL_DIR = Path(__file__).resolve().parents[1]

# Tolerances and RoPE constants mirror the SGLang reference test exactly.
ATOL = 8e-2
RTOL = 1e-2
MAX_SEQ_LEN = 131072
ROPE_BASE = 10000.0

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on the CUDA box (ion-b200) to run.",
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


def _load_wrapper_module():
    """Return THIS task's impl wrapper module (the dispatch gate + candidate build), loaded via
    register.py's slug-specific loader. Avoids a generic top-level ``import wrapper`` that could
    resolve another task's module in a multi-kernel test process; shares the same instance the
    registered ``optimized_wrapper`` forwards into."""
    return _load_register_module()._load_impl()


def _torch_dtype(name: str):
    return {"bfloat16": torch.bfloat16, "float16": torch.float16}[name]


def _position_dtype(name: str):
    return {"int32": torch.int32, "int64": torch.int64}[name]


# --- Production shapes (verbatim from prompt.md / docs/captured_shapes_b200.jsonl) ---
# All head_dim=128, rope_dim=128, is_neox=False, bfloat16, int64 positions.
_PRODUCTION_ROWS = [
    # (preset, bucket, num_tokens, num_heads, eps)
    ("joyai-edit", "large", 7904, 32, 1e-6),
    ("qwen", "large", 4096, 24, 1e-6),
    ("qwen-edit", "large", 8424, 24, 1e-6),
    ("zimage", "large", 4096, 30, 1e-5),
    ("zimage", "large", 4128, 30, 1e-5),
    ("qwen", "small", 19, 24, 1e-6),
    ("qwen", "small", 47, 24, 1e-6),
    ("qwen-edit", "small", 195, 24, 1e-6),
    ("qwen-edit", "small", 189, 24, 1e-6),
    ("zimage", "small", 32, 30, 1e-5),
]

# rope_dim choices per head_dim, from the SGLang reference test.
ROPE_DIM_CHOICES = {64: [64], 128: [64, 128], 256: [64, 128, 256]}


def make_cases() -> list[dict[str, Any]]:
    """The 10 fixed production rows (primary correctness + benchmark set)."""
    cases: list[dict[str, Any]] = []
    for preset, bucket, num_tokens, num_heads, eps in _PRODUCTION_ROWS:
        cases.append(
            {
                "name": f"{preset}__{bucket}__B{num_tokens}_H{num_heads}_D128_R128",
                "preset": preset,
                "bucket": bucket,
                "num_tokens": num_tokens,
                "num_heads": num_heads,
                "head_dim": 128,
                "rope_dim": 128,
                "is_neox": False,
                "eps": eps,
                "dtype": "bfloat16",
                "position_dtype": "int64",
                "ci_fallback": False,
                "atol": ATOL,
                "rtol": RTOL,
                "warmup": 25,
                "iters": 100,
            }
        )
    return cases


def _ci_ranges(full: bool):
    if full:
        bs = [2 ** n for n in range(13)]  # 1 .. 4096
        bs = sorted(set(bs + [x + 1 for x in bs] + [1, 9, 129, 257, 2049, 4097]))
        heads = [8, 16, 24, 32]
        head_dims = [64, 128, 256]
    else:
        # CI subset: enough to exercise every code path / fallback branch cheaply.
        bs = [1, 9, 129, 257]
        heads = [8, 24]
        head_dims = [64, 128, 256]
    return bs, heads, head_dims


def make_ci_grid_cases() -> list[dict[str, Any]]:
    """SGLang CI-grid correctness-or-fallback cases, kept separate from
    the production rows. Honors the kernel's support gate
    (`rope_dim % (head_dim//32) == 0`; for neox, power-of-two rotary lanes).

    The FULL grid is the default acceptance path; set ``KDA_CI_GRID_SUBSET=1`` for
    the reduced developer-smoke subset.
    """
    full = os.environ.get("KDA_CI_GRID_SUBSET") != "1"
    bs_list, heads_list, hd_list = _ci_ranges(full)
    cases: list[dict[str, Any]] = []
    for bs in bs_list:
        for h in heads_list:
            for hd in hd_list:
                elems = hd // 32
                for rd in ROPE_DIM_CHOICES[hd]:
                    if rd % elems != 0:
                        continue
                    for is_neox in (False, True):
                        if is_neox:
                            lanes = rd // elems
                            if lanes < 2 or (lanes & (lanes - 1)):
                                continue
                        for pos_dt in ("int32", "int64"):
                            cases.append(
                                {
                                    "name": f"cigrid__B{bs}_H{h}_D{hd}_R{rd}_neox{int(is_neox)}_{pos_dt}",
                                    "preset": "ci-grid",
                                    "bucket": "ci_fallback",
                                    "num_tokens": bs,
                                    "num_heads": h,
                                    "head_dim": hd,
                                    "rope_dim": rd,
                                    "is_neox": is_neox,
                                    "eps": 1e-6,
                                    "dtype": "bfloat16",
                                    "position_dtype": pos_dt,
                                    "ci_fallback": True,
                                    "atol": ATOL,
                                    "rtol": RTOL,
                                    "warmup": 5,
                                    "iters": 20,
                                }
                            )
    return cases


# Read-only cos/sin caches memoized by (rope_dim, device): the full CI grid reuses
# only a handful of distinct rope_dims, so this avoids rebuilding a large cache per case.
_COS_SIN_CACHE: dict = {}


def _create_cos_sin_cache(rope_dim: int, device: str) -> "torch.Tensor":
    """[MAX_SEQ_LEN, rope_dim] float32 cache: concat(cos, sin) halves.

    Identical construction to the SGLang reference test/benchmark; memoized per
    (rope_dim, device) since it is read-only.
    """
    key = (rope_dim, device)
    cached = _COS_SIN_CACHE.get(key)
    if cached is not None:
        return cached
    inv_freq = 1.0 / (
        ROPE_BASE
        ** (torch.arange(0, rope_dim, 2, dtype=torch.float32, device=device) / rope_dim)
    )
    t = torch.arange(MAX_SEQ_LEN, dtype=torch.float32, device=device)
    freqs = torch.einsum("i,j->ij", t, inv_freq)
    cache = torch.cat((freqs.cos(), freqs.sin()), dim=-1)
    _COS_SIN_CACHE[key] = cache
    return cache


def _make_inputs(case: dict[str, Any], device: str = "cuda") -> dict[str, "torch.Tensor"]:
    """Deterministic, seeded inputs so baseline() and candidate() get identical data."""
    dtype = _torch_dtype(case["dtype"])
    pos_dtype = _position_dtype(case["position_dtype"])
    n, h, d, r = case["num_tokens"], case["num_heads"], case["head_dim"], case["rope_dim"]

    seed = (n * 1_000_003 + h * 8191 + d * 127 + r * 17 + int(case["is_neox"])) & 0x7FFFFFFF
    g = torch.Generator(device=device)
    g.manual_seed(seed)

    return {
        "q": torch.randn(n, h, d, device=device, dtype=dtype, generator=g),
        "k": torch.randn(n, h, d, device=device, dtype=dtype, generator=g),
        "q_weight": torch.randn(d, device=device, dtype=dtype, generator=g),
        "k_weight": torch.randn(d, device=device, dtype=dtype, generator=g),
        "cos_sin_cache": _create_cos_sin_cache(r, device),
        "positions": torch.randint(0, MAX_SEQ_LEN, (n,), device=device, dtype=pos_dtype, generator=g),
    }


def _run_oracle(inputs: dict[str, "torch.Tensor"], case: dict[str, Any]) -> tuple:
    """SGLang split-path oracle: separate qknorm (bf16) + FlashInfer RoPE, in place."""
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace

    from sglang.jit_kernel.norm import fused_inplace_qknorm

    q, k = inputs["q"], inputs["k"]
    fused_inplace_qknorm(q, k, inputs["q_weight"], inputs["k_weight"], eps=case["eps"])
    apply_rope_with_cos_sin_cache_inplace(
        positions=inputs["positions"].long(),
        query=q.view(q.shape[0], -1),
        key=k.view(k.shape[0], -1),
        head_size=q.shape[-1],
        cos_sin_cache=inputs["cos_sin_cache"],
        is_neox=case["is_neox"],
    )
    return q, k


def baseline(case: dict[str, Any]) -> Any:
    """Semantic oracle result (mutated q, k) for one configured case."""
    inputs = _make_inputs(case)
    return _run_oracle(inputs, case)


def candidate(case: dict[str, Any]) -> Any:
    """Candidate result (mutated q, k) via the registered optimized wrapper."""
    module = _load_register_module()
    wrapper = getattr(module, "optimized_wrapper")
    inputs = _make_inputs(case)
    q, k = inputs["q"], inputs["k"]
    wrapper(
        q,
        k,
        inputs["q_weight"],
        inputs["k_weight"],
        inputs["cos_sin_cache"],
        inputs["positions"],
        is_neox=case["is_neox"],
        eps=case["eps"],
        head_dim=case["head_dim"],
        rope_dim=case["rope_dim"],
    )
    return q, k


def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    if torch is not None and isinstance(value, torch.Tensor):
        assert not torch.isnan(value).any(), f"{path} contains NaN"
        assert not torch.isinf(value).any(), f"{path} contains Inf"
    elif isinstance(value, (tuple, list)):
        for i, item in enumerate(value):
            _assert_no_nan_inf(item, path=f"{path}[{i}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            _assert_no_nan_inf(item, path=f"{path}.{key}")


def _assert_close(actual: Any, expected: Any, *, case: dict[str, Any], path: str = "out") -> None:
    atol = case.get("atol", ATOL)
    rtol = case.get("rtol", RTOL)
    _assert_no_nan_inf(actual, path=path)
    if torch is not None and isinstance(actual, torch.Tensor):
        assert isinstance(expected, torch.Tensor), f"{path} expected tensor, got {type(expected)}"
        assert actual.shape == expected.shape, f"{path} shape {actual.shape} != {expected.shape}"
        torch.testing.assert_close(actual.float(), expected.float(), atol=atol, rtol=rtol)
        return
    if isinstance(actual, (tuple, list)):
        assert isinstance(expected, type(actual)), f"{path} type mismatch"
        assert len(actual) == len(expected), f"{path} length mismatch"
        for i, (a_item, e_item) in enumerate(zip(actual, expected)):
            _assert_close(a_item, e_item, case=case, path=f"{path}[{i}]")
        return
    assert actual == expected, f"{path} value mismatch"


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def test_correctness_cases() -> None:
    cases = make_cases()
    assert len(cases) == 10, f"expected 10 production rows, got {len(cases)}"
    for case in cases:
        expected = baseline(case)
        actual = candidate(case)
        _assert_close(actual, expected, case=case, path=case.get("name", "out"))


def test_ci_grid_cases() -> None:
    """Every CI-grid signature either matches the oracle or falls back to the SGLang
    baseline (the wrapper handles the fallback internally)."""
    cases = make_ci_grid_cases()
    assert cases, "CI grid produced no cases."
    for case in cases:
        expected = baseline(case)
        actual = candidate(case)
        _assert_close(actual, expected, case=case, path=case["name"])


# --- Negative tests: prove the harness catches the documented failure modes ---

def test_negative_no_mutation_is_caught() -> None:
    """A candidate that does not mutate q/k must FAIL the comparison.

    Guards against a harness that compares the wrapper's return value (None)
    instead of the in-place-mutated tensors.
    """
    case = make_cases()[0]
    ref = baseline(case)  # oracle on identical seeded inputs
    untouched = _make_inputs(case)  # same seed -> raw inputs, never normed/roped
    with pytest.raises(AssertionError):
        _assert_close((untouched["q"], untouched["k"]), ref, case=case, path="noop")


def test_negative_ignored_positions_is_caught() -> None:
    """A candidate that ignores ``positions`` (uses 0 for all) must FAIL."""
    from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope

    case = make_cases()[0]
    ref = baseline(case)
    inputs = _make_inputs(case)
    q, k = inputs["q"], inputs["k"]
    fused_inplace_qknorm_rope(
        q,
        k,
        inputs["q_weight"],
        inputs["k_weight"],
        inputs["cos_sin_cache"],
        torch.zeros_like(inputs["positions"]),  # ignore real positions
        is_neox=case["is_neox"],
        eps=case["eps"],
        head_dim=case["head_dim"],
        rope_dim=case["rope_dim"],
    )
    with pytest.raises(AssertionError):
        _assert_close((q, k), ref, case=case, path="zeropos")


def test_negative_nan_inf_is_caught() -> None:
    """NaN/Inf in an output must raise."""
    nan_t = torch.full((4,), float("nan"), device="cuda")
    with pytest.raises(AssertionError):
        _assert_no_nan_inf(nan_t, path="nan")
    inf_t = torch.full((4,), float("inf"), device="cuda")
    with pytest.raises(AssertionError):
        _assert_no_nan_inf(inf_t, path="inf")


def _adhoc_case(name: str, num_tokens: int, num_heads: int, position_dtype: str = "int64") -> dict:
    return {
        "name": name, "preset": "fallback", "bucket": "fallback",
        "num_tokens": num_tokens, "num_heads": num_heads, "head_dim": 128, "rope_dim": 128,
        "is_neox": False, "eps": 1e-6, "dtype": "bfloat16", "position_dtype": position_dtype,
        "ci_fallback": True, "atol": ATOL, "rtol": RTOL, "warmup": 5, "iters": 10,
    }


def test_dispatch_routing_exact_shape() -> None:
    """Only the 5 large captured (tokens, heads, eps) rows are trusted for the staged kernel."""
    w = _load_wrapper_module()
    for n, h, eps in [(7904, 32, 1e-6), (4096, 24, 1e-6), (8424, 24, 1e-6), (4096, 30, 1e-5), (4128, 30, 1e-5)]:
        assert w._is_captured_large(n, h, eps), (n, h, eps)
    for n, h, eps in [(19, 24, 1e-6), (47, 24, 1e-6), (195, 24, 1e-6), (189, 24, 1e-6), (32, 30, 1e-5)]:
        assert not w._is_captured_large(n, h, eps), (n, h, eps)  # small captured rows -> baseline
    assert not w._is_captured_large(1000, 24, 1e-6)  # non-captured tokens
    assert not w._is_captured_large(4096, 16, 1e-6)  # non-captured head count
    assert not w._is_captured_large(4096, 24, 1e-5)  # captured (tokens,heads) but WRONG eps
    assert not w._is_captured_large(4096, 30, 1e-6)  # captured (tokens,heads) but WRONG eps


def _gate_inputs(n=4096, h=24, d=128, r=128, *, dtype=None, pos_dtype=None, device="cuda"):
    """A fully-valid captured-large (4096,24) signature on CUDA; mutate one field per case."""
    dtype = torch.bfloat16 if dtype is None else dtype
    pos_dtype = torch.int64 if pos_dtype is None else pos_dtype
    return {
        "q": torch.zeros(n, h, d, device=device, dtype=dtype),
        "k": torch.zeros(n, h, d, device=device, dtype=dtype),
        "q_weight": torch.zeros(d, device=device, dtype=dtype),
        "k_weight": torch.zeros(d, device=device, dtype=dtype),
        "cos_sin_cache": torch.zeros(8, r, device=device, dtype=torch.float32),
        "positions": torch.zeros(n, device=device, dtype=pos_dtype),
    }


def test_dispatch_gate_fails_closed() -> None:
    """``supported()`` admits ONLY the exact captured signature with the full production
    contract; every malformed / non-production variant fails closed (-> baseline), so it
    can never reach the staged C++ TensorMatcher. Uses CUDA tensors (the gate requires a
    CUDA device)."""
    w = _load_wrapper_module()

    def ok(inp, *, is_neox=False, eps=1e-6, head_dim=128, rope_dim=128):
        return w.supported(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
                           inp["cos_sin_cache"], inp["positions"],
                           is_neox=is_neox, eps=eps, head_dim=head_dim, rope_dim=rope_dim)

    assert ok(_gate_inputs())                                 # exact captured + full contract -> staged
    assert not ok(_gate_inputs(), eps=1e-5)                   # captured shape, WRONG eps
    assert not ok(_gate_inputs(), is_neox=True)               # neox
    assert not ok(_gate_inputs(), head_dim=64, rope_dim=64)   # non-production template
    assert not ok(_gate_inputs(pos_dtype=torch.int32))        # int32 positions
    assert not ok(_gate_inputs(dtype=torch.float16))          # fp16

    bad_cache = _gate_inputs()
    bad_cache["cos_sin_cache"] = torch.zeros(8, 128, device="cuda", dtype=torch.float64)
    assert not ok(bad_cache)                                  # non-float32 cache

    # Wrong q/k last dim with a misleading head_dim=128 claim -> falls back (no C++ matcher).
    assert not ok(_gate_inputs(d=64), head_dim=128, rope_dim=128)

    bad_cache_dim = _gate_inputs()
    bad_cache_dim["cos_sin_cache"] = torch.zeros(8, 64, device="cuda", dtype=torch.float32)
    assert not ok(bad_cache_dim)                              # cache last-dim != rope_dim

    bad_w = _gate_inputs()
    bad_w["q_weight"] = torch.zeros(64, device="cuda", dtype=torch.bfloat16)
    assert not ok(bad_w)                                      # wrong-shaped q_weight

    nc_w = _gate_inputs()
    nc_w["q_weight"] = torch.zeros(128, 2, device="cuda", dtype=torch.bfloat16)[:, 0]  # 1-D, stride 2
    assert not nc_w["q_weight"].is_contiguous()
    assert not ok(nc_w)                                       # non-contiguous q_weight

    bad_pos = _gate_inputs()
    bad_pos["positions"] = torch.zeros(100, device="cuda", dtype=torch.int64)
    assert not ok(bad_pos)                                    # positions length != num_tokens

    nc_q = _gate_inputs()
    nc_q["q"] = torch.zeros(4096, 128, 24, device="cuda", dtype=torch.bfloat16).transpose(1, 2)
    assert not nc_q["q"].is_contiguous()
    assert not ok(nc_q)                                       # non-contiguous q

    alias = _gate_inputs()
    alias["k"] = alias["q"]                                   # q/k aliased -> in-place order undefined
    assert not ok(alias)

    assert not ok(_gate_inputs(n=1000))                       # non-captured token count
    assert not ok(_gate_inputs(h=16))                         # non-captured head count


def test_fallback_routes_to_baseline_and_matches_oracle() -> None:
    """Non-captured / int32-position production-config shapes fall back to the SGLang
    baseline and still match the split-path oracle."""
    for case in [
        _adhoc_case("fb_B1000_H24", 1000, 24),         # non-captured token count
        _adhoc_case("fb_B4096_H16", 4096, 16),         # non-captured head count
        _adhoc_case("fb_int32pos_B4096_H24", 4096, 24, position_dtype="int32"),
    ]:
        _assert_close(candidate(case), baseline(case), case=case, path=case["name"])


def test_wrong_eps_falls_back_and_matches_oracle() -> None:
    """A captured (tokens, heads) shape called with a DIFFERENT eps than its production row
    is not a captured signature: it falls back to the baseline and still matches the oracle."""
    case = _adhoc_case("fb_wrong_eps_B4096_H24", 4096, 24)  # qwen row is eps=1e-6 ...
    case["eps"] = 1e-5                                       # ... call it with 1e-5 instead
    _assert_close(candidate(case), baseline(case), case=case, path=case["name"])


@pytest.mark.skipif(
    os.environ.get("KDA_RUN_INTEGRATED") != "1",
    reason="Set KDA_RUN_INTEGRATED=1 (needs the exported kda_kernels overlay) to run.",
)
def test_install_path_dropin_and_no_recursion() -> None:
    """Full AC-8 drop-in test on the LITERAL ``kda_kernels.install()`` path: after the
    monkey-patch, the INSTALLED public symbol routes a large captured row to the staged
    CUDA kernel and the small / int32 rows to the captured ORIGINAL baseline (NOT the
    swapped KDA symbol → no recursion). Each route is verified by both the dispatch tag
    and an oracle match, and the baseline is restored on exit."""
    import importlib

    root = KERNEL_DIR
    for _ in range(8):
        if (root / "kda_kernels" / "__init__.py").exists():
            if str(root) not in sys.path:
                sys.path.insert(0, str(root))
            break
        root = root.parent

    qmod = importlib.import_module("sglang.jit_kernel.diffusion.qknorm_rope")
    baseline_op = qmod.fused_inplace_qknorm_rope  # captured BEFORE install
    import kda_kernels
    import kda_kernels.diffusion.qknorm_rope as overlay

    # The committed overlay is an evidence-backed no-go (the staged kernel is a real device
    # win but a net regression on the literal install path, geomean ~0.92x — see
    # docs/sglang_jit_export.md). It ships UN-promoted, so skip unless re-exported.
    if not getattr(overlay, "KDA_OPTIMIZED_fused_inplace_qknorm_rope", False):
        pytest.skip("b200 overlay is not promoted; run "
                    "`python3 scripts/export_kda_kernels/export.py b200_diffusion_qknorm_rope__multi_shape` first.")

    key = "sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope"
    results = kda_kernels.install(force=True, strict=True)
    try:
        status = next((st for (sp, _kp, st) in results if sp == key), None)
        assert status == "swapped", results
        installed = qmod.fused_inplace_qknorm_rope
        assert installed is not baseline_op, "public symbol was not swapped"
        assert installed.__module__.startswith("kda_kernels"), installed.__module__
        # The installed b200 impl module (whose get_last_dispatch records the route taken).
        impl = importlib.import_module("kda_kernels.diffusion.qknorm_rope._impls.b200.wrapper")
        # large captured -> staged CUDA; small + int32 -> captured baseline (no recursion).
        for case, want in [
            (_adhoc_case("install_large_B4096_H24", 4096, 24), "cuda"),
            (_adhoc_case("install_small_B19_H24", 19, 24), "fallback"),
            (_adhoc_case("install_int32_B4096_H24", 4096, 24, position_dtype="int32"), "fallback"),
        ]:
            inputs = _make_inputs(case)
            q, k = inputs["q"], inputs["k"]
            installed(
                q, k, inputs["q_weight"], inputs["k_weight"],
                inputs["cos_sin_cache"], inputs["positions"],
                is_neox=case["is_neox"], eps=case["eps"],
                head_dim=case["head_dim"], rope_dim=case["rope_dim"],
            )
            assert impl.get_last_dispatch() == want, (case["name"], impl.get_last_dispatch())
            _assert_close((q, k), baseline(case), case=case, path=case["name"])
    finally:
        kda_kernels.uninstall()
        assert qmod.fused_inplace_qknorm_rope is baseline_op, "baseline not restored"
