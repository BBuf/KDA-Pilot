# PR Discussion Digest

- Source PR: [sgl-project/sglang#7148](https://github.com/sgl-project/sglang/pull/7148)
- Source page: `sources/prs/sglang/PR-7148.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7148`
- Generated at: `2026-05-20T15:31:02.619997+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-13T09:00:05Z`
- Merged: `2025-06-25T09:14:40Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: MtFitzRoy, Swipe4057, guoyuhong, hebiao064, josephrocca, zhyncs
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-13T09:00:37Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @guoyuhong, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7148#pullrequestreview-2923943202)
- `2025-06-13T09:02:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This PR fixes FP8 KV Cache support in the FA3 backend by adding conditional type conversions ... (https://github.com/sgl-project/sglang/pull/7148#pullrequestreview-2923947572)
- `2025-06-19T04:11:42Z` `APPROVED` by `hebiao064` - Overall LGTM if benchmark result looks good cc @yundai424 and @qingquansong to take a look if you have ... (https://github.com/sgl-project/sglang/pull/7148#pullrequestreview-2941486097)
- `2025-06-25T09:13:28Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/7148#pullrequestreview-2957355843)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-06-19T06:43:30Z` `issue` by `guoyuhong`; signals: attention, bf16, cache, fp8, kernel, kv cache, memory, shared memory; excerpt: "@guoyuhong I have a question, when using fp8 kvcache, will the kernel load fp8 kv to shared memory directly? and the loading buffer from ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2986824546)
- `2025-06-19T11:54:11Z` `issue` by `guoyuhong`; signals: cache, fp8, h100, kv cache, latency, throughput; excerpt: "I can confirm @MtFitzRoy, we also conducted load testing with and without fp8 kvcache, and enabling fp8 kvcache resulted in reduced throughput on H100. ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2987821118)
- `2025-06-23T04:32:18Z` `issue` by `MtFitzRoy`; signals: cache, fp8, kernel, kv cache, latency, throughput; excerpt: "@MtFitzRoy @Swipe4057 Our use case differs slightly as we employ this in a RL system. We measure throughput based on the total processing time ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2994883544)
- `2025-06-18T12:53:16Z` `issue` by `MtFitzRoy`; signals: cache, fp8, kernel, memory, shared memory; excerpt: "@guoyuhong I have a question, when using fp8 kvcache, will the kernel load fp8 kv to shared memory directly? and the loading buffer from ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2984079878)
- `2025-06-19T07:18:44Z` `issue` by `MtFitzRoy`; signals: cache, fp8, kernel, memory, throughput; excerpt: "@guoyuhong We have tested on the 50k long-context decoding, where the per-layer fp16 kvcache is 5GB. So the attn kernel is definitely memory BW ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2987002191)
- `2025-06-19T12:22:43Z` `issue` by `josephrocca`; signals: cache, fp8, h100, kv cache, throughput; excerpt: "I haven't tested this PR yet, but another use case where FP8 KV Cache helps throughput is when e.g. running DeepSeek V3/R1 with int4 ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2987908545)
- `2025-06-19T08:22:57Z` `issue` by `Swipe4057`; signals: cache, fp8, h100, throughput; excerpt: "I can confirm @MtFitzRoy, we also conducted load testing with and without fp8 kvcache, and enabling fp8 kvcache resulted in reduced throughput on H100. ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2987184563)
- `2025-06-19T04:07:02Z` `issue` by `hebiao064`; signals: accuracy, benchmark, hang; excerpt: "would you please share some benchmark (both accuracy and speed) for DS V3 with and without this change?" (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2986529435)
- `2025-06-19T04:11:42Z` `review` `APPROVED` by `hebiao064`; signals: benchmark; excerpt: "Overall LGTM if benchmark result looks good cc @yundai424 and @qingquansong to take a look if you have time" (https://github.com/sgl-project/sglang/pull/7148#pullrequestreview-2941486097)
- `2025-06-24T09:15:01Z` `issue` by `guoyuhong`; signals: hang; excerpt: "@zhyncs The UT failures ​​do not seem related to​​ my code change." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2999497921)
- `2025-06-18T03:56:37Z` `issue` by `guoyuhong`; signals: general review; excerpt: "@hebiao064 Hi Stefan, BBuf suggested you might have some insights on this PR. Would you mind taking a look when you’re available?" (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2982583629)
- `2025-06-18T15:45:15Z` `issue` by `hebiao064`; signals: general review; excerpt: "@hebiao064 Hi Stefan, BBuf suggested you might have some insights on this PR. Would you mind taking a look when you’re available? Will review ..." (https://github.com/sgl-project/sglang/pull/7148#issuecomment-2984763242)
