# PR Discussion Digest

- Source PR: [sgl-project/sglang#13087](https://github.com/sgl-project/sglang/pull/13087)
- Source page: `sources/prs/sglang/PR-13087.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13087`
- Generated at: `2026-05-20T15:27:44.382040+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-11T16:21:39Z`
- Merged: `2025-11-13T20:45:22Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: FlamingoPg, Fridge003, HanHan009527, whybeyoung
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-11T16:24:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for a custom fp8 flashmla kernel by updating the FlashMLA dependency, ... (https://github.com/sgl-project/sglang/pull/13087#pullrequestreview-3448893092)
- `2025-11-13T20:45:11Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13087#pullrequestreview-3461612175)

## Inline Comment Hotspots

- `sgl-kernel/tests/test_flashmla.py`: 2 inline comment(s)
- `sgl-kernel/python/sgl_kernel/flash_mla.py`: 1 inline comment(s)
- `sgl-kernel/include/sgl_kernel_ops.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-12T17:46:29Z` `issue` by `FlamingoPg`; signals: cuda, kernel, mla; excerpt: "Hi, could I know why we're putting FlashMLA into the sglang kernel, and where I can see the related plans? Hi, @HanHan009527 We didn’t ..." (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3523142362)
- `2025-11-13T02:15:09Z` `issue` by `HanHan009527`; signals: cuda, kernel, mla; excerpt: "Hi, could I know why we're putting FlashMLA into the sglang kernel, and where I can see the related plans? Hi, @HanHan009527 We didn’t ..." (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3524831263)
- `2025-11-13T20:44:17Z` `issue` by `Fridge003`; signals: fp8, kernel, mla; excerpt: "Custom fp8 flashmla kernel is only covered in sgl-kernel test, so as long as this passes it will be OK" (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3529642137)
- `2025-11-12T16:42:12Z` `issue` by `HanHan009527`; signals: kernel, mla; excerpt: "Hi, could I know why we're putting FlashMLA into the sglang kernel, and where I can see the related plans?" (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3522865447)
- `2025-11-13T02:10:46Z` `issue` by `Fridge003`; signals: failing; excerpt: "@FlamingoPg This test seems failing" (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3524816855)
- `2025-11-13T09:56:26Z` `issue` by `FlamingoPg`; signals: kernel; excerpt: "sgl-kernel fixed." (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3526878508)
- `2025-11-12T17:48:08Z` `issue` by `FlamingoPg`; signals: general review; excerpt: "Do you have any concerns about this PR, or are there any other integration-related questions I can answer for you?" (https://github.com/sgl-project/sglang/pull/13087#issuecomment-3523148932)
