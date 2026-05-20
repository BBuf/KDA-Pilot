# PR Discussion Digest

- Source PR: [sgl-project/sglang#11287](https://github.com/sgl-project/sglang/pull/11287)
- Source page: `sources/prs/sglang/PR-11287.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11287`
- Generated at: `2026-05-20T15:27:23.459782+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-07T01:14:48Z`
- Merged: `2025-10-21T18:02:25Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: FlamingoPg, Kh4L, trevor-m
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-07T01:16:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively adds support for new NVIDIA SM architectures by generalizing the SM version ... (https://github.com/sgl-project/sglang/pull/11287#pullrequestreview-3307982937)
- `2025-10-09T00:37:32Z` `COMMENTED` by `Kh4L` (https://github.com/sgl-project/sglang/pull/11287#pullrequestreview-3316889513)
- `2025-10-09T00:37:40Z` `COMMENTED` by `Kh4L` (https://github.com/sgl-project/sglang/pull/11287#pullrequestreview-3316889647)
- `2025-10-09T00:40:17Z` `COMMENTED` by `Kh4L` (https://github.com/sgl-project/sglang/pull/11287#pullrequestreview-3316892120)
- `2025-10-21T16:39:46Z` `APPROVED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/11287#pullrequestreview-3361704559)

## Inline Comment Hotspots

- `sgl-kernel/csrc/gemm/nvfp4_quant.cuh`: 4 inline comment(s)
- `python/sglang/srt/utils/common.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-09T00:40:17Z` `inline` by `Kh4L` `sgl-kernel/csrc/gemm/nvfp4_quant.cuh`:53; signals: fp4, gemm, kernel, nvfp4, sm100; excerpt: "That's not right, sm100f is the family-specific target keeping the comment" (https://github.com/sgl-project/sglang/pull/11287#discussion_r2415302943)
- `2025-10-15T22:48:45Z` `issue` by `Kh4L`; signals: cache, cuda, perf, performance, throughput; excerpt: "Hello, we don’t currently have a Thor machine available for testing. Could you share the test results～ @FlamingoPg ``` $ curl -H "Content-Type: application/json" ..." (https://github.com/sgl-project/sglang/pull/11287#issuecomment-3408563036)
- `2025-10-09T00:37:40Z` `inline` by `Kh4L` `sgl-kernel/csrc/gemm/nvfp4_quant.cuh`:49; signals: fp4, gemm, kernel, nvfp4; excerpt: "Outdated" (https://github.com/sgl-project/sglang/pull/11287#discussion_r2415300672)
- `2025-10-09T00:37:32Z` `inline` by `Kh4L` `python/sglang/srt/utils/common.py`:413; signals: general review; excerpt: "Updated" (https://github.com/sgl-project/sglang/pull/11287#discussion_r2415300559)
- `2025-10-15T03:52:28Z` `issue` by `FlamingoPg`; signals: general review; excerpt: "Hello, we don’t currently have a Thor machine available for testing. Could you share the test results～" (https://github.com/sgl-project/sglang/pull/11287#issuecomment-3404416066)
