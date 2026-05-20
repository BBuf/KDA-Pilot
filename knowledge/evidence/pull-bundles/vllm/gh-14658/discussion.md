# PR Discussion Digest

- Source PR: [vllm-project/vllm#14658](https://github.com/vllm-project/vllm/pull/14658)
- Source page: `sources/prs/vllm/PR-14658.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14658`
- Generated at: `2026-05-20T15:34:31.229816+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-12T06:27:41Z`
- Merged: `2025-03-24T13:21:33Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 5 (approved=3, changes_requested=1, commented=1)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: LagPixelLOL, LucasWilkinson, jeejeelee, jinzhen-lin, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-14T14:46:18Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14658#pullrequestreview-2685796357)
- `2025-03-14T14:48:01Z` `CHANGES_REQUESTED` by `tlrmchlsmth` - Sorry, accidentally hit approve -- The PR looks good but needs documentation on act order, and could you ... (https://github.com/vllm-project/vllm/pull/14658#pullrequestreview-2685814642)
- `2025-03-16T09:36:43Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14658#pullrequestreview-2688594982)
- `2025-03-16T20:39:17Z` `APPROVED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/14658#pullrequestreview-2688790032)
- `2025-03-24T13:20:18Z` `APPROVED` by `tlrmchlsmth` - Thank you! (https://github.com/vllm-project/vllm/pull/14658#pullrequestreview-2710364884)

## Inline Comment Hotspots

- `tests/kernels/test_marlin_gemm.py`: 3 inline comment(s)
- `csrc/quantization/gptq_marlin/gptq_marlin.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-14T14:45:24Z` `inline` by `tlrmchlsmth` `tests/kernels/test_marlin_gemm.py`; signals: gemm, kernel, layout; excerpt: "We should try to avoid ballooning the tests via combinatorial explosion. Could you add a separate smaller test for non-contiguous layouts, similar to what ..." (https://github.com/vllm-project/vllm/pull/14658#discussion_r1995713785)
- `2025-03-14T02:00:13Z` `issue` by `jinzhen-lin`; signals: benchmark, kernel, mla; excerpt: "It appears to be working now. The benchmarks results show that MLA + chunked-prefill still have some problems now. But I think it is ..." (https://github.com/vllm-project/vllm/pull/14658#issuecomment-2723132269)
- `2025-03-14T14:43:39Z` `inline` by `tlrmchlsmth` `tests/kernels/test_marlin_gemm.py`:268; signals: gemm, kernel; excerpt: "Does this not work for act order=True? Needs to be documented somewhere, with an explanation of why" (https://github.com/vllm-project/vllm/pull/14658#discussion_r1995710969)
- `2025-03-16T09:36:43Z` `inline` by `jinzhen-lin` `tests/kernels/test_marlin_gemm.py`:268; signals: gemm, kernel; excerpt: "I have added the support for act order." (https://github.com/vllm-project/vllm/pull/14658#discussion_r1997542489)
- `2025-03-14T14:41:54Z` `inline` by `tlrmchlsmth` `csrc/quantization/gptq_marlin/gptq_marlin.cu`:540; signals: gemm; excerpt: "light suggestion of naming this lda - stands for the "leading dimension of A", and is the name used in [GEMM]( for this concept, ..." (https://github.com/vllm-project/vllm/pull/14658#discussion_r1995708339)
- `2025-03-14T14:48:01Z` `review` `CHANGES_REQUESTED` by `tlrmchlsmth`; signals: general review; excerpt: "Sorry, accidentally hit approve -- The PR looks good but needs documentation on act order, and could you look at dialing down the number ..." (https://github.com/vllm-project/vllm/pull/14658#pullrequestreview-2685814642)
- `2025-03-12T11:42:07Z` `issue` by `LagPixelLOL`; signals: general review; excerpt: "It doesn't throw the error message anymore but the output is incoherent if the input length is longer than --max-num-batched-tokens. If prefix caching is ..." (https://github.com/vllm-project/vllm/pull/14658#issuecomment-2717590653)
- `2025-03-14T06:06:50Z` `issue` by `jeejeelee`; signals: general review; excerpt: "@mgoin The error test seems not related to this PR. You can merge the main branch to avoid lora test failure." (https://github.com/vllm-project/vllm/pull/14658#issuecomment-2723704513)
- `2025-03-24T02:48:53Z` `issue` by `LucasWilkinson`; signals: general review; excerpt: "Note there's 2 fixes for this in-flight and this one, I believe this PR is a better solution (avoid an unnecessary copy) but is ..." (https://github.com/vllm-project/vllm/pull/14658#issuecomment-2746746829)
