"""Build, load, and dispatch for the candidate fused GroupNorm+SiLU kernels.

Primary entry (destination-passing, the benchmark ABI):

    group_norm_silu_candidate_into(x, weight, bias, num_groups, eps, out)

plus an allocate-and-return convenience entry:

    group_norm_silu_candidate(x, weight, bias, num_groups, eps) -> Tensor

Every regime runs solution-owned CUDA kernels (full evidence in
docs/dispatch.md):

* one-CTA-per-group kernel for small groups (the host launcher widens to
  1024-thread blocks for the crossover band just under the chunked
  threshold, where 256-thread blocks starve per-SM memory parallelism);
* chunked three-kernel pipeline for large groups;
* register-lean exact-grid two-kernel pipeline with streaming-hint loads/
  stores and per-shape zero-straddle tiles for giant groups.

Reduction scratch is allocated per call through torch's caching allocator —
the candidate's natural behavior, mirroring how the copied baseline allocates
its partials internally. The CUDA module is built once per process (prefer
tvm_ffi.cpp.load; nvcc fallback) into solution/.build/ and loaded through
tvm_ffi — no sglang involvement anywhere.
"""

from __future__ import annotations

import functools
import hashlib
import os
import subprocess
import sys
from pathlib import Path

import torch

SOLUTION_DIR = Path(__file__).resolve().parent
KERNEL_CU = SOLUTION_DIR / "kernel.cu"
BUILD_ROOT = SOLUTION_DIR / ".build"

# Dispatch boundary between the one-CTA-per-group kernel and the chunked
# multi-CTA pipeline. Initial value = the prior tuned crossover; retuned
# against the freshly locked baseline before the final benchmark
# (override for tuning sweeps via GNS_SMALL_LARGE_THRESH).
LARGE_THRESHOLD = int(os.environ.get("GNS_SMALL_LARGE_THRESH", str(1 << 16)))
# Elements per CTA-task in the large path; must match kChunkElems in kernel.cu.
CHUNK_ELEMS = 8192
# Boundary where the persistent-grid large path measurably degrades and the
# register-lean exact-grid giant pipeline takes over (first benchmark showed
# the large path falling below parity from ~700K elements per group), plus
# the giant path's own CTA-task size. Both env-tunable for crossover sweeps.
GIANT_THRESHOLD = int(os.environ.get("GNS_GIANT_THRESH", str(700_000)))
GIANT_CHUNK_ELEMS = int(os.environ.get("GNS_GIANT_CHUNK", str(16384)))
# Giant groups whose spatial extent has an exact vector-aligned tile divisor
# take the clean-giant pipeline: channel-aligned tiles, hoisted-affine apply
# with no segment handling (the class where the baseline's own hoisted-affine
# apply previously held a 3-6% edge). Tile size is the per-shape zero-straddle
# divisor (fixed 8192 tiles were measured slower on the largest rows: more
# tiles -> more reduce rounds and partial traffic). Env override for sweeps.
CLEAN_CHUNK_ELEMS = int(os.environ.get("GNS_CLEAN_CHUNK", "0"))  # 0 = per-shape divisor
# The giant pipeline can tile its two kernels independently (the apply kernel
# reads only mean/rstd, never the partials). Measurements across the
# production set showed no robust win for larger stats tiles, so the default
# (0) keeps the stats tile equal to the per-shape apply tile; the env knob
# remains for future crossover sweeps.
GIANT_STATS_CHUNK_ELEMS = int(os.environ.get("GNS_GIANT_STATS_CHUNK", "0"))

_CUDA_ARCH = os.environ.get("GNS_CUDA_ARCH", "90")
_NVCC_BASE_FLAGS = [
    "-O3",
    "-std=c++20",
    "--expt-relaxed-constexpr",
    "-lineinfo",
    "-shared",
    "-Xcompiler",
    "-fPIC",
]


def _candidate_paths(paths: list[Path]) -> list[Path]:
    return [p for p in paths if p and p.is_dir()]


def _tvm_ffi_include_dirs() -> list[Path]:
    import tvm_ffi

    pkg = Path(tvm_ffi.__file__).resolve().parent
    candidates = [pkg / "include", pkg.parent / "include"]
    for attr in ("get_include", "include_dir", "include"):
        obj = getattr(tvm_ffi, attr, None)
        try:
            value = obj() if callable(obj) else obj
        except Exception:
            value = None
        if isinstance(value, (str, Path)):
            candidates.append(Path(value))
        elif isinstance(value, (list, tuple)):
            candidates.extend(Path(v) for v in value)
    libinfo = getattr(tvm_ffi, "libinfo", None)
    if libinfo is not None:
        for fn_name in ("find_include_path", "include_path"):
            fn = getattr(libinfo, fn_name, None)
            if callable(fn):
                try:
                    value = fn()
                except Exception:
                    continue
                if isinstance(value, (list, tuple)):
                    candidates.extend(Path(v) for v in value)
                elif value:
                    candidates.append(Path(value))
    dirs = _candidate_paths(candidates)
    if not dirs:
        raise RuntimeError("cannot locate tvm_ffi include directory")
    return dirs


def _tvm_ffi_lib_dirs() -> list[Path]:
    import tvm_ffi

    pkg = Path(tvm_ffi.__file__).resolve().parent
    candidates = [pkg, pkg / "lib", pkg.parent / "lib"]
    libinfo = getattr(tvm_ffi, "libinfo", None)
    if libinfo is not None:
        fn = getattr(libinfo, "find_lib_path", None)
        if callable(fn):
            try:
                value = fn()
            except Exception:
                value = None
            if isinstance(value, (list, tuple)):
                candidates.extend(Path(v).parent for v in value)
            elif value:
                candidates.append(Path(value).parent)
    return _candidate_paths(candidates)


def _find_tvm_ffi_lib() -> Path | None:
    for d in _tvm_ffi_lib_dirs():
        for pattern in ("libtvm_ffi*.so", "tvm_ffi*.so", "libtvm_ffi*.dylib"):
            hits = sorted(d.glob(pattern))
            if hits:
                return hits[0]
    return None


def _dlpack_include_dirs() -> list[Path]:
    candidates: list[Path] = []
    for inc in _tvm_ffi_include_dirs():
        candidates += [inc, inc / "dlpack"]
        if (inc / "dlpack" / "dlpack.h").exists():
            candidates.append(inc)
    try:
        import dlpack  # type: ignore

        candidates.append(Path(dlpack.__file__).resolve().parent / "include")
    except Exception:
        pass
    return _candidate_paths(candidates)


def _torch_abi_define() -> str:
    import torch._C

    return f"-D_GLIBCXX_USE_CXX11_ABI={int(torch._C._GLIBCXX_USE_CXX11_ABI)}"


def _build_command(out_so: Path) -> list[str]:
    from torch.utils import cpp_extension as cpp

    includes: list[str] = []
    seen: set[str] = set()
    for inc in _tvm_ffi_include_dirs() + _dlpack_include_dirs():
        if str(inc) not in seen:
            seen.add(str(inc))
            includes += ["-I", str(inc)]
    for inc in cpp.include_paths(device_type="cuda"):
        if str(inc) not in seen:
            seen.add(str(inc))
            includes += ["-I", str(inc)]

    link: list[str] = []
    torch_lib_dirs = cpp.library_paths(device_type="cuda")
    for lib_dir in torch_lib_dirs:
        link += [f"-L{lib_dir}", f"-Xlinker=-rpath,{lib_dir}"]
    link += ["-lc10", "-lc10_cuda", "-ltorch_cpu", "-ltorch_cuda", "-lcudart"]

    tvm_lib = _find_tvm_ffi_lib()
    if tvm_lib is not None:
        link += [
            f"-L{tvm_lib.parent}",
            f"-Xlinker=-rpath,{tvm_lib.parent}",
            f"-l:{tvm_lib.name}" if tvm_lib.name.startswith("lib") else str(tvm_lib),
        ]

    nvcc = os.environ.get("GNS_NVCC", "nvcc")
    return (
        [nvcc]
        + _NVCC_BASE_FLAGS
        + [_torch_abi_define()]
        + ["-gencode", f"arch=compute_{_CUDA_ARCH},code=sm_{_CUDA_ARCH}"]
        + includes
        + [str(KERNEL_CU), "-o", str(out_so)]
        + link
    )


def _try_tvm_ffi_cpp_load():
    """Prefer tvm_ffi's own builder when present (it owns the correct include
    set, DLPack headers, and ABI defines); fall back to the manual nvcc build
    otherwise. Both paths compile the same kernel.cu with the same -O3/-std/
    arch flags and no fast-math."""
    try:
        from tvm_ffi import cpp as tvm_cpp  # type: ignore
    except Exception:
        return None
    loader = getattr(tvm_cpp, "load", None)
    if not callable(loader):
        return None
    try:
        return loader(
            name="gns_candidate",
            sources=[str(KERNEL_CU)],
            extra_cuda_cflags=[
                "-O3",
                "-std=c++20",
                "--expt-relaxed-constexpr",
                "-lineinfo",
                "-gencode",
                f"arch=compute_{_CUDA_ARCH},code=sm_{_CUDA_ARCH}",
            ],
            build_directory=str(BUILD_ROOT / f"tvm_cpp_{_build_key()}"),
        )
    except TypeError:
        # Signature mismatch across tvm-ffi versions: retry with the minimal
        # call form before giving up on this path.
        try:
            return loader(str(KERNEL_CU))
        except Exception:
            return None
    except Exception:
        return None


def _build_key() -> str:
    payload = KERNEL_CU.read_bytes() + str(sorted(_NVCC_BASE_FLAGS)).encode() + _CUDA_ARCH.encode()
    payload += torch.__version__.encode()
    return hashlib.sha256(payload).hexdigest()[:12]


@functools.lru_cache(maxsize=1)
def _load_module():
    import tvm_ffi

    mod = None
    if os.environ.get("GNS_FORCE_NVCC", "") != "1":
        mod = _try_tvm_ffi_cpp_load()
    if mod is None:
        build_dir = BUILD_ROOT / _build_key()
        out_so = build_dir / "libgns_candidate.so"
        if not out_so.exists():
            build_dir.mkdir(parents=True, exist_ok=True)
            cmd = _build_command(out_so)
            log = build_dir / "build.log"
            with log.open("w") as fh:
                fh.write(" ".join(cmd) + "\n\n")
                fh.flush()
                proc = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT)
            if proc.returncode != 0:
                raise RuntimeError(
                    f"nvcc build failed (rc={proc.returncode}); see {log}\n"
                    + log.read_text()[-4000:]
                )
        mod = tvm_ffi.load_module(str(out_so))
    leaked = sorted(m for m in sys.modules if m == "sglang" or m.startswith("sglang."))
    if leaked:
        raise ImportError(f"purity violation in solution build: {leaked[:5]}")
    return mod


def _kernels():
    mod = _load_module()
    return (
        mod["gns_candidate_small"],
        mod["gns_candidate_large"],
        mod["gns_candidate_giant"],
        mod["gns_candidate_clean_giant"],
    )


def _normalized_3d(t: torch.Tensor) -> torch.Tensor:
    if t.dim() < 2:
        raise ValueError(f"expected >=2-D input, got {t.dim()}-D")
    batch, channels = t.shape[0], t.shape[1]
    return t.reshape(batch, channels, -1)


@functools.lru_cache(maxsize=256)
def _giant_chunk_for(spatial: int) -> int:
    """Pick the apply-kernel tile size for the giant path: the largest
    vector-aligned divisor of `spatial` not above the target (zero
    channel-straddling tiles). Falls back to the plain target when no divisor
    qualifies (the apply kernel handles straddles with vectorized two-segment
    tiles). Wave-cost-minimizing pickers were tried and measured slower on the
    large production shapes (the model underweights per-task overhead)."""
    target = GIANT_CHUNK_ELEMS
    k_min = -(-spatial // target)  # ceil: smallest task count per channel
    for k in range(k_min, min(4 * k_min, spatial) + 1):
        if spatial % k == 0 and (spatial // k) % 8 == 0:
            return spatial // k
    return target


# Self-cleaning arrival counters for the giant stats kernel's fused finalize
# (the last CTA of each row resets its slot to zero), cached per
# (device, stream): calls on one stream are ordered, so a stream-private
# buffer preserves the self-clean invariant, while concurrent calls on other
# streams of the same device get their own buffers and can never count each
# other's CTAs. The zeros-initialization launches on the same (current)
# stream the kernels run on, so first use is ordered too.
_row_counters: dict = {}


def _row_counter(num_rows: int, device: torch.device) -> torch.Tensor:
    stream = torch.cuda.current_stream(device)
    key = (device.type, device.index, stream.cuda_stream)
    buf = _row_counters.get(key)
    if buf is None or buf.numel() < num_rows:
        buf = torch.zeros(max(num_rows, 64), dtype=torch.int32, device=device)
        _row_counters[key] = buf
    return buf


def _fast_path_ok(x: torch.Tensor, weight: torch.Tensor, bias: torch.Tensor) -> bool:
    return (
        x.is_contiguous()
        and x.data_ptr() % 16 == 0
        and weight.is_contiguous()
        and bias.is_contiguous()
        and weight.data_ptr() % 16 == 0
        and bias.data_ptr() % 16 == 0
    )


def _run(x3: torch.Tensor, weight: torch.Tensor, bias: torch.Tensor, num_groups: int,
         eps: float, y3: torch.Tensor) -> None:
    # The FFI launchers run on the CURRENT device's stream
    # (at::cuda::getCurrentCUDAStream() on the C++ side); pin the device
    # context to the input's device so multi-GPU processes cannot launch on
    # the wrong card (mirrors the copied baseline's own device-context
    # behavior). Single-device callers see no behavior change.
    with torch.cuda.device(x3.device):
        _run_on_current_device(x3, weight, bias, num_groups, eps, y3)


def _run_on_current_device(x3: torch.Tensor, weight: torch.Tensor, bias: torch.Tensor,
                           num_groups: int, eps: float, y3: torch.Tensor) -> None:
    small, large, giant, clean_giant = _kernels()
    channels = x3.shape[1]
    spatial = x3.shape[2]
    group_size = (channels // num_groups) * spatial
    if group_size < LARGE_THRESHOLD:
        # The host launcher widens the block to 1024 threads for the
        # crossover band (>= 32K elements/group) where one CTA per group
        # otherwise starves per-SM memory parallelism.
        small(x3, weight, bias, int(num_groups), float(eps), y3)
        return
    num_rows = x3.shape[0] * num_groups
    # Clean-giant route: channel-aligned tiles, branch-free hoisted apply.
    clean_chunk = CLEAN_CHUNK_ELEMS or _giant_chunk_for(spatial)
    use_clean = (
        group_size >= GIANT_THRESHOLD
        and spatial >= clean_chunk
        and spatial % clean_chunk == 0
    )
    # The generic giant kernels assume a CTA tile never spans more than two
    # channels, which holds iff chunk <= spatial; shapes violating that stay
    # on the generic large path.
    use_giant = (
        not use_clean
        and group_size >= GIANT_THRESHOLD
        and spatial >= GIANT_CHUNK_ELEMS
    )
    device = x3.device
    if use_clean:
        stats_chunk = apply_chunk = clean_chunk
        total = num_rows * (group_size // clean_chunk)
    elif use_giant:
        # Scratch is keyed by the stats tiling (the apply kernel reads only
        # mean/rstd, so its tile size is independent).
        apply_chunk = _giant_chunk_for(spatial)
        stats_chunk = GIANT_STATS_CHUNK_ELEMS or apply_chunk
        stats_chunks_per_row = (group_size + stats_chunk - 1) // stats_chunk
        total = num_rows * stats_chunks_per_row
    else:
        chunk = CHUNK_ELEMS
        chunks_per_row = (group_size + chunk - 1) // chunk
        total = num_rows * chunks_per_row
    partial_sum = torch.empty(total, dtype=torch.float32, device=device)
    partial_sumsq = torch.empty(total, dtype=torch.float32, device=device)
    mean = torch.empty(num_rows, dtype=torch.float32, device=device)
    rstd = torch.empty(num_rows, dtype=torch.float32, device=device)
    if use_clean:
        clean_giant(x3, weight, bias, partial_sum, partial_sumsq, mean, rstd,
                    _row_counter(num_rows, device), int(num_groups), float(eps),
                    int(clean_chunk), y3)
    elif use_giant:
        giant(x3, weight, bias, partial_sum, partial_sumsq, mean, rstd,
              _row_counter(num_rows, device), int(num_groups), float(eps),
              int(stats_chunk), int(apply_chunk), y3)
    else:
        large(x3, weight, bias, partial_sum, partial_sumsq, mean, rstd, int(num_groups),
              float(eps), y3)


def group_norm_silu_candidate_into(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float,
    out: torch.Tensor,
) -> None:
    """Destination-passing entry (the benchmark ABI): writes into the
    caller-preallocated ``out``; never allocates an output tensor. Every
    regime runs solution-owned CUDA kernels."""
    if out.shape != x.shape or out.dtype != x.dtype:
        raise ValueError("out must match x in shape and dtype")
    if not (weight.device == x.device and bias.device == x.device and out.device == x.device):
        raise ValueError("x/weight/bias/out must live on the same CUDA device")
    if (
        _fast_path_ok(x, weight, bias)
        and out.is_contiguous()
        and out.data_ptr() % 16 == 0
    ):
        _run(_normalized_3d(x), weight, bias, num_groups, eps, _normalized_3d(out))
        return
    # Robust path for layouts no production row exhibits (non-contiguous
    # input, storage-offset-misaligned base, exotic out strides): normalize to
    # fresh contiguous 16B-aligned tensors, run the same solution-owned CUDA
    # kernels, and copy into the caller's buffer. Correctness-only path.
    xc = x.contiguous()
    if xc.data_ptr() % 16 != 0:
        xc = xc.clone()
    wc = weight.contiguous()
    if wc.data_ptr() % 16 != 0:
        wc = wc.clone()
    bc = bias.contiguous()
    if bc.data_ptr() % 16 != 0:
        bc = bc.clone()
    tmp = torch.empty(xc.shape, dtype=xc.dtype, device=xc.device)
    _run(_normalized_3d(xc), wc, bc, num_groups, eps, _normalized_3d(tmp))
    out.copy_(tmp.view(x.shape) if tmp.shape != x.shape else tmp)


def group_norm_silu_candidate(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float,
) -> torch.Tensor:
    """Allocate-and-return convenience entry over the same CUDA dispatch."""
    out = torch.empty_like(x)
    group_norm_silu_candidate_into(x, weight, bias, num_groups, eps, out)
    return out


__all__ = [
    "group_norm_silu_candidate",
    "group_norm_silu_candidate_into",
    "LARGE_THRESHOLD",
    "CHUNK_ELEMS",
]
