#!/usr/bin/env python3
"""Fetch useful PR review/discussion bullets for evidence bundles."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from _kb import parse_markdown
from _knowledge_root import knowledge_root


DISCUSSION_NAME = "discussion.md"
PULL_BUNDLE_ROOT = Path("evidence") / "pull-bundles"

AUTOMATION_LOGINS = {
    "chatgpt-codex-connector",
    "claude",
    "claude[bot]",
    "coderabbitai",
    "github-actions",
    "github-actions[bot]",
    "gemini-code-assist",
    "mergify",
    "pre-commit-ci[bot]",
    "dependabot[bot]",
    "renovate[bot]",
    "codecov[bot]",
    "coderabbitai[bot]",
    "copilot-pull-request-reviewer[bot]",
    "cursor",
    "vercel[bot]",
    "vllmellm",
    "web-flow",
}

STRONG_TERMS = {
    "accuracy",
    "alignment",
    "aligned",
    "attention",
    "autotune",
    "bank conflict",
    "b100",
    "b200",
    "benchmark",
    "bf16",
    "blackwell",
    "block",
    "cache",
    "coalesc",
    "compile",
    "correctness",
    "cuda",
    "cudagraph",
    "cute",
    "cutlass",
    "deadlock",
    "deepgemm",
    "dtype",
    "epilogue",
    "failing",
    "flash attention",
    "flashinfer",
    "fp4",
    "fp8",
    "gemm",
    "h100",
    "h200",
    "hang",
    "hopper",
    "kernel",
    "kv cache",
    "latency",
    "layout",
    "memory",
    "mla",
    "moe",
    "mxfp4",
    "nan",
    "nvfp4",
    "occupancy",
    "oom",
    "overflow",
    "perf",
    "performance",
    "pipeline",
    "ptx",
    "race",
    "regression",
    "register",
    "shared memory",
    "sm90",
    "sm100",
    "sm120",
    "speedup",
    "tensorrt",
    "tcgen05",
    "tile",
    "tiling",
    "tma",
    "tmem",
    "triton",
    "throughput",
    "vector",
    "warp",
    "wgmma",
}

LOW_SIGNAL_PATTERNS = (
    re.compile(r"^/[\w-]+(?:\s|$)"),
    re.compile(r"^thanks[!.]?$", re.I),
    re.compile(r"^thank you[!.]?$", re.I),
    re.compile(r"^lgtm\b", re.I),
    re.compile(r"^approved\b", re.I),
    re.compile(r"^done[!.]?$", re.I),
    re.compile(r"^fixed[!.]?$", re.I),
    re.compile(r"^updated[!.]?$", re.I),
    re.compile(r"^resolved[!.]?$", re.I),
    re.compile(r"^\[?(?:like|heart|thumbs[ -]?up)\]?", re.I),
    re.compile(r"reacted to your message", re.I),
)


@dataclass(frozen=True)
class PullTarget:
    repo_id: str
    repo: str
    pr: int
    title: str
    url: str
    source_page: Path
    bundle: Path
    created_at: str
    merged_at: str


def run_json(cmd: list[str], *, timeout: int = 180) -> dict[str, Any] | list[Any]:
    result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        msg = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(msg or f"command failed: {' '.join(cmd)}")
    return json.loads(result.stdout or "{}")


def gh_graphql(owner: str, name: str, numbers: list[int], first: int) -> dict[str, Any]:
    aliases = []
    for number in numbers:
        alias = f"pr{number}"
        aliases.append(
            f"""
            {alias}: pullRequest(number: {number}) {{
              number
              title
              url
              createdAt
              mergedAt
              author {{ login }}
              comments(first: {first}) {{
                totalCount
                nodes {{
                  author {{ login }}
                  createdAt
                  updatedAt
                  url
                  body
                  isMinimized
                  minimizedReason
                }}
              }}
              reviews(first: {first}) {{
                totalCount
                nodes {{
                  author {{ login }}
                  state
                  submittedAt
                  url
                  body
                }}
              }}
              reviewThreads(first: {first}) {{
                totalCount
                nodes {{
                  isResolved
                  isOutdated
                  comments(first: {first}) {{
                    totalCount
                    nodes {{
                      author {{ login }}
                      createdAt
                      updatedAt
                      url
                      path
                      line
                      originalLine
                      body
                    }}
                  }}
                }}
              }}
            }}
            """
        )
    query = (
        "query($owner:String!, $name:String!) {"
        "  repository(owner:$owner, name:$name) {"
        + "\n".join(aliases)
        + "  }"
        "  rateLimit { remaining cost resetAt }"
        "}"
    )
    data = run_json(
        [
            "gh",
            "api",
            "graphql",
            "-f",
            f"owner={owner}",
            "-f",
            f"name={name}",
            "-f",
            f"query={query}",
        ],
        timeout=240,
    )
    if not isinstance(data, dict):
        raise RuntimeError("unexpected GraphQL response")
    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"], ensure_ascii=False))
    return data.get("data") or {}


def gh_json_paginated(path: str) -> list[dict[str, Any]]:
    result = subprocess.run(
        ["gh", "api", "--paginate", path],
        check=False,
        capture_output=True,
        text=True,
        timeout=240,
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


def repo_owner_name(repo: str) -> tuple[str, str]:
    owner, name = repo.split("/", 1)
    return owner, name


def rel_to_root(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def bundle_path(root: Path, source: Path, meta: dict[str, Any]) -> Path:
    if meta.get("artifact_dir"):
        return root / str(meta["artifact_dir"])
    return root / PULL_BUNDLE_ROOT / source.parent.name / f"gh-{meta.get('pr')}"


def load_targets(root: Path, args: argparse.Namespace) -> list[PullTarget]:
    out: list[PullTarget] = []
    for source in sorted((root / "sources" / "prs").glob("*/*.md")):
        repo_id = source.parent.name
        if args.repo_id and repo_id not in args.repo_id:
            continue
        page = parse_markdown(source)
        meta = page.meta
        if not meta:
            continue
        pr = int(meta.get("pr"))
        if args.pr and pr not in args.pr:
            continue
        repo = str(meta.get("repo") or "")
        if args.repo and repo not in args.repo:
            continue
        bundle = bundle_path(root, source, meta)
        if not bundle.is_dir():
            continue
        if (bundle / DISCUSSION_NAME).exists() and not args.force:
            continue
        created_at = ""
        merged_at = str(meta.get("merged_at") or "")
        upstream_path = bundle / "upstream.json"
        if upstream_path.is_file():
            try:
                pull = (json.loads(upstream_path.read_text(encoding="utf-8")).get("pull") or {})
                created_at = str(pull.get("created_at") or "")
                merged_at = str(pull.get("merged_at") or merged_at)
            except json.JSONDecodeError:
                pass
        out.append(
            PullTarget(
                repo_id=repo_id,
                repo=repo,
                pr=pr,
                title=str(meta.get("title") or f"PR-{pr}"),
                url=str(meta.get("url") or f"https://github.com/{repo}/pull/{pr}"),
                source_page=source,
                bundle=bundle,
                created_at=created_at,
                merged_at=merged_at,
            )
        )
    return out


def author_login(node: dict[str, Any], rest_key: str = "user") -> str:
    author = node.get("author")
    if isinstance(author, dict) and author.get("login"):
        return str(author["login"])
    user = node.get(rest_key)
    if isinstance(user, dict) and user.get("login"):
        return str(user["login"])
    return "unknown"


def is_automation(login: str) -> bool:
    low = login.lower()
    return low in AUTOMATION_LOGINS or low.endswith("[bot]") or "bot" in low


def clean_body(body: str | None) -> str:
    if not body:
        return ""
    text = str(body)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]*\)", " ", text)
    text = re.sub(r"[*_>#|~]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def excerpt(body: str | None, max_words: int = 24) -> str:
    text = clean_body(body)
    if not text:
        return ""
    words = text.split()
    clipped = " ".join(words[:max_words])
    if len(words) > max_words:
        clipped += " ..."
    return clipped


def signal_terms(text: str) -> list[str]:
    low = text.lower()
    hits = [term for term in sorted(STRONG_TERMS) if term in low]
    return hits[:8]


def low_signal(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    return any(pattern.search(stripped) for pattern in LOW_SIGNAL_PATTERNS)


REVIEW_ACTION_TERMS = {
    "add",
    "avoid",
    "because",
    "benchmark",
    "break",
    "bug",
    "can",
    "check",
    "consider",
    "correct",
    "fail",
    "fix",
    "guard",
    "issue",
    "move",
    "need",
    "prefer",
    "regression",
    "remove",
    "should",
    "test",
    "update",
    "why",
    "would",
}


def is_substantive_review_text(item: dict[str, Any], text: str, terms: list[str]) -> bool:
    if low_signal(text):
        return False
    words = text.split()
    if len(words) < 4:
        return False
    low = text.lower()
    if terms:
        return True
    if item.get("kind") == "inline":
        if len(words) >= 6:
            return True
        return any(term in low for term in REVIEW_ACTION_TERMS)
    if item.get("kind") == "review" and item.get("state") in {"CHANGES_REQUESTED", "COMMENTED"}:
        return len(words) >= 6
    if len(words) >= 18 and any(term in low for term in REVIEW_ACTION_TERMS):
        return True
    return False


def score_item(item: dict[str, Any]) -> int:
    text = clean_body(item.get("body"))
    terms = signal_terms(text + " " + str(item.get("path") or ""))
    score = len(terms) * 3
    if item.get("kind") == "review" and item.get("state") in {"CHANGES_REQUESTED", "COMMENTED"}:
        score += 4
    if item.get("kind") == "inline":
        score += 2
    if len(text) > 100:
        score += 1
    if low_signal(text):
        score -= 4
    if is_automation(str(item.get("author") or "")):
        score -= 6
    return score


def in_review_window(item: dict[str, Any], merged_at: str) -> bool:
    if not merged_at:
        return True
    created_at = str(item.get("created_at") or "")
    if not created_at:
        return True
    return created_at <= merged_at


def graph_issue_comments(pr_data: dict[str, Any]) -> tuple[list[dict[str, Any]], bool, int]:
    conn = pr_data.get("comments") or {}
    nodes = conn.get("nodes") or []
    total = int(conn.get("totalCount") or len(nodes))
    rows = [
        {
            "kind": "issue",
            "author": author_login(node),
            "created_at": node.get("createdAt") or "",
            "url": node.get("url") or "",
            "body": node.get("body") or "",
            "is_minimized": bool(node.get("isMinimized")),
            "minimized_reason": node.get("minimizedReason") or "",
        }
        for node in nodes
    ]
    return rows, len(rows) >= total, total


def graph_reviews(pr_data: dict[str, Any]) -> tuple[list[dict[str, Any]], bool, int]:
    conn = pr_data.get("reviews") or {}
    nodes = conn.get("nodes") or []
    total = int(conn.get("totalCount") or len(nodes))
    rows = [
        {
            "kind": "review",
            "author": author_login(node),
            "created_at": node.get("submittedAt") or "",
            "url": node.get("url") or "",
            "body": node.get("body") or "",
            "state": node.get("state") or "",
        }
        for node in nodes
    ]
    return rows, len(rows) >= total, total


def graph_inline_comments(pr_data: dict[str, Any]) -> tuple[list[dict[str, Any]], bool, int, dict[str, int]]:
    conn = pr_data.get("reviewThreads") or {}
    threads = conn.get("nodes") or []
    total_threads = int(conn.get("totalCount") or len(threads))
    rows: list[dict[str, Any]] = []
    complete = len(threads) >= total_threads
    thread_state = Counter()
    for thread in threads:
        if thread.get("isResolved"):
            thread_state["resolved"] += 1
        if thread.get("isOutdated"):
            thread_state["outdated"] += 1
        comments = (thread.get("comments") or {})
        nodes = comments.get("nodes") or []
        total = int(comments.get("totalCount") or len(nodes))
        if len(nodes) < total:
            complete = False
        for node in nodes:
            rows.append(
                {
                    "kind": "inline",
                    "author": author_login(node),
                    "created_at": node.get("createdAt") or "",
                    "url": node.get("url") or "",
                    "body": node.get("body") or "",
                    "path": node.get("path") or "",
                    "line": node.get("line") or node.get("originalLine") or "",
                    "thread_resolved": bool(thread.get("isResolved")),
                    "thread_outdated": bool(thread.get("isOutdated")),
                }
            )
    return rows, complete, len(rows), dict(thread_state)


def rest_issue_comments(repo: str, pr: int) -> list[dict[str, Any]]:
    rows = gh_json_paginated(f"repos/{repo}/issues/{pr}/comments?per_page=100")
    return [
        {
            "kind": "issue",
            "author": author_login(row),
            "created_at": row.get("created_at") or "",
            "url": row.get("html_url") or "",
            "body": row.get("body") or "",
        }
        for row in rows
    ]


def rest_reviews(repo: str, pr: int) -> list[dict[str, Any]]:
    rows = gh_json_paginated(f"repos/{repo}/pulls/{pr}/reviews?per_page=100")
    return [
        {
            "kind": "review",
            "author": author_login(row),
            "created_at": row.get("submitted_at") or "",
            "url": row.get("html_url") or "",
            "body": row.get("body") or "",
            "state": row.get("state") or "",
        }
        for row in rows
    ]


def rest_inline_comments(repo: str, pr: int) -> list[dict[str, Any]]:
    rows = gh_json_paginated(f"repos/{repo}/pulls/{pr}/comments?per_page=100")
    return [
        {
            "kind": "inline",
            "author": author_login(row),
            "created_at": row.get("created_at") or "",
            "url": row.get("html_url") or "",
            "body": row.get("body") or "",
            "path": row.get("path") or "",
            "line": row.get("line") or row.get("original_line") or "",
        }
        for row in rows
    ]


def render_discussion_bullets(
    target: PullTarget,
    pr_data: dict[str, Any],
    issue_comments: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
    inline_comments: list[dict[str, Any]],
) -> str:
    all_rows = issue_comments + reviews + inline_comments
    candidates: list[dict[str, Any]] = []
    merged_at = target.merged_at or str(pr_data.get("mergedAt") or "")
    for row in all_rows:
        if not in_review_window(row, merged_at):
            continue
        if is_automation(str(row.get("author") or "")):
            continue
        text = clean_body(row.get("body"))
        terms = signal_terms(text + " " + str(row.get("path") or ""))
        if not is_substantive_review_text(row, text, terms):
            continue
        item = dict(row)
        item["text"] = text
        item["terms"] = terms
        item["score"] = score_item(row)
        candidates.append(item)

    if not candidates:
        return ""

    candidates.sort(key=lambda item: str(item.get("created_at") or ""))
    lines: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    for item in candidates:
        text = excerpt(item.get("body"), max_words=42)
        if not text:
            continue
        key = (str(item.get("path") or ""), text)
        if key in seen:
            continue
        seen.add(key)
        author = str(item.get("author") or "unknown")
        created_at = str(item.get("created_at") or "unknown")
        date = created_at[:10] if created_at != "unknown" else created_at
        path = str(item.get("path") or "")
        line = str(item.get("line") or "")
        location = f" on `{path}`" if path else ""
        if path and line:
            location += f":{line}"
        state = str(item.get("state") or "")
        state_text = f" {state.lower()}" if state else ""
        url = str(item.get("url") or target.url)
        lines.append(f"- {date} `{author}`{state_text}{location}: {text} ({url})")
    lines.append("")
    return "\n".join(lines)


def fetch_overflows(
    target: PullTarget,
    issue_comments: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
    inline_comments: list[dict[str, Any]],
    issue_complete: bool,
    reviews_complete: bool,
    inline_complete: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, str]]:
    completeness = {
        "issue_comments": "complete",
        "reviews": "complete",
        "inline_comments": "complete",
    }
    if not issue_complete:
        issue_comments = rest_issue_comments(target.repo, target.pr)
        completeness["issue_comments"] = "complete via REST overflow fallback"
    if not reviews_complete:
        reviews = rest_reviews(target.repo, target.pr)
        completeness["reviews"] = "complete via REST overflow fallback"
    if not inline_complete:
        inline_comments = rest_inline_comments(target.repo, target.pr)
        completeness["inline_comments"] = "complete via REST overflow fallback"
    return issue_comments, reviews, inline_comments, completeness


def write_one(root: Path, target: PullTarget, pr_data: dict[str, Any], args: argparse.Namespace) -> str:
    issue_comments, issue_complete, _issue_total = graph_issue_comments(pr_data)
    reviews, reviews_complete, _review_total = graph_reviews(pr_data)
    inline_comments, inline_complete, _inline_total, thread_state = graph_inline_comments(pr_data)
    issue_comments, reviews, inline_comments, _completeness = fetch_overflows(
        target,
        issue_comments,
        reviews,
        inline_comments,
        issue_complete,
        reviews_complete,
        inline_complete,
    )
    _ = thread_state
    text = render_discussion_bullets(
        target,
        pr_data,
        issue_comments,
        reviews,
        inline_comments,
    )
    if args.dry_run:
        action = "write" if text else "delete"
        print(f"would {action} {rel_to_root(root, target.bundle / DISCUSSION_NAME)}")
        return "written" if text else "deleted"
    path = target.bundle / DISCUSSION_NAME
    if text:
        path.write_text(text, encoding="utf-8")
        return "written"
    if path.exists():
        path.unlink()
        return "deleted"
    return "skipped_empty"


def grouped_batches(targets: list[PullTarget], batch_size: int):
    by_repo: dict[str, list[PullTarget]] = defaultdict(list)
    for target in targets:
        by_repo[target.repo].append(target)
    for repo in sorted(by_repo):
        group = by_repo[repo]
        for idx in range(0, len(group), batch_size):
            yield repo, group[idx : idx + batch_size]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-id", action="append", help="Limit to local repo id, e.g. vllm")
    parser.add_argument("--repo", action="append", help="Limit to GitHub repo, e.g. vllm-project/vllm")
    parser.add_argument("--pr", action="append", type=int, help="Limit to PR number; repeatable")
    parser.add_argument("--limit", type=int, default=0, help="Stop after N digests")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--first", type=int, default=100, help="GraphQL page size before REST overflow fallback")
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.first < 1 or args.first > 100:
        parser.error("--first must be between 1 and 100")
    if args.batch_size < 1:
        parser.error("--batch-size must be positive")

    root = knowledge_root()
    targets = load_targets(root, args)
    if args.limit:
        targets = targets[: args.limit]

    stats = Counter()
    failed = 0
    for repo, batch in grouped_batches(targets, args.batch_size):
        owner, name = repo_owner_name(repo)
        numbers = [target.pr for target in batch]
        try:
            data = gh_graphql(owner, name, numbers, args.first)
            repo_data = data.get("repository") or {}
            rate = data.get("rateLimit") or {}
            for target in batch:
                pr_data = repo_data.get(f"pr{target.pr}")
                if not pr_data:
                    raise RuntimeError(f"missing GraphQL PR payload for {target.repo}#{target.pr}")
                status = write_one(root, target, pr_data, args)
                stats[status] += 1
                print(f"discussion: {target.repo}#{target.pr} {status}")
            if rate:
                remaining = rate.get("remaining")
                if isinstance(remaining, int) and remaining < 250:
                    print(f"WARN: low GitHub GraphQL quota remaining={remaining}, resetAt={rate.get('resetAt')}", file=sys.stderr)
            if args.sleep:
                time.sleep(args.sleep)
        except Exception as exc:  # keep resumable for large corpus refreshes
            failed += len(batch)
            print(f"failed batch {repo} {numbers}: {exc}", file=sys.stderr)

    print(
        json.dumps(
            {
                "written": stats["written"],
                "deleted": stats["deleted"],
                "skipped_empty": stats["skipped_empty"],
                "failed": failed,
            },
            indent=2,
        )
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
