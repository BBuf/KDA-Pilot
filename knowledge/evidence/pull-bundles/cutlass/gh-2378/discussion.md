# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#2378](https://github.com/NVIDIA/cutlass/pull/2378)
- Source page: `sources/prs/cutlass/PR-2378.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-2378`
- Generated at: `2026-05-20T15:21:19.039255+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-07T09:03:28Z`
- Merged: `2025-07-31T02:12:09Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: Junkai-Wu, hwu36, kf-zhang, thakkarV, zhangxinze668
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-07T16:57:17Z` `COMMENTED` by `thakkarV` (https://github.com/NVIDIA/cutlass/pull/2378#pullrequestreview-2907583359)
- `2025-06-08T04:08:50Z` `COMMENTED` by `kf-zhang` (https://github.com/NVIDIA/cutlass/pull/2378#pullrequestreview-2908094954)
- `2025-07-31T02:12:03Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2378#pullrequestreview-3073790942)

## Inline Comment Hotspots

- `include/cute/atom/mma_traits_sm89.hpp`: 5 inline comment(s)

## High-Signal Discussion

- `2025-07-04T07:54:53Z` `issue` by `zhangxinze668`; signals: block, cuda, cutlass, epilogue, fp8, gemm, kernel, layout; excerpt: "I think I didn't express myself clearly. I wrote an FP8 GEMM kernel myself, which calls the GEMM API on SM89 to complete multiply-accumulate ..." (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034883033)
- `2025-07-04T05:40:26Z` `issue` by `zhangxinze668`; signals: block, compile, cutlass, gemm, hang; excerpt: "I added your commit on top of CUTLASS 4.0, but it fails to compile on the 4090. Here's the error message: error: 'cutlass::gemm::threadblock::GemmIdentityThreadblockSwizzle , ..." (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034605203)
- `2025-07-04T06:07:37Z` `issue` by `zhangxinze668`; signals: cuda, cute, cutlass; excerpt: "commit ID：889ff20648b06085f450e6c5d5bd22fe001ae95d build command: export TORCH CUDA ARCH LIST := 8.0;8.6;8.9;9.0;9.0a python -m build -n -w pip install --force-reinstall --no-deps ./cutlass/dist/ .whl The error ..." (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034649665)
- `2025-07-04T08:03:50Z` `issue` by `zhangxinze668`; signals: cutlass, gemm; excerpt: "I want to know if direct calls to the CUTLASS SM89 GEMM API are supported based on your commit." (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034905318)
- `2025-07-04T08:27:20Z` `issue` by `kf-zhang`; signals: cutlass, fp8; excerpt: "I don‘t think it calls my code. To see cutlass's fp8 on sm89, you can refer to [this](" (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034963856)
- `2025-06-08T04:08:50Z` `inline` by `kf-zhang` `include/cute/atom/mma_traits_sm89.hpp`:98; signals: cute; excerpt: "done" (https://github.com/NVIDIA/cutlass/pull/2378#discussion_r2134389790)
- `2025-07-04T05:54:15Z` `issue` by `kf-zhang`; signals: cute; excerpt: "The error message seems unrelated to cute. Can you provide more context, such as the build commands and the commit ID you are using?" (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034626519)
- `2025-07-04T06:42:26Z` `issue` by `kf-zhang`; signals: cutlass; excerpt: "I can't build with your command. The error message is WARNING: Requirement './cutlass/dist/ .whl' looks like a filename, but the file does not exist ..." (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3034714961)
- `2025-07-24T02:25:22Z` `issue` by `Junkai-Wu`; signals: hang; excerpt: "@kf-zhang Sorry for the late response, we will port these changes and merge this MR soon." (https://github.com/NVIDIA/cutlass/pull/2378#issuecomment-3111742181)
