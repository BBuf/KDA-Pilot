# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14306](https://github.com/NVIDIA/TensorRT-LLM/pull/14306)
- Source page: `sources/prs/tensorrt-llm/PR-14306.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14306`
- Generated at: `2026-05-20T15:19:11.413911+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-19T12:19:52Z`
- Merged: `2026-05-20T08:14:32Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: QiJune, coderabbitai, nv-guomingz, syuoni, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-19T12:28:26Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (3) tests/unittest/ torch/modules/test fused shared expert.py (2) 144-202: ⚡ Quick win Cover the non-contiguous input ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#pullrequestreview-4318848109)
- `2026-05-20T08:07:15Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#pullrequestreview-4326419938)
- `2026-05-20T08:14:29Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#pullrequestreview-4326477004)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-05-19T12:28:26Z` `review` `COMMENTED` by `coderabbitai`; signals: correctness, hang, kernel, latency, perf, performance, regression, tensorrt; excerpt: "🧹 Nitpick comments (3) tests/unittest/ torch/modules/test fused shared expert.py (2) 144-202: ⚡ Quick win Cover the non-contiguous input copy path too. fused sigmoid gate ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#pullrequestreview-4318848109)
- `2026-05-19T12:21:54Z` `issue` by `coderabbitai`; signals: bf16, block, correctness, dtype, hang, kernel, memory, moe; excerpt: "📝 Walkthrough Walkthrough This PR introduces a Triton-based fused kernel that combines sigmoid gating and shared-expert output merging into a single operation, integrates it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#issuecomment-4487658934)
- `2026-05-19T20:14:29Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49186]( [ run ] completed with state SUCCESS. Commit: c83f0c4 [/LLM/main/L0 MergeRequest PR pipeline 38863]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#issuecomment-4491652669)
- `2026-05-20T03:35:34Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49275]( [ run ] completed with state FAILURE. Commit: c83f0c4 [/LLM/main/L0 MergeRequest PR pipeline 38940]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#issuecomment-4494256884)
- `2026-05-20T07:52:32Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 49337]( [ run ] completed with state SUCCESS. Commit: c83f0c4 [/LLM/main/L0 MergeRequest PR pipeline 38994]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14306#issuecomment-4495910480)
