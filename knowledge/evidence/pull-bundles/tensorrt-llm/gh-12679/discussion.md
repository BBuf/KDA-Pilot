# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12679](https://github.com/NVIDIA/TensorRT-LLM/pull/12679)
- Source page: `sources/prs/tensorrt-llm/PR-12679.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12679`
- Generated at: `2026-05-20T15:18:15.666081+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T03:20:11Z`
- Merged: `2026-04-02T14:45:36Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 5 (approved=4, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: PerkzZheng, QiJune, coderabbitai, tensorrt-cicd, yunruis, yuxianq, zhenhuaw-me
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T03:34:49Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#pullrequestreview-4048157643)
- `2026-04-02T06:23:27Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#pullrequestreview-4048614163)
- `2026-04-02T08:35:05Z` `APPROVED` by `zhenhuaw-me` (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#pullrequestreview-4049181451)
- `2026-04-02T09:03:53Z` `APPROVED` by `QiJune` (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#pullrequestreview-4049331442)
- `2026-04-02T14:43:41Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#pullrequestreview-4051162856)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-02T03:34:49Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, b200, cache, hang, kernel, nan, perf, sm100; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#pullrequestreview-4048157643)
- `2026-04-02T03:34:45Z` `issue` by `coderabbitai`; signals: attention, b200, block, cuda, dtype, hang, kernel, nan; excerpt: "📝 Walkthrough Walkthrough Comprehensive removal of SageAttention (per-block quantized attention) support from TensorRT-LLM, including deletion of SageQuant kernels, simplification of FMHA kernel metadata/loading logic, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#issuecomment-4174406183)
- `2026-04-02T03:34:48Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:2; signals: benchmark, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Update the copyright year range. This header was modified in 2026, but the copyright line still ends at 2025. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#discussion_r3025703134)
- `2026-04-02T03:34:48Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`:1; signals: attention, benchmark, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Update the SPDX copyright year range. This file is modified in 2026, but the header still ends at 2025. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#discussion_r3025703138)
- `2026-04-02T03:34:48Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`:255; signals: attention, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard the unequal-length cross-attention path. This fused fallback only works when seq len kv == seq len. When they ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#discussion_r3025703143)
- `2026-04-02T12:18:47Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 41403]( [ run ] completed with state SUCCESS. Commit: a54b0a2 [/LLM/main/L0 MergeRequest PR pipeline 32338]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#issuecomment-4177433828)
- `2026-04-02T09:30:30Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 41400]( [ kill ] completed with state SUCCESS. Commit: a54b0a2 Successfully killed previous jobs for commit a54b0a2 [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/12679#issuecomment-4175928169)
