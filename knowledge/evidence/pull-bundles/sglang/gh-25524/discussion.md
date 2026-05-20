# PR Discussion Digest

- Source PR: [sgl-project/sglang#25524](https://github.com/sgl-project/sglang/pull/25524)
- Source page: `sources/prs/sglang/PR-25524.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25524`
- Generated at: `2026-05-20T15:29:50.227037+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-17T09:37:26Z`
- Merged: `2026-05-19T13:47:02Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: JustinTong0323, zRzRzRzRzRzRzR
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-17T09:39:05Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for GLM-4.7 speculative decoding and refactors environment variable management in the ... (https://github.com/sgl-project/sglang/pull/25524#pullrequestreview-4305239286)
- `2026-05-17T09:48:09Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/sgl-project/sglang/pull/25524#pullrequestreview-4305247540)
- `2026-05-19T13:10:52Z` `APPROVED` by `JustinTong0323` - Approved after manual verification on 4x H200 for GLM-4.7-FP8 with EAGLE/NextN speculative decoding on commit 821ce2f1ec95f4d3da64012c8bd5daa078b4d422.\n\nValidation notes:\n- Base ... (https://github.com/sgl-project/sglang/pull/25524#pullrequestreview-4319220805)

## Inline Comment Hotspots

- `python/sglang/srt/models/glm4_moe_nextn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-19T13:10:52Z` `review` `APPROVED` by `JustinTong0323`; signals: cuda, fp8, h200, moe; excerpt: "Approved after manual verification on 4x H200 for GLM-4.7-FP8 with EAGLE/NextN speculative decoding on commit 821ce2f1ec95f4d3da64012c8bd5daa078b4d422.\n\nValidation notes:\n- Base CI and NPU CI passed; PR ..." (https://github.com/sgl-project/sglang/pull/25524#pullrequestreview-4319220805)
- `2026-05-17T09:48:09Z` `inline` by `zRzRzRzRzRzRzR` `python/sglang/srt/models/glm4_moe_nextn.py`:172; signals: moe; excerpt: "fix with your suggestion" (https://github.com/sgl-project/sglang/pull/25524#discussion_r3254423827)
