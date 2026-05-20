# PR Discussion Digest

- Source PR: [sgl-project/sglang#21314](https://github.com/sgl-project/sglang/pull/21314)
- Source page: `sources/prs/sglang/PR-21314.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21314`
- Generated at: `2026-05-20T15:29:12.031436+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T13:12:36Z`
- Merged: `2026-04-01T01:04:35Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 14 (approved=1, changes_requested=1, commented=12)
- Inline review comments: 13
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: BBuf, DarkSharpness, HydraQYH, b8zhong
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-24T13:18:22Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request significantly refactors the NVFP4 scaled matrix multiplication (GEMM) kernels by modularizing the CUDA ... (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-3999107262)
- `2026-03-25T03:34:51Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4003699372)
- `2026-03-25T03:37:14Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4003709130)
- `2026-03-25T03:38:23Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4003712147)
- `2026-03-25T03:38:29Z` `CHANGES_REQUESTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4003712346)
- `2026-03-25T03:58:26Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4003760206)
- `2026-03-25T03:58:47Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4003760910)
- `2026-03-25T07:16:54Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4004382196)
- `2026-03-25T08:03:31Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4004731389)
- `2026-03-25T13:07:42Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4006541397)
- `2026-03-25T13:13:10Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4006575313)
- `2026-03-25T21:13:14Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4009910469)
- `2026-03-27T05:52:25Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4018976518)
- `2026-04-01T00:57:58Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21314#pullrequestreview-4041079358)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`: 6 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `sgl-kernel/benchmark/bench_fp4_gemm.py`: 2 inline comment(s)
- `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_sm120.cuh`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-25T07:16:45Z` `inline` by `HydraQYH` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_sm120.cuh`:24; signals: fp4, gemm, kernel, nvfp4, perf, performance, sm100, sm120; excerpt: "Have you tried the Swap A/B approach? If Swap A/B works, I believe it can also improve performance on the Sm100." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2986276319)
- `2026-03-25T13:07:42Z` `inline` by `b8zhong` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_sm120.cuh`:24; signals: cutlass, fp4, gemm, kernel, nvfp4, sm120, sm90, wgmma; excerpt: "Yes, I also agree. By the way, I'm only familiar with it's usage on SM90 with respect to WGMMA efficiency, but I assume it ..." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2988106183)
- `2026-03-25T06:47:52Z` `inline` by `HydraQYH` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`:91; signals: cuda, cutlass, fp4, gemm, kernel, memory, nvfp4; excerpt: "@DarkSharpness It appears that the workspace required by the CUTLASS Kernel is requested by itself via cudaMallocAsync. @b8zhong As far as I know, we ..." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2986158704)
- `2026-03-25T03:37:14Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_fp4_gemm.py`:361; signals: benchmark, fp4, gemm, kernel; excerpt: "The CSV schema looks inconsistent here. We now write [provider, M, N, K, ms, bandwidth gbs] below, but the header still only has 5 ..." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2985539568)
- `2026-03-25T08:03:31Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`:91; signals: fp4, gemm, kernel, nvfp4; excerpt: "I would recommend allocating the workspace from Python Side. As an alternative, you may also try some utility functions here for C++ allocation" (https://github.com/sgl-project/sglang/pull/21314#discussion_r2986475778)
- `2026-03-25T13:13:09Z` `inline` by `b8zhong` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`:91; signals: fp4, gemm, kernel, nvfp4; excerpt: "I see. Could I use ffi::empty? Because, otherwise we need to bring the workspace size up to Python level (it could be useful when ..." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2988137976)
- `2026-03-27T05:32:27Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`:57; signals: fp4, gemm, kernel, nvfp4; excerpt: "1. Why do we need thread local here? Can we use static? 2. Can we try to unify the initialization into 1 function? A ..." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2999073985)
- `2026-03-27T05:46:01Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`:57; signals: fp4, gemm, kernel, nvfp4; excerpt: "3. This workspace doesn't seems to be safe under multi-stream. 4. Can we allocate the workspace on demand (since it's empty tensor, we just ..." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2999108234)
- `2026-03-25T03:58:25Z` `inline` by `b8zhong` `sgl-kernel/benchmark/bench_fp4_gemm.py`:361; signals: benchmark, fp4, gemm, kernel; excerpt: "Good point. I fix it w: writer.writerow(["provider", "m", "n", "k", "time ms", "bandwidth gbs"])" (https://github.com/sgl-project/sglang/pull/21314#discussion_r2985589580)
- `2026-03-25T21:13:14Z` `inline` by `b8zhong` `python/sglang/jit_kernel/csrc/gemm/nvfp4/nvfp4_scaled_mm_common.cuh`:91; signals: fp4, gemm, kernel, nvfp4; excerpt: "@HydraQYH @DarkSharpness I do it in Let me know if it looks alright." (https://github.com/sgl-project/sglang/pull/21314#discussion_r2991081610)
- `2026-03-25T02:14:34Z` `issue` by `b8zhong`; signals: hang; excerpt: "@HydraQYH @BBuf, By the way, I just update the PR with the E2E acc, and the profiles to confirm the change." (https://github.com/sgl-project/sglang/pull/21314#issuecomment-4122657682)
- `2026-03-25T21:24:49Z` `issue` by `b8zhong`; signals: kernel; excerpt: "Latest UT result locally. I'm not sure if there is a 5090 machine running for jit-kernel tests (I don't think so)." (https://github.com/sgl-project/sglang/pull/21314#issuecomment-4129880151)
