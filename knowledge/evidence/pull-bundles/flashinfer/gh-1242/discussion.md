# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1242](https://github.com/flashinfer-ai/flashinfer/pull/1242)
- Source page: `sources/prs/flashinfer/PR-1242.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1242`
- Generated at: `2026-05-20T15:22:00.316941+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-11T03:28:32Z`
- Merged: `2025-07-16T17:50:19Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 7
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=4, outdated=0
- Human participants with discussion text: nvpohanh, weireweire, wenscarl, yyihuang, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-07-11T03:28:54Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @weireweire, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1242#pullrequestreview-3008360212)
- `2025-07-11T03:30:34Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for FP8 data types to the TRT-LLM generation kernel. The changes ... (https://github.com/flashinfer-ai/flashinfer/pull/1242#pullrequestreview-3008362115)
- `2025-07-11T05:31:48Z` `COMMENTED` by `yzh119` - Hi @weireweire , for fp8 input, we should add two operator inputs: 1. qk scale (will be passed ... (https://github.com/flashinfer-ai/flashinfer/pull/1242#pullrequestreview-3008651389)
- `2025-07-16T11:51:14Z` `APPROVED` by `yzh119` - Thanks for the great work! @weireweire @nvpohanh merged with 1258 (cc @yyihuang ) and all unittest passed on ... (https://github.com/flashinfer-ai/flashinfer/pull/1242#pullrequestreview-3024548558)

## Inline Comment Hotspots

- `csrc/trtllm_fmha_runner.cu`: 3 inline comment(s)
- `tests/test_trtllm_gen_decode.py`: 3 inline comment(s)
- `csrc/trtllm_fmha_kernel_launcher.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-11T05:31:48Z` `review` `COMMENTED` by `yzh119`; signals: attention, dtype, fp4, fp8, kernel, tma; excerpt: "Hi @weireweire , for fp8 input, we should add two operator inputs: 1. qk scale (will be passed to runner params as scaleSoftmaxLog2 2. ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#pullrequestreview-3008651389)
- `2025-07-14T02:23:26Z` `issue` by `nvpohanh`; signals: bf16, fp8, hang, kernel, tma; excerpt: "IMO, this is just a design choice: whether we should let users calculate the fused scaling factors , or whether we should let users ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3067570301)
- `2025-07-14T04:00:00Z` `issue` by `wenscarl`; signals: fp8, kernel, memory; excerpt: "@weireweire since we re-enabled a feature at generating kernels to load scaling factors from device memory, the scales relevant to fp8 couldn't be set ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3067756857)
- `2025-07-14T06:32:14Z` `issue` by `weireweire`; signals: block, fp4, memory; excerpt: "As per offline discussion with @yzh119 @nvpohanh , we will use these scale on host memory: The reason is BMM1 scale have some internal ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3068010305)
- `2025-07-11T07:20:01Z` `issue` by `weireweire`; signals: fp4, fp8; excerpt: "Thanks @yzh119 , I assume we don't need to keep API compatibility, and could we rename "scale" to "q scale” and reorder to make ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3060964718)
- `2025-07-11T07:39:12Z` `issue` by `yzh119`; signals: cuda, cudagraph; excerpt: "These 5 arguments seem redundant: we either keep q scale/k scale/v scale, or qk scale/o scale, (in the first case, o scale=v scale and ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3061052225)
- `2025-07-11T09:04:20Z` `issue` by `weireweire`; signals: kernel, tma; excerpt: "since softmax output scale is not a param, don't we have to provide the v scale so the kernel can calculate softmax output scale ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3061357477)
- `2025-07-12T01:16:19Z` `issue` by `yzh119`; signals: flashinfer, kernel; excerpt: "Hi @weireweire the trtllm-gen kernel accepts qk scale and o scale directly so I suppose it's better to expose these two as part of ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3064463140)
- `2025-07-11T08:11:53Z` `issue` by `nvpohanh`; signals: tma; excerpt: "I agree with Zihao that we only need qk scale and o scale, but I don't think o scale = v scale is correct. ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3061163688)
- `2025-07-11T08:19:18Z` `issue` by `weireweire`; signals: tma; excerpt: "I thought qk scale means the scale after softmax, but seems that scale is not a param. use qk scale as q scale k ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3061188237)
- `2025-07-16T05:42:41Z` `issue` by `weireweire`; signals: mla; excerpt: "@yyihuang I reverted some unused comment and scale param in mha files added in [this PR]( as I saw you said you will use ..." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3076864743)
- `2025-07-16T05:52:08Z` `issue` by `weireweire`; signals: kernel; excerpt: "@yzh119 the kernels is available in public server now, and this PR is ready to merge, please help to review and merge, thanks." (https://github.com/flashinfer-ai/flashinfer/pull/1242#issuecomment-3076906914)
