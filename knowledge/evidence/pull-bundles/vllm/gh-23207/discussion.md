# PR Discussion Digest

- Source PR: [vllm-project/vllm#23207](https://github.com/vllm-project/vllm/pull/23207)
- Source page: `sources/prs/vllm/PR-23207.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23207`
- Generated at: `2026-05-20T15:37:27.095931+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-19T21:15:13Z`
- Merged: `2025-10-28T22:36:43Z`

## Discussion Counts

- Issue comments: 53
- Review submissions: 27 (approved=3, commented=24)
- Inline review comments: 24
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=3, outdated=7
- Human participants with discussion text: DarkLight1337, JartX, Lucaskabela, ProExpertProg, ZJY0516, laithsakka, lgeiger, mergify, miladm, tanruixiang, tjtanaa, wwl2755, yanyongyu, ywang96, zou3519
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 15

## Review Decisions

- `2025-08-19T22:27:09Z` `COMMENTED` by `miladm` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3134030770)
- `2025-08-19T22:51:19Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3134129769)
- `2025-09-09T18:13:44Z` `COMMENTED` by `ywang96` - Hey @Lucaskabela! I actually had a chat with @youkaichao and the conclusion is that this current state is ... (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3202741234)
- `2025-09-11T16:12:40Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3212602063)
- `2025-09-11T18:36:22Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3212605863)
- `2025-09-29T21:58:15Z` `COMMENTED` by `ywang96` - Thanks for the work! I left two questions (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3281914135)
- `2025-09-29T22:48:08Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3282052225)
- `2025-09-29T22:51:30Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3282056585)
- `2025-10-02T06:28:27Z` `COMMENTED` by `ywang96` - @Lucaskabela Thanks for your work! I think this PR looks in a much better shape now, but I'm ... (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3292686119)
- `2025-10-10T23:50:15Z` `APPROVED` by `ywang96` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3326304073)
- `2025-10-11T12:24:22Z` `APPROVED` by `ProExpertProg` - LGTM overall! (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3327041004)
- `2025-10-13T13:44:34Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3331707295)
- `2025-10-13T13:47:01Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3331716011)
- `2025-10-13T13:48:08Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3331719896)
- `2025-10-13T14:01:14Z` `COMMENTED` by `lgeiger` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3331771447)
- `2025-10-13T14:02:37Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3331776341)
- `2025-10-13T17:39:39Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3332513075)
- `2025-10-13T17:43:37Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3332518570)
- `2025-10-13T18:29:44Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3332636284)
- `2025-10-13T20:37:22Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3332979071)
- `2025-10-13T20:39:11Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3332982651)
- `2025-10-13T21:56:59Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3333124927)
- `2025-10-15T02:33:17Z` `COMMENTED` by `yanyongyu` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3338145107)
- `2025-10-15T16:46:04Z` `COMMENTED` by `Lucaskabela` (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3341412165)
- ... 3 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/models/qwen2_5_vl.py`: 15 inline comment(s)
- `vllm/compilation/decorators.py`: 5 inline comment(s)
- `vllm/attention/ops/vit_attn_wrappers.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-09-30T02:52:01Z` `issue` by `DarkLight1337`; signals: benchmark, block, cuda, cudagraph, hang; excerpt: "@DarkLight1337 I went ahead and changed L477 (in VisionBlock) to use iadd: Did you use CUDAGraph for the benchmark? The original PR mentioned that ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3349745244)
- `2025-09-30T15:55:54Z` `issue` by `Lucaskabela`; signals: benchmark, block, cuda, cudagraph, hang; excerpt: "@DarkLight1337 I went ahead and changed L477 (in VisionBlock) to use iadd: Did you use CUDAGraph for the benchmark? The original PR mentioned that ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3352850979)
- `2025-09-09T18:13:44Z` `review` `COMMENTED` by `ywang96`; signals: compile, perf, performance; excerpt: "Hey @Lucaskabela! I actually had a chat with @youkaichao and the conclusion is that this current state is probably not good enough for us ..." (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3202741234)
- `2025-09-17T22:50:11Z` `issue` by `Lucaskabela`; signals: compile, perf, performance, race; excerpt: "Thanks for the great work! I'm wondering what would be the main concern to split the large nn module into smaller ones. Would it ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3304777701)
- `2025-09-18T00:10:54Z` `issue` by `wwl2755`; signals: compile, perf, performance, race; excerpt: "When we put compile at the top level, there may be some code that torch compile's dynamo is not able to trace. In these ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3304912979)
- `2025-09-29T21:55:23Z` `inline` by `ywang96` `vllm/model_executor/models/qwen2_5_vl.py`:389; signals: attention, compile, hang; excerpt: "Is there a reason why we're doing this at top level instead of per-attention backend? We have already changed the logic here so that ..." (https://github.com/vllm-project/vllm/pull/23207#discussion_r2389357763)
- `2025-09-29T22:51:30Z` `inline` by `Lucaskabela` `vllm/model_executor/models/qwen2_5_vl.py`:389; signals: attention, compile, flash attention; excerpt: "So there is a challenge here comes from two operations that don't play nicely with torch.compile (hence why we try to hide them here). ..." (https://github.com/vllm-project/vllm/pull/23207#discussion_r2389435304)
- `2025-10-13T21:56:59Z` `inline` by `Lucaskabela` `vllm/model_executor/models/qwen2_5_vl.py`:455; signals: compile, cuda, cudagraph; excerpt: "My understanding is that since we don't do anything different here Cudagraphs will be on, and we will capture with multiple compile sizes (although ..." (https://github.com/vllm-project/vllm/pull/23207#discussion_r2427396023)
- `2025-10-02T06:28:27Z` `review` `COMMENTED` by `ywang96`; signals: benchmark, perf; excerpt: "@Lucaskabela Thanks for your work! I think this PR looks in a much better shape now, but I'm not sure whether we want to ..." (https://github.com/vllm-project/vllm/pull/23207#pullrequestreview-3292686119)
- `2025-09-29T21:40:00Z` `issue` by `Lucaskabela`; signals: benchmark, block, hang; excerpt: "I wonder how much improvement this makes over 23932? @DarkLight1337 I went ahead and changed L477 (in VisionBlock) to use iadd: I didn't identify ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3349148141)
- `2025-10-16T17:42:45Z` `issue` by `Lucaskabela`; signals: compile, failing, hang; excerpt: "And now for the fun part - seems after these changes there is an Eagle3 test failing. I tried bisecting these changes to figure ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3412049223)
- `2025-10-16T21:33:13Z` `issue` by `Lucaskabela`; signals: h100, hang, throughput; excerpt: "Thanks @Lucaskabela! Can we reporting the MFU gains before and after this PR? MFU Estimate (from) Throughput Flops per token / Max theoretical Throughput ..." (https://github.com/vllm-project/vllm/pull/23207#issuecomment-3412942293)
