# PR Discussion Digest

- Source PR: [sgl-project/sglang#15551](https://github.com/sgl-project/sglang/pull/15551)
- Source page: `sources/prs/sglang/PR-15551.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15551`
- Generated at: `2026-05-20T15:28:12.968540+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-21T00:23:57Z`
- Merged: `2026-01-16T16:48:31Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Edenzzzz, Fridge003, Swipe4057, elvischenv, nvpohanh, zhyncs
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-12-21T00:25:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the flashinfer dependency to version 0.6.0. The changes are consistent across the ... (https://github.com/sgl-project/sglang/pull/15551#pullrequestreview-3601381572)
- `2026-01-08T07:16:21Z` `COMMENTED` by `elvischenv` - The Flashinfer MoE API breakage changes(remove tile tokens dim) should come together with this PR, otherwise the tests ... (https://github.com/sgl-project/sglang/pull/15551#pullrequestreview-3638062119)
- `2026-01-16T00:23:52Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/15551#pullrequestreview-3668209532)
- `2026-01-16T00:33:48Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/15551#pullrequestreview-3668228299)
- `2026-01-16T00:34:42Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/15551#pullrequestreview-3668229648)

## Inline Comment Hotspots

- `sgl-kernel/python/sgl_kernel/_fa4_interface.py`: 2 inline comment(s)
- `scripts/ci/ci_install_dependency.sh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-16T15:51:33Z` `issue` by `Fridge003`; signals: block, cache, cuda, failing, flashinfer, hang, kernel; excerpt: "Just checking this failing case: to be the only non flaky test) Seems the behavior of BatchDecodeWithPagedKVCacheWrapper in flashinfer backend has changed when upgrading ..." (https://github.com/sgl-project/sglang/pull/15551#issuecomment-3760702797)
- `2026-01-08T07:16:21Z` `review` `COMMENTED` by `elvischenv`; signals: flashinfer, hang, moe, tile; excerpt: "The Flashinfer MoE API breakage changes(remove tile tokens dim) should come together with this PR, otherwise the tests using Flashinfer MoE will fail." (https://github.com/sgl-project/sglang/pull/15551#pullrequestreview-3638062119)
- `2026-01-09T12:29:36Z` `issue` by `Fridge003`; signals: flashinfer, hang, moe, tile; excerpt: "The Flashinfer MoE API breakage changes(remove tile tokens dim) should come together with this PR, otherwise the tests using Flashinfer MoE will fail. Removed ..." (https://github.com/sgl-project/sglang/pull/15551#issuecomment-3728717721)
- `2026-01-16T00:34:42Z` `inline` by `zhyncs` `sgl-kernel/python/sgl_kernel/_fa4_interface.py`:4; signals: hang, kernel; excerpt: "We don't need to change this in the current PR as it will introduce unnecessary overhead for the kernel build." (https://github.com/sgl-project/sglang/pull/15551#discussion_r2696447314)
- `2026-01-08T08:19:11Z` `issue` by `Fridge003`; signals: block, kernel; excerpt: "We are currently blocked at the update of FA4 15182 Seems the FA kernels need to be upgraded first" (https://github.com/sgl-project/sglang/pull/15551#issuecomment-3722734199)
- `2026-01-12T08:29:27Z` `issue` by `nvpohanh`; signals: accuracy, flashinfer; excerpt: "Please be aware that FlashInfer v0.6.0 has a known TopK accuracy issue tracked in" (https://github.com/sgl-project/sglang/pull/15551#issuecomment-3737385320)
- `2026-01-14T05:55:52Z` `issue` by `nvpohanh`; signals: accuracy; excerpt: "@Fridge003 Could you update the version to 0.6.1? It fixed the topK accuracy issue in" (https://github.com/sgl-project/sglang/pull/15551#issuecomment-3747908349)
- `2026-01-16T16:18:01Z` `issue` by `Fridge003`; signals: perf, performance; excerpt: "/rerun-stage performance-test-2-gpu" (https://github.com/sgl-project/sglang/pull/15551#issuecomment-3760803033)
