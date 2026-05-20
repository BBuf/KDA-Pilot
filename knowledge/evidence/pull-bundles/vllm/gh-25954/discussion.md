# PR Discussion Digest

- Source PR: [vllm-project/vllm#25954](https://github.com/vllm-project/vllm/pull/25954)
- Source page: `sources/prs/vllm/PR-25954.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25954`
- Generated at: `2026-05-20T15:38:00.362407+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T13:39:51Z`
- Merged: `2026-01-24T01:28:06Z`

## Discussion Counts

- Issue comments: 36
- Review submissions: 83 (approved=6, changes_requested=1, commented=75, dismissed=1)
- Inline review comments: 102
- Review threads observed: 55
- Resolved/outdated thread markers: resolved=32, outdated=51
- Human participants with discussion text: ElizaWszola, LucasWilkinson, MatthewBonanni, NickLucche, ProExpertProg, chatgpt-codex-connector, cursor, elvischenv, mergify, mgoin, pavanimajety, tjtanaa, zou3519
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-02T20:20:53Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3285424785)
- `2025-10-02T20:21:47Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3296265062)
- `2025-10-06T17:05:00Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3306064239)
- `2025-10-07T13:50:31Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3310149419)
- `2025-10-08T12:46:52Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3314655677)
- `2025-10-08T13:09:28Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3314743624)
- `2025-10-08T13:10:30Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3314749113)
- `2025-10-08T13:26:21Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3314817748)
- `2025-10-08T13:32:21Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3314843497)
- `2025-10-09T12:51:16Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3318822120)
- `2025-10-09T19:48:38Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3320417581)
- `2025-10-09T20:05:30Z` `APPROVED` by `ProExpertProg` - Looks good to me! Let's see what CI says, also would be good to get a 👍 from ... (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3320424058)
- `2025-10-09T20:42:52Z` `APPROVED` by `MatthewBonanni` - LGTM! (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3320571938)
- `2025-10-09T23:37:18Z` `COMMENTED` by `pavanimajety` - Thanks for the PR, @ElizaWszola! A couple of questions/observations: 1. If the Attention and Cache Update is split ... (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3320940064)
- `2025-10-10T13:42:12Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3323579556)
- `2025-10-16T04:29:04Z` `CHANGES_REQUESTED` by `ProExpertProg` - I think we should hold off on merging this until after the release. Right now there's no immediate ... (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3343019708)
- `2025-11-17T22:41:03Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3474816716)
- `2025-11-21T03:47:06Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3491077555)
- `2025-11-21T09:37:30Z` `COMMENTED` by `NickLucche` - Thanks for the work @ElizaWszola ! Left some comments related to kv cache loading-saving, let me know what ... (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3491812131)
- `2025-11-21T14:00:36Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3492884985)
- `2025-12-02T15:13:41Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3530670619)
- `2025-12-02T15:25:48Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3530728948)
- `2025-12-10T16:41:23Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3563502777)
- `2026-01-07T23:21:00Z` `COMMENTED` by `ProExpertProg` - After discussion with @LucasWilkinson and @MatthewBonanni, we agreed we should separate slot mapping & block table from attention ... (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3636933168)
- ... 59 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/attention/layer.py`: 39 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 29 inline comment(s)
- `vllm/model_executor/layers/attention/mla_attention.py`: 5 inline comment(s)
- `vllm/v1/attention/backends/flash_attn.py`: 4 inline comment(s)
- `tests/v1/attention/utils.py`: 4 inline comment(s)
- `vllm/v1/worker/gpu/model_runner.py`: 4 inline comment(s)
- `vllm/model_executor/layers/attention/cross_attention.py`: 4 inline comment(s)
- `vllm/v1/spec_decode/eagle.py`: 4 inline comment(s)
- `vllm/model_executor/layers/mamba/linear_attn.py`: 3 inline comment(s)
- `vllm/v1/attention/backends/mla/common.py`: 2 inline comment(s)
- `vllm/v1/attention/backends/utils.py`: 2 inline comment(s)
- `vllm/forward_context.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-08T12:46:52Z` `inline` by `ElizaWszola` `vllm/attention/layer.py`:652; signals: attention, cache, compile, cuda, cudagraph, kv cache, mla; excerpt: "This is for the case when there are multiple different backends and some support the split kv cache, while some do not. In this ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2413743304)
- `2025-10-09T23:37:18Z` `review` `COMMENTED` by `pavanimajety`; signals: attention, cache, fp4, kv cache, mla, oom; excerpt: "Thanks for the PR, @ElizaWszola! A couple of questions/observations: 1. If the Attention and Cache Update is split only when MLA is disabled, why ..." (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3320940064)
- `2026-01-07T23:21:00Z` `review` `COMMENTED` by `ProExpertProg`; signals: attention, block, cache, nan; excerpt: "After discussion with @LucasWilkinson and @MatthewBonanni, we agreed we should separate slot mapping & block table from attention metadata. This makes sense because we're ..." (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3636933168)
- `2026-01-13T17:35:12Z` `review` `COMMENTED` by `LucasWilkinson`; signals: attention, cache, compile, hang; excerpt: "I think there may have been a bit of miscommunication; what we were suggesting with was that we add slot mapping to ForwardContext, so ..." (https://github.com/vllm-project/vllm/pull/25954#pullrequestreview-3656626905)
- `2025-10-10T04:49:04Z` `issue` by `ElizaWszola`; signals: attention, block, cache, kv cache, mla; excerpt: "If the Attention and Cache Update is split only when MLA is disabled, why are we testing with DeepSeek-Coder-V2-Lite-Instruct? For DeepSeek doesn't it make ..." (https://github.com/vllm-project/vllm/pull/25954#issuecomment-3388281271)
- `2025-10-08T13:10:30Z` `inline` by `ElizaWszola` `vllm/v1/worker/gpu_model_runner.py`:3915; signals: attention, cuda, cudagraph, mla; excerpt: "the "always force attention" solution broke when I was testing with MLA (it can only run build metadata for decode full CUDAGraph), and from ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2413812163)
- `2025-10-09T20:02:42Z` `inline` by `ProExpertProg` `vllm/v1/worker/gpu_model_runner.py`:3343; signals: attention, cuda, cudagraph, mla; excerpt: "Okay I think I understand now: if we always force attention, we are forcing MLA to build for cudagraph capture during the run for ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2417831694)
- `2025-11-17T22:41:03Z` `inline` by `ProExpertProg` `vllm/attention/layer.py`:868; signals: attention, cache, cute, kv cache; excerpt: "Do we need to remove these and execute them conditionally based on the forward includes kv cache property of the backend? cc @NickLucche" (https://github.com/vllm-project/vllm/pull/25954#discussion_r2535728152)
- `2025-11-21T09:36:05Z` `inline` by `NickLucche` `vllm/attention/layer.py`:868; signals: attention, block, cache, kv cache; excerpt: "Actually the cache update should just "append" the newly computed values on D, ignoring the unloaded ones. We only need those once we compute ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2549118521)
- `2025-12-02T15:13:41Z` `inline` by `zou3519` `vllm/attention/layer.py`:964; signals: attention, cache, kv cache, register; excerpt: "Replied offline, copy-pasting reply: Unfortunately I think mutating output might be the best way to do this right now. The alternatives are: 1) write ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2581627614)
- `2025-12-10T16:41:23Z` `inline` by `ElizaWszola` `tests/v1/attention/utils.py`:130; signals: attention, cache, correctness, kv cache; excerpt: "I still need to add a test that checks correctness, but since forward includes kv cache will become specific to each backend, we would ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2607416906)
- `2026-01-13T08:23:08Z` `inline` by `cursor` `vllm/model_executor/layers/attention/mla_attention.py`:777; signals: attention, cuda, cudagraph, mla; excerpt: "Removed MLA decode-only assertion weakens cudagraph safety Medium Severity The assertion assert m.max query len <source media="(prefers-color-scheme: dark)" srcset=" media="(prefers-color-scheme: light)" srcset=" alt="Fix in ..." (https://github.com/vllm-project/vllm/pull/25954#discussion_r2685360976)
