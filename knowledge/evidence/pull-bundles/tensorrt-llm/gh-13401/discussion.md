# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13401](https://github.com/NVIDIA/TensorRT-LLM/pull/13401)
- Source page: `sources/prs/tensorrt-llm/PR-13401.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13401`
- Generated at: `2026-05-20T15:18:42.373755+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T01:29:15Z`
- Merged: `2026-05-19T13:19:29Z`

## Discussion Counts

- Issue comments: 175
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: coderabbitai, leslie-fang25, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T01:36:13Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#pullrequestreview-4167285448)
- `2026-05-15T07:30:51Z` `APPROVED` by `leslie-fang25` (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#pullrequestreview-4296247201)
- `2026-05-17T23:27:35Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#pullrequestreview-4306453127)

## Inline Comment Hotspots

- `tests/unittest/_torch/modules/moe/quantize_utils.py`: 3 inline comment(s)
- `tests/unittest/_torch/modules/moe/test_moe_module.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-24T01:36:12Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/moe/test_moe_module.py`:1145; signals: fp4, fp8, moe, mxfp4; excerpt: "⚠️ Potential issue 🟠 Major Move this known-bad config skip into shared filtering. This only protects test configurable moe single gpu(). generate multi gpu ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#discussion_r3134960912)
- `2026-05-15T07:29:46Z` `inline` by `leslie-fang25` `tests/unittest/_torch/modules/moe/quantize_utils.py`:1922; signals: fp4, fp8, moe, mxfp4; excerpt: "a base class MXFP4QuantizeUtil for MXFP4MXFP8QuantizeUtil and MXFP4FP8QuantizeUtil might be cleaner." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#discussion_r3246594458)
- `2026-04-24T01:36:12Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/moe/quantize_utils.py`:1755; signals: bf16, dtype, moe; excerpt: "⚠️ Potential issue 🟠 Major Force this fallback reference to bf16 instead of reusing the test dtype. The class comment says this is a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#discussion_r3134960907)
- `2026-04-24T01:36:13Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, moe; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#pullrequestreview-4167285448)
- `2026-05-17T23:27:35Z` `inline` by `xxi-nv` `tests/unittest/_torch/modules/moe/quantize_utils.py`:1922; signals: moe; excerpt: "Thanks for the suggestion. Will do it in the next PR." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#discussion_r3255659860)
- `2026-05-15T21:17:13Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48507]( [ run ] completed with state FAILURE. Commit: 393947b [/LLM/main/L0 MergeRequest PR pipeline 38302]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#issuecomment-4463719488)
- `2026-05-18T08:10:24Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48794]( [ run ] completed with state SUCCESS. Commit: 898c373 [/LLM/main/L0 MergeRequest PR pipeline 38557]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#issuecomment-4475674528)
- `2026-05-18T18:53:28Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48913]( [ run ] completed with state SUCCESS. Commit: fc0fa7b [/LLM/main/L0 MergeRequest PR pipeline 38662]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#issuecomment-4480900242)
- `2026-05-19T13:19:09Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49155]( [ run ] completed with state SUCCESS. Commit: fc0fa7b [/LLM/main/L0 MergeRequest PR pipeline 38836]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13401#issuecomment-4488143542)
