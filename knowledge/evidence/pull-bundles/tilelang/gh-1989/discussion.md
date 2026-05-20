# PR Discussion Digest

- Source PR: [tile-ai/tilelang#1989](https://github.com/tile-ai/tilelang/pull/1989)
- Source page: `sources/prs/tilelang/PR-1989.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-1989`
- Generated at: `2026-05-20T15:32:45.322019+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-28T04:31:06Z`
- Merged: `2026-04-15T16:22:14Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 2 (commented=2)
- Inline review comments: 6
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: coderabbitai, copilot-pull-request-reviewer
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-28T04:36:08Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) testing/python/tilelang/test tma load.py (1) 18-40: Use the official get kernel source() API instead of ... (https://github.com/tile-ai/tilelang/pull/1989#pullrequestreview-4024822717)
- `2026-03-28T04:37:00Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview Adds a focused Python regression test intended to prevent reintroducing the 1D TMA load compile-time ... (https://github.com/tile-ai/tilelang/pull/1989#pullrequestreview-4024824898)

## Inline Comment Hotspots

- `testing/python/tilelang/test_tma_load.py`: 6 inline comment(s)

## High-Signal Discussion

- `2026-03-28T04:37:00Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: compile, correctness, cuda, cute, hang, hopper, kernel, regression; excerpt: "Pull request overview Adds a focused Python regression test intended to prevent reintroducing the 1D TMA load compile-time signature mismatch reported in 1842 by ..." (https://github.com/tile-ai/tilelang/pull/1989#pullrequestreview-4024824898)
- `2026-03-28T04:31:20Z` `issue` by `coderabbitai`; signals: compile, correctness, cuda, hang, kernel, regression, tile, tma; excerpt: "[!CAUTION] Review failed The pull request is closed. ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : CHILL Plan ..." (https://github.com/tile-ai/tilelang/pull/1989#issuecomment-4146928521)
- `2026-03-28T04:37:00Z` `inline` by `copilot-pull-request-reviewer` `testing/python/tilelang/test_tma_load.py`:50; signals: block, dtype, kernel, regression, tile, tma; excerpt: "This kernel shape doesn’t mirror the reported repro in 1842 (single-CTA copy of a 1D tensor with length 7168 and float32). Using a tiled ..." (https://github.com/tile-ai/tilelang/pull/1989#discussion_r3004171954)
- `2026-03-28T04:36:08Z` `review` `COMMENTED` by `coderabbitai`; signals: compile, hang, kernel, tile, tma; excerpt: "🧹 Nitpick comments (1) testing/python/tilelang/test tma load.py (1) 18-40: Use the official get kernel source() API instead of probing internal attributes. The JITKernel object ..." (https://github.com/tile-ai/tilelang/pull/1989#pullrequestreview-4024822717)
- `2026-03-28T04:37:00Z` `inline` by `copilot-pull-request-reviewer` `testing/python/tilelang/test_tma_load.py`:58; signals: cuda, hopper, sm90, tile, tma; excerpt: "Hard-coding target="cuda -arch=sm 90a" can make the test fail on Hopper devices that are sm 90 but not sm 90a (your skip condition only ..." (https://github.com/tile-ai/tilelang/pull/1989#discussion_r3004171950)
- `2026-03-28T04:36:59Z` `inline` by `copilot-pull-request-reviewer` `testing/python/tilelang/test_tma_load.py`:46; signals: block, failing, tile, tma; excerpt: "threads=128 while copying BLOCK=256 elements is an unusual configuration for a simple 1D bulk copy (the original repro uses 256 threads). If the intent ..." (https://github.com/tile-ai/tilelang/pull/1989#discussion_r3004171917)
- `2026-03-28T04:37:00Z` `inline` by `copilot-pull-request-reviewer` `testing/python/tilelang/test_tma_load.py`:40; signals: compile, kernel, tile, tma; excerpt: "extract source() will always fail for tl.compile(...) results: JITKernel exposes get kernel source(), but does not have get source, module, or rt mod attributes. ..." (https://github.com/tile-ai/tilelang/pull/1989#discussion_r3004171927)
- `2026-03-28T04:37:00Z` `inline` by `copilot-pull-request-reviewer` `testing/python/tilelang/test_tma_load.py`:67; signals: compile, kernel, tile, tma; excerpt: "With out idx=[1], the default tvm ffi adapter wraps the kernel to accept only non-output tensors (here: only A) and allocate B internally. Calling ..." (https://github.com/tile-ai/tilelang/pull/1989#discussion_r3004171934)
- `2026-03-28T04:37:00Z` `inline` by `copilot-pull-request-reviewer` `testing/python/tilelang/test_tma_load.py`:56; signals: cuda, tile, tma; excerpt: "The test uses ad-hoc pytest.mark.skipif checks and a custom get device capability() helper. The repo already provides tilelang.testing.requires cuda and tilelang.testing.requires cuda compute version ..." (https://github.com/tile-ai/tilelang/pull/1989#discussion_r3004171943)
