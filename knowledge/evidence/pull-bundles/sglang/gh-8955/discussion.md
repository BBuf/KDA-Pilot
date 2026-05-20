# PR Discussion Digest

- Source PR: [sgl-project/sglang#8955](https://github.com/sgl-project/sglang/pull/8955)
- Source page: `sources/prs/sglang/PR-8955.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8955`
- Generated at: `2026-05-20T15:31:30.301645+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-08T07:39:55Z`
- Merged: `2025-08-08T08:12:33Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: ch-wan, fzyzcjy, kaixih
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-08-08T07:40:10Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @kaixih, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8955#pullrequestreview-3099776840)
- `2025-08-08T07:43:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a crash on Blackwell hardware by providing a Python implementation for scale ... (https://github.com/sgl-project/sglang/pull/8955#pullrequestreview-3099785817)
- `2025-08-08T08:10:59Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8955#pullrequestreview-3099858673)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-08-08T07:42:09Z` `issue` by `kaixih`; signals: accuracy, flashinfer, moe; excerpt: "Accuracy test: sglang (pretrained=/model/models--deepseek-ai--DeepSeek-R1-0528/snapshots/4236a6af538feda4548eca9ab308586007567f52/,trust remote code=True,tp size=8,ep size=8,max model len=32768,add bos token=True,enable flashinfer trtllm moe=False,disable shared experts fusion=True), gen kwargs: (None), limit: None, num ..." (https://github.com/sgl-project/sglang/pull/8955#issuecomment-3166880757)
