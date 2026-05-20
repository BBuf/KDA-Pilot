# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9087](https://github.com/NVIDIA/TensorRT-LLM/pull/9087)
- Source page: `sources/prs/tensorrt-llm/PR-9087.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9087`
- Generated at: `2026-05-20T15:19:19.696885+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-12T07:28:54Z`
- Merged: `2025-11-14T00:37:21Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: coderabbitai, dongxuy04, hyukn, nekorobov, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-12T07:52:09Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 📜 Review details Configuration used : Path: .coderabbit.yaml Review profile : CHILL Plan : ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#pullrequestreview-3452087037)
- `2025-11-12T10:46:42Z` `APPROVED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#pullrequestreview-3452818915)
- `2025-11-13T02:33:18Z` `APPROVED` by `hyukn` - LGTM. But notice that these shapes are exactly stored in the profiling cache. And when inference happens, these ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#pullrequestreview-3456831295)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/trtllm_gen_custom_ops.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-12T07:52:09Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, block, cute, dtype, fp4, fp8, hang, kernel; excerpt: "Actionable comments posted: 2 📜 Review details Configuration used : Path: .coderabbit.yaml Review profile : CHILL Plan : Pro 📥 Commits Reviewing files that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#pullrequestreview-3452087037)
- `2025-11-12T07:52:05Z` `issue` by `coderabbitai`; signals: alignment, attention, autotune, block, cute, fp4, hang, kernel; excerpt: "📝 Walkthrough Walkthrough Routing constraint validation in the DeepSeek kernel is deferred to conditional execution paths rather than unconditional checks. A new helper function ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3520513985)
- `2025-11-12T07:52:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/trtllm_gen_custom_ops.py`:770; signals: autotune, benchmark, block, fp4, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Potential issue: Aliasing and in-place modification of tuner inputs. Line 747 creates an alias (input tensors = input tensors ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#discussion_r2517277364)
- `2025-11-13T02:33:18Z` `review` `APPROVED` by `hyukn`; signals: cache, perf; excerpt: "LGTM. But notice that these shapes are exactly stored in the profiling cache. And when inference happens, these are the ones we expect to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#pullrequestreview-3456831295)
- `2025-11-13T06:22:18Z` `issue` by `dongxuy04`; signals: cache, perf; excerpt: "LGTM. But notice that these shapes are exactly stored in the profiling cache. And when inference happens, these are the ones we expect to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3525706725)
- `2025-11-12T07:52:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/trtllm_gen_custom_ops.py`:1874; signals: tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Same aliasing issue: in-place modification of tuner inputs. Lines 1820-1824 have the same problematic pattern. Apply the same fix ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#discussion_r2517277374)
- `2025-11-12T11:34:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 24274]( [ run ] completed with state SUCCESS. Commit: efee075 [/LLM/main/L0 MergeRequest PR pipeline 18311]( completed with status: 'FAILURE'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3521484046)
- `2025-11-12T14:10:52Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 24299]( [ run ] completed with state SUCCESS. Commit: efee075 [/LLM/main/L0 MergeRequest PR pipeline 18331]( completed with status: 'SUCCESS'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3522139899)
- `2025-11-13T09:54:31Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 24403]( [ run ] completed with state SUCCESS. Commit: 7c6ffc0 [/LLM/main/L0 MergeRequest PR pipeline 18412]( completed with status: 'FAILURE'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3526868365)
- `2025-11-13T17:26:06Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 24466]( [ run ] completed with state SUCCESS. Commit: 008c6c4 [/LLM/main/L0 MergeRequest PR pipeline 18461]( completed with status: 'SUCCESS' Pipeline passed with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3528910085)
- `2025-11-12T07:48:26Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 24271]( [ kill ] completed with state SUCCESS. Commit: efee075 Successfully killed previous jobs for commit efee075" (https://github.com/NVIDIA/TensorRT-LLM/pull/9087#issuecomment-3520500100)
