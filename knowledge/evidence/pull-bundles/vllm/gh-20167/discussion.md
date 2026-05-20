# PR Discussion Digest

- Source PR: [vllm-project/vllm#20167](https://github.com/vllm-project/vllm/pull/20167)
- Source page: `sources/prs/vllm/PR-20167.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20167`
- Generated at: `2026-05-20T15:36:02.367581+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-27T05:47:06Z`
- Merged: `2025-07-08T01:07:22Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 20 (approved=2, commented=18)
- Inline review comments: 21
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: ElizaWszola, bnellnm, mergify, minosfuture, tlrmchlsmth, yeqcharlotte
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-27T05:47:33Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @minosfuture, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2964846846)
- `2025-06-27T05:49:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a correctness issue in cutlass moe by filling zero to cache space. ... (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2964849666)
- `2025-06-27T06:44:10Z` `COMMENTED` by `yeqcharlotte` - thanks for the unit test to repro the issue! cc: @bnellnm to also take a look! (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2964926320)
- `2025-06-27T12:29:26Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2966403184)
- `2025-06-27T15:23:16Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2966989939)
- `2025-06-27T22:32:57Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968101309)
- `2025-06-27T22:33:06Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968101448)
- `2025-06-27T22:33:23Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968101731)
- `2025-06-27T22:33:32Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968101860)
- `2025-06-27T22:34:28Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968102607)
- `2025-06-27T22:36:34Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968104314)
- `2025-06-27T22:37:00Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968104704)
- `2025-06-28T01:39:47Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968305766)
- `2025-06-28T02:14:44Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2968319090)
- `2025-06-30T15:17:54Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2971655970)
- `2025-07-03T00:03:03Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2980977893)
- `2025-07-03T00:51:13Z` `APPROVED` by `tlrmchlsmth` - A couple of questions but good to land once rebased. Thanks for the fix (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2981067567)
- `2025-07-03T17:29:32Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2984021530)
- `2025-07-03T17:31:33Z` `COMMENTED` by `minosfuture` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2984031634)
- `2025-07-07T19:39:47Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20167#pullrequestreview-2995079336)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 12 inline comment(s)
- `tests/kernels/moe/test_cutlass_moe.py`: 9 inline comment(s)

## High-Signal Discussion

- `2025-06-27T15:23:16Z` `inline` by `bnellnm` `tests/kernels/moe/test_cutlass_moe.py`:393; signals: cutlass, kernel, moe; excerpt: "If the body of this is the same as test cutlass moe 8 bit EP can you factor it out into a common function?" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172279344)
- `2025-06-27T22:36:34Z` `inline` by `minosfuture` `tests/kernels/moe/test_cutlass_moe.py`:345; signals: cutlass, kernel, moe; excerpt: "this is not very git-friendly, but note this line is not removed during refactoring. see test cutlass moe 8 bit no graph" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172945611)
- `2025-06-27T06:25:11Z` `inline` by `yeqcharlotte` `tests/kernels/moe/test_cutlass_moe.py`:374; signals: cutlass, kernel, moe; excerpt: "let's have some m 32k" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2170896061)
- `2025-06-27T06:41:53Z` `inline` by `yeqcharlotte` `tests/kernels/moe/test_cutlass_moe.py`:20; signals: cutlass, kernel, moe; excerpt: "does it help with the working sets at line 38-39?" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2170922377)
- `2025-06-27T22:33:05Z` `inline` by `minosfuture` `tests/kernels/moe/test_cutlass_moe.py`:374; signals: cutlass, kernel, moe; excerpt: "added" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172943635)
- `2025-06-27T22:33:23Z` `inline` by `minosfuture` `tests/kernels/moe/test_cutlass_moe.py`:20; signals: cutlass, kernel, moe; excerpt: "unfortunately no. We can look into this more separately." (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172943822)
- `2025-06-27T22:34:27Z` `inline` by `minosfuture` `tests/kernels/moe/test_cutlass_moe.py`:393; signals: cutlass, kernel, moe; excerpt: "Good point! thx. Updated with refactoring a few similar test functions here." (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172944408)
- `2025-06-27T22:37:00Z` `inline` by `minosfuture` `tests/kernels/moe/test_cutlass_moe.py`:462; signals: cutlass, kernel, moe; excerpt: "invalid suggestion. ignore" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172945872)
- `2025-06-27T22:32:57Z` `inline` by `minosfuture` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:182; signals: cutlass, moe; excerpt: "I think the non-chunking (batched) path is not impacted because c1 is fully overridden. I don't have solid proof though (I need to look ..." (https://github.com/vllm-project/vllm/pull/20167#discussion_r2172943553)
- `2025-06-28T01:39:47Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:182; signals: cutlass, moe; excerpt: "I tested this locally and found that the batched case needs to be cleared also. I think it's probably best to unconditionally zero out ..." (https://github.com/vllm-project/vllm/pull/20167#discussion_r2173077226)
- `2025-07-03T00:03:03Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:182; signals: cutlass, moe; excerpt: "I think the. condition should be expert map is not None or self.use batched format. Batched mode is almost always going to have some ..." (https://github.com/vllm-project/vllm/pull/20167#discussion_r2181190343)
- `2025-07-03T00:50:08Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:182; signals: cutlass, moe; excerpt: "Is the failure caused by reading in garbage data for dynamic per-tensor quantization? Does it work in the static per-tensor case?" (https://github.com/vllm-project/vllm/pull/20167#discussion_r2181253346)
