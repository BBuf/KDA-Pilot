# PR Discussion Digest

- Source PR: [vllm-project/vllm#13798](https://github.com/vllm-project/vllm/pull/13798)
- Source page: `sources/prs/vllm/PR-13798.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13798`
- Generated at: `2026-05-20T15:34:06.235426+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-25T02:27:07Z`
- Merged: `2025-03-04T15:55:08Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 13
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=2, outdated=8
- Human participants with discussion text: YSF-A, kushanam, mergify, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-02-25T02:40:01Z` `COMMENTED` by `tlrmchlsmth` - Thanks for the contribution @kushanam! Looks good overall, left a few comments/questions (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2638980216)
- `2025-02-25T02:57:48Z` `COMMENTED` by `kushanam` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2639020240)
- `2025-02-25T03:17:19Z` `COMMENTED` by `kushanam` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2639075909)
- `2025-02-25T03:33:29Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2639101316)
- `2025-02-25T16:30:10Z` `COMMENTED` by `kushanam` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2641731567)
- `2025-02-27T20:59:50Z` `COMMENTED` by `kushanam` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2649071642)
- `2025-02-27T21:21:55Z` `APPROVED` by `tlrmchlsmth` - Thanks, looks great to me now! Could you merge in the changes from latest main? (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2649111777)
- `2025-03-03T18:51:23Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2654977739)
- `2025-03-03T18:55:40Z` `COMMENTED` by `tlrmchlsmth` - There are some linker errors when CUDA < 12.8 that need to be addressed. (I left some inline ... (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2654991950)
- `2025-03-04T02:00:12Z` `COMMENTED` by `kushanam` (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2655736873)

## Inline Comment Hotspots

- `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x_blackwell.hpp`: 5 inline comment(s)
- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm.cuh`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_c3x.cu`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/c3x/cutlass_gemm_caller.cuh`: 1 inline comment(s)
- `CMakeLists.txt`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-25T03:17:19Z` `inline` by `kushanam` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm.cuh`:103; signals: alignment, blackwell, cutlass, hopper, perf, tma; excerpt: "Generally 128-bit alignment (i.e. 8 for 16-bit data types) is required for best TMA perf, 4 might work but perf will suffer and It's ..." (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968775332)
- `2025-03-03T18:55:40Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: blackwell, compile, cuda, kernel, sm90; excerpt: "There are some linker errors when CUDA < 12.8 that need to be addressed. (I left some inline comments) This made me realize we ..." (https://github.com/vllm-project/vllm/pull/13798#pullrequestreview-2654991950)
- `2025-02-25T02:31:45Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm.cuh`:103; signals: alignment, cutlass, kernel, perf, performance; excerpt: "We've been setting AlignmentD to 4 to reduce the alignment requirement of these kernels. Can this be 4 instead of 8? Also, do you ..." (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968727985)
- `2025-02-25T02:57:48Z` `inline` by `kushanam` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x_blackwell.hpp`; signals: blackwell, cutlass, epilogue, tile; excerpt: "BW doesn't like EpilogueDescriptor. On the other hand the only use for EpilogueDescriptor in scaled mm epilogues c3x seems to be tile shapes, so ..." (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968748066)
- `2025-02-25T03:33:29Z` `inline` by `tlrmchlsmth` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x_blackwell.hpp`; signals: blackwell, cutlass, epilogue, hang; excerpt: "Yep that's the only use. we could get rid of it all together and keep all under the same file I think that's the ..." (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968788712)
- `2025-02-25T02:34:50Z` `inline` by `tlrmchlsmth` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x_blackwell.hpp`; signals: blackwell, cutlass, epilogue; excerpt: "At first glance, this looks very similar to csrc/cutlass extensions/epilogue/scaled mm epilogues c3x.hpp. Why can't it be the same code?" (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968731472)
- `2025-03-03T18:50:51Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:134; signals: cuda, cutlass, sm100; excerpt: "This is causing linker errors in the CI. Need to guard against calling cutlass scaled mm sm100 when CUDA < 12.8 Something like this:" (https://github.com/vllm-project/vllm/pull/13798#discussion_r1978018240)
- `2025-02-25T02:29:26Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/c3x/cutlass_gemm_caller.cuh`:83; signals: cutlass, gemm, hang; excerpt: "Could you explain this change?" (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968726465)
- `2025-02-25T02:38:21Z` `inline` by `tlrmchlsmth` `CMakeLists.txt`:310; signals: cuda, fp8, sm100; excerpt: "Here we'll have to guard against compilation of scaled mm sm100 fp8.cu when CUDA < 12.8" (https://github.com/vllm-project/vllm/pull/13798#discussion_r1968734725)
- `2025-02-25T16:30:10Z` `inline` by `kushanam` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x_blackwell.hpp`; signals: blackwell, cutlass, epilogue; excerpt: "For sure!" (https://github.com/vllm-project/vllm/pull/13798#discussion_r1970135461)
- `2025-02-27T20:59:50Z` `inline` by `kushanam` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x_blackwell.hpp`; signals: blackwell, cutlass, epilogue; excerpt: "done." (https://github.com/vllm-project/vllm/pull/13798#discussion_r1974330200)
- `2025-03-03T18:49:31Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/scaled_mm_c3x.cu`:94; signals: cuda, cutlass; excerpt: "We might need to ifdef this out when CUDA < 12.8" (https://github.com/vllm-project/vllm/pull/13798#discussion_r1978015820)
