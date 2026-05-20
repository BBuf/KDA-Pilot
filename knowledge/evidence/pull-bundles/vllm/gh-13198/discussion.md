# PR Discussion Digest

- Source PR: [vllm-project/vllm#13198](https://github.com/vllm-project/vllm/pull/13198)
- Source page: `sources/prs/vllm/PR-13198.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13198`
- Generated at: `2026-05-20T15:33:58.488931+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-13T03:42:53Z`
- Merged: `2025-02-14T00:01:14Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 22
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=11, outdated=6
- Human participants with discussion text: alexm-redhat, dsikka, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-13T14:47:44Z` `COMMENTED` by `alexm-redhat` - LGTM in general, I don't fully understand the template of CUTLASS, but the code makes sense. (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615181782)
- `2025-02-13T14:51:44Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615244931)
- `2025-02-13T14:55:43Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615258108)
- `2025-02-13T15:06:24Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615324484)
- `2025-02-13T15:09:36Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615342061)
- `2025-02-13T15:19:33Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615390723)
- `2025-02-13T15:31:43Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615429740)
- `2025-02-13T16:20:09Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615578554)
- `2025-02-13T16:20:37Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615579842)
- `2025-02-13T18:38:07Z` `APPROVED` by `alexm-redhat` - LGTM (https://github.com/vllm-project/vllm/pull/13198#pullrequestreview-2615927117)

## Inline Comment Hotspots

- `tests/kernels/test_cutlass_2of4_sparse.py`: 7 inline comment(s)
- `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_24.py`: 3 inline comment(s)
- `CMakeLists.txt`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm.cuh`: 2 inline comment(s)
- `csrc/sparse/cutlass/sparse_scaled_mm_c3x.cu`: 2 inline comment(s)
- `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c2x.hpp`: 1 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_c2x.cuh`: 1 inline comment(s)
- `csrc/sparse/cutlass/sparse_scaled_mm_entry.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-13T15:31:43Z` `inline` by `tlrmchlsmth` `tests/kernels/test_cutlass_2of4_sparse.py`:61; signals: cutlass, hang, kernel; excerpt: "I added a comment below, also changed this to only happen for the int8 case (where it's needed so the inputs aren't all 0s)" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954738999)
- `2025-02-13T14:42:41Z` `inline` by `alexm-redhat` `tests/kernels/test_cutlass_2of4_sparse.py`:66; signals: cutlass, dtype, kernel; excerpt: "bfloat16 as default is something expected? or we want the dtype to be explicit always?" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954631179)
- `2025-02-13T14:36:59Z` `inline` by `alexm-redhat` `csrc/sparse/cutlass/sparse_scaled_mm_c3x.cu`:122; signals: cutlass, h100; excerpt: "the dispatching mechanism is hardcoded to specific numbers, does it work for different GPUs? or it is mainly for H100?" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954620511)
- `2025-02-13T14:51:44Z` `inline` by `tlrmchlsmth` `CMakeLists.txt`:232; signals: cutlass, kernel; excerpt: "We're already on 3.7. I just noticed this is out of date, which just means some incorrect messages are printed while building the cutlass ..." (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954647595)
- `2025-02-13T14:31:59Z` `inline` by `alexm-redhat` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c2x.hpp`:319; signals: cutlass, epilogue; excerpt: "formatting?" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954611784)
- `2025-02-13T14:32:39Z` `inline` by `alexm-redhat` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`:203; signals: cutlass, epilogue; excerpt: "but the bias = duplicate text" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954612946)
- `2025-02-13T14:33:02Z` `inline` by `alexm-redhat` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`:384; signals: cutlass, epilogue; excerpt: "formatting" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954613654)
- `2025-02-13T14:45:44Z` `inline` by `alexm-redhat` `tests/kernels/test_cutlass_2of4_sparse.py`:61; signals: cutlass, kernel; excerpt: "why 5?" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954636456)
- `2025-02-13T14:46:10Z` `inline` by `alexm-redhat` `tests/kernels/test_cutlass_2of4_sparse.py`:195; signals: cutlass, kernel; excerpt: "nice tests" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954637199)
- `2025-02-13T14:46:43Z` `inline` by `alexm-redhat` `tests/kernels/test_cutlass_2of4_sparse.py`:224; signals: cutlass, kernel; excerpt: "1e0 and 2e0 seem to be pretty large, no?" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954638153)
- `2025-02-13T14:55:42Z` `inline` by `tlrmchlsmth` `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`:384; signals: cutlass, epilogue; excerpt: "My editor adds this by default" (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954655382)
- `2025-02-13T15:06:24Z` `inline` by `tlrmchlsmth` `tests/kernels/test_cutlass_2of4_sparse.py`:66; signals: cutlass, kernel; excerpt: "I think the code is fine but is kind of weird/hacky/confusing, so I left a comment." (https://github.com/vllm-project/vllm/pull/13198#discussion_r1954688925)
