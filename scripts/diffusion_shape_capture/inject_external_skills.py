"""Inject the `## External Reference Skills` section into every diffusion
task prompt, plus a `## Implementation Language Policy` section that mandates
native CUDA C++/.cu candidates regardless of the baseline language.

KernelWiki and ncu-report-skill are described as **suggestions** the agent
queries autonomously based on judgement, not as gated reflex actions.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parent
KERNELS_DIR = REPO / "kernels"

ANCHOR_END = "## Optimization Exploration Policy"
SECTION_HEADER = "## External Reference Skills"
LANG_HEADER = "## Implementation Language Policy"

# Per-family KernelWiki query suggestions.
KW_QUERIES: dict[str, list[str]] = {
    "qknorm_rope": [
        'python3 ../../external/KernelWiki/scripts/query.py "fused RMS norm + RoPE inplace sm100"',
        'python3 ../../external/KernelWiki/scripts/query.py "qk norm rope blackwell"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag qk-norm --type kernel',
        'python3 ../../external/KernelWiki/scripts/query.py --repo sglang --tag rope --architecture sm100 --limit 20',
        'python3 ../../external/KernelWiki/scripts/query.py --repo flashinfer --tag rope --limit 20',
    ],
    "norm_infer": [
        'python3 ../../external/KernelWiki/scripts/query.py "layer norm 2-pass inference sm100"',
        'python3 ../../external/KernelWiki/scripts/query.py "one pass rmsnorm tiled per head"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag rms-norm --architecture sm100 --limit 20',
        'python3 ../../external/KernelWiki/scripts/query.py --tag layer-norm --architecture sm100 --limit 20',
    ],
    "group_norm_silu": [
        'python3 ../../external/KernelWiki/scripts/query.py "group norm silu fused vae blackwell"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag group-norm --type kernel',
        'python3 ../../external/KernelWiki/scripts/query.py --repo pytorch --tag group-norm --limit 20',
        'python3 ../../external/KernelWiki/scripts/query.py --symptom memory-bound --tag norm --limit 20',
    ],
    "rotary_embedding": [
        'python3 ../../external/KernelWiki/scripts/query.py "rope interleaved neox sm100"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag rope --type kernel',
        'python3 ../../external/KernelWiki/scripts/query.py --tag rope --architecture sm100 --limit 20',
        'python3 ../../external/KernelWiki/scripts/query.py --repo flashinfer --tag rope --limit 20',
    ],
    "fuse_scale_shift": [
        'python3 ../../external/KernelWiki/scripts/query.py "adaLN modulation fused scale shift gate"',
        'python3 ../../external/KernelWiki/scripts/query.py "DiT modulation kernel sm100"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag modulation --type kernel',
        'python3 ../../external/KernelWiki/scripts/query.py --repo sglang --tag modulation --limit 20',
    ],
    "cutedsl_norm_tanh_mul_add": [
        'python3 ../../external/KernelWiki/scripts/query.py "CuTe DSL layer norm modulation sm100"',
        'python3 ../../external/KernelWiki/scripts/query.py "Z-Image residual modulation kernel"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag cute-dsl --type kernel',
        'python3 ../../external/KernelWiki/scripts/query.py --tag modulation --architecture sm100 --limit 20',
    ],
    "cutedsl_norm_scale_shift": [
        'python3 ../../external/KernelWiki/scripts/query.py "CuTe DSL norm scale shift fused"',
        'python3 ../../external/KernelWiki/scripts/query.py "fused norm residual gate adaLN"',
        'python3 ../../external/KernelWiki/scripts/query.py --tag cute-dsl --type kernel',
        'python3 ../../external/KernelWiki/scripts/query.py --tag modulation --architecture sm100 --limit 20',
    ],
}

FAMILY_BLURB: dict[str, str] = {
    "qknorm_rope": "fused in-place RMS-norm + RoPE on (Q, K) for DiT joint attention blocks",
    "norm_infer": "inference-only 2-pass LayerNorm / RMSNorm and tiled one-pass RMSNorm baselines",
    "group_norm_silu": "fused GroupNorm + SiLU used by image (2D/3D) and video (5D) VAE decoders",
    "rotary_embedding": "standard apply_rotary_embedding plus the LTX-2 split-RoPE variant with 4D cos/sin",
    "fuse_scale_shift": "fused scale-shift modulation including the Z-Image / Qwen-Image-Edit `select01` dual-modulation path",
    "cutedsl_norm_tanh_mul_add": "Z-Image residual modulation `norm(x) * tanh(scale) + shift` (with the second-norm-scale variant)",
    "cutedsl_norm_scale_shift": "fused `norm(x) * (1 + scale) + shift` and its residual+gate variant used by Qwen-Image / Wan / HunyuanVideo / Helios",
}


def render_lang_section() -> str:
    return (
        f"{LANG_HEADER}\n"
        f"\n"
        f"**The optimized candidate must be a native CUDA kernel built from\n"
        f"workspace-owned `.cu` / `.cuh` / `.cpp` / `.h` sources compiled with\n"
        f"`nvcc` (via a CUDA extension build or torch JIT), regardless of\n"
        f"whether the SGLang baseline is CUDA, Triton, or CuTe-DSL.** Python\n"
        f"is allowed for the wrapper, the dispatcher, build glue, harnesses,\n"
        f"and benchmark scripts, but not as the primary kernel.\n"
        f"\n"
        f"The SGLang baseline — whatever language it is written in — is a\n"
        f"first-class **reference** for the CUDA candidate. Read its tile and\n"
        f"block choices, vectorization width, fast paths, fusion patterns,\n"
        f"numerical-stability tricks, dispatcher shape guards, and dtype\n"
        f"handling; the CUDA candidate is free to port any of those ideas\n"
        f"directly, replace them with a better algorithm, or mix them with\n"
        f"ideas pulled from KernelWiki PRs, CUTLASS / CuTe SM100 examples,\n"
        f"FlashAttention-4, DeepGEMM, FlashMLA, FlashInfer, or Hopper →\n"
        f"Blackwell migration notes. The baseline is one reference among\n"
        f"many — not a ceiling and not a required porting target. Record\n"
        f"every source whose idea ended up in the candidate in\n"
        f"`solutions.jsonl` with its file path / PR url / wiki page id.\n"
        f"\n"
        f"After promotion, the export tool copies the CUDA sources into\n"
        f"`kda_kernels/diffusion/<family>/` so the shippable overlay stays\n"
        f"CUDA-only end-to-end. See the `## Promotion: Export Into\n"
        f"kda_kernels` section below for the export contract.\n"
    )


def render_external_section(family: str) -> str:
    queries = KW_QUERIES[family]
    blurb = FAMILY_BLURB[family]
    bullets = "\n".join(f"  - `{q}`" for q in queries)
    harness_note = (
        "Build the harness from your `src/` `.cu` / `.cuh` sources with\n"
        "  `-lineinfo` so SASS maps back to source. Match the exact captured\n"
        "  shape from `docs/captured_shapes_<arch>.jsonl` for the slice you\n"
        "  are profiling."
    )
    return (
        f"{SECTION_HEADER}\n"
        f"\n"
        f"Two repo-vendored skills live under `../../external/` (they are git\n"
        f"submodules; if either folder is empty, run\n"
        f"`git submodule update --init --recursive` from the repo root before\n"
        f"starting RLCR).\n"
        f"\n"
        f"### KernelWiki (`../../external/KernelWiki/`)\n"
        f"\n"
        f"Searchable knowledge base of 2,179 merged PRs across CUTLASS, SGLang,\n"
        f"vLLM, FlashInfer, PyTorch, Triton (Blackwell / SM100 + Hopper / SM90),\n"
        f"plus 48 wiki pages, 7 competitions, and 20 blog summaries. Read\n"
        f"`../../external/KernelWiki/SKILL.md` first for the full query syntax.\n"
        f"\n"
        f"Treat KernelWiki as a **reference the agent consults at its own\n"
        f"discretion** — when designing the first candidate, when choosing\n"
        f"between two implementation directions, after any focused attempt\n"
        f"comes back slower than the SGLang baseline, when an ncu profile\n"
        f"surfaces a stall the playbook can't fully explain, or any time a\n"
        f"prior-art PR would unblock the next edit. The wiki is never\n"
        f"mandatory; skip it when the candidate direction is obvious and the\n"
        f"profiler evidence is clean.\n"
        f"\n"
        f"Suggested targeted queries for this kernel family ({blurb}):\n"
        f"\n"
        f"{bullets}\n"
        f"\n"
        f"Record any PR / wiki page that influenced a design decision in\n"
        f"`docs/draft.md` and `solutions.jsonl` with its KernelWiki page id\n"
        f"or upstream PR URL.\n"
        f"\n"
        f"### ncu-report-skill (`../../external/ncu-report-skill/`)\n"
        f"\n"
        f"Nsight Compute B200 / SM100 workflow. Read\n"
        f"`../../external/ncu-report-skill/SKILL.md` first; the\n"
        f"`reference/` subdirectory has the directory layout, harness guide,\n"
        f"collection options, Python API, six analysis dimensions, diagnosis\n"
        f"playbook, and report template.\n"
        f"\n"
        f"Profile **whenever profiler evidence would change the next edit** —\n"
        f"that is, after any benchmark result you do not fully understand,\n"
        f"whether the candidate got *faster* or *slower* than the baseline.\n"
        f"A speedup that comes from an unexpected dimension is just as worth\n"
        f"diagnosing as a regression: the active hardware bound from the\n"
        f"winning candidate tells you the next direction, and the bound from\n"
        f"a losing candidate tells you why the attempted edit didn't pay off.\n"
        f"Skip ncu only when both the result and the cause are already\n"
        f"obvious from code review or microbenchmark.\n"
        f"\n"
        f"The mandatory pattern in this repo when you do profile:\n"
        f"\n"
        f"  1. Create `profile/<run_name>/{{harness,reports,analysis}}/` — one\n"
        f"     dir per run, never reuse.\n"
        f"  2. Build a standalone harness under `profile/<run_name>/harness/`.\n"
        f"     {harness_note}\n"
        f"  3. Run two profiles into `profile/<run_name>/reports/`:\n"
        f"\n"
        f"     ```bash\n"
        f"     ncu --set full --target-processes all \\\n"
        f"       -o profile/<run_name>/reports/full \\\n"
        f"       <harness binary or python entrypoint>\n"
        f"\n"
        f"     ncu --set source --section SourceCounters \\\n"
        f"       -o profile/<run_name>/reports/source \\\n"
        f"       <harness binary or python entrypoint>\n"
        f"     ```\n"
        f"\n"
        f"  4. Parse with the `ncu_report` Python module via the helpers in\n"
        f"     `../../external/ncu-report-skill/helpers/`; write parsed CSVs\n"
        f"     into `profile/<run_name>/analysis/`.\n"
        f"  5. Walk the six analysis dimensions (compute / memory / occupancy\n"
        f"     / latency-hiding / launch-overhead / tail-effect) listed in\n"
        f"     `../../external/ncu-report-skill/reference/05-analysis-dimensions.md`.\n"
        f"  6. Match the dominant signal to\n"
        f"     `../../external/ncu-report-skill/reference/06-diagnosis-playbook.md`\n"
        f"     and write `profile/<run_name>/REPORT.md` using\n"
        f"     `reference/07-report-template.md`.\n"
        f"\n"
        f"Record the matched diagnosis, before/after metric, and the resulting\n"
        f"design change in `solutions.jsonl` together with the report path.\n"
        f"\n"
    )


def patch_one(prompt_path: Path, family: str) -> None:
    text = prompt_path.read_text(encoding="utf-8")

    # 1. Drop / replace any existing External Reference Skills section.
    ext_section = render_external_section(family)
    if SECTION_HEADER in text:
        start = text.index(SECTION_HEADER)
        rest = text[start:]
        next_header_idx = rest.find("\n## ", len(SECTION_HEADER))
        if next_header_idx == -1:
            text = text[:start] + ext_section.rstrip() + "\n"
        else:
            text = text[:start] + ext_section.rstrip() + "\n\n" + rest[next_header_idx + 1 :]
    else:
        anchor_idx = text.find(ANCHOR_END)
        if anchor_idx == -1:
            text = text.rstrip() + "\n\n" + ext_section.rstrip() + "\n"
        else:
            text = (
                text[:anchor_idx].rstrip()
                + "\n\n"
                + ext_section.rstrip()
                + "\n\n"
                + text[anchor_idx:]
            )

    # 2. Drop / replace any existing Implementation Language Policy section.
    lang_section = render_lang_section()
    if LANG_HEADER in text:
        start = text.index(LANG_HEADER)
        rest = text[start:]
        next_header_idx = rest.find("\n## ", len(LANG_HEADER))
        if next_header_idx == -1:
            text = text[:start] + lang_section.rstrip() + "\n"
        else:
            text = text[:start] + lang_section.rstrip() + "\n\n" + rest[next_header_idx + 1 :]
    else:
        # Insert the language section just above External Reference Skills.
        ext_idx = text.find(SECTION_HEADER)
        if ext_idx == -1:
            text = text.rstrip() + "\n\n" + lang_section.rstrip() + "\n"
        else:
            text = (
                text[:ext_idx].rstrip()
                + "\n\n"
                + lang_section.rstrip()
                + "\n\n"
                + text[ext_idx:]
            )

    prompt_path.write_text(text, encoding="utf-8")


def family_of(task_name: str) -> str:
    if not task_name.startswith(("b200_diffusion_", "h200_diffusion_")):
        return ""
    stripped = task_name.split("_diffusion_", 1)[1]
    return stripped.split("__multi_shape", 1)[0]


def main() -> None:
    for task_dir in sorted(KERNELS_DIR.iterdir()):
        if not task_dir.is_dir():
            continue
        family = family_of(task_dir.name)
        if family not in KW_QUERIES:
            continue
        prompt = task_dir / "prompt.md"
        if not prompt.exists():
            continue
        patch_one(prompt, family)
        print(f"patched {task_dir.name}")


if __name__ == "__main__":
    main()
