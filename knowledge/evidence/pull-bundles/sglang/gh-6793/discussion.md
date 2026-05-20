# PR Discussion Digest

- Source PR: [sgl-project/sglang#6793](https://github.com/sgl-project/sglang/pull/6793)
- Source page: `sources/prs/sglang/PR-6793.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6793`
- Generated at: `2026-05-20T15:30:49.020465+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-31T16:10:15Z`
- Merged: `2025-06-25T09:00:22Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 23 (approved=1, changes_requested=1, commented=21)
- Inline review comments: 23
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=14, outdated=9
- Human participants with discussion text: ByronHsu, Hongbosherlock, ShangmingCai, ishandhanani, jokerwyt
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-05-31T16:10:37Z` `COMMENTED` by `gemini-code-assist` - Hello @Hongbosherlock, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2884282052)
- `2025-05-31T16:11:58Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces an important feature: support for different Tensor Parallel (TP) sizes between prefill ... (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2884287063)
- `2025-06-02T08:02:30Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887225260)
- `2025-06-02T08:02:58Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887226927)
- `2025-06-02T08:04:45Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887231605)
- `2025-06-02T08:15:43Z` `COMMENTED` by `ShangmingCai` - These newly added args are not straightforward in my opinion, How about we change it into the , ... (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887263154)
- `2025-06-02T08:40:41Z` `COMMENTED` by `ShangmingCai` - Since the data addrs are not contiguous anymore because we have to split every item either at the ... (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887354245)
- `2025-06-02T15:25:24Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2888936556)
- `2025-06-02T15:27:45Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2888946902)
- `2025-06-04T09:08:51Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2895929370)
- `2025-06-04T09:19:27Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2895962013)
- `2025-06-04T13:25:32Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2896734182)
- `2025-06-04T13:29:43Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2896750489)
- `2025-06-05T11:04:16Z` `COMMENTED` by `ShangmingCai` - The code is very clean and I have verified the accuracy with page size == 1. Great job! ... (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2897282582)
- `2025-06-05T13:22:26Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2900320037)
- `2025-06-05T13:22:30Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2900320286)
- `2025-06-10T13:07:58Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2913506458)
- `2025-06-10T13:12:16Z` `APPROVED` by `ShangmingCai` - LGTM now, @ByronHsu PTAL. I will take some time to run accuracy and performance tests again this week. (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2913522814)
- `2025-06-10T13:37:27Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2913626049)
- `2025-06-11T11:11:50Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2916705588)
- `2025-06-12T03:31:23Z` `COMMENTED` by `ByronHsu` - Since most of the change is on mooncake side. I will defer to @ShangmingCai to review/approve (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2919399812)
- `2025-06-12T03:54:40Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2919456563)
- `2025-06-12T04:07:38Z` `COMMENTED` by `Hongbosherlock` (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2919487626)

## Inline Comment Hotspots

- `python/sglang/srt/disaggregation/mooncake/conn.py`: 18 inline comment(s)
- `python/sglang/srt/disaggregation/prefill.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-06-02T08:40:41Z` `review` `COMMENTED` by `ShangmingCai`; signals: cache, mla, perf, performance; excerpt: "Since the data addrs are not contiguous anymore because we have to split every item either at the src or the dst, I think ..." (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887354245)
- `2025-06-05T11:04:16Z` `review` `COMMENTED` by `ShangmingCai`; signals: accuracy, perf, performance, throughput; excerpt: "The code is very clean and I have verified the accuracy with page size == 1. Great job! However, there seems to be a ..." (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2897282582)
- `2025-06-10T12:44:46Z` `issue` by `Hongbosherlock`; signals: accuracy, h100, hang, perf, performance; excerpt: "@ShangmingCai Sorry for the late reply, I've added support for page size 1 and have also verified both the accuracy and performance. for example: ..." (https://github.com/sgl-project/sglang/pull/6793#issuecomment-2959061587)
- `2025-06-04T09:19:27Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/mooncake/conn.py`:841; signals: mla, perf, performance; excerpt: "We should probably use logger.warning once() here to notify users that the performance with different TP for non-MLA models is not yet guaranteed." (https://github.com/sgl-project/sglang/pull/6793#discussion_r2126116622)
- `2025-06-02T16:42:40Z` `issue` by `Hongbosherlock`; signals: accuracy, cache, kv cache; excerpt: "prefill tp size:4 , decode tp size:2 Looking into accuracy issue when Decode TP < Prefill TP. Each decode rank needs to receive KV ..." (https://github.com/sgl-project/sglang/pull/6793#issuecomment-2931544692)
- `2025-06-10T13:12:16Z` `review` `APPROVED` by `ShangmingCai`; signals: accuracy, perf, performance; excerpt: "LGTM now, @ByronHsu PTAL. I will take some time to run accuracy and performance tests again this week." (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2913522814)
- `2025-06-18T03:45:25Z` `issue` by `ShangmingCai`; signals: perf, performance, throughput; excerpt: "@Hongbosherlock Hello, after I talk this PR with some maintainers, some people are worrying that the performance is too poor to be used in ..." (https://github.com/sgl-project/sglang/pull/6793#issuecomment-2982567665)
- `2025-06-02T08:02:30Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/mooncake/conn.py`:305; signals: block, cache; excerpt: "Since we have to split the kvcache and calculate the offset either at the prefill side or the decode side, I don't see the ..." (https://github.com/sgl-project/sglang/pull/6793#discussion_r2120363844)
- `2025-06-02T08:15:43Z` `review` `COMMENTED` by `ShangmingCai`; signals: hang; excerpt: "These newly added args are not straightforward in my opinion, How about we change it into the , and we use them to calculate ..." (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2887263154)
- `2025-06-04T08:49:34Z` `issue` by `Hongbosherlock`; signals: accuracy, h100; excerpt: "Fixed the accuracy issue when Decode TP < Prefill TP in Updated Evaluation - prefill tp size:4 , decode tp size:2 - prefill tp ..." (https://github.com/sgl-project/sglang/pull/6793#issuecomment-2939175468)
- `2025-06-12T03:31:23Z` `review` `COMMENTED` by `ByronHsu`; signals: hang; excerpt: "Since most of the change is on mooncake side. I will defer to @ShangmingCai to review/approve" (https://github.com/sgl-project/sglang/pull/6793#pullrequestreview-2919399812)
- `2025-06-12T04:42:52Z` `issue` by `ShangmingCai`; signals: hang, mla; excerpt: "@Hongbosherlock When prefill tp decode tp (with MLA), the current PR will hang. I think some code hasn't been included yet. The CI and ..." (https://github.com/sgl-project/sglang/pull/6793#issuecomment-2965090235)
