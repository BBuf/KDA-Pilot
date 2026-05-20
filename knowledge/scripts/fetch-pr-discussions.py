#!/usr/bin/env python3
"""Fetch and summarize PR review/discussion history for evidence bundles."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from _kb import parse_markdown
from _knowledge_root import knowledge_root


DISCUSSION_NAME = "discussion.md"
PULL_BUNDLE_ROOT = Path("evidence") / "pull-bundles"

AUTOMATION_LOGINS = {
    "github-actions",
    "github-actions[bot]",
    "gemini-code-assist",
    "pre-commit-ci[bot]",
    "dependabot[bot]",
    "renovate[bot]",
    "codecov[bot]",
    "coderabbitai[bot]",
    "copilot-pull-request-reviewer[bot]",
    "vercel[bot]",
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
    re.compile(r"^lgtm[!.]?$", re.I),
    re.compile(r"^approved[!.]?$", re.I),
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


def bullets(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items]


def render_digest(
    root: Path,
    target: PullTarget,
    pr_data: dict[str, Any],
    issue_comments: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
    inline_comments: list[dict[str, Any]],
    completeness: dict[str, Any],
    thread_state: dict[str, int],
) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()
    review_states = Counter(str(row.get("state") or "COMMENT").upper() for row in reviews)
    humans = sorted(
        {
            str(row.get("author"))
            for row in issue_comments + reviews + inline_comments
            if row.get("author") and not is_automation(str(row.get("author")))
        }
    )
    all_rows = issue_comments + reviews + inline_comments
    automation_count = sum(1 for row in all_rows if is_automation(str(row.get("author"))))
    post_merge_count = sum(1 for row in all_rows if not in_review_window(row, target.merged_at or str(pr_data.get("mergedAt") or "")))
    path_counts = Counter(str(row.get("path")) for row in inline_comments if row.get("path"))

    candidates: list[dict[str, Any]] = []
    merged_at = target.merged_at or str(pr_data.get("mergedAt") or "")
    for row in all_rows:
        if not in_review_window(row, merged_at):
            continue
        if is_automation(str(row.get("author") or "")):
            continue
        row_score = score_item(row)
        if row_score > 0:
            item = dict(row)
            item["score"] = row_score
            candidates.append(item)
    if not candidates:
        fallback = [
            row
            for row in all_rows
            if in_review_window(row, merged_at)
            if row.get("body") and not is_automation(str(row.get("author"))) and not low_signal(clean_body(row.get("body")))
        ]
        for row in fallback[:3]:
            item = dict(row)
            item["score"] = 0
            candidates.append(item)
    candidates.sort(key=lambda item: (-int(item.get("score") or 0), str(item.get("created_at") or "")))
    candidates = candidates[:12]

    lines = [
        "# PR Discussion Digest",
        "",
        f"- Source PR: [{target.repo}#{target.pr}]({target.url})",
        f"- Source page: `{rel_to_root(root, target.source_page)}`",
        f"- Evidence bundle: `{rel_to_root(root, target.bundle)}`",
        f"- Generated at: `{generated_at}`",
        "- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.",
        f"- Completeness: issue comments `{completeness['issue_comments']}`, reviews `{completeness['reviews']}`, inline comments `{completeness['inline_comments']}`.",
        "",
        "## Timeline",
        "",
        f"- Opened: `{target.created_at or pr_data.get('createdAt') or 'unknown'}`",
        f"- Merged: `{target.merged_at or pr_data.get('mergedAt') or 'unknown'}`",
        "",
        "## Discussion Counts",
        "",
    ]
    lines.extend(
        bullets(
            [
                f"Issue comments: {len(issue_comments)}",
                f"Review submissions: {len(reviews)} ({', '.join(f'{k.lower()}={v}' for k, v in sorted(review_states.items())) or 'no states'})",
                f"Inline review comments: {len(inline_comments)}",
                f"Review threads observed: {completeness.get('review_threads_observed', 0)}",
                f"Resolved/outdated thread markers: resolved={thread_state.get('resolved', 0)}, outdated={thread_state.get('outdated', 0)}",
                f"Human participants with discussion text: {', '.join(humans[:20]) if humans else 'none observed'}",
                f"Automation comments/reviews omitted from high-signal summary: {automation_count}",
                f"Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: {post_merge_count}",
            ]
        )
    )
    lines.extend(["", "## Review Decisions", ""])
    review_rows = [
        row
        for row in sorted(reviews, key=lambda item: str(item.get("created_at") or ""))
        if row.get("state") and in_review_window(row, merged_at)
    ]
    if review_rows:
        for row in review_rows[:24]:
            body = excerpt(row.get("body"), 18)
            suffix = f" - {body}" if body else ""
            lines.append(
                f"- `{row.get('created_at') or 'unknown'}` `{row.get('state')}` by `{row.get('author')}`{suffix} ({row.get('url') or target.url})"
            )
        if len(review_rows) > 24:
            lines.append(f"- ... {len(review_rows) - 24} additional review decision entries omitted from this digest.")
    else:
        lines.append("- No review submissions were returned by GitHub.")

    lines.extend(["", "## Inline Comment Hotspots", ""])
    if path_counts:
        for path, count in path_counts.most_common(12):
            lines.append(f"- `{path}`: {count} inline comment(s)")
    else:
        lines.append("- No inline review comments were returned by GitHub.")

    lines.extend(["", "## High-Signal Discussion", ""])
    if candidates:
        for item in candidates:
            text = excerpt(item.get("body"))
            if not text:
                continue
            terms = signal_terms(clean_body(item.get("body")) + " " + str(item.get("path") or ""))
            term_text = ", ".join(terms) if terms else "general review"
            path = f" `{item.get('path')}`" if item.get("path") else ""
            line = f":{item.get('line')}" if item.get("line") else ""
            state = f" `{item.get('state')}`" if item.get("state") else ""
            lines.append(
                f"- `{item.get('created_at') or 'unknown'}` `{item.get('kind')}`{state} by `{item.get('author')}`{path}{line}; signals: {term_text}; excerpt: \"{text}\" ({item.get('url') or target.url})"
            )
    else:
        lines.append("- No high-signal human discussion was captured; the PR discussion was empty or consisted of low-signal/automation-only comments.")
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


def write_one(root: Path, target: PullTarget, pr_data: dict[str, Any], args: argparse.Namespace) -> None:
    issue_comments, issue_complete, _issue_total = graph_issue_comments(pr_data)
    reviews, reviews_complete, _review_total = graph_reviews(pr_data)
    inline_comments, inline_complete, _inline_total, thread_state = graph_inline_comments(pr_data)
    issue_comments, reviews, inline_comments, completeness = fetch_overflows(
        target,
        issue_comments,
        reviews,
        inline_comments,
        issue_complete,
        reviews_complete,
        inline_complete,
    )
    completeness["review_threads_observed"] = int((pr_data.get("reviewThreads") or {}).get("totalCount") or 0)
    text = render_digest(
        root,
        target,
        pr_data,
        issue_comments,
        reviews,
        inline_comments,
        completeness,
        thread_state,
    )
    if args.dry_run:
        print(f"would write {rel_to_root(root, target.bundle / DISCUSSION_NAME)}")
        return
    (target.bundle / DISCUSSION_NAME).write_text(text, encoding="utf-8")


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

    written = failed = 0
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
                write_one(root, target, pr_data, args)
                written += 1
                print(f"discussion: {target.repo}#{target.pr}")
            if rate:
                remaining = rate.get("remaining")
                if isinstance(remaining, int) and remaining < 250:
                    print(f"WARN: low GitHub GraphQL quota remaining={remaining}, resetAt={rate.get('resetAt')}", file=sys.stderr)
            if args.sleep:
                time.sleep(args.sleep)
        except Exception as exc:  # keep resumable for large corpus refreshes
            failed += len(batch)
            print(f"failed batch {repo} {numbers}: {exc}", file=sys.stderr)

    print(json.dumps({"written": written, "failed": failed, "skipped_existing": 0}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
