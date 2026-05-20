# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14054](https://github.com/NVIDIA/TensorRT-LLM/pull/14054)
- Source page: `sources/prs/tensorrt-llm/PR-14054.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14054`
- Generated at: `2026-05-20T15:19:02.317006+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-12T18:42:46Z`
- Merged: `2026-05-15T21:01:42Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 2 (approved=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: QiJune, coderabbitai, dongfengy, tensorrt-cicd, xinhe-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-14T05:05:36Z` `APPROVED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#pullrequestreview-4287401941)
- `2026-05-14T23:23:33Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#pullrequestreview-4294162161)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-05-12T18:45:16Z` `issue` by `coderabbitai`; signals: accuracy, cute, fp4, h200, hang, layout, memory, moe; excerpt: "📝 Walkthrough Walkthrough This PR refactors device capability detection for MXFP4 swizzling by introducing a reusable is swizzling supported() function that detects H20-family GPU ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4433677155)
- `2026-05-12T23:13:44Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48012]( [ run ] completed with state SUCCESS. Commit: d90971c [/LLM/main/L0 MergeRequest PR pipeline 37847]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4435592178)
- `2026-05-13T17:49:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48208]( [ run ] completed with state SUCCESS. Commit: cf715ae [/LLM/main/L0 MergeRequest PR pipeline 38026]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4443809739)
- `2026-05-14T04:34:24Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48250]( [ run ] completed with state SUCCESS. Commit: c012f23 [/LLM/main/L0 MergeRequest PR pipeline 38066]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4447557667)
- `2026-05-14T12:42:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48313]( [ run ] completed with state SUCCESS. Commit: 4e8fc41 [/LLM/main/L0 MergeRequest PR pipeline 38122]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4450755247)
- `2026-05-14T17:27:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48402]( [ run ] completed with state SUCCESS. Commit: 8c4bbb4 [/LLM/main/L0 MergeRequest PR pipeline 38205]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4453087585)
- `2026-05-14T23:54:06Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48455]( [ run ] completed with state SUCCESS. Commit: 57825e9 [/LLM/main/L0 MergeRequest PR pipeline 38251]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4455665262)
- `2026-05-15T20:45:38Z` `issue` by `dongfengy`; signals: accuracy; excerpt: "NVIDIA H20 ============================================================= slowest durations ============================================================= 2445.12s call accuracy/test llm api pytorch.py::TestGPTOSS::test eagle3 vswa reuse 4gpus[one model] 0.92s setup accuracy/test llm api pytorch.py::TestGPTOSS::test eagle3 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4463472934)
- `2026-05-15T20:49:40Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48638]( [ reuse-pipeline ] triggered by Bot. Commit: 0e0c1ca [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/14054#issuecomment-4463498675)
