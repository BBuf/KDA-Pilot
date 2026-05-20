# PR Discussion Digest

- Source PR: [vllm-project/vllm#17280](https://github.com/vllm-project/vllm/pull/17280)
- Source page: `sources/prs/vllm/PR-17280.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17280`
- Generated at: `2026-05-20T15:35:08.255467+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-28T03:25:53Z`
- Merged: `2025-07-02T12:47:19Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: UmakantKulkarni, cyril23, kaln27, mergify, mgoin, voipmonitor, waltstephen
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-01T01:54:11Z` `APPROVED` by `mgoin` - Apologies for missing this PR, thanks for the kernel support! This looks reasonable to me, but could you ... (https://github.com/vllm-project/vllm/pull/17280#pullrequestreview-2973229683)
- `2025-07-01T13:23:11Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17280#pullrequestreview-2974737720)
- `2025-07-02T03:09:39Z` `COMMENTED` by `kaln27` - I found that other cutlass scaled mm (use cutlass 3.0) in cmake also have this comment. LGTM (https://github.com/vllm-project/vllm/pull/17280#pullrequestreview-2975556959)

## Inline Comment Hotspots

- `CMakeLists.txt`: 2 inline comment(s)

## High-Signal Discussion

- `2025-07-01T02:45:25Z` `issue` by `kaln27`; signals: accuracy, benchmark, fp8, kernel; excerpt: "Apologies for missing this PR, thanks for the kernel support! This looks reasonable to me, but could you share an e2e accuracy eval to ..." (https://github.com/vllm-project/vllm/pull/17280#issuecomment-3021543190)
- `2025-06-27T16:57:26Z` `issue` by `cyril23`; signals: compile, hang, ptx; excerpt: "After merging vllm-project/vllm today's main into (I did it on my current I've build it via The pytorch wheel size is still Furthermore the ..." (https://github.com/vllm-project/vllm/pull/17280#issuecomment-3013759134)
- `2025-06-30T02:58:05Z` `issue` by `UmakantKulkarni`; signals: hang, sm120; excerpt: "Hi @tlrmchlsmth, May I know when this PR is expected to be merged? I’ve also verified @kaln27 's changes on an RTX 5090 (sm120), ..." (https://github.com/vllm-project/vllm/pull/17280#issuecomment-3017606301)
- `2025-07-01T01:54:11Z` `review` `APPROVED` by `mgoin`; signals: accuracy, kernel; excerpt: "Apologies for missing this PR, thanks for the kernel support! This looks reasonable to me, but could you share an e2e accuracy eval to ..." (https://github.com/vllm-project/vllm/pull/17280#pullrequestreview-2973229683)
- `2025-07-02T03:09:39Z` `review` `COMMENTED` by `kaln27`; signals: cutlass; excerpt: "I found that other cutlass scaled mm (use cutlass 3.0) in cmake also have this comment. LGTM" (https://github.com/vllm-project/vllm/pull/17280#pullrequestreview-2975556959)
- `2025-06-18T17:40:07Z` `issue` by `voipmonitor`; signals: fp8; excerpt: "I have verified that this PR works on FP8 models and it has the same speed as the TRT-LLM FP8" (https://github.com/vllm-project/vllm/pull/17280#issuecomment-2985167312)
- `2025-07-01T10:25:49Z` `inline` by `mgoin` `CMakeLists.txt`:437; signals: general review; excerpt: "I think this comment is incorrect" (https://github.com/vllm-project/vllm/pull/17280#discussion_r2177146677)
- `2025-07-01T13:54:03Z` `inline` by `kaln27` `CMakeLists.txt`:437; signals: general review; excerpt: "I just copy from the top one. If you think that's incorrect you can delete it." (https://github.com/vllm-project/vllm/pull/17280#discussion_r2177671007)
- `2025-06-13T05:37:20Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @kaln27." (https://github.com/vllm-project/vllm/pull/17280#issuecomment-2969119342)
- `2025-06-18T14:30:02Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @kaln27." (https://github.com/vllm-project/vllm/pull/17280#issuecomment-2984456741)
- `2025-06-30T06:57:05Z` `issue` by `waltstephen`; signals: general review; excerpt: "Please check and merge the PR ASAP, this is very useful for the people using 50 series and black wall...." (https://github.com/vllm-project/vllm/pull/17280#issuecomment-3018018016)
