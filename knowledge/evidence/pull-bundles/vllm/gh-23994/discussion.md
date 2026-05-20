# PR Discussion Digest

- Source PR: [vllm-project/vllm#23994](https://github.com/vllm-project/vllm/pull/23994)
- Source page: `sources/prs/vllm/PR-23994.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23994`
- Generated at: `2026-05-20T15:37:47.139344+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-30T15:55:43Z`
- Merged: `2025-09-01T03:33:40Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: Isotr0py, JartX
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-30T15:56:41Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fix for GPTQ quantization compatibility for Qwen3 MoE models, specifically to ... (https://github.com/vllm-project/vllm/pull/23994#pullrequestreview-3171100027)
- `2025-08-31T07:49:09Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/23994#pullrequestreview-3171477286)
- `2025-08-31T07:56:05Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/23994#pullrequestreview-3171480216)
- `2025-08-31T08:28:05Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/23994#pullrequestreview-3171495233)
- `2025-08-31T16:02:03Z` `APPROVED` by `Isotr0py` - Have confirmed [Intel/Qwen3-30B-A3B-Instruct-2507-int4-AutoRound]( GPTQ model can still work: (https://github.com/vllm-project/vllm/pull/23994#pullrequestreview-3171693166)

## Inline Comment Hotspots

- `vllm/model_executor/models/qwen3_moe.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-08-31T07:49:09Z` `inline` by `Isotr0py` `vllm/model_executor/models/qwen3_moe.py`:129; signals: moe; excerpt: "How about adding a from autoround gptq attr to GPTQConfig and GPTQMarlinConfig instead of only Qwen3MoE model? I think other models like Qwen2.5-VL may ..." (https://github.com/vllm-project/vllm/pull/23994#discussion_r2312314247)
- `2025-08-31T08:28:05Z` `inline` by `JartX` `vllm/model_executor/models/qwen3_moe.py`:129; signals: moe; excerpt: "@Isotr0py I'm thinking... if we add it there, for example the auto-round itself, auto-gptq that is combined may fail, because it needs the quant ..." (https://github.com/vllm-project/vllm/pull/23994#discussion_r2312329623)
- `2025-08-31T07:56:05Z` `inline` by `JartX` `vllm/model_executor/models/qwen3_moe.py`:129; signals: moe; excerpt: "@Isotr0py Okay, I'm going to try ;)" (https://github.com/vllm-project/vllm/pull/23994#discussion_r2312317471)
- `2025-08-31T10:22:19Z` `issue` by `JartX`; signals: hang; excerpt: "@Isotr0py yum, I need to unlock the PR, in order to continue at the main level, would you mind passing the PR if you're ..." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3240027629)
- `2025-08-31T12:25:58Z` `issue` by `JartX`; signals: perf; excerpt: "Thank you very much for helping and testing @Isotr0py ,I didn't want to move forward without being able to test everything perfectly, and if ..." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3240109173)
- `2025-08-30T16:18:33Z` `issue` by `Isotr0py`; signals: general review; excerpt: "Hmmm, the problematic checkpoint looks quite weird... AutoRound should use AutoRoundConfig instead of GPTQConfig or GPTQMarlinConfig: Seems the correct AutoRound config should look like ..." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3239376828)
- `2025-08-30T16:23:03Z` `issue` by `JartX`; signals: general review; excerpt: "Hi! @Isotr0py thanks for the speed in your response, in ROCM the autoround-gptq method only works by auto gptq as flag in Intel/autoround, so ..." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3239380918)
- `2025-08-30T16:27:17Z` `issue` by `JartX`; signals: general review; excerpt: "@Isotr0py Note: With the flag auto gptq only, only the quant method is gptq which is that it admits me rocm I've gone around ..." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3239384498)
- `2025-08-30T16:47:06Z` `issue` by `Isotr0py`; signals: general review; excerpt: "With the flag auto gptq only, only the quant method is gptq which is that it admits me rocm Oh, I see. Let me ..." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3239395575)
- `2025-08-31T12:14:54Z` `issue` by `Isotr0py`; signals: general review; excerpt: "@JartX I just pushed some updates after making sure the compatability with and Let me double check the compatibility of then." (https://github.com/vllm-project/vllm/pull/23994#issuecomment-3240102297)
