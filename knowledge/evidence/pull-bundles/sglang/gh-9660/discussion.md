# PR Discussion Digest

- Source PR: [sgl-project/sglang#9660](https://github.com/sgl-project/sglang/pull/9660)
- Source page: `sources/prs/sglang/PR-9660.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9660`
- Generated at: `2026-05-20T15:31:37.894659+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-26T16:27:26Z`
- Merged: `2025-12-03T18:07:42Z`

## Discussion Counts

- Issue comments: 52
- Review submissions: 19 (approved=1, commented=18)
- Inline review comments: 24
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=6, outdated=11
- Human participants with discussion text: AniZpZ, Fridge003, Huixxi, MengYu10151, Sulfur6, Zqy11, ch-wan, fzyzcjy, justinSmileDate, lixiuhong, lizhiqihhh, programmer-lxj, whybeyoung, zhou9402
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 11

## Review Decisions

- `2025-09-05T14:40:11Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3189650025)
- `2025-09-05T15:06:20Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3189741474)
- `2025-09-06T01:26:08Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3191228868)
- `2025-09-06T01:26:25Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3191229008)
- `2025-09-06T01:27:44Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3191231049)
- `2025-09-06T01:31:49Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3191242566)
- `2025-09-08T08:28:36Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3195485502)
- `2025-09-08T08:31:30Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3195501967)
- `2025-09-08T08:34:36Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3195512381)
- `2025-09-10T07:03:24Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3204705921)
- `2025-11-12T12:39:22Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3453218305)
- `2025-11-12T13:07:45Z` `COMMENTED` by `Zqy11` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3453354954)
- `2025-11-13T16:25:57Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3460629844)
- `2025-11-20T19:39:42Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3489611524)
- `2025-11-27T14:06:49Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3515585910)
- `2025-11-27T14:10:47Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3515612791)
- `2025-11-30T23:30:41Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3522684671)
- `2025-12-02T01:52:31Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3527825156)
- `2025-12-02T02:00:42Z` `COMMENTED` by `Sulfur6` (https://github.com/sgl-project/sglang/pull/9660#pullrequestreview-3527850736)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 7 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 5 inline comment(s)
- `sgl-kernel/CMakeLists.txt`: 4 inline comment(s)
- `python/sglang/srt/single_batch_overlap.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`: 3 inline comment(s)
- `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`: 1 inline comment(s)
- `python/sglang/srt/batch_overlap/single_batch_overlap.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-02T09:51:18Z` `issue` by `Sulfur6`; signals: cute, gemm, hang, memory, perf, performance, tma, warp; excerpt: "this change looks great, but I am still a bit worried (1) shall we use atomicAdd (doc says relaxed ordering) or use released ordering ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3244616986)
- `2025-12-01T11:40:55Z` `issue` by `Zqy11`; signals: b200, blackwell, deepgemm, gemm, hang, kernel; excerpt: "@Sulfur6 Can you please open a sub-PR that only contains the git tag change on DeepGemm? We want to merge that PR first, release ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3596064275)
- `2025-09-02T09:40:01Z` `issue` by `fzyzcjy`; signals: fp4, hang, nvfp4, tma, warp; excerpt: "this change looks great, but I am still a bit worried (1) shall we use atomicAdd (doc says relaxed ordering) or use released ordering ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3244575014)
- `2025-09-03T08:37:04Z` `issue` by `fzyzcjy`; signals: aligned, blackwell, deepgemm, gemm, hopper; excerpt: "FYI I am waiting for the refactored deepgemm (hopper), since I need to implement deepgemm blackwell and want to be aligned with your style ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3248241967)
- `2025-09-03T08:46:03Z` `issue` by `Sulfur6`; signals: aligned, blackwell, deepgemm, gemm, hopper; excerpt: "FYI I am waiting for the refactored deepgemm (hopper), since I need to implement deepgemm blackwell and want to be aligned with your style ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3248275190)
- `2025-12-01T07:04:46Z` `issue` by `Sulfur6`; signals: blackwell, deepgemm, gemm, hang, kernel; excerpt: "@Sulfur6 Can you please open a sub-PR that only contains the git tag change on DeepGemm? We want to merge that PR first, release ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3594899548)
- `2025-10-22T08:44:41Z` `issue` by `justinSmileDate`; signals: compile, fp8, gemm, register; excerpt: "Hello, sorry to bother you. On the commit d232a36f28c0eb46f5d202701a02dc10fca1e6b5, it shows 'Merge remote-tracking branch 'origin/main' into sbo.v2.public'. I tried the sbo.v2.public branch and the ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3431138718)
- `2025-11-06T06:52:53Z` `issue` by `Zqy11`; signals: deepgemm, gemm, kernel, throughput; excerpt: "2 questions: 1. Does the communication kernel need to remain active while waiting for a signal, keeping SMs occupied during the entire process? 2. ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3495374566)
- `2025-11-09T11:40:43Z` `issue` by `Sulfur6`; signals: compile, fp8, gemm, register; excerpt: "Hello, sorry to bother you. On the commit d232a36f28c0eb46f5d202701a02dc10fca1e6b5, it shows 'Merge remote-tracking branch 'origin/main' into sbo.v2.public'. I tried the sbo.v2.public branch and the ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3508048171)
- `2025-12-01T02:34:57Z` `issue` by `Fridge003`; signals: deepgemm, gemm, hang, kernel; excerpt: "@Sulfur6 Can you please open a sub-PR that only contains the git tag change on DeepGemm? We want to merge that PR first, release ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3594278932)
- `2025-12-01T02:44:26Z` `issue` by `Sulfur6`; signals: deepgemm, gemm, hang, kernel; excerpt: "@Sulfur6 Can you please open a sub-PR that only contains the git tag change on DeepGemm? We want to merge that PR first, release ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3594296606)
- `2025-12-02T09:58:19Z` `issue` by `Sulfur6`; signals: deepgemm, gemm, kernel, moe; excerpt: "The current version of sgl-kernel's DeepGEMM does not include the modifications in which causes the deep gemm moe runner to malfunction. I have fixed ..." (https://github.com/sgl-project/sglang/pull/9660#issuecomment-3601189584)
