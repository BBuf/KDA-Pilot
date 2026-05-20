# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10429](https://github.com/NVIDIA/TensorRT-LLM/pull/10429)
- Source page: `sources/prs/tensorrt-llm/PR-10429.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10429`
- Generated at: `2026-05-20T15:17:37.026986+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-06T02:40:53Z`
- Merged: `2026-01-07T01:31:50Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 11 (approved=3, commented=8)
- Inline review comments: 10
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=2
- Human participants with discussion text: coderabbitai, hyukn, liyuhannnnn, syuoni, tensorrt-cicd, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-06T02:51:29Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 Fix all issues with AI Agents 🤖 [!CAUTION] Some comments are outside the diff ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3629139335)
- `2026-01-06T05:37:43Z` `COMMENTED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3629452255)
- `2026-01-06T05:39:02Z` `COMMENTED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3629454290)
- `2026-01-06T05:42:04Z` `APPROVED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3629459767)
- `2026-01-06T11:29:38Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3630553779)
- `2026-01-06T12:55:44Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3630799672)
- `2026-01-06T14:16:23Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3631064134)
- `2026-01-06T14:16:41Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3631065292)
- `2026-01-06T14:22:21Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3631089933)
- `2026-01-06T14:22:31Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3631090669)
- `2026-01-07T01:30:05Z` `APPROVED` by `syuoni` - LGTM, thanks (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3633050140)

## Inline Comment Hotspots

- `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-06T02:51:29Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, benchmark, blackwell, block, cache, compile, cute, dtype; excerpt: "Actionable comments posted: 2 Fix all issues with AI Agents 🤖 [!CAUTION] Some comments are outside the diff and can’t be posted inline due ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#pullrequestreview-3629139335)
- `2026-01-06T02:51:25Z` `issue` by `coderabbitai`; signals: benchmark, blackwell, block, cache, cuda, cute, cutlass, dtype; excerpt: "📝 Walkthrough Walkthrough Introduce a raster along m parameter to CuteDSL-based NVFP4 grouped GEMM tactics and kernel scheduling. Tactics expand to 3-tuples including a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#issuecomment-3712903232)
- `2026-01-06T02:51:28Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:293; signals: blackwell, block, cute, gemm, kernel, tensorrt, tile; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 11647 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2663405239)
- `2026-01-06T02:51:28Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:559; signals: block, cute, gemm, kernel, nan, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 164 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2663405242)
- `2026-01-06T05:39:01Z` `inline` by `liyuhannnnn` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:1175; signals: aligned, block, cute, gemm, kernel; excerpt: "Let's remove the m aligned knob, like what we do here:" (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2663675426)
- `2026-01-06T05:37:43Z` `inline` by `liyuhannnnn` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:28; signals: block, cute, gemm, kernel; excerpt: "Let's give some example cmd like what we do here:" (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2663673451)
- `2026-01-06T14:22:21Z` `inline` by `zongfeijing` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:1175; signals: block, cute, gemm, kernel; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2665092827)
- `2026-01-06T14:22:31Z` `inline` by `zongfeijing` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:28; signals: block, cute, gemm, kernel; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2665093554)
- `2026-01-06T11:25:21Z` `inline` by `syuoni` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2024; signals: cache, cute, tensorrt; excerpt: "raster along m should be added to cache key" (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2664609779)
- `2026-01-06T11:29:10Z` `inline` by `syuoni` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1868; signals: cute, tensorrt; excerpt: "Are we seeing any case where raster along m=True is better than raster along m=False? If not, I think we can keep raster along ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2664619510)
- `2026-01-06T14:16:23Z` `inline` by `zongfeijing` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1868; signals: cute, tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2665072088)
- `2026-01-06T14:16:41Z` `inline` by `zongfeijing` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2024; signals: cute, tensorrt; excerpt: "Thanks for your catch." (https://github.com/NVIDIA/TensorRT-LLM/pull/10429#discussion_r2665072967)
