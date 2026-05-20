# PR Discussion Digest

- Source PR: [sgl-project/sglang#11717](https://github.com/sgl-project/sglang/pull/11717)
- Source page: `sources/prs/sglang/PR-11717.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11717`
- Generated at: `2026-05-20T15:27:27.059334+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-16T10:25:11Z`
- Merged: `2025-10-22T04:17:50Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=0, outdated=5
- Human participants with discussion text: FlamingoPg, Fridge003
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-16T10:27:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates the FlashMLA library to add support for libtorch, which involves updating the ... (https://github.com/sgl-project/sglang/pull/11717#pullrequestreview-3344110615)
- `2025-10-22T03:24:55Z` `APPROVED` by `Fridge003` - Wonderful work! (https://github.com/sgl-project/sglang/pull/11717#pullrequestreview-3363565071)

## Inline Comment Hotspots

- `sgl-kernel/tests/test_flashmla.py`: 4 inline comment(s)
- `sgl-kernel/python/sgl_kernel/flash_mla.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-10-17T09:35:16Z` `issue` by `FlamingoPg`; signals: compile; excerpt: "Compile fixed, need upd tests." (https://github.com/sgl-project/sglang/pull/11717#issuecomment-3414653797)
- `2025-10-18T21:38:37Z` `issue` by `Fridge003`; signals: mla; excerpt: "@FlamingoPg What will be the size of wheel after integration of FlashMLA" (https://github.com/sgl-project/sglang/pull/11717#issuecomment-3418846420)
- `2025-10-20T06:40:17Z` `issue` by `FlamingoPg`; signals: mla; excerpt: "@FlamingoPg What will be the size of wheel after integration of FlashMLA About 10M" (https://github.com/sgl-project/sglang/pull/11717#issuecomment-3420763876)
- `2025-10-21T07:31:20Z` `issue` by `FlamingoPg`; signals: kernel; excerpt: "No need for flash attn varlen forward this kernel, this is a custom MHA forward kernel" (https://github.com/sgl-project/sglang/pull/11717#issuecomment-3425173388)
