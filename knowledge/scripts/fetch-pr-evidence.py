#!/usr/bin/env python3
"""Materialize PR evidence bundles from candidate ledgers."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import yaml

from _knowledge_root import knowledge_root


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

BUNDLE_ROOT = Path("evidence") / "pull-bundles"
DIFF_NAME = "review.diff"
UPSTREAM_NAME = "upstream.json"
ORIGIN_NAME = "ORIGIN.yaml"
SNAPSHOT_DIR = "source-snapshot"


def gh_api(path: str, *, accept: str | None = None, raw: bool = False) -> bytes:
    cmd = ["gh", "api"]
    if accept:
        cmd.extend(["-H", f"Accept: {accept}"])
    cmd.append(path)
    result = subprocess.run(cmd, check=False, capture_output=True)
    if result.returncode != 0:
        msg = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(msg or f"gh api failed for {path}")
    return result.stdout if raw else result.stdout


def gh_json(path: str):
    return json.loads(gh_api(path).decode("utf-8"))


def gh_json_paginated(path: str) -> list[dict]:
    result = subprocess.run(
        ["gh", "api", "--paginate", path],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"gh api failed for {path}")
    text = result.stdout.strip()
    if not text:
        return []
    decoder = json.JSONDecoder()
    idx = 0
    pages = []
    while idx < len(text):
        while idx < len(text) and text[idx].isspace():
            idx += 1
        obj, idx = decoder.raw_decode(text, idx)
        pages.extend(obj if isinstance(obj, list) else [obj])
    return pages


def safe_relpath(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"unsafe path from GitHub: {path}")
    return candidate


def repo_id(repo: str) -> str:
    return repo.split("/", 1)[-1].lower()


def family_for_arch(arch: str) -> str:
    arch = arch.lower()
    if arch in {"sm90", "h100", "h200", "hopper"}:
        return "hopper"
    if arch in {"sm100", "sm103", "sm120", "sm121", "b100", "b200", "blackwell"}:
        return "blackwell"
    return arch


def families_for_entry(entry: dict) -> list[str]:
    families = []
    for arch in entry.get("architectures") or []:
        family = family_for_arch(str(arch))
        if family not in families:
            families.append(family)
    return families


def is_source_candidate(filename: str) -> bool:
    path = Path(filename)
    if path.name == "CMakeLists.txt":
        return True
    if path.suffix.lower() in SOURCE_SUFFIXES:
        return True
    lower = filename.lower()
    return any(hint in lower for hint in SOURCE_HINTS)


def select_key_files(files: list[dict], max_files: int) -> list[dict]:
    fetchable = [
        item
        for item in files
        if item.get("status") != "removed" and is_source_candidate(item.get("filename", ""))
    ]
    if len(fetchable) < max_files:
        seen = {item.get("filename") for item in fetchable}
        for item in files:
            if item.get("status") == "removed":
                continue
            filename = item.get("filename")
            if filename and filename not in seen:
                fetchable.append(item)
                seen.add(filename)
            if len(fetchable) >= max_files:
                break
    return fetchable[:max_files]


def render_diff_fallback(files: list[dict], reason: str) -> bytes:
    lines = [
        "# GitHub diff fallback",
        "# The PR-wide diff endpoint was unavailable for this PR.",
        f"# Reason: {reason}",
        "# This file is reconstructed from the GitHub Pull Request files API.",
        "",
    ]
    for item in files:
        filename = item.get("filename") or "unknown"
        previous = item.get("previous_filename") or filename
        status = item.get("status") or "unknown"
        additions = item.get("additions", 0)
        deletions = item.get("deletions", 0)
        lines.append(f"diff --git a/{previous} b/{filename}")
        lines.append(f"# status={status} additions={additions} deletions={deletions}")
        patch = item.get("patch")
        if patch:
            lines.append(str(patch))
        else:
            lines.append("# GitHub files API did not provide a textual patch for this file.")
        lines.append("")
    return ("\n".join(lines) + "\n").encode("utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def fetch_raw_file(repo: str, ref: str, filename: str) -> bytes:
    quoted = quote(filename, safe="/")
    return gh_api(
        f"repos/{repo}/contents/{quoted}?ref={quote(ref, safe='')}",
        accept="application/vnd.github.v3.raw",
        raw=True,
    )


def artifact_complete(path: Path) -> bool:
    return (
        (path / DIFF_NAME).is_file()
        and (path / UPSTREAM_NAME).is_file()
        and (path / ORIGIN_NAME).is_file()
        and (path / SNAPSHOT_DIR).is_dir()
    )


def bundle_path(root: Path, rid: str, pr: int) -> Path:
    return root / BUNDLE_ROOT / rid / f"gh-{pr}"


def materialize(entry: dict, root: Path, args: argparse.Namespace, rid: str | None = None) -> tuple[bool, str]:
    repo = entry["repo"]
    pr = int(entry.get("pr", entry.get("number")))
    rid = rid or repo_id(repo)
    bundle = bundle_path(root, rid, pr)
    if artifact_complete(bundle) and not args.force:
        entry["artifact_dir"] = str(bundle.relative_to(root))
        return False, "exists"

    bundle.mkdir(parents=True, exist_ok=True)
    key_root = bundle / SNAPSHOT_DIR
    key_root.mkdir(parents=True, exist_ok=True)

    pull = gh_json(f"repos/{repo}/pulls/{pr}")
    files = gh_json_paginated(f"repos/{repo}/pulls/{pr}/files?per_page=100")
    diff_fallback_error = ""
    try:
        diff = gh_api(
            f"repos/{repo}/pulls/{pr}",
            accept="application/vnd.github.v3.diff",
            raw=True,
        )
    except RuntimeError as exc:
        message = str(exc)
        if "diff exceeded" not in message and "maximum number" not in message:
            raise
        diff_fallback_error = message
        diff = render_diff_fallback(files, message)

    (bundle / DIFF_NAME).write_bytes(diff)
    (bundle / UPSTREAM_NAME).write_text(
        json.dumps({"pull": pull, "files": files}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    head_sha = pull.get("head", {}).get("sha") or entry.get("head_ref_oid") or ""
    key_files = []
    for item in select_key_files(files, args.max_files):
        filename = item.get("filename")
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
        try:
            content = fetch_raw_file(repo, head_sha, filename)
            if len(content) > args.max_bytes:
                write_text(
                    local.with_suffix(local.suffix + ".SKIPPED.txt"),
                    f"Skipped {filename}: {len(content)} bytes exceeds --max-bytes={args.max_bytes}\n",
                )
                record["local_path"] = str(
                    local.with_suffix(local.suffix + ".SKIPPED.txt").relative_to(bundle)
                )
                record["skip_reason"] = "max_bytes"
            else:
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_bytes(content)
                record["fetched"] = True
        except Exception as exc:  # keep the bundle useful even for deleted/vendor files
            write_text(
                local.with_suffix(local.suffix + ".ERROR.txt"),
                f"Failed to fetch {filename} at {head_sha}: {exc}\n",
            )
            record["local_path"] = str(
                local.with_suffix(local.suffix + ".ERROR.txt").relative_to(bundle)
            )
            record["error"] = str(exc)
        key_files.append(record)
        if args.sleep:
            time.sleep(args.sleep)

    provenance = {
        "schema_version": 1,
        "source_key": f"{repo}#{pr}",
        "repo": repo,
        "repo_id": rid,
        "pr_number": pr,
        "title": pull.get("title") or entry.get("title"),
        "url": pull.get("html_url") or entry.get("url"),
        "state": pull.get("state"),
        "merged_at": pull.get("merged_at"),
        "base_ref_oid": pull.get("base", {}).get("sha"),
        "head_ref_oid": head_sha,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "architectures": entry.get("architectures") or [],
        "architecture_families": families_for_entry(entry),
        "tags": entry.get("tags") or [],
        "techniques": entry.get("techniques") or [],
        "hardware_features": entry.get("hardware_features") or [],
        "kernel_types": entry.get("kernel_types") or [],
        "languages": entry.get("languages") or [],
        "bundle": {
            "diff": DIFF_NAME,
            "upstream": UPSTREAM_NAME,
            "source_snapshot": key_files,
        },
    }
    if diff_fallback_error:
        provenance["bundle"]["diff_fallback"] = "github-files-api"
        provenance["bundle"]["diff_fallback_reason"] = diff_fallback_error
    (bundle / ORIGIN_NAME).write_text(
        yaml.safe_dump(provenance, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    readme = [
        f"# gh-{pr}: {provenance['title']}",
        "",
        f"- Repository: `{repo}`",
        f"- URL: {provenance['url']}",
        f"- Head SHA: `{head_sha}`" if head_sha else "- Head SHA: `unknown`",
        f"- Diff: `{DIFF_NAME}`",
        f"- Source snapshot: `{len(key_files)}` captured under `{SNAPSHOT_DIR}/`",
        "",
        f"See `{ORIGIN_NAME}` for upstream refs and fetch status.",
        "",
    ]
    write_text(bundle / "README.md", "\n".join(readme))

    entry["artifact_dir"] = str(bundle.relative_to(root))
    return True, "fetched"


def load_ledgers(root: Path) -> list[tuple[Path, dict]]:
    ledgers = []
    for path in sorted((root / "candidates").glob("*.yaml")):
        ledgers.append((path, yaml.safe_load(path.read_text(encoding="utf-8"))))
    return ledgers


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", action="append", help="Limit to GitHub repo, e.g. pytorch/pytorch")
    parser.add_argument("--decision", action="append", help="Limit to decision value; repeatable")
    parser.add_argument("--limit", type=int, default=0, help="Stop after N fetched bundles")
    parser.add_argument("--max-files", type=int, default=32, help="Max changed source files per PR")
    parser.add_argument("--max-bytes", type=int, default=2_000_000, help="Max bytes per key file")
    parser.add_argument("--sleep", type=float, default=0.0, help="Sleep between raw file requests")
    parser.add_argument("--force", action="store_true", help="Refetch existing complete bundles")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = knowledge_root()
    ledgers = load_ledgers(root)
    allowed_repos = set(args.repo or [])
    allowed_decisions = set(args.decision or [])

    fetched = skipped = failed = 0
    for path, data in ledgers:
        changed = False
        entries = data.get("candidates")
        if entries is None:
            entries = data.get("prs", [])
        for entry in entries or []:
            if "repo" not in entry and data.get("repo"):
                entry["repo"] = data["repo"]
            if "pr" not in entry and entry.get("number") is not None:
                entry["pr"] = entry["number"]
            if allowed_repos and entry.get("repo") not in allowed_repos:
                continue
            if allowed_decisions and entry.get("decision") not in allowed_decisions:
                continue
            if args.limit and fetched >= args.limit:
                break
            if entry.get("artifact_dir"):
                bundle = root / str(entry["artifact_dir"])
            else:
                bundle = bundle_path(root, path.stem, int(entry["pr"]))
            if artifact_complete(bundle) and not args.force:
                entry["artifact_dir"] = str(bundle.relative_to(root))
                skipped += 1
                changed = True
                continue
            label = f"{entry['repo']}#{entry['pr']}"
            if args.dry_run:
                print(f"would fetch {label}")
                fetched += 1
                continue
            try:
                did_fetch, status = materialize(entry, root, args, path.stem)
                changed = True
                if did_fetch:
                    fetched += 1
                else:
                    skipped += 1
                print(f"{status}: {label}")
            except Exception as exc:
                failed += 1
                print(f"failed: {label}: {exc}", file=sys.stderr)
        if changed and not args.dry_run:
            path.write_text(
                yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
        if args.limit and fetched >= args.limit:
            break

    print(json.dumps({"fetched": fetched, "skipped": skipped, "failed": failed}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
