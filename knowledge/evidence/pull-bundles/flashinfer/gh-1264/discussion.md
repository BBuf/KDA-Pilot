# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1264](https://github.com/flashinfer-ai/flashinfer/pull/1264)
- Source page: `sources/prs/flashinfer/PR-1264.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1264`
- Generated at: `2026-05-20T15:22:05.041706+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-15T19:53:48Z`
- Merged: `2025-07-16T09:41:25Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 21 (approved=1, commented=20)
- Inline review comments: 23
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=9
- Human participants with discussion text: Anerudhan, ttyio, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-15T19:54:09Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ttyio, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022090262)
- `2025-07-15T19:56:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces cuDNN-backed FP8 GEMM functionality with new tests. My feedback focuses on improving ... (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022097940)
- `2025-07-15T20:12:01Z` `COMMENTED` by `yzh119` - Better to create an benchmark script like cc @elfiegg in case you are working on something related. (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022127830)
- `2025-07-15T20:38:48Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022235398)
- `2025-07-15T20:47:16Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022258173)
- `2025-07-15T20:59:26Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022297301)
- `2025-07-15T21:00:58Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022303621)
- `2025-07-15T21:15:30Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022343100)
- `2025-07-15T21:16:10Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022345741)
- `2025-07-15T21:17:30Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022352357)
- `2025-07-15T21:23:42Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022371975)
- `2025-07-15T22:31:52Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022532869)
- `2025-07-15T22:34:46Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022537237)
- `2025-07-15T23:22:10Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022599906)
- `2025-07-15T23:23:25Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022601372)
- `2025-07-15T23:29:39Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022610453)
- `2025-07-15T23:35:56Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022620515)
- `2025-07-15T23:35:58Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022621985)
- `2025-07-16T00:16:12Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022677486)
- `2025-07-16T00:34:12Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3022705845)
- `2025-07-16T07:02:05Z` `APPROVED` by `yzh119` - LGTM, thank you for bringing cudnn gemm! (https://github.com/flashinfer-ai/flashinfer/pull/1264#pullrequestreview-3023457986)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 17 inline comment(s)
- `tests/test_fp8_gemm.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-07-15T20:47:15Z` `inline` by `ttyio` `flashinfer/gemm.py`:1390; signals: bf16, block, dtype, flashinfer, fp8, gemm; excerpt: "Thank you for comment. In this PR I added 2 apis: gemm f8f8 f32 bf16 and gemm f8f8 f32 fp16. And you prefer to ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208637208)
- `2025-07-15T23:34:37Z` `inline` by `yzh119` `flashinfer/gemm.py`:747; signals: dtype, flashinfer, gemm, kernel; excerpt: "here the f32 means the compute dtype, not output, so it might be confusing, we can either indicate it's compute dtype, or safely ignore ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208897840)
- `2025-07-15T20:08:48Z` `inline` by `yzh119` `flashinfer/gemm.py`:1390; signals: dtype, flashinfer, gemm; excerpt: "Please also add an out dtype argument, in case out is not provided, we create temporary output buffer with out dtype. out dtype should ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208554681)
- `2025-07-15T21:23:42Z` `inline` by `ttyio` `flashinfer/gemm.py`:1390; signals: flashinfer, gemm, regression; excerpt: "How do we decide which backend to use? can we add a new argument backend here? and maybe default to cublaslt to avoid regression." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208717128)
- `2025-07-15T22:34:46Z` `inline` by `ttyio` `flashinfer/gemm.py`:1390; signals: flashinfer, fp8, gemm; excerpt: "In the latest commit, now we merge into single bmm fp8 and add a new backend argument, please help to check if this align ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208838413)
- `2025-07-15T23:29:39Z` `inline` by `yzh119` `flashinfer/gemm.py`:29; signals: cache, flashinfer, gemm; excerpt: "User might spawm multiple process (each process work on a different GPU) after import this module. So I would encourage creating a get cudnn ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208892317)
- `2025-07-15T21:17:30Z` `inline` by `yzh119` `flashinfer/gemm.py`:1390; signals: flashinfer, fp8, gemm; excerpt: "btw there is an early api: that calls into cublas bmm fp8, is it possible to unify them?" (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208702395)
- `2025-07-15T21:00:58Z` `inline` by `ttyio` `tests/test_fp8_gemm.py`:42; signals: fp8, gemm; excerpt: "checked cudnn has all the needed FP8 E and M combination ('FP8 E4M3', 'FP8 E5M2', 'FP8 E8M0'), this comment is generated in cursor when ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208669402)
- `2025-07-15T21:15:30Z` `inline` by `yzh119` `flashinfer/gemm.py`:1267; signals: flashinfer, gemm; excerpt: "We can specify them as package level dependencies: Currently the only bottleneck is the aarch64 wheels availability." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208695806)
- `2025-07-15T23:35:58Z` `inline` by `yzh119` `flashinfer/gemm.py`:1390; signals: flashinfer, gemm; excerpt: "I'm not pretty sure if their semantics are equivalent as the cublas API is batched matmul. Can you double check?" (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208898998)
- `2025-07-16T00:16:12Z` `inline` by `ttyio` `flashinfer/gemm.py`:1390; signals: flashinfer, gemm; excerpt: "I checked the spec for , then a batched matrix multiply is returned. for cudnn, batch gemm and gemm are supported is single API ..." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208938517)
- `2025-07-15T20:07:12Z` `inline` by `yzh119` `tests/test_fp8_gemm.py`:26; signals: fp8, gemm; excerpt: "Please add more problem shapes here." (https://github.com/flashinfer-ai/flashinfer/pull/1264#discussion_r2208551548)
