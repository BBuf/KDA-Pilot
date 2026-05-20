# PR Discussion Digest

- Source PR: [vllm-project/vllm#10995](https://github.com/vllm-project/vllm/pull/10995)
- Source page: `sources/prs/vllm/PR-10995.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-10995`
- Generated at: `2026-05-20T15:33:38.607716+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-12-08T20:42:38Z`
- Merged: `2024-12-18T14:57:16Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 67 (approved=2, commented=65)
- Inline review comments: 109
- Review threads observed: 64
- Resolved/outdated thread markers: resolved=5, outdated=58
- Human participants with discussion text: Faraz9877, LucasWilkinson, ProExpertProg, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2024-12-09T00:17:13Z` `COMMENTED` by `tlrmchlsmth` - Looks like landed during the development of this PR and a bunch of stuff got messed up during ... (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2487342368)
- `2024-12-11T04:19:32Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494264136)
- `2024-12-11T04:19:41Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494264260)
- `2024-12-11T04:20:01Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494264504)
- `2024-12-11T04:21:15Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494265560)
- `2024-12-11T04:21:25Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494265705)
- `2024-12-11T04:22:21Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494266446)
- `2024-12-11T04:23:15Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494267187)
- `2024-12-11T04:25:20Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494269486)
- `2024-12-11T04:26:21Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2494270419)
- `2024-12-11T14:20:49Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2495817783)
- `2024-12-11T14:29:34Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2495849825)
- `2024-12-11T14:31:32Z` `COMMENTED` by `tlrmchlsmth` - With this PR, the Python code requires B to be the activation matrix and A to be the ... (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2495855869)
- `2024-12-11T15:43:18Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2496077410)
- `2024-12-11T21:39:04Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497066060)
- `2024-12-11T22:22:33Z` `COMMENTED` by `tlrmchlsmth` - Same overall comments as before -- there is a lot of duplicated code in this PR that shouldn't ... (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497094369)
- `2024-12-12T00:47:27Z` `COMMENTED` by `Faraz9877` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497325657)
- `2024-12-12T04:03:56Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497558888)
- `2024-12-12T04:05:41Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497560252)
- `2024-12-12T04:05:52Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497560385)
- `2024-12-12T04:07:50Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497561910)
- `2024-12-12T04:09:49Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497563396)
- `2024-12-12T04:13:29Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497566796)
- `2024-12-12T04:16:21Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/10995#pullrequestreview-2497569890)
- ... 43 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `csrc/sparse/cutlass/sparse_compressor.cu`: 23 inline comment(s)
- `vllm/_custom_ops.py`: 12 inline comment(s)
- `csrc/sparse/cutlass/sparse_scaled_mm_c3x.cuh`: 12 inline comment(s)
- `CMakeLists.txt`: 6 inline comment(s)
- `csrc/cutlass_extensions/common.hpp`: 6 inline comment(s)
- `csrc/torch_bindings.cpp`: 5 inline comment(s)
- `tests/kernels/test_semi_structured.py`: 4 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_c2x.cu`: 3 inline comment(s)
- `setup.py`: 2 inline comment(s)
- `sane_cute_errors.py`: 2 inline comment(s)
- `requirements-cpu.txt`: 2 inline comment(s)
- `csrc/sparse/cutlass/util/device_memory.h`: 2 inline comment(s)

## High-Signal Discussion

- `2024-12-11T04:25:20Z` `inline` by `Faraz9877` `csrc/sparse/cutlass/sparse_compressor.cu`:134; signals: benchmark, cutlass, kernel, tile; excerpt: "This is the provided code by NVIDIA to compress a 2:4 tile and it's used for benchmarking the kernel. It works for all row-major ..." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1879312673)
- `2024-12-14T06:36:11Z` `inline` by `Faraz9877` `csrc/sparse/cutlass/sparse_compressor.cu`:43; signals: cutlass, epilogue, gemm, kernel; excerpt: "Done. The CUTLASS's CompressorUtility necessitates that a Gemm be defined with all operand types, schedules, etc with an epilogue, albeit the default. I had ..." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1884853390)
- `2024-12-09T00:00:09Z` `inline` by `tlrmchlsmth` `csrc/sparse/cutlass/util/device_memory.h`; signals: compile, cutlass, memory; excerpt: "It looks like several of these files were copied unmodified from the file in the CUTLASS repo (in tools/util/include/cutlass/util? If so, instead of copy-pasting ..." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1875103668)
- `2024-12-11T04:23:15Z` `inline` by `Faraz9877` `csrc/quantization/cutlass_w8a8/scaled_mm_c2x.cu`; signals: cutlass, epilogue, hang; excerpt: "The current changes are necessary to avoid the build problems since we moved to cutlass 3.6.0 and refactored the epilogue header files." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1879311139)
- `2024-12-11T21:54:27Z` `inline` by `tlrmchlsmth` `CMakeLists.txt`:411; signals: compile, cutlass, kernel; excerpt: "Please remove the cutlass extensions path here. Better to be explicit about where the included files are coming from. This also adds to the ..." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1881054736)
- `2024-12-11T22:06:04Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/scaled_mm_c2x.cuh`; signals: cutlass, epilogue, hang; excerpt: "Why is is csrc/cutlass extensions/epilogue/scaled mm epilogues c2x.hpp copied into this file? Could you please revert that change?" (https://github.com/vllm-project/vllm/pull/10995#discussion_r1881067118)
- `2024-12-11T22:18:18Z` `inline` by `tlrmchlsmth` `csrc/sparse/cutlass/sparse_scaled_mm_entry.cu`:26; signals: cuda, cutlass, fp8; excerpt: "We don't support cutlass scaled sparse mm supports fp8 on lovelace systems at all and it requires CUDA 12.2:" (https://github.com/vllm-project/vllm/pull/10995#discussion_r1881082264)
- `2024-12-12T05:08:13Z` `inline` by `LucasWilkinson` `tests/kernels/test_semi_structured.py`; signals: cuda, cutlass, kernel; excerpt: "maybe for a future PR but there should be more tests here, test more shapes, there should be and opcheck test (see test cutlass ..." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1881388833)
- `2024-12-13T14:22:54Z` `inline` by `tlrmchlsmth` `csrc/sparse/cutlass/sparse_compressor.cu`:43; signals: cutlass, epilogue, kernel; excerpt: "These should be pared down further. For example: "cutlass extensions/epilogue/scaled mm epilogues c3x.hpp" already includes "cutlass extensions/epilogue/broadcast load epilogue c3x.hpp" and most of our ..." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1884010655)
- `2024-12-09T00:09:23Z` `inline` by `tlrmchlsmth` `benchmarks/cutlass_benchmarks/sparse_mm/stable_kernels.json`; signals: benchmark, cutlass, kernel; excerpt: "What is this used for?" (https://github.com/vllm-project/vllm/pull/10995#discussion_r1875107344)
- `2024-12-11T04:22:20Z` `inline` by `Faraz9877` `benchmarks/cutlass_benchmarks/sparse_mm/stable_kernels.json`; signals: benchmark, cutlass, kernel; excerpt: "That's for benchmarking only the stable kernels. Not needed here. Removed it." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1879310680)
- `2024-12-11T14:20:49Z` `inline` by `tlrmchlsmth` `csrc/sparse/cutlass/sparse_compressor.cu`:134; signals: cutlass, gemm, kernel; excerpt: "Ok you're right, I checked the actual GEMM kernel and you are doing it the right way there." (https://github.com/vllm-project/vllm/pull/10995#discussion_r1880286883)
