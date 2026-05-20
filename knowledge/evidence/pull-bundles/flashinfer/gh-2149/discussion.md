# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2149](https://github.com/flashinfer-ai/flashinfer/pull/2149)
- Source page: `sources/prs/flashinfer/PR-2149.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2149`
- Generated at: `2026-05-20T15:24:14.109039+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-28T08:55:19Z`
- Merged: `2025-12-04T17:56:43Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: aleozlx, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-28T08:57:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables the sm103 moe dsl backend and updates the nvidia-cutlass-dsl dependency. The changes ... (https://github.com/flashinfer-ai/flashinfer/pull/2149#pullrequestreview-3518006165)
- `2025-11-28T09:00:07Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (3) tests/gemm/test cute dsl blockscaled gemm.py (1) 83-88: Device capability gating ... (https://github.com/flashinfer-ai/flashinfer/pull/2149#pullrequestreview-3518016018)
- `2025-11-28T09:07:50Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2149#pullrequestreview-3518046677)
- `2025-11-29T07:33:42Z` `APPROVED` by `yzh119` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/2149#pullrequestreview-3520543343)

## Inline Comment Hotspots

- `flashinfer/cute_dsl/blockscaled_gemm.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-11-28T09:00:07Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, block, cute, cutlass, flashinfer, gemm, hang, kernel; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (3) tests/gemm/test cute dsl blockscaled gemm.py (1) 83-88: Device capability gating correctly adds sm 103; consider de‑duplicating ..." (https://github.com/flashinfer-ai/flashinfer/pull/2149#pullrequestreview-3518016018)
- `2025-11-28T08:55:30Z` `issue` by `coderabbitai`; signals: attention, block, correctness, cute, cutlass, flashinfer, gemm, hang; excerpt: "Walkthrough This change extends SM architecture support for BlockScaledPersistentDenseGemmKernel to include sm 103 with a temporary shared memory capacity workaround, updates the CUTLASS DSL ..." (https://github.com/flashinfer-ai/flashinfer/pull/2149#issuecomment-3588428705)
- `2025-11-28T09:07:50Z` `inline` by `aleozlx` `flashinfer/cute_dsl/blockscaled_gemm.py`:569; signals: block, cute, cutlass, flashinfer, gemm, kernel; excerpt: "this get smem capacity in bytes issue has been reported to cutlass team internally, if there is a quick turn around for this i'll ..." (https://github.com/flashinfer-ai/flashinfer/pull/2149#discussion_r2570910886)
- `2025-11-29T07:33:37Z` `inline` by `yzh119` `flashinfer/cute_dsl/blockscaled_gemm.py`:569; signals: block, cute, flashinfer, gemm, memory, shared memory; excerpt: "I have no problem with this at the moment, considering sm 100 and sm 103 should have the same shared memory size." (https://github.com/flashinfer-ai/flashinfer/pull/2149#discussion_r2572861704)
- `2025-11-28T09:06:17Z` `issue` by `aleozlx`; signals: block, cute, gemm; excerpt: "UT GB300 pytest tests/gemm/test cute dsl blockscaled gemm.py 256 passed, 128 xfailed, 768 warnings" (https://github.com/flashinfer-ai/flashinfer/pull/2149#issuecomment-3588464700)
