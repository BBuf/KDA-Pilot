# PR Discussion Digest

- Source PR: [vllm-project/vllm#21078](https://github.com/vllm-project/vllm/pull/21078)
- Source page: `sources/prs/vllm/PR-21078.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21078`
- Generated at: `2026-05-20T15:36:19.926621+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-16T20:55:51Z`
- Merged: `2025-09-10T22:31:10Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 5 (approved=3, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: 842974287, LucasWilkinson, MatthewBonanni, benchislett, farazkh80, hjjq, kushanam, mergify, mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-16T20:57:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new FlashInfer MLA (Multi-LoRA Attention) decode kernel for the vLLM V1 ... (https://github.com/vllm-project/vllm/pull/21078#pullrequestreview-3026881018)
- `2025-08-22T20:31:31Z` `APPROVED` by `farazkh80` (https://github.com/vllm-project/vllm/pull/21078#pullrequestreview-3145889722)
- `2025-09-09T15:17:56Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/21078#pullrequestreview-3202127160)
- `2025-09-10T20:48:41Z` `APPROVED` by `LucasWilkinson` - LGTM! Thanks! (https://github.com/vllm-project/vllm/pull/21078#pullrequestreview-3207776273)
- `2025-09-10T22:30:59Z` `APPROVED` by `mgoin` - Thanks! (https://github.com/vllm-project/vllm/pull/21078#pullrequestreview-3208023186)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/flashinfer_mla.py`: 2 inline comment(s)
- `tests/kernels/test_flashinfer_mla_decode.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-09T21:10:51Z` `issue` by `hjjq`; signals: attention, correctness, flash attention, hang, nan, triton; excerpt: "Thanks @MatthewBonanni and @LucasWilkinson, I've made the changes and verified correctness with gsm8k. I've also reverted @mgoin 's changes so that test flex attention ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3272278007)
- `2025-09-09T15:17:56Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/mla/flashinfer_mla.py`:106; signals: attention, flashinfer, hang, mla; excerpt: "please return o, None instead of self. v up proj(o); sorry this changed with" (https://github.com/vllm-project/vllm/pull/21078#discussion_r2333987072)
- `2025-08-22T20:31:23Z` `issue` by `farazkh80`; signals: accuracy, benchmark, kernel, mla; excerpt: "LGTM, is it possible to get accuracy benchmarks on datasets like GPQA, MMLU, GSM8k using both trtllm mla kernel and a reference mla kernel ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3215551999)
- `2025-08-26T18:43:26Z` `issue` by `hjjq`; signals: accuracy, bf16, cutlass; excerpt: "@farazkh80 I've updated the accuracy tests in the main PR body. I haven't found a way to get the GPQA score reported by the ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3225315078)
- `2025-08-28T19:07:01Z` `issue` by `pavanimajety`; signals: fp8, kernel, mla; excerpt: "hey @842974287, sorry but I am picking up the integration of FP8 MLA kernel since I am looking at the integration of Rope + ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3234632031)
- `2025-08-28T17:56:58Z` `issue` by `842974287`; signals: fp8, mla; excerpt: "@hjjq Thanks for adding the trtllm mla support! Looks like this diff doesn't add fp8 kv support yet, I'm wondering if you are already ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3234432083)
- `2025-09-03T17:18:06Z` `issue` by `hjjq`; signals: blackwell, hang; excerpt: "Hi @mgoin , the current [blackwell failure]( seem to be unrelated to my change. Is it safe to merge? cc @kushanam @benchislett" (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3250110545)
- `2025-08-14T15:08:46Z` `issue` by `mgoin`; signals: perf, performance; excerpt: "Moving to draft while investigating performance" (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3188805215)
- `2025-08-27T17:18:59Z` `issue` by `hjjq`; signals: flashinfer; excerpt: "Taking a look at the failed tests. Update: I was able to reproduce the failures with flashinfer v0.2.14.post1. The tests still pass with flashinfer ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3229071495)
- `2025-08-28T19:48:06Z` `issue` by `842974287`; signals: throughput; excerpt: "@pavanimajety Oh no worries at all. Good to know you are on that already. It's a feature we want to test to see how ..." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3234744143)
- `2025-08-28T15:24:53Z` `issue` by `hjjq`; signals: blackwell; excerpt: "I have fixed the blackwell test. For the . Should we revert and exclude them for now? @mgoin" (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3233963772)
- `2025-08-29T17:41:48Z` `issue` by `kushanam`; signals: failing; excerpt: "@mgoin gentle ping on the failing test. Thanks." (https://github.com/vllm-project/vllm/pull/21078#issuecomment-3237763094)
