# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13740](https://github.com/NVIDIA/TensorRT-LLM/pull/13740)
- Source page: `sources/prs/tensorrt-llm/PR-13740.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13740`
- Generated at: `2026-05-20T15:18:53.676289+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-04T22:28:02Z`
- Merged: `2026-05-14T16:59:51Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: LarryXFly, coderabbitai, tensorrt-cicd, yijingl-nvidia
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-04T22:32:47Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#pullrequestreview-4223998620)
- `2026-05-08T23:37:59Z` `COMMENTED` by `yijingl-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#pullrequestreview-4256007350)
- `2026-05-08T23:38:47Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#pullrequestreview-4256008820)
- `2026-05-14T03:24:30Z` `APPROVED` by `LarryXFly` (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#pullrequestreview-4287026975)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`: 3 inline comment(s)
- `cpp/tensorrt_llm/thop/dsv3RouterGemmOp.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-04T22:32:46Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`:292; signals: gemm, hang, kernel, latency, perf, performance, regression, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift Add perf-regression coverage for the new 6144 router-GEMM path. This PR is explicitly performance-driven, but the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#discussion_r3184916063)
- `2026-05-08T23:38:47Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`:292; signals: cute, fp8, gemm, kernel, latency, perf, regression, tensorrt; excerpt: "🧩 Analysis chain Let me verify by checking the QA perf list files directly. --- 🏁 Script executed: Length of output: 1109 --- @yijingl-nvidia, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#discussion_r3211881632)
- `2026-05-04T22:32:47Z` `review` `COMMENTED` by `coderabbitai`; signals: cuda, gemm, hang, kernel, latency, regression, tensorrt; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#pullrequestreview-4223998620)
- `2026-05-04T22:32:43Z` `issue` by `coderabbitai`; signals: bf16, cute, gemm, hang, kernel, latency, memory, nan; excerpt: "📝 Walkthrough Walkthrough This PR extends the DeepSeek V3 router GEMM operation to support an additional hidden dimension value of 6144 alongside the existing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#issuecomment-4374990349)
- `2026-05-08T23:37:59Z` `inline` by `yijingl-nvidia` `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`:292; signals: gemm, kernel, latency, perf, tensorrt; excerpt: "QA perf list already covers it." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#discussion_r3211880095)
- `2026-05-04T22:32:46Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/dsv3RouterGemmOp.cpp`:103; signals: compile, gemm, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical ⚡ Quick win Add inner-dimension validation before custom-kernel dispatch. shape ok does not verify mat b.sizes()[0] == hidden dim. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#discussion_r3184916065)
- `2026-05-04T23:56:29Z` `issue` by `yijingl-nvidia`; signals: accuracy, kernel; excerpt: "Coderabbit suggested accuracy tests on new kernel dimension range. Will work on that later" (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#issuecomment-4375454534)
- `2026-05-09T09:45:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47488]( [ run ] completed with state SUCCESS. Commit: 301fe88 [/LLM/main/L0 MergeRequest PR pipeline 37408]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#issuecomment-4412198823)
- `2026-05-10T08:28:33Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47554]( [ run ] completed with state SUCCESS. Commit: 4990d77 [/LLM/main/L0 MergeRequest PR pipeline 37467]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#issuecomment-4414837755)
- `2026-05-10T16:48:03Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47602]( [ run ] completed with state SUCCESS. Commit: 4990d77 [/LLM/main/L0 MergeRequest PR pipeline 37508]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#issuecomment-4415814317)
- `2026-05-08T23:37:27Z` `issue` by `yijingl-nvidia`; signals: regression; excerpt: "Ran GLM-5 QA tests on nsc-svg, no significant regression" (https://github.com/NVIDIA/TensorRT-LLM/pull/13740#issuecomment-4410600126)
