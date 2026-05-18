#!/usr/bin/env python3
"""Audit materialized PR bundles for real CUDA/Triton/CuTe kernel relevance."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from _knowledge_root import knowledge_root


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
DIFF_FILE_RE = re.compile(r"^diff --git a/(.*?) b/(.*?)$", re.M)

DIRECT_SUFFIXES = {
    ".cu",
    ".cuh",
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
    ".inl",
    ".inc",
    ".ptx",
    ".py",
    ".pyi",
}

DOC_SUFFIXES = {".md", ".rst", ".txt", ".adoc", ".ipynb"}
CONFIG_SUFFIXES = {
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".lock",
    ".bazel",
    ".cmake",
    ".sh",
}

KERNEL_PATH_RE = re.compile(
    r"(^|/)(csrc|cuda|cutlass|cute|cutedsl|cute_dsl|cute_dsl_kernels|triton|tritongpu|"
    r"tilelang|tile_kernels|tilekernels|quack|cub|thrust|libcudacxx|kernel|kernels|"
    r"jit_kernels|jit|fmha|attention|flash_attn|flashinfer|prefill|decode|sampling|"
    r"moe|gemm|matmul|quant|quantization|deep_gemm|inductor|aoti|aten/src/aten/native/cuda|"
    r"analysis|conversion|dialect|dispatch|tuning|scheduler|heuristics?|collective|mainloop|epilogue|"
    r"benchmarks?|microbenchmarks?|profiler)(/|$)",
    re.I,
)
PURE_META_PATH_RE = re.compile(
    r"(^|/)(docs?|doc|readme|\.github|ci|docker|build|cmake|packaging|"
    r"website|examples/docs?)(/|$)|(^|/)README(\.[^/]*)?$",
    re.I,
)
TEST_PATH_RE = re.compile(r"(^|/)(tests?|unit_tests?|integration_tests?)(/|$)|(^|/)test[_-]", re.I)
BENCH_PATH_RE = re.compile(r"(^|/)(benchmarks?|microbenchmarks?|perf|profiles?|profiler)(/|$)|bench|benchmark|ncu|nsight", re.I)
KERNEL_PATH_TOKEN_RE = re.compile(
    r"(cuda|cutlass|cute[_-]?dsl|cutedsl|triton[_-]?kernels?|flashinfer|flash[_-]?attn|"
    r"deep[_-]?gemm|tvm[_-]?binding|trtllm[_-]?gen|custom[_-]?ops|fused[_-]?moe|"
    r"rms[_-]?norm|attention[_-]?backend|mla|dsa|matmul|gemm|fmha|decode|prefill|"
    r"sampling|quant|fp8|fp4|nvfp4|mxfp4|blackwell|hopper|sm90|sm100|topk)",
    re.I,
)
NON_CUDA_PATH_RE = re.compile(
    r"(^|/)(third_party|3rdparty)/amd(/|$)|tritonamdgpu|gfx\d+|(^|/)system/omp(/|$)",
    re.I,
)

KERNEL_TEXT_RE = re.compile(
    r"(__global__|__device__|__launch_bounds__|cuda|cublas|cudnn|cutlass|cute|"
    r"cute[_-]?dsl|cutedsl|triton|tritongpu|tl\.|@triton\.jit|tilelang|tcgen05|wgmma|"
    r"mma|tma|tmem|mbarrier|cp\.async|ldmatrix|nvfp4|mxfp4|fp4|fp8|bf16|int8|"
    r"int4|ptx|inline.?asm|flash.?attention|attention|fmha|paged.?kv|decode|prefill|sampling|moe|"
    r"grouped.?gemm|gemm|matmul|epilogue|mainloop|collective|warp|warpgroup|"
    r"block.?scale|swizzle|persistent|autotun|occupancy|register|shared memory|"
    r"sm90|sm100|blackwell|hopper|b200|h100|vectori[sz]ed|scan|reduce|reduction|"
    r"blockload|block.?load|thread.?reduce|device.?transform|topk|policy|policies|"
    r"tuning|scheduler|heuristic|raster|2cta|pdl|tma\.red|torch\.ops|"
    r"torch\.library|custom.?op|inductor|aotinductor|pallas)",
    re.I,
)
OPT_TEXT_RE = re.compile(
    r"(speed|latency|throughput|tflops?|gb/s|perf|performance|optimi[sz]|faster|"
    r"benchmark|profile|ncu|nsight|occupancy|bandwidth|reg(ister)? pressure|"
    r"stall|pipeline|tile|schedule|autotun|fusion|fused|regression|tune|tuning|"
    r"vectori[sz]ed|heuristic|policy|policies|persistent|swizzle|raster)",
    re.I,
)

GPU_CODE_SUFFIXES = {
    ".cu",
    ".cuh",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
    ".inl",
    ".inc",
    ".ptx",
}


@dataclass
class AuditResult:
    repo_id: str
    number: int
    keep: bool
    reason: str
    title: str
    source_page: str | None
    bundle: str
    changed_paths: list[str]
    direct_paths: list[str]
    bench_paths: list[str]
    test_paths: list[str]
    doc_or_meta_paths: list[str]
    kernel_text_hits: int
    opt_text_hits: int


def parse_page(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    return yaml.safe_load(match.group(1)) or {}


def source_page_for(root: Path, repo_id: str, number: int) -> Path:
    return root / "sources" / "prs" / repo_id / f"PR-{number}.md"


def changed_paths_from_diff(diff_text: str) -> list[str]:
    paths: list[str] = []
    seen: set[str] = set()
    for match in DIFF_FILE_RE.finditer(diff_text):
        path = match.group(2)
        if path == "/dev/null":
            path = match.group(1)
        if path not in seen:
            paths.append(path)
            seen.add(path)
    return paths


def changed_lines(diff_text: str) -> str:
    lines = []
    for line in diff_text.splitlines():
        if line.startswith(("+++", "---", "@@", "diff --git", "index ", "new file", "deleted file")):
            continue
        if line.startswith(("+", "-")):
            lines.append(line[1:])
    return "\n".join(lines)


def is_doc_or_meta(path: str) -> bool:
    p = Path(path)
    lower = path.lower()
    if p.suffix.lower() in DOC_SUFFIXES:
        return True
    if PURE_META_PATH_RE.search(path):
        return True
    if p.suffix.lower() in CONFIG_SUFFIXES and not KERNEL_PATH_RE.search(path):
        return True
    return any(
        token in lower
        for token in (
            "requirements",
            "setup.py",
            "pyproject.toml",
            "package.json",
            "pnpm-lock",
            "license",
            "changelog",
            "maintainer",
        )
    )


def direct_relevant_path(path: str, evidence_text: str) -> bool:
    suffix = Path(path).suffix.lower()
    if suffix not in DIRECT_SUFFIXES:
        return False
    if is_doc_or_meta(path):
        return False
    if NON_CUDA_PATH_RE.search(path):
        return False
    if TEST_PATH_RE.search(path) and not BENCH_PATH_RE.search(path):
        return False

    kernelish_path = bool(KERNEL_PATH_RE.search(path) or KERNEL_PATH_TOKEN_RE.search(path))
    kernelish_text = bool(KERNEL_TEXT_RE.search(evidence_text))
    optimization_text = bool(OPT_TEXT_RE.search(evidence_text))

    if suffix in {".py", ".pyi"}:
        return bool(kernelish_path and (kernelish_text or optimization_text))
    if suffix in GPU_CODE_SUFFIXES and kernelish_path:
        return bool(kernelish_text or optimization_text)
    return bool(kernelish_text and optimization_text)


def bench_relevant_path(path: str, evidence_text: str) -> bool:
    suffix = Path(path).suffix.lower()
    if is_doc_or_meta(path):
        return False
    if NON_CUDA_PATH_RE.search(path):
        return False
    return bool(BENCH_PATH_RE.search(path) and suffix in DIRECT_SUFFIXES and KERNEL_TEXT_RE.search(evidence_text))


def audit_bundle(root: Path, bundle: Path) -> AuditResult:
    repo_id = bundle.parent.name
    number = int(bundle.name.removeprefix("gh-"))
    source = source_page_for(root, repo_id, number)
    meta = parse_page(source) if source.exists() else {}
    diff_path = bundle / "review.diff"
    diff_text = diff_path.read_text(encoding="utf-8", errors="replace") if diff_path.exists() else ""
    paths = changed_paths_from_diff(diff_text)
    body = changed_lines(diff_text)
    title = str(meta.get("title") or "")
    evidence_text = "\n".join([title, "\n".join(paths), body])

    direct = [path for path in paths if direct_relevant_path(path, evidence_text)]
    bench = [path for path in paths if bench_relevant_path(path, evidence_text)]
    tests = [path for path in paths if TEST_PATH_RE.search(path)]
    docs = [path for path in paths if is_doc_or_meta(path)]
    kernel_hits = len(KERNEL_TEXT_RE.findall(evidence_text))
    opt_hits = len(OPT_TEXT_RE.findall(evidence_text))

    if not paths:
        keep = False
        reason = "empty-or-unparseable-diff"
    elif direct:
        keep = True
        reason = "direct-kernel-or-dsl-diff"
    elif bench and opt_hits:
        keep = True
        reason = "kernel-benchmark-or-profile-diff"
    elif len(docs) == len(paths):
        keep = False
        reason = "docs-or-metadata-only"
    elif len(tests) == len(paths):
        keep = False
        reason = "test-only-without-kernel-implementation"
    elif kernel_hits and opt_hits and any(
        (KERNEL_PATH_RE.search(path) or KERNEL_PATH_TOKEN_RE.search(path)) and not NON_CUDA_PATH_RE.search(path)
        for path in paths
    ):
        keep = True
        reason = "kernel-path-with-performance-signals"
    else:
        keep = False
        reason = "no-cuda-triton-cute-kernel-optimization-diff"

    return AuditResult(
        repo_id=repo_id,
        number=number,
        keep=keep,
        reason=reason,
        title=title,
        source_page=str(source.relative_to(root)) if source.exists() else None,
        bundle=str(bundle.relative_to(root)),
        changed_paths=paths,
        direct_paths=direct,
        bench_paths=bench,
        test_paths=tests,
        doc_or_meta_paths=docs,
        kernel_text_hits=kernel_hits,
        opt_text_hits=opt_hits,
    )


def update_ledger(root: Path, pruned: dict[tuple[str, int], AuditResult]) -> int:
    changed = 0
    for ledger in sorted((root / "candidates").glob("*.yaml")):
        data = yaml.safe_load(ledger.read_text(encoding="utf-8")) or {}
        rows = data.get("prs")
        if rows is None:
            rows = data.get("candidates") or []
        kept_rows = []
        removed = 0
        for row in rows:
            number = row.get("number", row.get("pr"))
            if number is None:
                kept_rows.append(row)
                continue
            key = (ledger.stem, int(number))
            if key in pruned:
                removed += 1
                continue
            kept_rows.append(row)
        if removed:
            counts = Counter(str(row.get("decision", "")).lower() for row in kept_rows)
            data["total_candidates"] = len(kept_rows)
            data["included"] = counts.get("include", 0)
            data["excluded"] = counts.get("exclude", 0)
            data["deferred"] = counts.get("defer", 0)
            data["prs"] = kept_rows
            ledger.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")
            changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="delete rejected source pages and bundles, and update ledgers")
    parser.add_argument("--repo", action="append", help="limit to repo id; repeatable")
    args = parser.parse_args()

    root = knowledge_root()
    repos = {repo.lower() for repo in args.repo or []}
    results: list[AuditResult] = []
    for bundle in sorted((root / "evidence" / "pull-bundles").glob("*/*")):
        if not bundle.is_dir() or not bundle.name.startswith("gh-"):
            continue
        if repos and bundle.parent.name.lower() not in repos:
            continue
        results.append(audit_bundle(root, bundle))

    keep = [result for result in results if result.keep]
    reject = [result for result in results if not result.keep]
    by_repo: dict[str, Counter[str]] = defaultdict(Counter)
    reason_counts = Counter(result.reason for result in results)
    for result in results:
        by_repo[result.repo_id]["keep" if result.keep else "reject"] += 1

    report = {
        "schema_version": 1,
        "mode": "apply" if args.apply else "dry-run",
        "policy": "Keep only PR diffs with direct CUDA/Triton/CuTe/CUTLASS/TileLang kernel, kernel-runtime, benchmark, or profile changes.",
        "total": len(results),
        "keep": len(keep),
        "reject": len(reject),
        "by_repo": {repo: dict(counts) for repo, counts in sorted(by_repo.items())},
        "reason_counts": dict(reason_counts),
        "rejected_pr_details_written": False,
    }

    if args.apply:
        pruned = {(result.repo_id, result.number): result for result in reject}
        for result in reject:
            source = root / result.source_page if result.source_page else source_page_for(root, result.repo_id, result.number)
            bundle = root / result.bundle
            if source.exists():
                source.unlink()
            if bundle.exists():
                shutil.rmtree(bundle)
        report["updated_ledgers"] = update_ledger(root, pruned)

    out_path = root / "data" / "pr-diff-relevance-audit.yaml"
    out_path.write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("mode", "total", "keep", "reject", "by_repo", "reason_counts")}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
