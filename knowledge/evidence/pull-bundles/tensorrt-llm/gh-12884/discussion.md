# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12884](https://github.com/NVIDIA/TensorRT-LLM/pull/12884)
- Source page: `sources/prs/tensorrt-llm/PR-12884.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12884`
- Generated at: `2026-05-20T15:18:23.633757+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-09T07:09:40Z`
- Merged: `2026-05-10T05:51:18Z`

## Discussion Counts

- Issue comments: 41
- Review submissions: 14 (approved=5, commented=9)
- Inline review comments: 12
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: StanleySun639, Wanli-Jiang, coderabbitai, hyukn, syuoni, tensorrt-cicd, xxi-nv, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-17T05:56:00Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4126441762)
- `2026-04-17T06:12:39Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4126518617)
- `2026-04-20T07:28:06Z` `APPROVED` by `hyukn` - Agree with @syuoni that is gated can be improved with a more general ActivationType enum arg. Overall LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4137989992)
- `2026-04-22T06:48:57Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4152588099)
- `2026-04-22T06:49:10Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4152589010)
- `2026-04-22T06:49:47Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4152591752)
- `2026-04-22T06:50:23Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4152594477)
- `2026-04-22T06:50:45Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4152596227)
- `2026-04-22T06:52:10Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4152602596)
- `2026-04-22T09:46:36Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4153674670)
- `2026-04-23T02:07:48Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4159095094)
- `2026-04-23T05:40:55Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4159943879)
- `2026-04-23T06:27:07Z` `APPROVED` by `zongfeijing` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4160146867)
- `2026-04-23T08:54:31Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4161035937)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`: 7 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 3 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-17T05:56:00Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, b200, blackwell, block, cute, epilogue, gemm, hang; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#pullrequestreview-4126441762)
- `2026-04-17T05:55:59Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:3808; signals: blackwell, block, cute, gemm, kernel, overflow, tensorrt, tiling; excerpt: "⚠️ Potential issue 🟠 Major Potential mismatch between wrapper's is gated parameter and self.is gated. The wrapper method accepts an is gated parameter and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3098173193)
- `2026-04-17T05:55:56Z` `issue` by `coderabbitai`; signals: accuracy, b200, blackwell, block, cute, epilogue, gemm, hang; excerpt: "📝 Walkthrough Walkthrough This PR generalizes a SwiGLU-specific gather-grouped GEMM kernel to support both gated (SwiGLU) and non-gated (ReLU²) activation modes. Custom ops are ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#issuecomment-4265776851)
- `2026-04-22T06:50:23Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:3808; signals: blackwell, block, cute, gemm, kernel, tensorrt, tiling; excerpt: "@Wanli-Jiang, understood — the docstring on wrapper documents the contract that activation type must match the value passed to init , and since both ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3122066490)
- `2026-04-17T06:12:36Z` `inline` by `syuoni` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:64; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "Currently, gated is hard-coded to swiglu, while non-gated is hard-coded to relu2. This is not general. Can we reuse the ? For non-supported activation ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3098235376)
- `2026-04-22T06:52:10Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:6886; signals: accuracy, b200, blackwell, cute, fp4, nvfp4; excerpt: "@Wanli-Jiang Thanks! skip pre blackwell is necessary, but it isn’t sufficient here. It still allows running on unsupported Blackwell variants (e.g., SM 120/121) and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3122074567)
- `2026-04-20T07:23:53Z` `inline` by `hyukn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:3800; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "Will this shadow the self.is gated? Maybe a little confusing." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3108910915)
- `2026-04-22T06:48:57Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:64; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "done." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3122060431)
- `2026-04-22T06:49:10Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:3800; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "solved." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3122061295)
- `2026-04-22T06:49:46Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`:3808; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "solved, no we are decide by self.activation type, so no such issue." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3122063854)
- `2026-04-17T05:55:59Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:6886; signals: accuracy, cute, fp4, nvfp4; excerpt: "⚠️ Potential issue 🟠 Major Add SM gating for the newly added CUTEDSL backend. Line 6362 adds CUTEDSL, but test nvfp4 8gpus does not ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3098173201)
- `2026-04-22T06:50:45Z` `inline` by `Wanli-Jiang` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:6886; signals: accuracy, blackwell; excerpt: "guard by skip pre blackwell." (https://github.com/NVIDIA/TensorRT-LLM/pull/12884#discussion_r3122068184)
