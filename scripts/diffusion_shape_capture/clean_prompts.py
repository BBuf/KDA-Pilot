"""Clean inconsistent leading whitespace in the auto-generated prompt.md files.

Each line in the prompt was generated via textwrap.dedent with embedded
substitutions of multi-line variables that already used leading whitespace.
Strip leading whitespace from every line that isn't inside a fenced code
block, so the markdown renders cleanly.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
KERNELS_DIR = REPO_ROOT / "kernels"

FAMILIES = [
    "diffusion_qknorm_rope__multi_shape",
    "diffusion_norm_infer__multi_shape",
    "diffusion_group_norm_silu__multi_shape",
    "diffusion_rotary_embedding__multi_shape",
    "diffusion_fuse_scale_shift__multi_shape",
    "diffusion_cutedsl_norm_tanh_mul_add__multi_shape",
    "diffusion_cutedsl_norm_scale_shift__multi_shape",
]
ARCHS = ["b200", "h200"]


def clean_md(text: str) -> str:
    out_lines = []
    in_code = False
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if stripped.startswith("```"):
            in_code = not in_code
            # Code-block fences themselves get unindented to column 0.
            out_lines.append(stripped)
            continue
        if in_code:
            # Inside a code block, keep the indentation relative to the
            # first column of code (strip up to 8 leading spaces).
            if raw.startswith("        "):
                out_lines.append(raw[8:])
            elif raw.startswith("    "):
                out_lines.append(raw[4:])
            else:
                out_lines.append(raw)
            continue
        # Markdown body — strip leading whitespace entirely.
        out_lines.append(stripped)
    cleaned = "\n".join(out_lines)
    # Trim trailing whitespace per line.
    cleaned = "\n".join(line.rstrip() for line in cleaned.splitlines())
    if not cleaned.endswith("\n"):
        cleaned += "\n"
    return cleaned


def main() -> None:
    for family in FAMILIES:
        for arch in ARCHS:
            slug = f"{arch}_{family}"
            for name in ("prompt.md", "interface.md", "README.md"):
                p = KERNELS_DIR / slug / name
                if not p.exists():
                    continue
                p.write_text(clean_md(p.read_text()))
            print(f"cleaned {slug}")


if __name__ == "__main__":
    main()
