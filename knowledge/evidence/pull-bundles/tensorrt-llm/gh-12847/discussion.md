# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12847](https://github.com/NVIDIA/TensorRT-LLM/pull/12847)
- Source page: `sources/prs/tensorrt-llm/PR-12847.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12847`
- Generated at: `2026-05-20T15:18:20.246649+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T12:59:11Z`
- Merged: `2026-04-11T17:51:17Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: coderabbitai, nvchenghaoz, suyoggupta, taylor-yb-lee, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T13:04:19Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (2) tensorrt llm/ torch/auto deploy/compile/piecewise utils.py (1) 88-100: String-based function name matching is fragile but ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#pullrequestreview-4075273041)
- `2026-04-08T17:40:17Z` `APPROVED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#pullrequestreview-4077037190)
- `2026-04-08T18:33:01Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#pullrequestreview-4077369766)
- `2026-04-08T19:10:37Z` `COMMENTED` by `suyoggupta` (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#pullrequestreview-4077622119)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/compile/piecewise_utils.py`: 4 inline comment(s)
- `examples/auto_deploy/model_registry/configs/gemma4_moe.yaml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-08T13:04:19Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, block, compile, cuda, cute, gemm, hang, latency; excerpt: "🧹 Nitpick comments (2) tensorrt llm/ torch/auto deploy/compile/piecewise utils.py (1) 88-100: String-based function name matching is fragile but acceptable. The STREAM SWITCH FUNCTION NAMES ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#pullrequestreview-4075273041)
- `2026-04-08T13:04:16Z` `issue` by `coderabbitai`; signals: accuracy, compile, cuda, cudagraph, gemm, hang, moe, perf; excerpt: "📝 Walkthrough Walkthrough This pull request introduces multi-stream MOE (Mixture of Experts) support by adding a configuration entry, implementing stream-switch detection logic for partition ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#issuecomment-4206429032)
- `2026-04-08T17:37:49Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_utils.py`:355; signals: compile, hang, tensorrt; excerpt: "This seems to change the whole static module that has stream switch to dynamic one. What about just mark the subgraph / region that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#discussion_r3053114658)
- `2026-04-08T19:10:37Z` `inline` by `suyoggupta` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_utils.py`:355; signals: compile, tensorrt; excerpt: "subgraph based approach was turning out to be too fragile -- many corner cases where splitting between dynamic and static regions land up introducing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#discussion_r3053606185)
- `2026-04-08T17:39:17Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_utils.py`:366; signals: compile, tensorrt; excerpt: "%d does not format well from my local test.." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#discussion_r3053121159)
- `2026-04-08T17:40:01Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_utils.py`:368; signals: compile, tensorrt; excerpt: "consider adding an unit test for this case." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#discussion_r3053124616)
- `2026-04-08T18:33:02Z` `inline` by `taylor-yb-lee` `examples/auto_deploy/model_registry/configs/gemma4_moe.yaml`:30; signals: gemm, moe; excerpt: "nit: we can remove this" (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#discussion_r3053388347)
- `2026-04-09T04:35:00Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42408]( [ run ] completed with state SUCCESS. Commit: 0cf1def [/LLM/main/L0 MergeRequest PR pipeline 33179]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#issuecomment-4211474277)
- `2026-04-09T13:15:42Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42494]( [ run ] completed with state SUCCESS. Commit: ebc4b6a [/LLM/main/L0 MergeRequest PR pipeline 33241]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#issuecomment-4214500770)
- `2026-04-10T01:32:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42572]( [ run ] completed with state SUCCESS. Commit: af4fea0 [/LLM/main/L0 MergeRequest PR pipeline 33305]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#issuecomment-4219252792)
- `2026-04-10T09:06:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42616]( [ run ] completed with state SUCCESS. Commit: af4fea0 [/LLM/main/L0 MergeRequest PR pipeline 33336]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#issuecomment-4222422583)
- `2026-04-11T08:39:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42774]( [ run ] completed with state SUCCESS. Commit: 8c92704 [/LLM/main/L0 MergeRequest PR pipeline 33451]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12847#issuecomment-4229121661)
