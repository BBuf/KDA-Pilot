# PR Discussion Digest

- Source PR: [vllm-project/vllm#13932](https://github.com/vllm-project/vllm/pull/13932)
- Source page: `sources/prs/vllm/PR-13932.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13932`
- Generated at: `2026-05-20T15:34:17.016573+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-26T23:10:53Z`
- Merged: `2025-04-01T16:07:43Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 23 (approved=3, commented=20)
- Inline review comments: 22
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=13, outdated=12
- Human participants with discussion text: LucasWilkinson, bnellnm, huangtingwei9988, mergify, tlrmchlsmth, youkaichao
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-12T12:43:16Z` `COMMENTED` by `huangtingwei9988` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2678336245)
- `2025-03-26T01:20:29Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2715637619)
- `2025-03-26T01:27:31Z` `COMMENTED` by `youkaichao` - how large is the wheel? do we want to ship it by default? (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2715666103)
- `2025-03-26T01:45:20Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2715695482)
- `2025-03-26T13:55:37Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2717290459)
- `2025-03-26T14:47:01Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2717539946)
- `2025-03-26T20:13:57Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2718517617)
- `2025-03-27T01:40:42Z` `COMMENTED` by `LucasWilkinson` - Overall looks pretty good! left a few more comments (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2718939462)
- `2025-03-27T02:01:22Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2719177931)
- `2025-03-27T02:06:39Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2719195527)
- `2025-03-27T02:07:08Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2719197267)
- `2025-03-27T02:08:47Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2719200282)
- `2025-03-27T04:04:36Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2719505060)
- `2025-03-27T12:48:11Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2721327443)
- `2025-03-27T16:59:23Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2722690632)
- `2025-03-27T18:40:32Z` `APPROVED` by `LucasWilkinson` - LGTM now, thanks for the updates! (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2723084276)
- `2025-03-28T21:34:29Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2726863672)
- `2025-03-28T21:45:57Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2726899089)
- `2025-03-31T19:37:29Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2730332589)
- `2025-03-31T19:37:37Z` `COMMENTED` by `tlrmchlsmth` - The expert map doesn't work if it has -1 in it, right? (so basically it doesn't work at ... (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2730332864)
- `2025-03-31T20:21:32Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2730422730)
- `2025-03-31T20:22:34Z` `APPROVED` by `tlrmchlsmth` - LGTM (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2730424915)
- `2025-03-31T22:13:49Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13932#pullrequestreview-2730635164)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 16 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-27T12:48:11Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1589; signals: block, deepgemm, gemm, kernel, moe, triton; excerpt: "moe align block size doesn't literally pad the M dimension it comes up with num tokens post padded which the Triton kernels use to ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r2016503911)
- `2025-03-27T01:05:43Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/quantization/fp8.py`:618; signals: aligned, fp8, layout, tma; excerpt: "Does get col major tma aligned tensor require that its column major? for a cursory reading of it seems like it could handle none ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015215330)
- `2025-03-27T02:06:39Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/fp8.py`:618; signals: deepgemm, fp8, gemm, kernel; excerpt: "I did this to try to avoid the transpose at runtime. I check for col major so that we don't accidentally transpose the weights ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015395602)
- `2025-03-27T02:08:47Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1485; signals: deepgemm, gemm, moe, triton; excerpt: "I agree the flags are not nice. I think pulling the DeepGemm implementation out into a separate function/class would end up being just as ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015399032)
- `2025-03-26T01:47:32Z` `issue` by `bnellnm`; signals: cutlass, deepgemm, gemm, kernel; excerpt: "how large is the wheel? do we want to ship it by default? The DeepGemm repo is around 200Mb. Most of that comes from ..." (https://github.com/vllm-project/vllm/pull/13932#issuecomment-2753036717)
- `2025-03-27T04:04:36Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1589; signals: aligned, block, moe; excerpt: "im a bit confused on why this is required, doesn't moe align block size pad so we are block aligned after permuting?" (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015584859)
- `2025-03-27T01:38:55Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:206; signals: deepgemm, gemm, moe; excerpt: "nit: is this comment needed? it doesnt appear that compressed tensors currently supports DeepGEMM" (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015335678)
- `2025-03-27T02:07:08Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:206; signals: deepgemm, gemm, moe; excerpt: "I wasn't sure whether compressed tensors could use DeepGemm or not. I'll remove the comment," (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015396817)
- `2025-03-12T12:42:52Z` `inline` by `huangtingwei9988` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1371; signals: block, moe; excerpt: "hi～, @bnellnm new S may be just padded to (M top k + pad size)// 128 = 0? Because the size of sorted token ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r1991417451)
- `2025-03-26T13:55:37Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1406; signals: block, moe; excerpt: "nit: in utils.py we have round up, i.e. this could be round up(sorted token ids.numel(), block m) - - sorted token ids.numel()" (https://github.com/vllm-project/vllm/pull/13932#discussion_r2014206933)
- `2025-03-27T01:02:16Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/quantization/fp8.py`:427; signals: fp8, gemm; excerpt: "nit: for consistency it might be nice to use allow deep gemm or use deep gemm everywhere, I find the mix a bit confusing ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r2015204832)
- `2025-03-27T16:59:23Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1589; signals: block, moe; excerpt: "For posterity, @bnellnm spoke offline, after the perm the activations have shape sorted token ids.shape(0) so moe align block size does cause the activation ..." (https://github.com/vllm-project/vllm/pull/13932#discussion_r2017160565)
