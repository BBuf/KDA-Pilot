# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9852](https://github.com/NVIDIA/TensorRT-LLM/pull/9852)
- Source page: `sources/prs/tensorrt-llm/PR-9852.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9852`
- Generated at: `2026-05-20T15:19:29.059788+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T21:32:28Z`
- Merged: `2025-12-14T02:47:24Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, jhaotingc, nvxuanyuc, symphonylyh, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-09T21:40:18Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3559858516)
- `2025-12-09T21:51:03Z` `APPROVED` by `jhaotingc` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3559888614)
- `2025-12-10T21:13:14Z` `APPROVED` by `symphonylyh` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3564504195)
- `2025-12-11T06:56:47Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3565993548)
- `2025-12-13T06:45:03Z` `COMMENTED` by `nvxuanyuc` (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3574240575)
- `2025-12-14T02:46:29Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3574697451)

## Inline Comment Hotspots

- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-09T21:40:18Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, aligned, attention, benchmark, block, cache, compile, cuda; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#pullrequestreview-3559858516)
- `2025-12-09T21:40:15Z` `issue` by `coderabbitai`; signals: accuracy, attention, correctness, fp4, hang, kernel, memory, moe; excerpt: "📝 Walkthrough Walkthrough Added rotary dim parameter support to fused QK norm RoPE kernels for partial RoPE handling. Introduced Glm4WeightLoader class to centralize GLM-4 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#issuecomment-3634403452)
- `2025-12-11T06:56:47Z` `inline` by `yuxianq` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:2911; signals: accuracy; excerpt: "Please add all new tests to test list and run them locally before merged." (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#discussion_r2609403452)
- `2025-12-13T06:45:02Z` `inline` by `nvxuanyuc` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:2911; signals: accuracy; excerpt: "Have verified all tests locally and added to qa list." (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#discussion_r2616132941)
- `2025-12-10T18:52:44Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 27740]( [ run ] completed with state SUCCESS. Commit: 3de8159 [/LLM/main/L0 MergeRequest PR pipeline 21168]( completed with status: 'SUCCESS'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#issuecomment-3638511786)
- `2025-12-13T06:22:45Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 28079]( [ run ] completed with state SUCCESS. Commit: 1c8ff8b [/LLM/main/L0 MergeRequest PR pipeline 21451]( completed with status: 'SUCCESS'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9852#issuecomment-3649035212)
