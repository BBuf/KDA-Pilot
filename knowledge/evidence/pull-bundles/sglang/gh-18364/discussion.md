# PR Discussion Digest

- Source PR: [sgl-project/sglang#18364](https://github.com/sgl-project/sglang/pull/18364)
- Source page: `sources/prs/sglang/PR-18364.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18364`
- Generated at: `2026-05-20T15:28:38.514393+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-06T09:59:42Z`
- Merged: `2026-02-08T03:20:41Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: DarkSharpness, Fridge003, b8zhong
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-06T10:01:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a performance regression on Hopper GPUs caused by a recent flashinfer update, ... (https://github.com/sgl-project/sglang/pull/18364#pullrequestreview-3762017500)
- `2026-02-06T15:50:35Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18364#pullrequestreview-3763822963)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashinfer_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-06T13:19:45Z` `issue` by `DarkSharpness`; signals: sm100; excerpt: "QQ: will this select the right backend under SM100 Yes (at least for now). Currently, the default "auto" backend will only fallback to "fa3" ..." (https://github.com/sgl-project/sglang/pull/18364#issuecomment-3860410182)
- `2026-02-06T12:51:57Z` `issue` by `b8zhong`; signals: sm100; excerpt: "QQ: will this select the right backend under SM100" (https://github.com/sgl-project/sglang/pull/18364#issuecomment-3860282851)
