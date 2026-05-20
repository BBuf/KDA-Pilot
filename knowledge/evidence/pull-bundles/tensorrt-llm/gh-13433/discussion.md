# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13433](https://github.com/NVIDIA/TensorRT-LLM/pull/13433)
- Source page: `sources/prs/tensorrt-llm/PR-13433.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13433`
- Generated at: `2026-05-20T15:18:42.389520+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T12:41:17Z`
- Merged: `2026-04-29T02:28:28Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: HuiGao-NV, coderabbitai, nv-guomingz, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T12:46:36Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) cpp/tensorrt llm/kernels/customMoeRoutingKernels.cu (1) 256-265: CASE(384) is unreachable dead code. nextPowerOfTwo() only returns powers of ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#pullrequestreview-4170519424)
- `2026-04-29T02:28:25Z` `APPROVED` by `HuiGao-NV` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#pullrequestreview-4193697442)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-24T12:46:33Z` `issue` by `coderabbitai`; signals: block, cuda, hang, kernel, moe, tensorrt, warp; excerpt: "📝 Walkthrough Walkthrough The PR extends MoE routing capabilities to support larger expert counts (up to 512) and higher top-k values (up to 16). ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#issuecomment-4313255598)
- `2026-04-24T12:46:36Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, kernel, moe, tensorrt; excerpt: "🧹 Nitpick comments (1) cpp/tensorrt llm/kernels/customMoeRoutingKernels.cu (1) 256-265: CASE(384) is unreachable dead code. nextPowerOfTwo() only returns powers of 2 (32, 64, 128, 256, 512, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#pullrequestreview-4170519424)
- `2026-04-24T13:33:31Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45396]( [ run ] completed with state FAILURE. Commit: 1620bcf [/LLM/main/L0 MergeRequest PR pipeline 35636]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#issuecomment-4313583093)
- `2026-04-26T22:43:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45579]( [ run ] completed with state SUCCESS. Commit: 8c509b8 [/LLM/main/L0 MergeRequest PR pipeline 35797]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#issuecomment-4323222167)
- `2026-04-27T03:12:26Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45632]( [ run ] completed with state FAILURE. Commit: bc693ed [/LLM/main/L0 MergeRequest PR pipeline 35844]( completed with status: 'ABORTED' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#issuecomment-4323895859)
- `2026-04-27T10:03:07Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45641]( [ run ] completed with state SUCCESS. Commit: bc693ed [/LLM/main/L0 MergeRequest PR pipeline 35854]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#issuecomment-4326013555)
- `2026-04-28T23:45:52Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45959]( [ run ] completed with state SUCCESS. Commit: bc693ed [/LLM/main/L0 MergeRequest PR pipeline 36113]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13433#issuecomment-4339883351)
