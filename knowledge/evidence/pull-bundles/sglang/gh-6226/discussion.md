# PR Discussion Digest

- Source PR: [sgl-project/sglang#6226](https://github.com/sgl-project/sglang/pull/6226)
- Source page: `sources/prs/sglang/PR-6226.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6226`
- Generated at: `2026-05-20T15:30:37.579014+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-12T10:05:42Z`
- Merged: `2025-09-08T05:05:35Z`

## Discussion Counts

- Issue comments: 30
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=7
- Human participants with discussion text: AniZpZ, FlamingoPg, WeiweiZhang1, mingfeima, wenhuach21, yiliu30, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-20T03:21:17Z` `APPROVED` by `FlamingoPg` - LGTM (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-2944444065)
- `2025-07-09T06:47:48Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3000255332)
- `2025-07-11T01:29:55Z` `COMMENTED` by `wenhuach21` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3008120639)
- `2025-07-11T01:30:08Z` `COMMENTED` by `wenhuach21` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3008121191)
- `2025-07-11T01:30:39Z` `COMMENTED` by `wenhuach21` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3008121866)
- `2025-07-11T01:31:13Z` `COMMENTED` by `wenhuach21` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3008122614)
- `2025-07-11T02:11:09Z` `COMMENTED` by `wenhuach21` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3008196196)
- `2025-07-11T02:12:21Z` `COMMENTED` by `wenhuach21` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3008197530)
- `2025-07-11T07:58:46Z` `APPROVED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/6226#pullrequestreview-3009102372)

## Inline Comment Hotspots

- `docs/backend/quantization.md`: 6 inline comment(s)
- `python/sglang/srt/layers/quantization/auto_round.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-06T09:36:40Z` `issue` by `yiliu30`; signals: accuracy, b200, fp4, hang, memory, mxfp4; excerpt: "Hi @zhyncs, regarding the failed UTs, here’s the summary: 1) unit-test-backend-8-gpu-b200 (TestGptOss4Gpu.test mxfp4 120b) This accuracy test seems a bit unstable. In our local ..." (https://github.com/sgl-project/sglang/pull/6226#issuecomment-3261700202)
- `2025-07-11T02:11:09Z` `inline` by `wenhuach21` `docs/backend/quantization.md`:97; signals: kernel, moe; excerpt: "Most quantized MoE models may encounter inference issues due to kernel-related limitation. These issues might be resolved in future updates of sglang. If you ..." (https://github.com/sgl-project/sglang/pull/6226#discussion_r2199303894)
- `2025-06-04T06:10:20Z` `issue` by `WeiweiZhang1`; signals: kernel, moe; excerpt: "MoE quantization is quite important. Is there hope that these MoE issues will be resolved in the near future? For MoE and VLM model, ..." (https://github.com/sgl-project/sglang/pull/6226#issuecomment-2938702735)
- `2025-06-04T06:13:52Z` `issue` by `FlamingoPg`; signals: kernel, moe; excerpt: "MoE quantization is quite important. Is there hope that these MoE issues will be resolved in the near future? For MoE and VLM model, ..." (https://github.com/sgl-project/sglang/pull/6226#issuecomment-2938712221)
- `2025-06-04T05:46:59Z` `issue` by `FlamingoPg`; signals: moe; excerpt: "MoE quantization is quite important. Is there hope that these MoE issues will be resolved in the near future?" (https://github.com/sgl-project/sglang/pull/6226#issuecomment-2938649442)
- `2025-06-09T07:45:18Z` `issue` by `wenhuach21`; signals: hang; excerpt: "@yinfan98 Hi Yinfan, when you have a moment, could you kindly review this PR? It's been open for nearly a month. Regarding the CI ..." (https://github.com/sgl-project/sglang/pull/6226#issuecomment-2954967053)
- `2025-07-09T06:49:55Z` `issue` by `AniZpZ`; signals: hang; excerpt: "@WeiweiZhang1 Thanks for the work! I think it would be better to list known issues in the quantization documentation and provide specific user guidance ..." (https://github.com/sgl-project/sglang/pull/6226#issuecomment-3051386564)
- `2025-06-04T05:40:28Z` `issue` by `FlamingoPg`; signals: hang; excerpt: "Hi @WeiweiZhang1 , i will help review this pr" (https://github.com/sgl-project/sglang/pull/6226#issuecomment-2938639913)
- `2025-07-08T07:47:56Z` `issue` by `zhyncs`; signals: hang; excerpt: "@WeiweiZhang1 please rebase @AniZpZ please help review" (https://github.com/sgl-project/sglang/pull/6226#issuecomment-3047759387)
- `2025-07-09T06:46:36Z` `inline` by `AniZpZ` `python/sglang/srt/layers/quantization/auto_round.py`:9; signals: general review; excerpt: "We are planning to remove the dependency on vLLM in the SGLang quantization module. Could you please implement this with minimal vLLM dependency?" (https://github.com/sgl-project/sglang/pull/6226#discussion_r2194196839)
- `2025-07-11T01:29:54Z` `inline` by `wenhuach21` `docs/backend/quantization.md`:45; signals: general review; excerpt: "add known issues" (https://github.com/sgl-project/sglang/pull/6226#discussion_r2199248047)
- `2025-07-11T01:30:08Z` `inline` by `wenhuach21` `docs/backend/quantization.md`:67; signals: general review; excerpt: "remove comment" (https://github.com/sgl-project/sglang/pull/6226#discussion_r2199248808)
