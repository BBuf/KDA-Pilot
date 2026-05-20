# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1810](https://github.com/flashinfer-ai/flashinfer/pull/1810)
- Source page: `sources/prs/flashinfer/PR-1810.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1810`
- Generated at: `2026-05-20T15:23:26.766687+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T00:05:41Z`
- Merged: `2025-10-01T21:05:05Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: Yang-YiFan, jimmyzho, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-30T00:07:08Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly updates the tgv gemm function to support only the SM100 architecture and ... (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3282194637)
- `2025-09-30T00:09:36Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3282197343)
- `2025-09-30T00:13:25Z` `COMMENTED` by `jimmyzho` (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3282201657)
- `2025-09-30T00:54:06Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3282257555)
- `2025-09-30T03:08:09Z` `COMMENTED` by `Yang-YiFan` (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3282422832)
- `2025-09-30T19:05:51Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3286344380)
- `2025-10-01T00:23:07Z` `APPROVED` by `yzh119` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/1810#pullrequestreview-3287125036)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 7 inline comment(s)
- `tests/GEMM/test_tgv_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-30T19:04:30Z` `inline` by `yzh119` `flashinfer/gemm.py`:934; signals: b200, compile, flashinfer, gemm, sm100; excerpt: "Hi @jimmyzho we shouldn't use any gpu related functions inside gen module files because they are designed to be host-only (CPU machines can compile ..." (https://github.com/flashinfer-ai/flashinfer/pull/1810#discussion_r2392563851)
- `2025-09-30T00:54:06Z` `inline` by `yzh119` `flashinfer/gemm.py`:1017; signals: compile, flashinfer, gemm, kernel; excerpt: "sm 100 kernels should be compatible with sm 103 if compiled with sm 100f, but I believe these kernels haven't used sm 103 specific ..." (https://github.com/flashinfer-ai/flashinfer/pull/1810#discussion_r2389589753)
- `2025-09-30T00:09:33Z` `inline` by `yzh119` `flashinfer/gemm.py`:1017; signals: flashinfer, gemm, kernel; excerpt: "@yangs75 @yang-yifan have you tested with b300? I guess the kernel should also be compatible with sm 103?" (https://github.com/flashinfer-ai/flashinfer/pull/1810#discussion_r2389540916)
- `2025-09-30T03:08:09Z` `inline` by `Yang-YiFan` `flashinfer/gemm.py`:1017; signals: b200, flashinfer, gemm; excerpt: "Yeah it should work on B200 and B300 since it hasn’t used any sm103 specific features." (https://github.com/flashinfer-ai/flashinfer/pull/1810#discussion_r2389730038)
- `2025-09-30T19:05:48Z` `inline` by `yzh119` `flashinfer/gemm.py`:934; signals: flashinfer, gemm, sm100; excerpt: "sm100f nvcc flags is not defined in you can add another line there:" (https://github.com/flashinfer-ai/flashinfer/pull/1810#discussion_r2392570383)
- `2025-09-30T00:13:25Z` `inline` by `jimmyzho` `flashinfer/gemm.py`:1017; signals: flashinfer, gemm; excerpt: "I can confirm that the unit tests can pass with B300 - if they were meant to be compatible with SM103" (https://github.com/flashinfer-ai/flashinfer/pull/1810#discussion_r2389544641)
- `2025-10-01T06:05:02Z` `issue` by `yzh119`; signals: cuda; excerpt: "Another issue emerges, sm 100f is not available until cuda 12.9+" (https://github.com/flashinfer-ai/flashinfer/pull/1810#issuecomment-3354875026)
- `2025-10-01T18:01:52Z` `issue` by `yzh119`; signals: general review; excerpt: "Hi @jimmyzho I added some version checks in to fix the CI error, does that look good to you (some random files introduced in ..." (https://github.com/flashinfer-ai/flashinfer/pull/1810#issuecomment-3357482375)
