# PR Discussion Digest

- Source PR: [sgl-project/sglang#15835](https://github.com/sgl-project/sglang/pull/15835)
- Source page: `sources/prs/sglang/PR-15835.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15835`
- Generated at: `2026-05-20T15:28:16.768055+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-25T15:00:25Z`
- Merged: `2025-12-28T03:53:50Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 9
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: BBuf, DarkSharpness, merrymercy, mickqian
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-12-25T15:06:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a JIT fused QK norm kernel, which significantly improves performance, especially for ... (https://github.com/sgl-project/sglang/pull/15835#pullrequestreview-3612425542)
- `2025-12-26T01:40:04Z` `APPROVED` by `BBuf` - LGTM. (https://github.com/sgl-project/sglang/pull/15835#pullrequestreview-3612614505)
- `2025-12-26T14:14:25Z` `COMMENTED` by `BBuf` - It seems that the kUsePDL template parameter in the JIT kernel doesn't automatically enable or disable itself based ... (https://github.com/sgl-project/sglang/pull/15835#pullrequestreview-3613532715)
- `2025-12-26T14:18:37Z` `APPROVED` by `BBuf` - Great job. apporved! (https://github.com/sgl-project/sglang/pull/15835#pullrequestreview-3613546525)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/norm.cuh`: 4 inline comment(s)
- `python/sglang/jit_kernel/benchmark/bench_qknorm.py`: 2 inline comment(s)
- `python/sglang/jit_kernel/norm.py`: 2 inline comment(s)
- `python/sglang/jit_kernel/tests/test_qknorm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-26T14:14:25Z` `review` `COMMENTED` by `BBuf`; signals: kernel; excerpt: "It seems that the kUsePDL template parameter in the JIT kernel doesn't automatically enable or disable itself based on GPU architecture?" (https://github.com/sgl-project/sglang/pull/15835#pullrequestreview-3613532715)
- `2025-12-26T14:07:38Z` `inline` by `BBuf` `python/sglang/jit_kernel/csrc/norm.cuh`:168; signals: kernel; excerpt: "Can you add a comment for this line, I can't easily understand now." (https://github.com/sgl-project/sglang/pull/15835#discussion_r2648291364)
- `2025-12-26T14:10:12Z` `inline` by `BBuf` `python/sglang/jit_kernel/tests/test_qknorm.py`:66; signals: kernel; excerpt: "Add a torch.float16 is better" (https://github.com/sgl-project/sglang/pull/15835#discussion_r2648296130)
