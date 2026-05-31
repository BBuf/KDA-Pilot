"""Inject a `## Promotion: Export Into kda_kernels` section into every
diffusion task prompt so the agent ends the RLCR loop by running
`scripts/export_kda_kernels/export.py <task-slug>` and surfacing the
required `src/register.py` EXPORTS dict shape.

The section lands right before `## Completion Bar` and replaces itself
idempotently on rerun.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parent
KERNELS_DIR = REPO / "kernels"

ANCHOR = "## Completion Bar"
SECTION_HEADER = "## Promotion: Export Into kda_kernels"

FAMILY_TO_FUNCTIONS: dict[str, list[str]] = {
    "qknorm_rope": ["fused_inplace_qknorm_rope"],
    "norm_infer": ["norm_infer", "triton_one_pass_rms_norm"],
    "group_norm_silu": ["triton_group_norm_silu", "apply_group_norm_silu"],
    "rotary_embedding": ["apply_rotary_embedding", "apply_ltx2_split_rotary_emb"],
    "fuse_scale_shift": [
        "fuse_scale_shift_kernel",
        "fuse_layernorm_scale_shift_gate_select01_kernel",
        "fuse_residual_layernorm_scale_shift_gate_select01_kernel",
    ],
    "cutedsl_norm_tanh_mul_add": [
        "fused_norm_tanh_mul_add",
        "fused_norm_tanh_mul_add_norm_scale",
    ],
    "cutedsl_norm_scale_shift": [
        "fused_norm_scale_shift",
        "fused_scale_residual_norm_scale_shift",
    ],
}


def family_of(task_name: str) -> str:
    if not task_name.startswith(("b200_diffusion_", "h200_diffusion_")):
        return ""
    stripped = task_name.split("_diffusion_", 1)[1]
    return stripped.split("__multi_shape", 1)[0]


def render_section(slug: str, family: str) -> str:
    fns = FAMILY_TO_FUNCTIONS[family]
    exports_block = "\n".join(f'        "{fn}": {fn},' for fn in fns)
    intro_funcs = ", ".join(f"`{fn}`" for fn in fns)
    return (
        f"{SECTION_HEADER}\n"
        f"\n"
        f"When the candidate is correct on every configured shape, beats the\n"
        f"promotion bar, and the dispatcher decision table is recorded, run\n"
        f"the export tool to promote the optimized wrapper into the\n"
        f"shippable `kda_kernels/` overlay:\n"
        f"\n"
        f"```bash\n"
        f"python3 scripts/export_kda_kernels/export.py {slug}\n"
        f"```\n"
        f"\n"
        f"That copies this task's `src/` into\n"
        f"`kda_kernels/_impls/{slug}/`, rewires the matching\n"
        f"kda_kernels stub for {intro_funcs} to import from there, and flips\n"
        f"`KDA_OPTIMIZED_<fn> = True` on each listed function.\n"
        f"\n"
        f"For the export to know which functions to promote, `src/register.py`\n"
        f"must expose an `EXPORTS` dict alongside the existing `register()` /\n"
        f"`optimized_wrapper()` entries:\n"
        f"\n"
        f"```python\n"
        f"# kernels/{slug}/src/register.py\n"
        f"\n"
        f"# ... optimized implementations of the wrapped functions live here ...\n"
        f"\n"
        f"EXPORTS = {{\n"
        f"{exports_block}\n"
        f"}}\n"
        f"```\n"
        f"\n"
        f"Functions not present in `EXPORTS` keep their kda_kernels stub on\n"
        f"the SGLang baseline. Partial promotion is safe; rerun export.py\n"
        f"after each additional function is ready, or run\n"
        f"`scripts/export_kda_kernels/export.py --revert {slug}` to roll back.\n"
        f"\n"
        f"After export, end-to-end activation inside an sglang checkout is:\n"
        f"\n"
        f"```bash\n"
        f"export PYTHONPATH=/path/to/kernel-pilot:$PYTHONPATH\n"
        f"cd /path/to/sglang\n"
        f"git apply /path/to/kernel-pilot/patches/sglang_kda_kernels.patch\n"
        f"python3 -c 'import sglang; import kda_kernels; print(kda_kernels.status())'\n"
        f"```\n"
        f"\n"
        f"and `kda_kernels.uninstall()` restores the SGLang baseline at runtime\n"
        f"without touching the patch.\n"
        f"\n"
        f"See `kda_kernels/README.md`, `patches/README.md`, and\n"
        f"`scripts/export_kda_kernels/README.md` for the full contract.\n"
    )


def patch_one(prompt_path: Path, family: str, slug: str) -> None:
    text = prompt_path.read_text(encoding="utf-8")
    section = render_section(slug, family)

    if SECTION_HEADER in text:
        start = text.index(SECTION_HEADER)
        rest = text[start:]
        next_header_idx = rest.find("\n## ", len(SECTION_HEADER))
        if next_header_idx == -1:
            new_text = text[:start] + section.rstrip() + "\n"
        else:
            new_text = text[:start] + section.rstrip() + "\n\n" + rest[next_header_idx + 1 :]
    else:
        anchor_idx = text.find(ANCHOR)
        if anchor_idx == -1:
            new_text = text.rstrip() + "\n\n" + section.rstrip() + "\n"
        else:
            new_text = (
                text[:anchor_idx].rstrip()
                + "\n\n"
                + section.rstrip()
                + "\n\n"
                + text[anchor_idx:]
            )
    prompt_path.write_text(new_text, encoding="utf-8")


def main() -> None:
    for task_dir in sorted(KERNELS_DIR.iterdir()):
        if not task_dir.is_dir():
            continue
        family = family_of(task_dir.name)
        if family not in FAMILY_TO_FUNCTIONS:
            continue
        prompt = task_dir / "prompt.md"
        if not prompt.exists():
            continue
        patch_one(prompt, family, task_dir.name)
        print(f"patched {task_dir.name}")


if __name__ == "__main__":
    main()
