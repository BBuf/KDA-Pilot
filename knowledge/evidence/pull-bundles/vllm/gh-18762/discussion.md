# PR Discussion Digest

- Source PR: [vllm-project/vllm#18762](https://github.com/vllm-project/vllm/pull/18762)
- Source page: `sources/prs/vllm/PR-18762.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18762`
- Generated at: `2026-05-20T15:35:21.090179+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-27T12:35:22Z`
- Merged: `2025-06-07T01:26:11Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 36 (approved=2, commented=34)
- Inline review comments: 37
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=19, outdated=16
- Human participants with discussion text: ElizaWszola, bennorris123, bnellnm, mergify, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-05-28T20:31:51Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876352944)
- `2025-05-28T20:33:38Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876356615)
- `2025-05-28T20:49:12Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876393224)
- `2025-05-28T20:51:30Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876398752)
- `2025-05-28T20:51:49Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876399398)
- `2025-05-28T20:52:44Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876401066)
- `2025-05-28T20:56:21Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876409106)
- `2025-05-28T21:16:10Z` `COMMENTED` by `tlrmchlsmth` - Left a few comments, but looks good overall -- lets try to get it landed once those and ... (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876435965)
- `2025-05-28T21:23:23Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876478587)
- `2025-05-28T21:24:14Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876479947)
- `2025-05-28T21:32:03Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876493993)
- `2025-05-28T21:35:26Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876499540)
- `2025-05-28T21:36:27Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876501737)
- `2025-05-28T21:43:04Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876513132)
- `2025-05-28T21:43:12Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2876513339)
- `2025-05-29T17:27:44Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2879069684)
- `2025-05-29T23:54:42Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2879854633)
- `2025-05-30T02:17:16Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880028129)
- `2025-05-30T02:20:52Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880031539)
- `2025-05-30T02:21:43Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880032699)
- `2025-05-30T02:21:57Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880032930)
- `2025-05-30T02:24:10Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880035145)
- `2025-05-30T02:28:15Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880038786)
- `2025-05-30T03:07:11Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18762#pullrequestreview-2880074972)
- ... 12 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 11 inline comment(s)
- `vllm/model_executor/layers/fused_moe/pplx_prepare_finalize.py`: 8 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/modular_kernel.py`: 4 inline comment(s)
- `tests/kernels/moe/test_pplx_cutlass_moe.py`: 3 inline comment(s)
- `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-30T02:20:51Z` `inline` by `ElizaWszola` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:262; signals: cutlass, fp4, kernel, moe, sm100; excerpt: "Copy-paste issue, I didn't notice that the old MoE data kernel I copied it from has SM100 support for fp4 now" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2115031728)
- `2025-05-30T02:24:09Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:115; signals: cuda, cutlass, kernel, moe; excerpt: "potentially... I think I can circumvent it with a custom CUDA kernel and extra mapping for expert offsets and problem sizes1/2 if needed" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2115034369)
- `2025-05-30T03:07:11Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/pplx_prepare_finalize.py`:104; signals: alignment, correctness, fp8, moe; excerpt: "I don't know if you've got correctness yet but I had to use torch.zeros here to get some of my fp8 + pplx tests ..." (https://github.com/vllm-project/vllm/pull/18762#discussion_r2115064886)
- `2025-05-28T20:33:37Z` `inline` by `bnellnm` `tests/kernels/moe/test_pplx_cutlass_moe.py`:301; signals: cutlass, kernel, moe, ptx; excerpt: "Type pptx - pplx" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2112704477)
- `2025-05-28T21:35:26Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:115; signals: cuda, cudagraph, cutlass, moe; excerpt: "Is this going to interfere with cudagraphs?" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2112793982)
- `2025-05-28T20:31:51Z` `inline` by `bnellnm` `tests/kernels/moe/test_pplx_cutlass_moe.py`:36; signals: cutlass, kernel, moe; excerpt: "We should probably put all these multiprocess utilities in a separate file now since they are also used by test pplx moe.py" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2112701845)
- `2025-05-28T21:07:24Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:262; signals: cutlass, sm100, sm90; excerpt: "Should this be the following? I'm not sure why we're looking at ENABLE SCALED MM SM90, but the check for ENABLE SCALED MM SM100 ..." (https://github.com/vllm-project/vllm/pull/18762#discussion_r2112754538)
- `2025-05-28T21:09:40Z` `inline` by `tlrmchlsmth` `tests/kernels/moe/test_pplx_cutlass_moe.py`:21; signals: cutlass, kernel, moe; excerpt: "IIUC, AllToAll dispatches to AllToAllInternode under the hood, so we shouldn't need to interact with it directly" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2112757328)
- `2025-05-28T21:43:03Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:308; signals: cutlass, fp8, moe; excerpt: "Why is this bit pulled out? It should be handled by whatever PrepareAndFinalze object is used w/CutlassExpertsFp8." (https://github.com/vllm-project/vllm/pull/18762#discussion_r2112803021)
- `2025-05-30T02:28:15Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:308; signals: cutlass, hang, moe; excerpt: "This should be the function that runs the old version of cutlass MoE when no PrepareAndFinalize is being run. I changed the structure of ..." (https://github.com/vllm-project/vllm/pull/18762#discussion_r2115037195)
- `2025-05-30T03:13:36Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:308; signals: cutlass, fp8, moe; excerpt: "I was thinking more in terms of not duplicating code and using the new modular classes to serve as the implementation of cutlass moe ..." (https://github.com/vllm-project/vllm/pull/18762#discussion_r2115069145)
- `2025-05-30T02:17:16Z` `inline` by `ElizaWszola` `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`:112; signals: cutlass, hang, moe; excerpt: "I don't see this producing any new warnings, I'll make the change" (https://github.com/vllm-project/vllm/pull/18762#discussion_r2115029105)
