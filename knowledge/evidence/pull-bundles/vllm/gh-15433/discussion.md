# PR Discussion Digest

- Source PR: [vllm-project/vllm#15433](https://github.com/vllm-project/vllm/pull/15433)
- Source page: `sources/prs/vllm/PR-15433.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-15433`
- Generated at: `2026-05-20T15:34:37.192581+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-25T03:16:37Z`
- Merged: `2025-03-29T10:33:56Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 18 (approved=2, commented=16)
- Inline review comments: 26
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=0, outdated=11
- Human participants with discussion text: ProExpertProg, mergify, mgoin, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-26T14:08:05Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2717346928)
- `2025-03-26T14:19:47Z` `COMMENTED` by `ProExpertProg` - A few initial comments! (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2717338197)
- `2025-03-26T15:17:09Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2717644419)
- `2025-03-27T16:19:08Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2722436667)
- `2025-03-27T16:19:22Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2722439045)
- `2025-03-27T16:19:58Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2722442916)
- `2025-03-27T16:20:14Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2722444446)
- `2025-03-27T23:44:19Z` `COMMENTED` by `ProExpertProg` - A few more comments, thanks for working with me on this! (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2723944818)
- `2025-03-28T09:23:03Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2724795658)
- `2025-03-28T09:23:13Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2724796076)
- `2025-03-28T09:23:59Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2724798274)
- `2025-03-28T17:02:31Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726154625)
- `2025-03-28T17:52:32Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726287326)
- `2025-03-28T17:52:53Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726288010)
- `2025-03-28T17:57:47Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726299885)
- `2025-03-28T18:27:19Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726367786)
- `2025-03-28T18:27:37Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726368631)
- `2025-03-28T18:51:38Z` `APPROVED` by `mgoin` - LGTM, nice work! (https://github.com/vllm-project/vllm/pull/15433#pullrequestreview-2726421236)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`: 17 inline comment(s)
- `tests/quantization/test_compressed_tensors.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/triton_scaled_mm.py`: 1 inline comment(s)
- `vllm/_custom_ops.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-28T17:57:47Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:109; signals: block, cutlass, gemm, kernel; excerpt: "Typos/inaccuracies: And then what does this mean: cutlass scaled mm does not support AITER block scaled GEMM yet."?" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2019107000)
- `2025-03-26T14:10:48Z` `inline` by `ProExpertProg` `vllm/_custom_ops.py`:550; signals: cutlass, kernel, triton; excerpt: "This shouldn't live inside cutlass scaled mm, has nothing to do with cutlass. This code should just live inside AiterScaledMMLinearKernel.apply. I know the Triton ..." (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014248057)
- `2025-03-28T17:02:22Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:119; signals: cutlass, fp8, kernel; excerpt: "Just curious for future work: does this kernel support fp8? Also, can you add a comment why w q needs to be transposed here? ..." (https://github.com/vllm-project/vllm/pull/15433#discussion_r2019033945)
- `2025-03-27T16:19:58Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:40; signals: hang, kernel; excerpt: "Thank you. It seems ruff remove the import aiter. I have annotated this line. Ruff will not changed it into pass." (https://github.com/vllm-project/vllm/pull/15433#discussion_r2017048551)
- `2025-03-26T14:05:24Z` `inline` by `ProExpertProg` `tests/quantization/test_compressed_tensors.py`:312; signals: dtype, fp8; excerpt: "Use current platform.fp8 dtype()" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014232606)
- `2025-03-28T17:52:32Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:119; signals: fp8, kernel; excerpt: "ROCm/aiter does not support FP8 at this moment. I have added the comment." (https://github.com/vllm-project/vllm/pull/15433#discussion_r2019099726)
- `2025-03-26T15:17:09Z` `inline` by `tjtanaa` `tests/quantization/test_compressed_tensors.py`:77; signals: gemm; excerpt: "AITER only supports per-channel-per-channel INT8 gemm and per-tensor-per-tensor INT8 GEMM. It does not support mix precision MM and mix quantization scheme." (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014411868)
- `2025-03-26T14:07:24Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:40; signals: kernel; excerpt: "It seems you forgot to import aiter here" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014237546)
- `2025-03-26T14:09:34Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/compressed_tensors/triton_scaled_mm.py`:151; signals: triton; excerpt: "Please clean up comments" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014244069)
- `2025-03-26T14:11:45Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:28; signals: kernel; excerpt: "This can be a single check" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014250672)
- `2025-03-26T14:12:02Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/kernels/scaled_mm/aiter.py`:40; signals: kernel; excerpt: "Yeah agreed this is missing the import" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014251325)
- `2025-03-26T14:13:40Z` `inline` by `ProExpertProg` `tests/quantization/test_compressed_tensors.py`:77; signals: triton; excerpt: "This logic is a bit confusing. What models are and aren't supported by aiter vs Triton?" (https://github.com/vllm-project/vllm/pull/15433#discussion_r2014255957)
