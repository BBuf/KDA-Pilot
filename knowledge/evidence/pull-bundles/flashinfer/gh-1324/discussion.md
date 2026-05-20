# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1324](https://github.com/flashinfer-ai/flashinfer/pull/1324)
- Source page: `sources/prs/flashinfer/PR-1324.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1324`
- Generated at: `2026-05-20T15:22:20.891076+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-25T00:45:42Z`
- Merged: `2025-07-30T09:44:22Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: Edenzzzz, happierpig, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-25T00:46:12Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Edenzzzz, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1324#pullrequestreview-3053719597)
- `2025-07-25T00:47:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for logits soft cap and removes the max packed qo lens ... (https://github.com/flashinfer-ai/flashinfer/pull/1324#pullrequestreview-3053720888)
- `2025-07-25T00:51:28Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1324#pullrequestreview-3053725025)
- `2025-07-25T11:45:21Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1324#pullrequestreview-3055102310)

## Inline Comment Hotspots

- `flashinfer/attention.py`: 2 inline comment(s)
- `include/flashinfer/attention/scheduler.cuh`: 2 inline comment(s)
- `include/flashinfer/attention/persistent.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-25T00:51:28Z` `inline` by `Edenzzzz` `include/flashinfer/attention/persistent.cuh`:305; signals: attention, flashinfer; excerpt: "Seems no need to guard with something like LOOP SPLIT MASK because the func uses static if else branch? Feel free to suggest" (https://github.com/flashinfer-ai/flashinfer/pull/1324#discussion_r2229866259)
- `2025-07-25T00:52:13Z` `issue` by `happierpig`; signals: cuda, kernel; excerpt: "@Edenzzzz IMO, the constant buffer size, starting with max is for cuda graph-compatiable. Only by keeping the same offsets, the same pointer can be ..." (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3115439888)
- `2025-07-25T00:54:20Z` `issue` by `Edenzzzz`; signals: cuda, kernel; excerpt: "@Edenzzzz IMO, the constant buffer size, starting with max is for cuda graph-compatiable. Only by keeping the same offsets, the same pointer can be ..." (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3115442834)
- `2025-07-25T05:10:11Z` `issue` by `Edenzzzz`; signals: compile, kernel; excerpt: "Now the kernel compiles and runs fine. ADDITIONAL FUNC PARAMS was buggy due to the use of params[i] in persistent launch" (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3116413013)
- `2025-07-25T11:46:50Z` `issue` by `yzh119`; signals: kernel; excerpt: "ADDITIONAL FUNC PARAMS was buggy due to the use of params[i] in persistent launch We should figure out a more elegant solution for additional ..." (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3117491057)
- `2025-07-30T09:44:13Z` `issue` by `yzh119`; signals: attention; excerpt: "@yzh119 tests/test batch attention.py now passes. Should we add tests to the CI build at some point? Sure I'll create a PR for that." (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3135564924)
- `2025-07-25T14:41:01Z` `issue` by `Edenzzzz`; signals: failing; excerpt: "Precision is failing for logits soft cap, still investigating" (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3118193282)
- `2025-07-25T19:29:25Z` `issue` by `Edenzzzz`; signals: attention; excerpt: "@yzh119 tests/test batch attention.py now passes. Should we add tests to the CI build at some point?" (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3120089455)
- `2025-07-25T22:20:01Z` `issue` by `Edenzzzz`; signals: general review; excerpt: "I increased max total num works to 65536 because under input len 8192, output len 400 and 8 reqs/s, this breaks in SGlang. Maybe ..." (https://github.com/flashinfer-ai/flashinfer/pull/1324#issuecomment-3120548176)
