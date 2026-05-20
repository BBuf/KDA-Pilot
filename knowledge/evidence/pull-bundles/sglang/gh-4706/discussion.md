# PR Discussion Digest

- Source PR: [sgl-project/sglang#4706](https://github.com/sgl-project/sglang/pull/4706)
- Source page: `sources/prs/sglang/PR-4706.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4706`
- Generated at: `2026-05-20T15:30:15.210062+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-24T04:00:53Z`
- Merged: `2025-03-27T08:42:29Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 6 (commented=6)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=1
- Human participants with discussion text: WineChord, hebiao064, yiakwy-xpu-ml-framework-team, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-03-24T05:40:13Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4706#pullrequestreview-2709171588)
- `2025-03-25T05:59:03Z` `COMMENTED` by `WineChord` (https://github.com/sgl-project/sglang/pull/4706#pullrequestreview-2712454132)
- `2025-03-26T06:47:50Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4706#pullrequestreview-2716057411)
- `2025-03-26T21:35:25Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4706#pullrequestreview-2718670352)

## Inline Comment Hotspots

- `sgl-kernel/pyproject_rocm.toml`: 2 inline comment(s)
- `sgl-kernel/CMakeLists.txt`: 2 inline comment(s)
- `sgl-kernel/include/utils.h`: 2 inline comment(s)
- `.github/workflows/pr-test-amd.yml`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-25T05:58:59Z` `inline` by `WineChord` `sgl-kernel/CMakeLists.txt`:138; signals: hang, kernel; excerpt: "The file name has been changed to per token group quant 8bit in main branch." (https://github.com/sgl-project/sglang/pull/4706#discussion_r2011366477)
- `2025-03-27T08:09:31Z` `issue` by `zhyncs`; signals: deepgemm, gemm; excerpt: "manylinux2014 x86 64 is only used for PyPI. Use this workaround for DeepGEMM Sampling tiny differences can be ignored for now. All of these ..." (https://github.com/sgl-project/sglang/pull/4706#issuecomment-2757081473)
- `2025-03-24T05:40:13Z` `inline` by `zhyncs` `.github/workflows/pr-test-amd.yml`:50; signals: kernel; excerpt: "Currently AMD's sgl-kernel has not been adapted for CMake yet, hai @HaiShaw and bruce @BruceXcluding need to follow up. Thanks!" (https://github.com/sgl-project/sglang/pull/4706#discussion_r2009492362)
- `2025-03-26T06:47:50Z` `inline` by `hebiao064` `sgl-kernel/CMakeLists.txt`:138; signals: kernel; excerpt: "resolved, thanks" (https://github.com/sgl-project/sglang/pull/4706#discussion_r2013489224)
