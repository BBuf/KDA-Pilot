# PR Discussion Digest

- Source PR: [sgl-project/sglang#15514](https://github.com/sgl-project/sglang/pull/15514)
- Source page: `sources/prs/sglang/PR-15514.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15514`
- Generated at: `2026-05-20T15:28:12.959985+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-20T05:54:38Z`
- Merged: `2026-02-01T00:56:23Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Fridge003, b8zhong
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-06T01:45:32Z` `COMMENTED` by `b8zhong` - Added accuracy numbers too (https://github.com/sgl-project/sglang/pull/15514#pullrequestreview-3629026031)
- `2026-01-31T16:46:14Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15514#pullrequestreview-3732925906)
- `2026-01-31T22:03:25Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/15514#pullrequestreview-3733661774)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-04T10:24:45Z` `issue` by `Fridge003`; signals: deepgemm, flashinfer, gemm, kernel; excerpt: "@b8zhong Will the warmup process be handled by flashinfer for this case? We know that original deepgemm kernels need a lot of time for ..." (https://github.com/sgl-project/sglang/pull/15514#issuecomment-3707947590)
- `2026-01-06T01:03:24Z` `issue` by `b8zhong`; signals: compile, deepgemm, fp8, gemm; excerpt: "@Fridge003 I think, it uses the same DeepGEMM compiler under the hood. E.g during warmup you can see this process and a few similar ..." (https://github.com/sgl-project/sglang/pull/15514#issuecomment-3712665567)
- `2026-01-31T15:55:39Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8_utils.py`:139; signals: flashinfer, fp8, hang; excerpt: "Maybe change this variable to FLASHINFER TRTLLM to avoid confusion" (https://github.com/sgl-project/sglang/pull/15514#discussion_r2749696672)
- `2026-01-26T14:21:57Z` `issue` by `Fridge003`; signals: fp8, gemm, kernel; excerpt: "Can we add a test for this new fp8 gemm kernel" (https://github.com/sgl-project/sglang/pull/15514#issuecomment-3799857283)
- `2026-01-06T01:45:32Z` `review` `COMMENTED` by `b8zhong`; signals: accuracy; excerpt: "Added accuracy numbers too" (https://github.com/sgl-project/sglang/pull/15514#pullrequestreview-3629026031)
- `2026-01-31T22:03:25Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/fp8_utils.py`:139; signals: fp8; excerpt: "Sure. Done." (https://github.com/sgl-project/sglang/pull/15514#discussion_r2750096076)
