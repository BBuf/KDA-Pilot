# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14244](https://github.com/NVIDIA/TensorRT-LLM/pull/14244)
- Source page: `sources/prs/tensorrt-llm/PR-14244.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14244`
- Generated at: `2026-05-20T15:19:05.943543+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-18T07:51:34Z`
- Merged: `2026-05-20T07:00:41Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 6 (approved=4, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: bmarimuthu-nv, brb-nv, byshiue, coderabbitai, dongjiyingdjy, tensorrt-cicd, yihwang-nv, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-18T16:46:10Z` `APPROVED` by `brb-nv` - LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#pullrequestreview-4312047630)
- `2026-05-19T09:14:51Z` `APPROVED` by `yihwang-nv` - Thanks, LGTM! (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#pullrequestreview-4317510078)
- `2026-05-20T00:33:46Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#pullrequestreview-4324356142)
- `2026-05-20T01:55:21Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#pullrequestreview-4324664546)
- `2026-05-20T04:40:25Z` `APPROVED` by `byshiue` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#pullrequestreview-4325218314)
- `2026-05-20T04:55:17Z` `APPROVED` by `dongjiyingdjy` (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#pullrequestreview-4325283041)

## Inline Comment Hotspots

- `tests/unittest/auto_deploy/singlegpu/models/test_qwen3_5_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-18T07:55:58Z` `issue` by `coderabbitai`; signals: attention, fp4, hang, mla, nvfp4, tensorrt; excerpt: "📝 Walkthrough Walkthrough This PR refactors how mRoPE (multi-head RoPE) parameters flow through attention layers by moving them from a mrope config dict to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4475568660)
- `2026-05-20T01:55:21Z` `inline` by `yuxianq` `tests/unittest/auto_deploy/singlegpu/models/test_qwen3_5_moe.py`:73; signals: hang, moe; excerpt: "Sure, revert it. There is no AutoDeploy related change now." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#discussion_r3270788203)
- `2026-05-20T00:33:46Z` `inline` by `bmarimuthu-nv` `tests/unittest/auto_deploy/singlegpu/models/test_qwen3_5_moe.py`:73; signals: moe; excerpt: "This is waived in already and will be fixed in a separate PR." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#discussion_r3270543703)
- `2026-05-18T11:53:21Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48862]( [ run ] completed with state SUCCESS. Commit: 3296d60 [/LLM/main/L0 MergeRequest PR pipeline 38616]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4477386261)
- `2026-05-18T17:33:44Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48915]( [ run ] completed with state SUCCESS. Commit: 3296d60 [/LLM/main/L0 MergeRequest PR pipeline 38663]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4480211615)
- `2026-05-18T21:20:55Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48954]( [ run ] completed with state SUCCESS. Commit: 3296d60 [/LLM/main/L0 MergeRequest PR pipeline 38700]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4482326239)
- `2026-05-19T06:22:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49015]( [ run ] completed with state SUCCESS. Commit: 388b537 [/LLM/main/L0 MergeRequest PR pipeline 38753]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4484972361)
- `2026-05-19T14:19:04Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49159]( [ run ] completed with state SUCCESS. Commit: 388b537 [/LLM/main/L0 MergeRequest PR pipeline 38840]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4488687968)
- `2026-05-19T17:21:55Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49229]( [ run ] completed with state SUCCESS. Commit: 388b537 [/LLM/main/L0 MergeRequest PR pipeline 38901]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4490277674)
- `2026-05-20T04:54:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49306]( [ run ] completed with state FAILURE. Commit: 3296d60 [/LLM/main/L0 MergeRequest PR pipeline 38968]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4494639934)
- `2026-05-20T06:57:54Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49347]( [ run ] completed with state SUCCESS. Commit: 3296d60 [/LLM/main/L0 MergeRequest PR pipeline 39003]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14244#issuecomment-4495474879)
