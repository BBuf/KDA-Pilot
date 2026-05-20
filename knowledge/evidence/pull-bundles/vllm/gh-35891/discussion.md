# PR Discussion Digest

- Source PR: [vllm-project/vllm#35891](https://github.com/vllm-project/vllm/pull/35891)
- Source page: `sources/prs/vllm/PR-35891.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35891`
- Generated at: `2026-05-20T15:40:03.424076+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-03T18:04:39Z`
- Merged: `2026-03-07T21:51:54Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: LucasWilkinson, MatthewBonanni, benchislett, ivanbaldo, mergify, pavanimajety, wzhao18
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-03-03T18:07:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables FP8 KV cache for the Flashinfer MLA Sparse attention backend and also ... (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3884283365)
- `2026-03-03T18:23:25Z` `APPROVED` by `benchislett` - LGTM. Will wait for another reviewer to sign-off, but starting CI now (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3884359809)
- `2026-03-03T18:31:47Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3884402703)
- `2026-03-05T21:36:18Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3899819146)
- `2026-03-05T21:53:20Z` `APPROVED` by `pavanimajety` - LGTM, thanks for the PR! q: If "fp8" is resolving to "fp8 ds mla" for FLASHMLA SPARSE, why ... (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3899876956)
- `2026-03-06T21:56:07Z` `APPROVED` by `MatthewBonanni` - LGTM, thanks! (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3906230045)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/flashmla_sparse.py`: 3 inline comment(s)
- `vllm/model_executor/models/config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-05T16:31:51Z` `issue` by `wzhao18`; signals: accuracy, cache, dtype, flashinfer, fp8, kv cache, mla, nan; excerpt: "Update: the concern for merging this PR is that flashinfer MLA sparse uses the standard fp8 kv cache whereas flashMLA uses the custom FP8 ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4006318416)
- `2026-03-06T22:11:32Z` `issue` by `wzhao18`; signals: accuracy, bf16, cache, flashinfer, fp4, fp8, kv cache, mla; excerpt: "AVG 32 evals. It seems fp8 kv cache gives noticeably better results in both AIME25 and GPQA than fp8 ds mla, achieving even slightly ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4014436819)
- `2026-03-05T20:22:15Z` `issue` by `wzhao18`; signals: bf16, cache, flashinfer, fp4, kv cache, mla, nvfp4; excerpt: "DSv3.2 NVFP4 Weight + BF16 KV Cache (Baseline) AIME25 @ AVG-2 GPQA-diamond @ AVG-2 DSv3.2 NVFP4 Weight + F8 KV Cache (FlashMLA) AIME25 @ ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4007533513)
- `2026-03-05T21:53:20Z` `review` `APPROVED` by `pavanimajety`; signals: accuracy, cache, dtype, flashinfer, fp8, kv cache, mla; excerpt: "LGTM, thanks for the PR! q: If "fp8" is resolving to "fp8 ds mla" for FLASHMLA SPARSE, why is there an accuracy loss? Isn't ..." (https://github.com/vllm-project/vllm/pull/35891#pullrequestreview-3899876956)
- `2026-03-05T21:55:36Z` `issue` by `wzhao18`; signals: accuracy, flashinfer, fp8, mla, perf, performance; excerpt: "@pavanimajety vllm may automatically select flashinfer over flashmla for performance. In those cases, we use the standard fp8, which may potentially lead to accuracy ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4008061103)
- `2026-03-03T18:31:47Z` `inline` by `wzhao18` `vllm/v1/attention/backends/mla/flashmla_sparse.py`:575; signals: attention, cache, dtype, fp8, mla; excerpt: "The inelegance in the code roots from the need to support --kv-cache-dtype fp8 for FlashMLA Sparse even though effectively it only uses fp8 ds ..." (https://github.com/vllm-project/vllm/pull/35891#discussion_r2879884283)
- `2026-03-05T21:36:18Z` `inline` by `wzhao18` `vllm/v1/attention/backends/mla/flashmla_sparse.py`:575; signals: attention, cache, dtype, fp8, mla; excerpt: "No. This PR allows --kv-cache-dtype fp8 for flashMLA, automatically converting "fp8" to "fp8 ds mla". This code snippet is an internal check, which asserts ..." (https://github.com/vllm-project/vllm/pull/35891#discussion_r2892456872)
- `2026-03-05T21:44:31Z` `issue` by `LucasWilkinson`; signals: accuracy, cache, flashinfer, fp8, mla; excerpt: "This goal is just to communicate that FlashMLASparse uses the special per-token quantization scheme developed by DeepSeek for accuracy preservation and released with this ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4007996767)
- `2026-03-06T15:50:05Z` `issue` by `wzhao18`; signals: cache, dtype, fp8, kv cache, nan; excerpt: "@MatthewBonanni @LucasWilkinson I added logging message about the Fp8 KV cache dtype and the alternative options, as well as ways to enable. Please feel ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4012527109)
- `2026-03-05T16:41:22Z` `issue` by `MatthewBonanni`; signals: accuracy, flashinfer, fp8, mla; excerpt: "I chatted with @LucasWilkinson offline - we think that we should continue to let fp8 resolve to fp8 ds mla on FlashMLA and have ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4006354113)
- `2026-03-05T16:55:52Z` `issue` by `benchislett`; signals: nan; excerpt: "@MatthewBonanni that's the current behaviour of this PR I think. I agree that a warning would be helpful. We'll see what the evals look ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4006409910)
- `2026-03-05T21:07:57Z` `issue` by `benchislett`; signals: nan; excerpt: "Seems like variance is too high with AVG@2 to tell. Would probably need AVG@32 to know for certain, but these results at least confirm ..." (https://github.com/vllm-project/vllm/pull/35891#issuecomment-4007797734)
