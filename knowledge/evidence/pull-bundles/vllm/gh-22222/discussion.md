# PR Discussion Digest

- Source PR: [vllm-project/vllm#22222](https://github.com/vllm-project/vllm/pull/22222)
- Source page: `sources/prs/vllm/PR-22222.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22222`
- Generated at: `2026-05-20T15:36:58.234406+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-05T01:23:12Z`
- Merged: `2025-09-15T14:43:26Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 20 (approved=1, changes_requested=2, commented=17)
- Inline review comments: 26
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=9, outdated=12
- Human participants with discussion text: BowenBao, amd-xiaoyu12, gshtras, mergify, xiao-llm
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-05T01:28:23Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces updates for FP8 paged attention on ROCm. I've identified two critical compilation ... (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3086222244)
- `2025-08-05T01:37:00Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3086238360)
- `2025-08-08T20:38:41Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3102101855)
- `2025-08-11T14:36:37Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3106217856)
- `2025-08-13T15:28:04Z` `CHANGES_REQUESTED` by `gshtras` - Solid job overall. Could we have unit tests to cover the new fp8 path? Extend the additional rocm ... (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3116518727)
- `2025-08-26T22:46:29Z` `COMMENTED` by `amd-xiaoyu12` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3157537523)
- `2025-08-26T23:15:45Z` `COMMENTED` by `amd-xiaoyu12` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3157596539)
- `2025-08-26T23:15:54Z` `COMMENTED` by `amd-xiaoyu12` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3157596966)
- `2025-08-27T15:21:47Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3160347637)
- `2025-08-27T17:04:59Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3160870633)
- `2025-08-28T19:12:11Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3166180328)
- `2025-08-28T19:12:42Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3166181867)
- `2025-08-28T19:17:53Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3166198917)
- `2025-08-28T19:29:11Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3166232833)
- `2025-09-02T01:55:09Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3174689000)
- `2025-09-08T16:18:59Z` `CHANGES_REQUESTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3197238994)
- `2025-09-09T22:54:55Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3203639259)
- `2025-09-09T23:02:54Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3203672599)
- `2025-09-09T23:10:56Z` `COMMENTED` by `xiao-llm` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3203701963)
- `2025-09-10T21:58:17Z` `APPROVED` by `gshtras` (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3207966474)

## Inline Comment Hotspots

- `csrc/rocm/attention.cu`: 9 inline comment(s)
- `vllm/_custom_ops.py`: 6 inline comment(s)
- `pyproject.toml`: 3 inline comment(s)
- `CMakeLists.txt`: 3 inline comment(s)
- `vllm/envs.py`: 3 inline comment(s)
- `examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_proxy_p2p_nccl_xpyd.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-02T01:55:09Z` `inline` by `xiao-llm` `CMakeLists.txt`:197; signals: attention, compile, hang; excerpt: "Resolved by remove the CMake changes and use conditional compile in attention.cu, tested on ROCm 6.30." (https://github.com/vllm-project/vllm/pull/22222#discussion_r2314752628)
- `2025-08-13T15:28:04Z` `review` `CHANGES_REQUESTED` by `gshtras`; signals: attention, fp8; excerpt: "Solid job overall. Could we have unit tests to cover the new fp8 path? Extend the additional rocm attention test. Another major point is ..." (https://github.com/vllm-project/vllm/pull/22222#pullrequestreview-3116518727)
- `2025-09-08T16:18:52Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:613; signals: attention, fp8; excerpt: "Consider adding a new variable at the top for fp8 supporting Instinct cards similar to the others there" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2330739295)
- `2025-09-09T22:54:54Z` `inline` by `xiao-llm` `csrc/rocm/attention.cu`:613; signals: attention, fp8; excerpt: "Created a new flag for fp8 instinct, please review." (https://github.com/vllm-project/vllm/pull/22222#discussion_r2335008795)
- `2025-08-13T20:27:25Z` `issue` by `xiao-llm`; signals: attention, fp8; excerpt: "Solid job overall. Could we have unit tests to cover the new fp8 path? Extend the additional rocm attention test. Another major point is ..." (https://github.com/vllm-project/vllm/pull/22222#issuecomment-3185635294)
- `2025-08-27T15:21:47Z` `inline` by `gshtras` `CMakeLists.txt`:197; signals: fp8; excerpt: "On a Radeon card without fp8 support (and likely other similar GPUs) this results in the following warnings:" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2304328152)
- `2025-08-05T01:37:00Z` `inline` by `xiao-llm` `csrc/rocm/attention.cu`:289; signals: attention; excerpt: "The ifdef can be found at line 260" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2252906726)
- `2025-08-08T20:38:40Z` `inline` by `BowenBao` `pyproject.toml`:19; signals: hang; excerpt: "is this change intended?" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2263950881)
- `2025-08-13T15:20:28Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:3644; signals: attention; excerpt: "Please remove debug leftovers" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2273807733)
- `2025-08-13T15:22:45Z` `inline` by `gshtras` `vllm/_custom_ops.py`:120; signals: fp8; excerpt: "How is the fp8 path actually being enabled?" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2273814118)
- `2025-08-13T15:24:26Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:310; signals: attention; excerpt: "This commented out endif could be misleading" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2273818443)
- `2025-08-13T15:26:17Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:3673; signals: attention; excerpt: "Just a thought. Maybe we could simplify this logic, it's becoming a bit hard to follow" (https://github.com/vllm-project/vllm/pull/22222#discussion_r2273823276)
