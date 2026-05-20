# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9811](https://github.com/NVIDIA/TensorRT-LLM/pull/9811)
- Source page: `sources/prs/tensorrt-llm/PR-9811.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9811`
- Generated at: `2026-05-20T15:19:26.773184+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-08T23:03:35Z`
- Merged: `2025-12-13T03:37:57Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: coderabbitai, farazkh80, mikeiovine, pamelap-nvidia, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-08T23:11:27Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3554475953)
- `2025-12-11T18:46:45Z` `APPROVED` by `mikeiovine` - Accept to unblock (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3568822573)
- `2025-12-11T19:13:01Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3568932228)
- `2025-12-11T19:13:10Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3568932670)
- `2025-12-11T19:13:18Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3568933055)
- `2025-12-11T22:02:13Z` `APPROVED` by `pamelap-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3569486805)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/thop/cublasScaledMMLut.h`: 3 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_llama.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/thop/cublasScaledMM.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-08T23:11:27Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, bf16, blackwell, block, compile, correctness, cuda, cute; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#pullrequestreview-3554475953)
- `2025-12-08T23:11:23Z` `issue` by `coderabbitai`; signals: attention, bf16, cuda, fp8, hang, perf, performance, tensorrt; excerpt: "📝 Walkthrough Walkthrough The changes introduce a centralized cuBLAS algorithm lookup table (LUT) to replace inline hard-coded configurations and propagate a use custom cublas ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#issuecomment-3629416263)
- `2025-12-08T23:11:27Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/cublasScaledMMLut.h`:39; signals: cute, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 182 --- Align hash functor key type with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2600451316)
- `2025-12-11T18:42:57Z` `inline` by `mikeiovine` `tensorrt_llm/_torch/models/modeling_llama.py`:898; signals: tensorrt; excerpt: "Use get sm version():" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2611678673)
- `2025-12-11T18:45:00Z` `inline` by `mikeiovine` `cpp/tensorrt_llm/thop/cublasScaledMMLut.h`:41; signals: tensorrt; excerpt: "Looks like these can be const" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2611684775)
- `2025-12-11T18:46:08Z` `inline` by `mikeiovine` `cpp/tensorrt_llm/thop/cublasScaledMM.cpp`:72; signals: tensorrt; excerpt: "Existing issue + probably doesn't matter much but this is going to cause a copy" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2611688386)
- `2025-12-11T19:13:01Z` `inline` by `farazkh80` `tensorrt_llm/_torch/models/modeling_llama.py`:898; signals: tensorrt; excerpt: "done" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2611767647)
- `2025-12-11T19:13:10Z` `inline` by `farazkh80` `cpp/tensorrt_llm/thop/cublasScaledMM.cpp`:72; signals: tensorrt; excerpt: "good call, I switched to pointers" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2611768127)
- `2025-12-11T19:13:18Z` `inline` by `farazkh80` `cpp/tensorrt_llm/thop/cublasScaledMMLut.h`:41; signals: tensorrt; excerpt: "added const" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#discussion_r2611768429)
- `2025-12-08T23:49:36Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 27373]( [ run ] completed with state FAILURE. Commit: a962717 [/LLM/main/L0 MergeRequest PR pipeline 20915]( completed with status: 'FAILURE'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#issuecomment-3629531797)
- `2025-12-09T20:15:52Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 27534]( [ run ] completed with state SUCCESS. Commit: 4e76ba9 [/LLM/main/L0 MergeRequest PR pipeline 21013]( completed with status: 'FAILURE'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#issuecomment-3634090205)
- `2025-12-11T00:07:35Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 27749]( [ run ] completed with state SUCCESS. Commit: 0e261d9 [/LLM/main/L0 MergeRequest PR pipeline 21176]( completed with status: 'FAILURE'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9811#issuecomment-3639447826)
