# PR Discussion Digest

- Source PR: [vllm-project/vllm#34448](https://github.com/vllm-project/vllm/pull/34448)
- Source page: `sources/prs/vllm/PR-34448.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34448`
- Generated at: `2026-05-20T15:39:49.088367+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-12T18:05:17Z`
- Merged: `2026-03-02T07:31:20Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 14
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=6
- Human participants with discussion text: EdalatiAli, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-12T18:10:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates SM100+ MXFP8 blockscaled grouped kernels from SGLang into vLLM, including kernel sources, ... (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3792781095)
- `2026-02-14T19:14:05Z` `COMMENTED` by `mgoin` - Thanks for working on this @EdalatiAli, it seems reasonable to me overall. Just a few nits. Generally we'd ... (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3802340758)
- `2026-02-19T21:58:00Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3828757690)
- `2026-02-20T21:18:14Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3834251232)
- `2026-02-20T22:01:09Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3834401638)
- `2026-02-20T22:01:23Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3834402701)
- `2026-02-20T22:02:05Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3834406451)
- `2026-02-20T23:08:38Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3834561181)
- `2026-02-26T22:32:01Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3863886707)
- `2026-02-26T22:39:04Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3863917559)
- `2026-02-26T22:39:59Z` `APPROVED` by `mgoin` - LGTM! (https://github.com/vllm-project/vllm/pull/34448#pullrequestreview-3863920611)

## Inline Comment Hotspots

- `csrc/moe/mxfp8_grouped_gemm/es_sm100_mxfp8_blockscaled.cu`: 2 inline comment(s)
- `csrc/moe/mxfp8_grouped_gemm/es_sm100_mxfp8_blockscaled_group_quant.cu`: 2 inline comment(s)
- `csrc/moe/mxfp8_moe/mxfp8_experts_quant.cuh`: 2 inline comment(s)
- `tests/kernels/moe/test_es_mxfp8_blockscaled_moe.py`: 2 inline comment(s)
- `tests/kernels/moe/test_cutlass_mxfp8_moe.py`: 2 inline comment(s)
- `csrc/torch_bindings.cpp`: 2 inline comment(s)
- `tests/kernels/moe/test_cutlass_mxfp8_grouped_mm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-14T19:02:46Z` `inline` by `mgoin` `tests/kernels/moe/test_es_mxfp8_blockscaled_moe.py`:38; signals: block, cuda, fp8, kernel, moe, sm120; excerpt: "Could replace with return current platform.is cuda() and current platform.is device capability family(100). We don't want to allow sm120 for this kernel" (https://github.com/vllm-project/vllm/pull/34448#discussion_r2807804978)
- `2026-02-14T19:09:47Z` `inline` by `mgoin` `csrc/torch_bindings.cpp`:444; signals: block, cutlass, fp8, moe, sm100; excerpt: "nit: IMO the naming is a bit weird, although I can understand wanting to keep the code similar to the sglang impl. For instance ..." (https://github.com/vllm-project/vllm/pull/34448#discussion_r2807810411)
- `2026-02-20T22:01:09Z` `inline` by `EdalatiAli` `csrc/moe/mxfp8_grouped_gemm/es_sm100_mxfp8_blockscaled.cu`:14; signals: block, fp8, gemm, moe, sm100; excerpt: "Addressed!" (https://github.com/vllm-project/vllm/pull/34448#discussion_r2835273982)
- `2026-02-20T22:01:23Z` `inline` by `EdalatiAli` `csrc/moe/mxfp8_grouped_gemm/es_sm100_mxfp8_blockscaled_group_quant.cu`:13; signals: block, fp8, gemm, moe, sm100; excerpt: "Addressed!" (https://github.com/vllm-project/vllm/pull/34448#discussion_r2835274711)
- `2026-02-14T19:04:03Z` `inline` by `mgoin` `tests/kernels/moe/test_cutlass_mxfp8_moe.py`:90; signals: cutlass, fp8, kernel, moe; excerpt: "Could you use the torch moe util used in other moe tests?" (https://github.com/vllm-project/vllm/pull/34448#discussion_r2807805865)
- `2026-02-19T21:58:00Z` `inline` by `EdalatiAli` `tests/kernels/moe/test_es_mxfp8_blockscaled_moe.py`:38; signals: block, fp8, kernel, moe; excerpt: "Done!" (https://github.com/vllm-project/vllm/pull/34448#discussion_r2830359928)
- `2026-02-20T23:08:38Z` `inline` by `EdalatiAli` `tests/kernels/moe/test_cutlass_mxfp8_moe.py`:90; signals: cutlass, fp8, kernel, moe; excerpt: "Updated the test to use torch moe signle to follow other tests." (https://github.com/vllm-project/vllm/pull/34448#discussion_r2835434543)
- `2026-02-20T23:14:37Z` `issue` by `EdalatiAli`; signals: fp8, kernel, moe, perf; excerpt: "Thanks for working on this @EdalatiAli, it seems reasonable to me overall. Just a few nits. Generally we'd like to land kernels that we ..." (https://github.com/vllm-project/vllm/pull/34448#issuecomment-3937589734)
- `2026-02-20T21:18:14Z` `inline` by `EdalatiAli` `csrc/torch_bindings.cpp`:444; signals: cutlass, fp8, kernel; excerpt: "I renamed the kernels to cutlass mxfp8 grouped mm and mxfp8 experts quant following your suggestion. I renamed the related files and code accordingly." (https://github.com/vllm-project/vllm/pull/34448#discussion_r2835135267)
- `2026-02-20T22:02:05Z` `inline` by `EdalatiAli` `csrc/moe/mxfp8_moe/mxfp8_experts_quant.cuh`:354; signals: fp8, kernel, moe; excerpt: "Will leave it for future improvement on the kernel." (https://github.com/vllm-project/vllm/pull/34448#discussion_r2835278015)
