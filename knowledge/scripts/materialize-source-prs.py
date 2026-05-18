#!/usr/bin/env python3
"""Materialize evidence bundles for every PR page under sources/prs/."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import yaml

from _knowledge_root import knowledge_root


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

SOURCE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".cu",
    ".cuh",
    ".h",
    ".hh",
    ".hpp",
    ".inl",
    ".inc",
    ".py",
    ".pyi",
    ".pyx",
    ".cmake",
    ".txt",
    ".md",
    ".yaml",
    ".yml",
    ".json",
}

SOURCE_HINTS = (
    "attention",
    "benchmark",
    "bench",
    "blackwell",
    "cuda",
    "cutlass",
    "decode",
    "fp8",
    "fp4",
    "gemm",
    "hopper",
    "kernel",
    "moe",
    "nvfp4",
    "profile",
    "sm90",
    "sm100",
    "sm120",
    "test",
    "triton",
    "wgmma",
)

REPO_ID_ALIASES = {
    "deepgemm": "deepgemm",
    "DeepGEMM": "deepgemm",
}

BUNDLE_ROOT = Path("evidence") / "pull-bundles"
DIFF_NAME = "review.diff"
UPSTREAM_NAME = "upstream.json"
ORIGIN_NAME = "ORIGIN.yaml"
SNAPSHOT_DIR = "source-snapshot"


def get_token() -> str | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(["gh", "auth", "token"], check=False, capture_output=True, text=True)
    except OSError:
        return None
    if result.returncode == 0:
        return result.stdout.strip() or None
    return None


def headers(token: str | None, *, accept: str = "application/vnd.github+json") -> dict[str, str]:
    out = {
        "Accept": accept,
        "User-Agent": "KernelPilot-Knowledge-Materializer",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        out["Authorization"] = f"Bearer {token}"
    return out


def fetch_bytes(url: str, token: str | None = None, *, accept: str = "*/*", timeout: int = 45) -> bytes:
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            req = Request(url, headers=headers(token, accept=accept))
            with urlopen(req, timeout=timeout) as response:
                return response.read()
        except HTTPError as exc:
            if exc.code == 403 and "rate limit" in (exc.read().decode("utf-8", "replace").lower()):
                raise RuntimeError(f"rate limited while fetching {url}") from exc
            if exc.code in {404, 410}:
                raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
            last_error = exc
        except (TimeoutError, URLError) as exc:
            last_error = exc
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def fetch_json(url: str, token: str | None) -> Any:
    return json.loads(fetch_bytes(url, token, accept="application/vnd.github+json").decode("utf-8"))


def fetch_json_pages(url: str, token: str | None, *, max_pages: int = 20) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    sep = "&" if "?" in url else "?"
    for page in range(1, max_pages + 1):
        page_rows = fetch_json(f"{url}{sep}per_page=100&page={page}", token)
        if not page_rows:
            break
        rows.extend(page_rows)
        if len(page_rows) < 100:
            break
    return rows


def paths_from_diff(diff: bytes) -> list[str]:
    paths: list[str] = []
    seen: set[str] = set()
    for line in diff.decode("utf-8", "replace").splitlines():
        if not line.startswith("diff --git a/"):
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        path = parts[3]
        if path.startswith("b/"):
            path = path[2:]
        if path == "/dev/null" or path in seen:
            continue
        paths.append(path)
        seen.add(path)
    return paths


def parse_page(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    meta = yaml.safe_load(match.group(1)) or {}
    meta["_source_page"] = path
    return meta


def repo_id(repo: str) -> str:
    return repo.split("/", 1)[-1].lower()


def source_repo_id(path: Path, repo: str) -> str:
    parent = path.parent.name
    return REPO_ID_ALIASES.get(parent, parent.lower())


def safe_relpath(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"unsafe path from GitHub: {path}")
    return candidate


def is_source_candidate(filename: str) -> bool:
    path = Path(filename)
    if path.name == "CMakeLists.txt":
        return True
    if path.suffix.lower() in SOURCE_SUFFIXES:
        return True
    lower = filename.lower()
    return any(hint in lower for hint in SOURCE_HINTS)


def select_key_files(files: list[dict[str, Any]], changed_paths: list[str], max_files: int) -> list[dict[str, Any]]:
    if files:
        selected = [
            item
            for item in files
            if item.get("status") != "removed" and is_source_candidate(str(item.get("filename", "")))
        ]
        if len(selected) < max_files:
            seen = {item.get("filename") for item in selected}
            for item in files:
                if item.get("status") == "removed":
                    continue
                filename = item.get("filename")
                if filename and filename not in seen:
                    selected.append(item)
                    seen.add(filename)
                if len(selected) >= max_files:
                    break
        return selected[:max_files]

    out = []
    for filename in changed_paths:
        if is_source_candidate(filename):
            out.append({"filename": filename, "status": "unknown"})
        if len(out) >= max_files:
            break
    return out


def bundle_complete(bundle: Path) -> bool:
    return (
        (bundle / DIFF_NAME).is_file()
        and (bundle / UPSTREAM_NAME).is_file()
        and (bundle / ORIGIN_NAME).is_file()
        and (bundle / SNAPSHOT_DIR).is_dir()
    )


def bundle_path(root: Path, rid: str, pr: int) -> Path:
    return root / BUNDLE_ROOT / rid / f"gh-{pr}"


def write_error(path: Path, message: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(message + "\n", encoding="utf-8")


def materialize_one(meta: dict[str, Any], root: Path, token: str | None, args: argparse.Namespace) -> tuple[str, str]:
    repo = str(meta["repo"])
    pr = int(meta["pr"])
    rid = source_repo_id(meta["_source_page"], repo)
    bundle = bundle_path(root, rid, pr)
    label = f"{repo}#{pr}"

    if bundle_complete(bundle) and not args.force:
        return label, "exists"

    bundle.mkdir(parents=True, exist_ok=True)
    key_root = bundle / SNAPSHOT_DIR
    key_root.mkdir(parents=True, exist_ok=True)

    api_base = f"https://api.github.com/repos/{repo}/pulls/{pr}"
    pull = fetch_json(api_base, token)

    diff_url = f"https://github.com/{repo}/pull/{pr}.diff"
    try:
        diff = fetch_bytes(diff_url, None, accept="text/plain")
    except Exception as exc:  # noqa: BLE001
        if "429" not in str(exc):
            raise
        diff = fetch_bytes(api_base, token, accept="application/vnd.github.v3.diff")
    (bundle / DIFF_NAME).write_bytes(diff)

    changed_paths = [str(path) for path in (meta.get("changed_paths") or [])]
    diff_paths = paths_from_diff(diff)
    if not changed_paths:
        changed_paths = diff_paths
    files = fetch_json_pages(f"{api_base}/files", token) if args.use_files_api else []
    if not files:
        files = [{"filename": path, "status": "unknown"} for path in changed_paths]

    metadata = {
        "pull": pull,
        "files": files,
        "files_source": "github-api" if args.use_files_api else "diff-parse",
        "source_page": str(meta["_source_page"].relative_to(root)),
    }
    (bundle / UPSTREAM_NAME).write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    head_sha = pull.get("head", {}).get("sha") or meta.get("head_ref_oid") or ""
    key_files = []
    for item in select_key_files(files, changed_paths, args.max_files):
        filename = str(item.get("filename") or "")
        if not filename:
            continue
        rel = safe_relpath(filename)
        local = key_root / rel
        record = {
            "source_path": filename,
            "local_path": str(local.relative_to(bundle)),
            "ref": head_sha,
            "status": item.get("status"),
            "fetched": False,
        }
        if args.no_source_snapshot:
            write_error(local.with_suffix(local.suffix + ".SKIPPED.txt"), "Skipped by --no-source-snapshot")
            record["local_path"] = str(local.with_suffix(local.suffix + ".SKIPPED.txt").relative_to(bundle))
            record["skip_reason"] = "no_source_snapshot"
            key_files.append(record)
            continue
        try:
            raw_url = f"https://raw.githubusercontent.com/{repo}/{quote(head_sha, safe='')}/{quote(filename, safe='/')}"
            content = fetch_bytes(raw_url, None, accept="text/plain,application/octet-stream")
            if len(content) > args.max_bytes:
                skipped = local.with_suffix(local.suffix + ".SKIPPED.txt")
                write_error(skipped, f"Skipped {filename}: {len(content)} bytes exceeds --max-bytes={args.max_bytes}")
                record["local_path"] = str(skipped.relative_to(bundle))
                record["skip_reason"] = "max_bytes"
            else:
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_bytes(content)
                record["fetched"] = True
        except Exception as exc:  # noqa: BLE001
            error_path = local.with_suffix(local.suffix + ".ERROR.txt")
            write_error(error_path, f"Failed to fetch {filename} at {head_sha}: {exc}")
            record["local_path"] = str(error_path.relative_to(bundle))
            record["error"] = str(exc)
        key_files.append(record)

    provenance = {
        "schema_version": 1,
        "source_key": f"{repo}#{pr}",
        "repo": repo,
        "repo_id": rid,
        "pr_number": pr,
        "title": pull.get("title") or meta.get("title"),
        "url": pull.get("html_url") or meta.get("url"),
        "state": pull.get("state"),
        "merged_at": pull.get("merged_at"),
        "base_ref_oid": pull.get("base", {}).get("sha"),
        "head_ref_oid": head_sha,
        "source_page": str(meta["_source_page"].relative_to(root)),
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "architectures": meta.get("architectures") or [],
        "tags": meta.get("tags") or [],
        "techniques": meta.get("techniques") or [],
        "hardware_features": meta.get("hardware_features") or [],
        "kernel_types": meta.get("kernel_types") or [],
        "languages": meta.get("languages") or [],
        "bundle": {
            "diff": DIFF_NAME,
            "upstream": UPSTREAM_NAME,
            "source_snapshot": key_files,
        },
    }
    (bundle / ORIGIN_NAME).write_text(
        yaml.safe_dump(provenance, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    readme = [
        f"# gh-{pr}: {provenance['title']}",
        "",
        f"- Repository: `{repo}`",
        f"- URL: {provenance['url']}",
        f"- Source page: `{provenance['source_page']}`",
        f"- Diff: `{DIFF_NAME}`",
        f"- Source snapshot: `{len(key_files)}` captured under `{SNAPSHOT_DIR}/`",
        "",
        f"See `{ORIGIN_NAME}` for upstream refs and fetch status.",
        "",
    ]
    (bundle / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return label, "fetched"


def load_source_pages(root: Path, repos: set[str] | None) -> list[dict[str, Any]]:
    pages = []
    for path in sorted((root / "sources" / "prs").glob("*/*.md")):
        meta = parse_page(path)
        if repos and repo_id(str(meta["repo"])) not in repos and path.parent.name.lower() not in repos:
            continue
        pages.append(meta)
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", action="append", help="Limit to repo id/full repo; repeatable")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--max-files", type=int, default=8)
    parser.add_argument("--max-bytes", type=int, default=2_000_000)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--no-source-snapshot", action="store_true")
    parser.add_argument("--use-files-api", action="store_true", help="Fetch GitHub PR file list instead of parsing review.diff")
    args = parser.parse_args()

    root = knowledge_root()
    token = get_token()
    repos = None
    if args.repo:
        repos = {value.split("/", 1)[-1].lower() for value in args.repo}

    metas = load_source_pages(root, repos)
    pending = []
    for meta in metas:
        rid = source_repo_id(meta["_source_page"], str(meta["repo"]))
        bundle = bundle_path(root, rid, int(meta["pr"]))
        if args.force or not bundle_complete(bundle):
            pending.append(meta)
    if args.limit:
        pending = pending[: args.limit]

    print(json.dumps({"source_pages": len(metas), "pending": len(pending)}, indent=2), flush=True)
    if not pending:
        return 0

    fetched = exists = failed = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(materialize_one, meta, root, token, args) for meta in pending]
        for future in as_completed(futures):
            try:
                label, status = future.result()
            except Exception as exc:  # noqa: BLE001
                failed += 1
                print(f"failed: {exc}", file=sys.stderr, flush=True)
                continue
            if status == "fetched":
                fetched += 1
            elif status == "exists":
                exists += 1
            print(f"{status}: {label}", flush=True)

    print(json.dumps({"fetched": fetched, "exists": exists, "failed": failed}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
