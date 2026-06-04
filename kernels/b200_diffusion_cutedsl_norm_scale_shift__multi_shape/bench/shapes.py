"""Captured workload signatures for the norm-scale-shift kernel family.

Parses ``docs/captured_shapes_b200.jsonl`` (the verbatim captured workload —
never derived or broadened) into canonical call signatures, deduplicates
identical signatures, and provides deterministic input builders shared by the
correctness and benchmark harnesses.

Run as a script to print the dedup summary and write
``docs/captured_shapes_unique.md`` (row -> unique-signature mapping).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

KERNEL_DIR = Path(__file__).resolve().parents[1]
CAPTURED_JSONL = KERNEL_DIR / "docs" / "captured_shapes_b200.jsonl"

NSS = "fused_norm_scale_shift"
SRNSS = "fused_scale_residual_norm_scale_shift"

# Positional tensor-slot names per entry point (trailing args: norm_type, eps).
ARG_NAMES = {
    NSS: ("x", "weight", "bias", "scale", "shift"),
    SRNSS: ("residual", "x", "gate", "weight", "bias", "scale", "shift"),
}

_DTYPE_ABBREV = {
    "torch.bfloat16": "bf16",
    "torch.float16": "fp16",
    "torch.float32": "fp32",
}


@dataclass(frozen=True)
class TensorSpec:
    shape: tuple
    dtype: str  # "torch.bfloat16" etc.

    @property
    def dtype_abbrev(self) -> str:
        return _DTYPE_ABBREV[self.dtype]

    def layout_code(self, B: int, S: int, D: int) -> str:
        """Compact index-mode code mirroring the SGLang test naming."""
        s = self.shape
        if len(s) == 1:
            return "1" if s[0] == 1 else "D"
        if len(s) == 2:
            return "1D" if s[0] == 1 else "BD"
        if len(s) == 3:
            if s == (B, S, D):
                return "BSD" if B > 1 else "1SD" if s[1] == S and S > 1 else "11D"
            if s[1] == 1:
                return "11D" if s[0] == 1 else "B1D"
            return "1SD"
        if len(s) == 4:
            return "BF1D"
        raise ValueError(f"unsupported spec shape {s}")


@dataclass(frozen=True)
class Signature:
    kernel: str  # NSS or SRNSS
    norm_type: str
    eps: float
    args: tuple  # tuple of Optional[TensorSpec], one per tensor slot

    @property
    def x_spec(self) -> TensorSpec:
        idx = 0 if self.kernel == NSS else 1
        return self.args[idx]

    @property
    def BSD(self) -> tuple:
        return tuple(self.x_spec.shape)

    def operand(self, name: str) -> Optional[TensorSpec]:
        return self.args[ARG_NAMES[self.kernel].index(name)]

    def make_id(self) -> str:
        B, S, D = self.BSD
        abbrev = "nss" if self.kernel == NSS else "srnss"
        parts = [abbrev, f"b{B}", f"s{S}", f"d{D}", self.x_spec.dtype_abbrev]
        for nm in ("gate", "weight", "scale", "shift"):
            if nm not in ARG_NAMES[self.kernel]:
                continue
            spec = self.operand(nm)
            if spec is None:
                if nm == "gate":
                    parts.append("gnone")
                continue
            code = spec.layout_code(B, S, D)
            parts.append(f"{nm[0]}{code}.{spec.dtype_abbrev}")
        parts.append(f"eps{self.eps:g}")
        return "-".join(parts)


@dataclass
class UniqueCase:
    sig: Signature
    case_id: str
    rows: list = field(default_factory=list)  # (jsonl line no, model, call_idx)

    @property
    def models(self) -> list:
        return sorted({m for _, m, _ in self.rows})


def _parse_record(line_no: int, rec: dict):
    kernel = rec["kernel"].split(".")[-1]
    if kernel not in ARG_NAMES:
        raise ValueError(f"line {line_no}: unknown kernel {rec['kernel']}")
    raw_args = rec["args"]
    n_slots = len(ARG_NAMES[kernel])
    tensor_args = raw_args[:n_slots]
    norm_type, eps = raw_args[n_slots], float(raw_args[n_slots + 1])
    specs = tuple(
        TensorSpec(tuple(a["shape"]), a["dtype"]) if a is not None else None
        for a in tensor_args
    )
    sig = Signature(kernel=kernel, norm_type=norm_type, eps=eps, args=specs)
    return sig, rec.get("model", "?"), rec.get("call_idx", -1)


def load_unique_cases(jsonl_path: Path = CAPTURED_JSONL):
    """Return (unique_cases ordered by first appearance, total_row_count)."""
    uniques: dict = {}
    order = []
    total = 0
    with jsonl_path.open() as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            total += 1
            sig, model, call_idx = _parse_record(line_no, json.loads(line))
            if sig not in uniques:
                case = UniqueCase(sig=sig, case_id=sig.make_id())
                uniques[sig] = case
                order.append(case)
            uniques[sig].rows.append((line_no, model, call_idx))
    ids = [c.case_id for c in order]
    assert len(ids) == len(set(ids)), "case id collision"
    return order, total


# ---------------------------------------------------------------------------
# Deterministic input construction (shared by parity/correctness/benchmark)
# ---------------------------------------------------------------------------


def _torch_dtype(name: str):
    import torch

    return {
        "torch.bfloat16": torch.bfloat16,
        "torch.float16": torch.float16,
        "torch.float32": torch.float32,
    }[name]


def build_inputs(case: UniqueCase, device: str = "cuda", seed: int = 1234):
    """Materialize deterministic inputs for one unique case.

    Returns (args_list, kwargs) matching the entry point's positional order
    (tensor slots filled, then norm_type, then eps). Values are generated in
    fp32 from a seeded generator and cast to the captured dtype; identical
    (torch version, GPU, seed) yields identical tensors across processes.
    """
    import torch

    gen = torch.Generator(device=device)
    sig = case.sig
    names = ARG_NAMES[sig.kernel]
    out = []
    for idx, (name, spec) in enumerate(zip(names, sig.args)):
        if spec is None:
            out.append(None)
            continue
        gen.manual_seed((seed * 1000003 + idx * 9176 + len(case.case_id)) % (2**31))
        base = torch.randn(spec.shape, generator=gen, device=device, dtype=torch.float32)
        if name in ("scale", "shift", "gate"):
            base = base * 0.5
        elif name in ("weight",):
            base = base * 0.25 + 1.0
        elif name in ("bias",):
            base = base * 0.25
        out.append(base.to(_torch_dtype(spec.dtype)))
    return out, sig.norm_type, sig.eps


def write_mapping_doc(path: Path = KERNEL_DIR / "docs" / "captured_shapes_unique.md"):
    cases, total = load_unique_cases()
    lines = [
        "# Unique captured signatures (dedup mapping)",
        "",
        f"Source: `docs/captured_shapes_b200.jsonl` ({total} rows). "
        f"{len(cases)} unique call signatures (geomean basis per DEC-1).",
        "",
        "| # | Case ID | Kernel | norm/eps | Models | JSONL rows |",
        "|---|---------|--------|----------|--------|------------|",
    ]
    for i, c in enumerate(cases, start=1):
        rows = ", ".join(str(ln) for ln, _, _ in c.rows)
        lines.append(
            f"| {i} | `{c.case_id}` | {c.sig.kernel} | {c.sig.norm_type}/{c.sig.eps:g} "
            f"| {', '.join(c.models)} | {rows} |"
        )
    lines.append("")
    path.write_text("\n".join(lines))
    return cases, total


if __name__ == "__main__":
    cases, total = write_mapping_doc()
    print(f"{total} captured rows -> {len(cases)} unique signatures")
    for c in cases:
        print(f"  {c.case_id}  (rows: {[ln for ln, _, _ in c.rows]})")
