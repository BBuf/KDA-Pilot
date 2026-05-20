# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12929](https://github.com/NVIDIA/TensorRT-LLM/pull/12929)
- Source page: `sources/prs/tensorrt-llm/PR-12929.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12929`
- Generated at: `2026-05-20T15:18:23.649514+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-10T08:56:33Z`
- Merged: `2026-04-15T08:15:59Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: Wanli-Jiang, coderabbitai, hyukn, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-10T09:00:28Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#pullrequestreview-4088511238)
- `2026-04-13T05:46:13Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#pullrequestreview-4096605067)
- `2026-04-13T05:46:55Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#pullrequestreview-4096607000)
- `2026-04-13T06:39:47Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#pullrequestreview-4096800023)
- `2026-04-13T07:37:02Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#pullrequestreview-4097077646)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-13T05:46:55Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:360; signals: deepgemm, gemm, latency, moe, tensorrt; excerpt: "@Wanli-Jiang, understood — thank you for the clarification. Looking at prepare workspace deepgemm, it uses the exact same pattern (if self.use dp and self.comm ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#discussion_r3071071424)
- `2026-04-10T09:00:28Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, moe, tensorrt; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#pullrequestreview-4088511238)
- `2026-04-10T09:00:27Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:360; signals: benchmark, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Scope the max-based row formula to A2A only. On Line 357, the condition uses self.comm is not None, which ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#discussion_r3063223709)
- `2026-04-10T09:00:24Z` `issue` by `coderabbitai`; signals: hang, moe, tensorrt; excerpt: "📝 Walkthrough Walkthrough The calculate num chunks() function logic was modified to compute chunking row count differently when data-parallel mode is active with communication ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#issuecomment-4222388884)
- `2026-04-13T05:46:13Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:360; signals: moe, tensorrt; excerpt: "The other comm can also be right." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#discussion_r3071069537)
- `2026-04-10T23:28:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42697]( [ run ] completed with state SUCCESS. Commit: c20ceb6 [/LLM/main/L0 MergeRequest PR pipeline 33392]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#issuecomment-4227315874)
- `2026-04-13T15:57:03Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42959]( [ run ] completed with state SUCCESS. Commit: c20ceb6 [/LLM/main/L0 MergeRequest PR pipeline 33616]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#issuecomment-4237803251)
- `2026-04-14T13:21:34Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 43238]( [ run ] completed with state DISABLED Freeze main and open the PR merge only after CI is back to healthy ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#issuecomment-4244202113)
- `2026-04-15T07:56:00Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 43434]( [ skip ] completed with state SUCCESS. Commit: cf4333e Skipping testing for commit cf4333e [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/12929#issuecomment-4250240572)
