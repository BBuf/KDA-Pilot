# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13186](https://github.com/NVIDIA/TensorRT-LLM/pull/13186)
- Source page: `sources/prs/tensorrt-llm/PR-13186.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13186`
- Generated at: `2026-05-20T15:18:34.839828+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-19T08:56:10Z`
- Merged: `2026-05-08T04:22:12Z`

## Discussion Counts

- Issue comments: 44
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Wanli-Jiang, coderabbitai, tensorrt-cicd, xxi-nv, yweng0828
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-20T02:10:57Z` `APPROVED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#pullrequestreview-4136944709)
- `2026-04-24T17:57:32Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) tests/unittest/ torch/thop/parallel/test noaux tc.py (1) 8-19: Good coverage expansion, but consider adding a case ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#pullrequestreview-4172463600)
- `2026-05-07T02:41:06Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#pullrequestreview-4240909681)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-24T17:57:32Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, kernel, moe, tensorrt, tma; excerpt: "🧹 Nitpick comments (1) tests/unittest/ torch/thop/parallel/test noaux tc.py (1) 8-19: Good coverage expansion, but consider adding a case for the new MaxNumTopGroups=8 kernel path. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#pullrequestreview-4172463600)
- `2026-04-24T17:57:29Z` `issue` by `coderabbitai`; signals: hang, kernel, memory, moe, tensorrt; excerpt: "📝 Walkthrough Walkthrough Refactors top-k sorting logic by implementing a complete sorting network, updates MoE kernel constants and dispatch predicates, adds validation guards for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4315246881)
- `2026-04-24T17:31:23Z` `issue` by `yweng0828`; signals: hang, kernel, moe, warp; excerpt: "Summary: Supported-Configuration Changes Before vs. After PR 13186 This PR broadens the range of MoE routing configurations that can use the fused deepseek v3 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4315097585)
- `2026-04-25T15:06:37Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45430]( [ run ] completed with state SUCCESS. Commit: 24dec37 [/LLM/main/L0 MergeRequest PR pipeline 35663]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4319910735)
- `2026-04-26T17:32:16Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45587]( [ run ] completed with state SUCCESS. Commit: 24dec37 [/LLM/main/L0 MergeRequest PR pipeline 35803]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4322597644)
- `2026-04-27T10:07:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45642]( [ run ] completed with state SUCCESS. Commit: db3381f [/LLM/main/L0 MergeRequest PR pipeline 35855]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4326040196)
- `2026-04-28T11:56:13Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45739]( [ run ] completed with state SUCCESS. Commit: db3381f [/LLM/main/L0 MergeRequest PR pipeline 35934]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4334977780)
- `2026-04-30T00:44:17Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46094]( [ run ] completed with state SUCCESS. Commit: 8e2b341 [/LLM/main/L0 MergeRequest PR pipeline 36237]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4348619267)
- `2026-04-30T12:33:26Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46254]( [ run ] completed with state SUCCESS. Commit: 8e2b341 [/LLM/main/L0 MergeRequest PR pipeline 36362]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4352473533)
- `2026-05-01T05:30:19Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46367]( [ run ] completed with state SUCCESS. Commit: 8e2b341 [/LLM/main/L0 MergeRequest PR pipeline 36452]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4357987417)
- `2026-05-02T06:42:21Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46499]( [ run ] completed with state FAILURE. Commit: 8dcd590 [/LLM/main/L0 MergeRequest PR pipeline 36560]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4363196760)
- `2026-05-06T11:54:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46895]( [ run ] completed with state SUCCESS. Commit: 596a67e [/LLM/main/L0 MergeRequest PR pipeline 36904]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13186#issuecomment-4387656702)
