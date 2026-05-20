# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1610](https://github.com/flashinfer-ai/flashinfer/pull/1610)
- Source page: `sources/prs/flashinfer/PR-1610.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1610`
- Generated at: `2026-05-20T15:23:03.875040+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-30T07:47:07Z`
- Merged: `2025-09-04T20:47:15Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: aleozlx, nvmbreughe, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-02T21:03:45Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3178117175)
- `2025-09-03T00:29:29Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3178559843)
- `2025-09-03T17:47:18Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3181757142)
- `2025-09-03T22:02:20Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3182661504)
- `2025-09-04T00:02:38Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3182925443)
- `2025-09-04T00:57:37Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3183010117)
- `2025-09-04T05:30:24Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3183484346)
- `2025-09-04T16:50:14Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3186203149)
- `2025-09-04T17:59:28Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1610#pullrequestreview-3186472037)

## Inline Comment Hotspots

- `csrc/gemm_groupwise_sm120.cu`: 7 inline comment(s)
- `flashinfer/gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-04T00:18:11Z` `issue` by `yzh119`; signals: gemm, hang, perf, sm100, sm120, tcgen05; excerpt: "There might be some misunderstanding of MmaSM here: we use it in sm100 gemm because sm100 supports tcgen05 and 2-cta mode (where 2 ctas ..." (https://github.com/flashinfer-ai/flashinfer/pull/1610#issuecomment-3251193531)
- `2025-09-03T22:02:20Z` `inline` by `yongwww` `csrc/gemm_groupwise_sm120.cu`:37; signals: gemm, sm120, tile; excerpt: "will run into static assertion failed with "Scale Granularity M must evenly divide the tile shape M."" (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2320323517)
- `2025-09-04T00:02:38Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:37; signals: gemm, sm120, tile; excerpt: "This error should only happend when ScaleGranularityM == 128 and TileShapeM = 64: which is the case when MmaSM == 1 here: which you ..." (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2320501781)
- `2025-09-04T16:50:14Z` `inline` by `yongwww` `csrc/gemm_groupwise_sm120.cu`:38; signals: gemm, hang, sm120; excerpt: "Good catch! A divisor of 128 should be valid. I added scale granularity m=1 and scale granularity m=128, the change was:" (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2322787241)
- `2025-09-04T05:30:09Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:38; signals: gemm, hang, sm120; excerpt: "Is this still the case after your changes? If not, let's add 128 back." (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2320874939)
- `2025-09-02T21:01:58Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:526; signals: flashinfer, gemm; excerpt: "seems like this parameter is unused?" (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2317166658)
- `2025-09-03T00:29:28Z` `inline` by `yongwww` `flashinfer/gemm.py`:526; signals: flashinfer, gemm; excerpt: "Good catch. They’re part of TunableRunner, keeping them for consistency with the others." (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2317474301)
- `2025-09-03T17:32:28Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:70; signals: gemm, sm120; excerpt: "I don't understand this error message here, why MmaSM=2 will make M < 128?" (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2319706902)
- `2025-09-03T17:47:16Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:37; signals: gemm, sm120; excerpt: "Didn't see this constraint in what's the error message if you set it to 128?" (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2319736785)
- `2025-09-04T00:57:37Z` `inline` by `yongwww` `csrc/gemm_groupwise_sm120.cu`:37; signals: gemm, sm120; excerpt: "right. I used a standalone test (not in this pr) to trigger that error message. will go with the" (https://github.com/flashinfer-ai/flashinfer/pull/1610#discussion_r2320553258)
- `2025-09-04T02:29:51Z` `issue` by `yongwww`; signals: cutlass, gemm; excerpt: "Thanks, @yzh119, @nvmbreughe , @aleozlx for the helpful and insightful comments! I’ve incorporated them. Please take a look. For the PingPong gemm, I left ..." (https://github.com/flashinfer-ai/flashinfer/pull/1610#issuecomment-3251512663)
