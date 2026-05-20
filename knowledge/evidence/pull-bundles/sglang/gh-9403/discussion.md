# PR Discussion Digest

- Source PR: [sgl-project/sglang#9403](https://github.com/sgl-project/sglang/pull/9403)
- Source page: `sources/prs/sglang/PR-9403.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9403`
- Generated at: `2026-05-20T15:31:35.104183+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-20T14:56:00Z`
- Merged: `2025-10-27T06:45:45Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: FlamingoPg, Fridge003, celsowm, kaln27, voipmonitor, zhyncs, ziyye
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-20T14:56:18Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @kaln27, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9403#pullrequestreview-3137029738)
- `2025-08-20T14:58:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for sm120 (Blackwell) architecture for FP8 GEMM kernels using CUTLASS. The ... (https://github.com/sgl-project/sglang/pull/9403#pullrequestreview-3137036843)
- `2025-08-20T15:25:13Z` `COMMENTED` by `kaln27` (https://github.com/sgl-project/sglang/pull/9403#pullrequestreview-3137143008)
- `2025-10-27T06:37:06Z` `APPROVED` by `Fridge003` - Thanks for your work (https://github.com/sgl-project/sglang/pull/9403#pullrequestreview-3381999802)
- `2025-10-27T06:45:34Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9403#pullrequestreview-3382016727)

## Inline Comment Hotspots

- `sgl-kernel/csrc/gemm/fp8_gemm_kernel.cu`: 4 inline comment(s)

## High-Signal Discussion

- `2025-08-25T01:37:13Z` `issue` by `kaln27`; signals: cutlass, deepgemm, epilogue, fp8, gemm, kernel, perf, performance; excerpt: "@voipmonitor Have you try USE VLLM CUTLASS W8A8 FP8 KERNEL=1 to test vllm fp8 kernel backend speed. Btw, when I use SGL ENABLE JIT ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3218567989)
- `2025-08-25T07:16:22Z` `issue` by `voipmonitor`; signals: b200, cutlass, deepgemm, epilogue, fp8, gemm, kernel, perf; excerpt: "@voipmonitor Have you try USE VLLM CUTLASS W8A8 FP8 KERNEL=1 to test vllm fp8 kernel backend speed. Btw, when I use SGL ENABLE JIT ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3219112723)
- `2025-08-20T15:57:46Z` `issue` by `voipmonitor`; signals: block, cutlass, fp8, gemm, kernel; excerpt: "Motivation In this PR I support cutlass fp8 gemm kernel. Issue 7482 says that some fp8 model are failed to load. Those model are ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3206981950)
- `2025-08-21T00:57:55Z` `issue` by `kaln27`; signals: benchmark, cutlass, fp8, kernel, triton; excerpt: "@voipmonitor I use single RTX 5070Ti with model Qwen2.5VL-7B-FP8-Dynamic. I use vllm benchmark serving.py script to bench the model. Result for triton kernel Result ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3208579968)
- `2025-08-20T15:25:13Z` `inline` by `kaln27` `sgl-kernel/csrc/gemm/fp8_gemm_kernel.cu`:1405; signals: fp8, gemm, kernel, sm120; excerpt: "no programmatic multicast on this arch sm120. only support cluster shape" (https://github.com/sgl-project/sglang/pull/9403#discussion_r2288532624)
- `2025-08-20T20:49:57Z` `issue` by `voipmonitor`; signals: cutlass, fp8, kernel, triton; excerpt: "@kaln27 I have tested this PR on 2x 6000 PRO python -m sglang.launch server --model /mnt/GLM-4.5-Air-FP8/ --tp 2 --host 0.0.0.0 --port 8001 --mem-fraction-static 0.95 ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3208048722)
- `2025-08-22T11:12:07Z` `issue` by `voipmonitor`; signals: cutlass, fp8, kernel, triton; excerpt: "@kaln27 I'm still getting worse results with the cutlass - do you have docker image in which I could reproduce your results so I ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3213999835)
- `2025-10-26T17:54:23Z` `issue` by `Fridge003`; signals: fp8, gemm, kernel, sm120; excerpt: "@kaln27 Can you please post the result of sgl-kernel/tests/test fp8 gemm.py on SM120?" (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3448732057)
- `2025-10-27T02:37:10Z` `issue` by `kaln27`; signals: fp8, gemm, kernel; excerpt: "sgl-kernel/tests/test fp8 gemm.py Here is the results" (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3449281326)
- `2025-08-21T02:13:44Z` `issue` by `ziyye`; signals: fp8; excerpt: "I have tested this PR for Qwen 2.5 FP8 w8a8 quantization model (quantized by llm-compressor) on 5070Ti, and it works well. Hope the community ..." (https://github.com/sgl-project/sglang/pull/9403#issuecomment-3208740386)
