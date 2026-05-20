#!/usr/bin/env python3
"""Expand the PR candidate corpus from the current source map and GitHub search."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from _knowledge_root import knowledge_root


CATALOG_PATH = Path("data") / "repo-catalog.yaml"
REFRESH_CUTOFF_PATH = Path("data") / "refresh-cutoff.yaml"
REFRESH_RESULTS_PATH = Path("data") / "refresh-search-results.yaml"
REFRESH_SELECTION_AUDIT_PATH = Path("data") / "refresh-selection-audit.yaml"

DUPLICATE_OF = {
    "cute-dsl": "cutlass",
}

DEFAULT_SEARCH_KEYWORDS = [
    "cuda kernel",
    "triton kernel",
    "cutlass",
    "cute",
    "hopper",
    "blackwell",
    "sm90",
    "sm100",
    "fp8",
    "fp4",
    "nvfp4",
    "mxfp4",
    "gemm",
    "attention kernel",
    "moe kernel",
    "benchmark kernel",
]

KERNEL_SOURCE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".cu",
    ".cuh",
    ".h",
    ".hpp",
    ".inl",
    ".inc",
    ".py",
    ".pyx",
    ".pyi",
    ".cmake",
}

PATH_SIGNAL_TERMS = (
    "attention",
    "benchmark",
    "blackwell",
    "cuda",
    "cudagraph",
    "cute",
    "cutlass",
    "decode",
    "deepgemm",
    "flash_attn",
    "flashinfer",
    "fp4",
    "fp8",
    "gemm",
    "hopper",
    "kernel",
    "kv_cache",
    "mla",
    "moe",
    "mxfp4",
    "nvfp4",
    "paged",
    "ptx",
    "quant",
    "sm90",
    "sm100",
    "sm120",
    "tensorrt",
    "tilelang",
    "tma",
    "triton",
    "wgmma",
)

TEXT_SIGNAL_TERMS = DEFAULT_SEARCH_KEYWORDS + [
    "cudagraph",
    "deepgemm",
    "flashinfer",
    "flash attention",
    "paged attention",
    "performance",
    "optimize",
    "speedup",
    "latency",
    "throughput",
    "regression",
    "kernel fusion",
]

CATEGORY_TO_KERNEL_TYPE = {
    "attention_kv": "attention",
    "gemm_quant": "gemm",
    "memory_primitives": "memory",
    "moe_routing": "moe",
    "norm_epilogue": "norm",
    "scheduler_autotune": "scheduler",
    "arch_pipeline": "runtime",
    "compiler_runtime": "compiler",
}


def run(cmd: list[str], *, timeout: int = 120) -> str:
    return subprocess.check_output(cmd, text=True, timeout=timeout)


def gh_json_paginated(path: str, *, timeout: int = 180) -> list[dict[str, Any]]:
    result = subprocess.run(
        ["gh", "api", "--paginate", path],
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"gh api failed for {path}")
    text = result.stdout.strip()
    if not text:
        return []
    decoder = json.JSONDecoder()
    idx = 0
    rows: list[dict[str, Any]] = []
    while idx < len(text):
        while idx < len(text) and text[idx].isspace():
            idx += 1
        obj, idx = decoder.raw_decode(text, idx)
        if isinstance(obj, list):
            rows.extend(obj)
        elif isinstance(obj, dict):
            rows.append(obj)
    return rows


def today_utc() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def infer_architectures(text: str) -> list[str]:
    lower = text.lower()
    arch = []
    if any(token in lower for token in ("blackwell", "sm100", "sm120", "b200", "tcgen05", "tmem", "nvfp4", "mxfp4")):
        arch.append("sm100")
    if any(token in lower for token in ("hopper", "sm90", "h100", "h200", "wgmma")):
        arch.append("sm90")
    return arch or ["sm100"]


def infer_languages(text: str) -> list[str]:
    lower = text.lower()
    languages = []
    if any(token in lower for token in (".cu", ".cuh", "cuda", "kernel")):
        languages.append("cuda-cpp")
    if "triton" in lower:
        languages.append("triton")
    if any(token in lower for token in ("cute", "cutlass", "tcgen05", "wgmma")):
        languages.append("cute-dsl")
    if "ptx" in lower:
        languages.append("ptx")
    return sorted(set(languages))


def infer_hardware_features(text: str) -> list[str]:
    lower = text.lower()
    features = []
    for token in ("tcgen05", "tmem", "tma", "wgmma", "nvfp4", "mxfp4", "fp4", "fp8", "clc", "pdl", "gdc"):
        if token in lower:
            features.append(token)
    if "blackwell" in lower or "sm100" in lower:
        features.append("blackwell")
    if "hopper" in lower or "sm90" in lower:
        features.append("hopper")
    return sorted(set(features))


def infer_kernel_types(text: str, categories: list[str] | None = None) -> list[str]:
    lower = text.lower()
    out = []
    for category in categories or []:
        mapped = CATEGORY_TO_KERNEL_TYPE.get(category)
        if mapped:
            out.append(mapped)
    for token, kind in (
        ("attention", "attention"),
        ("fmha", "attention"),
        ("mla", "mla"),
        ("gemm", "gemm"),
        ("matmul", "gemm"),
        ("moe", "moe"),
        ("norm", "norm"),
        ("softmax", "softmax"),
        ("decode", "decode"),
        ("sampling", "sampling"),
        ("reduction", "reduction"),
        ("scan", "scan"),
        ("sort", "sort"),
    ):
        if token in lower:
            out.append(kind)
    return sorted(set(out))


def infer_techniques(text: str) -> list[str]:
    lower = text.lower()
    pairs = (
        ("fusion", "kernel-fusion"),
        ("fused", "kernel-fusion"),
        ("epilogue", "epilogue-fusion"),
        ("pipeline", "pipeline-stages"),
        ("warp", "warp-specialization"),
        ("persistent", "persistent-kernels"),
        ("swizzle", "swizzling"),
        ("tma", "async-copy"),
        ("quant", "fine-grained-quantization"),
        ("autotune", "autotuning"),
        ("scheduler", "tile-scheduling"),
        ("cache", "cache-policy"),
        ("vector", "vectorized-loads"),
    )
    return sorted({technique for token, technique in pairs if token in lower})


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def save_yaml(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def existing_corpus_summary(root: Path) -> dict[str, Any]:
    pages = list((root / "sources" / "prs").glob("*/*.md"))
    by_repo: Counter[str] = Counter()
    fields: dict[str, Counter[str]] = {
        "tags": Counter(),
        "kernel_types": Counter(),
        "languages": Counter(),
        "architectures": Counter(),
        "hardware_features": Counter(),
    }
    for page in pages:
        meta = parse_frontmatter(page)
        by_repo[page.parent.name] += 1
        for field, counter in fields.items():
            for value in meta.get(field) or []:
                counter[str(value)] += 1
    return {
        "source_prs": len(pages),
        "by_repo": dict(sorted(by_repo.items())),
        "top_tags": dict(fields["tags"].most_common(30)),
        "top_kernel_types": dict(fields["kernel_types"].most_common(30)),
        "top_languages": dict(fields["languages"].most_common(20)),
        "top_architectures": dict(fields["architectures"].most_common(20)),
        "top_hardware_features": dict(fields["hardware_features"].most_common(20)),
    }


def _iter_framework_sources(root: Path) -> list[dict[str, Any]]:
    """Yield framework metadata entries from both source files.

    `index.json` scopes Route B to complementary repos; `data/pr-frameworks.yaml`
    keeps metadata for the Route A PR-bundled frameworks so the PR pipeline can
    still refresh them after they were removed from `index.json`.
    """

    sources: list[dict[str, Any]] = []
    index = load_json(root / "index.json")
    for framework in index.get("frameworks", []):
        sources.append(framework)
    pr_frameworks_path = root / "data" / "pr-frameworks.yaml"
    if pr_frameworks_path.exists():
        pr_data = load_yaml(pr_frameworks_path)
        for framework in pr_data.get("frameworks", []):
            sources.append(framework)
    return sources


def build_catalog(root: Path, start: str, cutoff: str) -> dict[str, Any]:
    candidate_ids = {path.stem for path in (root / "candidates").glob("*.yaml")}
    frameworks = []
    seen_ids: set[str] = set()
    for framework in _iter_framework_sources(root):
        rid = framework["id"]
        if rid in seen_ids:
            continue
        seen_ids.add(rid)
        entry = {
            "id": rid,
            "name": framework.get("name", rid),
            "repo": framework.get("repo"),
            "url": framework.get("url"),
            "kernel_paths": framework.get("kernel_paths") or [],
            "tags": framework.get("tags") or [],
            "start_date": start,
            "cutoff_date": cutoff,
            "scan_mode": "pr-diff" if rid in candidate_ids else "source-reference",
        }
        if rid in DUPLICATE_OF:
            entry["scan_mode"] = "duplicate-pr-view"
            entry["duplicate_of"] = DUPLICATE_OF[rid]
        frameworks.append(entry)
    return {
        "schema_version": 1,
        "generated_at": today_utc(),
        "start_date": start,
        "cutoff_date": cutoff,
        "source": "knowledge/index.json plus knowledge/data/pr-frameworks.yaml plus PR candidate ledgers",
        "frameworks": frameworks,
    }


def fetch_pr_files(repo: str, number: int) -> list[dict[str, Any]]:
    try:
        return gh_json_paginated(f"repos/{repo}/pulls/{number}/files?per_page=100")
    except Exception as exc:
        print(f"WARN: file fetch failed for {repo}#{number}: {exc}", file=sys.stderr)
        return []


def is_kernel_path(filename: str, kernel_paths: list[str]) -> bool:
    lower = filename.lower()
    normalized = lower.rstrip("/")
    for path in kernel_paths:
        prefix = str(path).lower().rstrip("/")
        if normalized == prefix or normalized.startswith(prefix + "/"):
            return True
    suffix_ok = Path(lower).suffix in KERNEL_SOURCE_SUFFIXES or Path(lower).name == "cmakelists.txt"
    return suffix_ok and any(term in lower for term in PATH_SIGNAL_TERMS)


def is_borderline_path(filename: str) -> bool:
    lower = filename.lower()
    return any(part in lower for part in ("test", "bench", "benchmark", ".github", "ci", "docker", "docs")) and any(
        term in lower for term in PATH_SIGNAL_TERMS
    )


def classify_candidate(entry: dict[str, Any], files: list[dict[str, Any]], framework: dict[str, Any], seed_keywords: set[str]) -> dict[str, Any]:
    paths = [str(item.get("filename") or "") for item in files if item.get("filename")]
    text = " ".join([entry.get("title", ""), " ".join(seed_keywords), " ".join(paths)]).lower()
    kernel_paths = framework.get("kernel_paths") or []
    strong_paths = [path for path in paths if is_kernel_path(path, kernel_paths)]
    borderline_paths = [path for path in paths if is_borderline_path(path)]
    text_hits = sorted({term for term in TEXT_SIGNAL_TERMS if term.lower() in text})
    if strong_paths:
        decision = "include"
        reason = "file-path kernel signal: " + ", ".join(strong_paths[:4])
        inclusion_reason = "Merged CUDA/kernel optimization PR with changed files matching existing corpus kernel paths or kernel source signals."
    elif text_hits and borderline_paths:
        decision = "defer"
        reason = "borderline benchmark/runtime/docs signal: " + ", ".join(borderline_paths[:4])
        inclusion_reason = "Search-matched CUDA/kernel PR with benchmark, test, runtime, CI, or docs-adjacent paths; keep as contextual PR evidence."
    elif text_hits and not paths:
        decision = "defer"
        reason = "borderline: search/title signal but changed files unavailable"
        inclusion_reason = "Search-matched CUDA/kernel PR; changed-file fetch was unavailable, so keep as contextual evidence until materialization."
    else:
        decision = "exclude"
        reason = "no changed-file or title signal matching the existing CUDA/kernel corpus"
        inclusion_reason = "Excluded during refresh selection audit."

    entry["decision"] = decision
    entry["reason"] = reason
    entry["inclusion_reason"] = inclusion_reason
    entry["changed_paths"] = paths
    entry["path_signals"] = strong_paths[:12]
    entry["borderline_path_signals"] = borderline_paths[:12]
    entry["selection_text_signals"] = text_hits[:20]
    if files:
        entry["additions"] = sum(int(item.get("additions") or 0) for item in files)
        entry["deletions"] = sum(int(item.get("deletions") or 0) for item in files)
        entry["changed_file_count"] = len(files)
    combined = " ".join([text, " ".join(paths)])
    entry["architectures"] = infer_architectures(combined)
    entry["techniques"] = infer_techniques(combined)
    entry["hardware_features"] = infer_hardware_features(combined)
    entry["kernel_types"] = infer_kernel_types(combined)
    entry["languages"] = infer_languages(combined)
    return entry


def merge_entries(ledger: dict[str, Any], entries: list[dict[str, Any]], repo: str, cutoff: str, start: str) -> tuple[dict[str, Any], int]:
    rows = ledger.get("prs")
    if rows is None:
        rows = ledger.get("candidates") or []
    existing = {}
    for row in rows:
        number = row.get("number", row.get("pr"))
        if number is not None:
            existing[int(number)] = row

    added = 0
    for entry in entries:
        number = int(entry.get("number", entry.get("pr")))
        if number in existing:
            row = existing[number]
            for key, value in entry.items():
                if key not in row or row.get(key) in (None, "", [], {}):
                    row[key] = value
            continue
        rows.append(entry)
        existing[number] = entry
        added += 1

    counts = Counter(str(row.get("decision", "")).lower() for row in rows)
    ledger["repo"] = ledger.get("repo") or repo
    ledger["searched_at"] = cutoff
    ledger["scan_start_date"] = start
    ledger["cutoff_date"] = cutoff
    ledger["total_candidates"] = sum(counts.values())
    ledger["included"] = counts.get("include", 0)
    ledger["excluded"] = counts.get("exclude", 0)
    ledger["deferred"] = counts.get("defer", 0)
    ledger["prs"] = rows
    return ledger, added


def keyword_hits(repo: str, keyword: str, start: str, cutoff: str, limit: int) -> list[dict[str, Any]]:
    query = f"{keyword} closed:{start}..{cutoff}"
    cmd = [
        "gh",
        "search",
        "prs",
        "--repo",
        repo,
        "--state",
        "closed",
        "--merged",
        "--limit",
        str(limit),
        "--json",
        "number,title,closedAt,url,author",
        query,
    ]
    try:
        return json.loads(run(cmd, timeout=90))
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        print(f"WARN: search failed for {repo} keyword={keyword!r}: {exc}", file=sys.stderr)
        return []


def live_search_entries(repo_id: str, repo: str, framework: dict[str, Any], keywords: list[str], start: str, cutoff: str, per_keyword: int, max_new: int) -> list[dict[str, Any]]:
    seen: dict[int, dict[str, Any]] = {}
    reasons: dict[int, set[str]] = {}
    for keyword in keywords:
        for row in keyword_hits(repo, keyword, start, cutoff, per_keyword):
            number = int(row["number"])
            seen.setdefault(number, row)
            reasons.setdefault(number, set()).add(keyword)
        time.sleep(2.2)
    entries = []
    for number in sorted(seen, reverse=True):
        row = seen[number]
        closed = (row.get("closedAt") or "")[:10]
        text = f"{row.get('title', '')} {' '.join(sorted(reasons.get(number, [])))} {repo_id}"
        entries.append(
            {
                "number": number,
                "pr": number,
                "title": row.get("title", f"PR-{number}"),
                "repo": repo,
                "url": row.get("url", f"https://github.com/{repo}/pull/{number}"),
                "date": closed,
                "merged_at": row.get("closedAt"),
                "author": ((row.get("author") or {}).get("login") if isinstance(row.get("author"), dict) else "unknown") or "unknown",
                "decision": "defer",
                "status": "merged",
                "reason": f"github search seed: {', '.join(sorted(reasons.get(number, [])))}",
                "inclusion_reason": "Search-matched CUDA kernel optimization PR; materialize diff/source before synthesis.",
                "seed_source": "github-search",
                "tags": sorted(reasons.get(number, [])),
                "architectures": infer_architectures(text),
                "techniques": infer_techniques(text),
                "hardware_features": infer_hardware_features(text),
                "kernel_types": infer_kernel_types(text),
                "languages": infer_languages(text),
                "changed_paths": [],
            }
        )
        if len(entries) >= max_new:
            break
    out = []
    for entry in entries:
        number = int(entry["number"])
        files = fetch_pr_files(repo, number)
        out.append(classify_candidate(entry, files, framework, reasons.get(number, set())))
        time.sleep(0.25)
    return out


def write_cutoff(root: Path, start: str, cutoff: str, repos: list[str]) -> None:
    payload = {
        "start_date": start,
        "cutoff_date": cutoff,
        "updated_at": today_utc(),
        "policy": "Merged PRs from the start_date through cutoff_date are eligible when they match CUDA kernel optimization signals.",
        "repo_ids": repos,
    }
    save_yaml(root / REFRESH_CUTOFF_PATH, payload)


def write_refresh_results(root: Path, start: str, cutoff: str, per_repo: dict[str, list[dict[str, Any]]]) -> None:
    payload = {
        "schema_version": 2,
        "start_date": start,
        "cutoff_date": cutoff,
        "generated_at": today_utc(),
        "repos": [],
    }
    for repo_id in sorted(per_repo):
        rows = per_repo[repo_id]
        payload["repos"].append(
            {
                "repo_slug": repo_id,
                "searched_at": cutoff,
                "scan_start_date": start,
                "pr_numbers_seen": sorted({int(row.get("number", row.get("pr"))) for row in rows}),
                "last_pr_date_seen": max([str(row.get("date") or "") for row in rows], default=""),
            }
        )
    save_yaml(root / REFRESH_RESULTS_PATH, payload)


def write_selection_audit(root: Path, corpus_start: str, search_start: str, cutoff: str, corpus_summary: dict[str, Any], per_repo: dict[str, list[dict[str, Any]]]) -> None:
    rows = []
    for repo_id in sorted(per_repo):
        for row in per_repo[repo_id]:
            rows.append(
                {
                    "repo_slug": repo_id,
                    "repo": row.get("repo"),
                    "pr": int(row.get("number", row.get("pr"))),
                    "title": row.get("title"),
                    "date": row.get("date"),
                    "decision": row.get("decision"),
                    "reason": row.get("reason"),
                    "path_signals": row.get("path_signals") or [],
                    "borderline_path_signals": row.get("borderline_path_signals") or [],
                    "selection_text_signals": row.get("selection_text_signals") or [],
                    "changed_file_count": row.get("changed_file_count", 0),
                }
            )
    payload = {
        "schema_version": 1,
        "generated_at": today_utc(),
        "corpus_start_date": corpus_start,
        "search_start_date": search_start,
        "cutoff_date": cutoff,
        "pre_refresh_corpus_summary": corpus_summary,
        "selection_policy": {
            "include": "merged PRs whose changed files match existing kernel_paths or CUDA/kernel source path signals",
            "defer": "merged PRs with CUDA/kernel text hits but only benchmark/test/runtime/CI/docs-adjacent or unavailable file signals",
            "exclude": "search hits without title or changed-file evidence matching the existing CUDA/kernel corpus",
        },
        "new_candidate_judgments": sorted(rows, key=lambda item: (str(item["repo_slug"]), int(item["pr"]))),
    }
    save_yaml(root / REFRESH_SELECTION_AUDIT_PATH, payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default="2024-01-01")
    parser.add_argument("--search-start", default=None, help="Incremental GitHub search start date; defaults to --start")
    parser.add_argument("--cutoff", default=date.today().isoformat())
    parser.add_argument("--live-search", action="store_true")
    parser.add_argument("--repos", default=None, help="comma-separated repo ids for live search")
    parser.add_argument("--per-keyword", type=int, default=35)
    parser.add_argument("--max-new-per-repo", type=int, default=160)
    parser.add_argument("--sleep", type=float, default=0.0)
    args = parser.parse_args()

    root = knowledge_root()
    search_start = args.search_start or args.start
    corpus_summary = existing_corpus_summary(root)
    catalog = build_catalog(root, args.start, args.cutoff)
    save_yaml(root / CATALOG_PATH, catalog)

    repo_catalog = {entry["id"]: entry for entry in catalog.get("frameworks", []) if entry.get("scan_mode") == "pr-diff"}
    target_live_repos = sorted(repo_catalog)
    if args.repos:
        requested = {item.strip() for item in args.repos.split(",") if item.strip()}
        target_live_repos = [repo_id for repo_id in target_live_repos if repo_id in requested]

    all_seen: dict[str, list[dict[str, Any]]] = {}
    if args.live_search:
        for repo_id in target_live_repos:
            info = repo_catalog[repo_id]
            repo_full = info.get("repo")
            if not repo_full:
                continue
            keywords = list(dict.fromkeys((info.get("tags") or [])[:8] + DEFAULT_SEARCH_KEYWORDS))
            print(f"search {repo_id}: {repo_full} with {len(keywords)} keywords", flush=True)
            entries = live_search_entries(repo_id, repo_full, info, keywords, search_start, args.cutoff, args.per_keyword, args.max_new_per_repo)
            ledger_path = root / "candidates" / f"{repo_id}.yaml"
            ledger = load_yaml(ledger_path)
            ledger, added = merge_entries(ledger, entries, repo_full, args.cutoff, args.start)
            save_yaml(ledger_path, ledger)
            all_seen.setdefault(repo_id, []).extend(entries)
            print(f"  -> {len(entries)} search seeds, +{added} ledger rows", flush=True)
            if args.sleep:
                time.sleep(args.sleep)
        write_refresh_results(root, search_start, args.cutoff, all_seen)
        write_selection_audit(root, args.start, search_start, args.cutoff, corpus_summary, all_seen)
    else:
        print("live search disabled; refreshed repo catalog only")

    write_cutoff(root, args.start, args.cutoff, sorted(repo_catalog))

    print(
        json.dumps(
            {
                "catalog_entries": len(catalog.get("frameworks", [])),
                "pr_repos": len(repo_catalog),
                "seen_prs": sum(len(v) for v in all_seen.values()),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
