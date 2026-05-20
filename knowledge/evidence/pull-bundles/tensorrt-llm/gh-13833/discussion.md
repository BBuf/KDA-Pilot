# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13833](https://github.com/NVIDIA/TensorRT-LLM/pull/13833)
- Source page: `sources/prs/tensorrt-llm/PR-13833.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13833`
- Generated at: `2026-05-20T15:18:55.983216+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-07T05:57:56Z`
- Merged: `2026-05-18T04:22:21Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=0
- Human participants with discussion text: JacobHu-NV, coderabbitai, hyukn, tensorrt-cicd, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-07T06:07:58Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (2) tensorrt llm/ torch/cute dsl kernels/blackwell/moe as dense gemm/fc2.py (1) 2574-2580: ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#pullrequestreview-4241480978)
- `2026-05-08T08:30:07Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#pullrequestreview-4250777462)
- `2026-05-14T08:50:16Z` `APPROVED` by `zongfeijing` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#pullrequestreview-4288597309)
- `2026-05-15T07:10:08Z` `APPROVED` by `hyukn` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#pullrequestreview-4296125434)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-07T06:07:58Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, correctness, cute, gemm, hang, kernel, moe, overflow; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (2) tensorrt llm/ torch/cute dsl kernels/blackwell/moe as dense gemm/fc2.py (1) 2574-2580: 💤 Low value Int64 to Int32 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#pullrequestreview-4241480978)
- `2026-05-08T08:30:07Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, blackwell, cache, cute, failing, fp4, gemm, hang; excerpt: "Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#pullrequestreview-4250777462)
- `2026-05-08T08:30:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`:919; signals: alignment, blackwell, cute, gemm, kernel, moe, tensorrt, tile; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 45 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#discussion_r3207413834)
- `2026-05-08T08:30:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`:1585; signals: blackwell, cute, epilogue, gemm, kernel, moe, tensorrt, tile; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1430 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#discussion_r3207413841)
- `2026-05-08T08:30:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`:2286; signals: blackwell, cute, gemm, kernel, layout, moe, tensorrt, tile; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Missing cute.size() call for thr id.shape. Line 2267 divides by tiled mma.thr id.shape directly, but other ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#discussion_r3207413846)
- `2026-05-07T06:07:54Z` `issue` by `coderabbitai`; signals: alignment, autotune, benchmark, blackwell, block, cache, compile, cute; excerpt: "[ Summary --- --- Low-level Atomic Operations tensorrt llm/ torch/cute dsl kernels/blackwell/utils.py New vectorized atomic add fp16x8 for vectorized FP16 atomics and added cutlass.Float16 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#issuecomment-4394503591)
- `2026-05-07T06:07:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`:1891; signals: blackwell, cute, gemm, kernel, memory, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical ⚡ Quick win Critical bug: Wrong variable used in scalar atomic fallback — corrupts output. scatter j is computed ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#discussion_r3199206554)
- `2026-05-08T08:30:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:4339; signals: cute, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Fix the split-K predicate indentation. The wrapped condition at Line 4312 currently triggers flake8 E129, so ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#discussion_r3207413826)
- `2026-05-08T13:45:49Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47359]( [ run ] completed with state SUCCESS. Commit: f7b6b2e [/LLM/main/L0 MergeRequest PR pipeline 37294]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#issuecomment-4406898722)
- `2026-05-11T07:53:45Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47645]( [ run ] completed with state SUCCESS. Commit: b12b493 [/LLM/main/L0 MergeRequest PR pipeline 37550]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#issuecomment-4418590058)
- `2026-05-12T08:04:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47883]( [ run ] completed with state SUCCESS. Commit: b12b493 [/LLM/main/L0 MergeRequest PR pipeline 37736]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#issuecomment-4428519181)
- `2026-05-14T06:48:08Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48282]( [ run ] completed with state SUCCESS. Commit: 7ddc37e [/LLM/main/L0 MergeRequest PR pipeline 38094]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13833#issuecomment-4448336885)
