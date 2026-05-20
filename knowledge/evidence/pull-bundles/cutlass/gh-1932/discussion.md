# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#1932](https://github.com/NVIDIA/cutlass/pull/1932)
- Source page: `sources/prs/cutlass/PR-1932.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-1932`
- Generated at: `2026-05-20T15:21:13.877646+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-11-08T23:54:59Z`
- Merged: `2025-01-09T16:22:09Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: IonThruster, hwu36, manishucsd, soundOfDestiny, thakkarV, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2024-11-11T04:01:28Z` `COMMENTED` by `IonThruster` (https://github.com/NVIDIA/cutlass/pull/1932#pullrequestreview-2425173812)
- `2024-11-12T01:32:01Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1932#pullrequestreview-2428412585)
- `2024-11-12T01:32:11Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1932#pullrequestreview-2428412703)
- `2024-11-12T01:35:24Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1932#pullrequestreview-2428415166)
- `2024-11-12T01:53:10Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1932#pullrequestreview-2428430095)
- `2025-01-09T16:21:53Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/1932#pullrequestreview-2540379513)

## Inline Comment Hotspots

- `examples/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling.cu`: 4 inline comment(s)
- `examples/54_hopper_fp8_warp_specialized_gemm/54_hopper_fp8_warp_specialized_gemm.cu`: 2 inline comment(s)
- `include/cutlass/gemm/collective/fp8_accumulation.hpp`: 2 inline comment(s)

## High-Signal Discussion

- `2024-11-12T01:35:24Z` `inline` by `manishucsd` `examples/54_hopper_fp8_warp_specialized_gemm/54_hopper_fp8_warp_specialized_gemm.cu`:103; signals: fp8, gemm, hang, hopper, perf, performance, ptx, warp; excerpt: "I changed it to match with the example 65 configuration to compare the performance of FADD version and FFMA version with the same configuration, ..." (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1837369325)
- `2024-12-28T01:33:28Z` `issue` by `soundOfDestiny`; signals: block, cutlass, gemm, kernel, perf, performance, triton, wgmma; excerpt: "@zhyncs and @soundOfDestiny, I have rebased it on top of the latest commit (CUTLASS 3.6). Apologies for the delay, I was AFK. Looking forward ..." (https://github.com/NVIDIA/cutlass/pull/1932#issuecomment-2564130902)
- `2024-11-11T02:48:04Z` `inline` by `IonThruster` `examples/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling.cu`:155; signals: block, fp8, gemm, hopper, warp; excerpt: "Is it implicit that Element Block Scale will always be same as ElementAccum ? if so, would be good to add some static assert ..." (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1835893997)
- `2024-11-12T01:32:01Z` `inline` by `manishucsd` `examples/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling.cu`:155; signals: block, fp8, gemm, hopper, warp; excerpt: "For now it is the case that ElementBlockScale = ElementAccumulator. I still prefer to write have an alias type in the code to increase ..." (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1837367627)
- `2024-11-11T02:45:24Z` `inline` by `IonThruster` `examples/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling.cu`:33; signals: block, fp8, gemm, hopper, warp; excerpt: "Would be good to update this description" (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1835892752)
- `2024-11-12T01:32:11Z` `inline` by `manishucsd` `examples/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/64_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling.cu`:33; signals: block, fp8, gemm, hopper, warp; excerpt: "Done!" (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1837367704)
- `2024-11-11T03:49:09Z` `inline` by `IonThruster` `include/cutlass/gemm/collective/fp8_accumulation.hpp`:83; signals: block, cutlass, fp8, gemm; excerpt: "Two suggestions : - One can do way more than just scaling accums with this approach - so you might optionally want to consider ..." (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1835920109)
- `2024-11-12T01:53:10Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/fp8_accumulation.hpp`:83; signals: block, cutlass, fp8, gemm; excerpt: "This is a great suggestion and we can consider it in the future. For now, we are looking for scaling the accumulators blockwise and ..." (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1837379552)
- `2024-11-09T03:11:12Z` `inline` by `IonThruster` `examples/54_hopper_fp8_warp_specialized_gemm/54_hopper_fp8_warp_specialized_gemm.cu`:103; signals: fp8, gemm, hopper, warp; excerpt: "can probably skip modifying this example" (https://github.com/NVIDIA/cutlass/pull/1932#discussion_r1835233338)
- `2024-11-12T01:55:52Z` `issue` by `manishucsd`; signals: cutlass, hang; excerpt: "Super cool! Thanks for upstream :) Will do a full review soon. One comment to make to start would to please not extend the ..." (https://github.com/NVIDIA/cutlass/pull/1932#issuecomment-2469433614)
- `2024-12-27T17:32:30Z` `issue` by `manishucsd`; signals: cutlass, kernel; excerpt: "@zhyncs and @soundOfDestiny, I have rebased it on top of the latest commit (CUTLASS 3.6). Apologies for the delay, I was AFK. Looking forward ..." (https://github.com/NVIDIA/cutlass/pull/1932#issuecomment-2563897499)
- `2024-11-09T16:41:34Z` `issue` by `thakkarV`; signals: cutlass; excerpt: "Super cool! Thanks for upstream :) Will do a full review soon. One comment to make to start would to please not extend the ..." (https://github.com/NVIDIA/cutlass/pull/1932#issuecomment-2466279466)
