# PR Discussion Digest

- Source PR: [vllm-project/vllm#23642](https://github.com/vllm-project/vllm/pull/23642)
- Source page: `sources/prs/vllm/PR-23642.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23642`
- Generated at: `2026-05-20T15:37:35.062979+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-26T09:31:37Z`
- Merged: `2025-10-30T17:36:57Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Isotr0py, bufferoverflow, robertgshaw2-redhat, simon-mo, tomschelsen
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-08-26T09:34:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds tuned configurations for the H200 NVL GPU by copying the existing configurations ... (https://github.com/vllm-project/vllm/pull/23642#pullrequestreview-3154807942)
- `2025-08-26T09:42:41Z` `COMMENTED` by `bufferoverflow` (https://github.com/vllm-project/vllm/pull/23642#pullrequestreview-3154838960)
- `2025-10-21T08:47:14Z` `COMMENTED` by `bufferoverflow` (https://github.com/vllm-project/vllm/pull/23642#pullrequestreview-3359480103)
- `2025-10-30T14:06:22Z` `APPROVED` by `Isotr0py` - Look reasonable to me! (https://github.com/vllm-project/vllm/pull/23642#pullrequestreview-3399831878)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/configs/E=128,N=192,device_name=NVIDIA_H200_NVL.json`: 3 inline comment(s)

## High-Signal Discussion

- `2025-10-21T08:47:14Z` `inline` by `bufferoverflow` `vllm/model_executor/layers/fused_moe/configs/E=128,N=192,device_name=NVIDIA_H200_NVL.json`:146; signals: h200, hang, moe; excerpt: "I just changes to do so." (https://github.com/vllm-project/vllm/pull/23642#discussion_r2447300521)
- `2025-08-26T09:42:41Z` `inline` by `bufferoverflow` `vllm/model_executor/layers/fused_moe/configs/E=128,N=192,device_name=NVIDIA_H200_NVL.json`:146; signals: h200, moe; excerpt: "I was thinking about the same:" (https://github.com/vllm-project/vllm/pull/23642#discussion_r2300431996)
- `2025-10-13T12:45:00Z` `issue` by `tomschelsen`; signals: h200, moe; excerpt: "In the same vein, what about the GH200 ? Running Qwen/Qwen3-Coder-30B-A3B-Instruct on an Nvidia GH200 NVL2 system, I get the following warning : So ..." (https://github.com/vllm-project/vllm/pull/23642#issuecomment-3397382717)
- `2025-10-21T08:48:09Z` `issue` by `bufferoverflow`; signals: h200, hang; excerpt: "@tomschelsen I changed to use the same config for all H200 devices" (https://github.com/vllm-project/vllm/pull/23642#issuecomment-3425472165)
