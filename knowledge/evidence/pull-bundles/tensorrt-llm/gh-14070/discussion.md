# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14070](https://github.com/NVIDIA/TensorRT-LLM/pull/14070)
- Source page: `sources/prs/tensorrt-llm/PR-14070.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14070`
- Generated at: `2026-05-20T15:19:02.328205+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-13T03:16:05Z`
- Merged: `2026-05-15T20:15:57Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: coderabbitai, kaiyux, tensorrt-cicd, yuantailing
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-13T03:19:59Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4277974008)
- `2026-05-13T03:34:59Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4278032272)
- `2026-05-13T12:02:48Z` `COMMENTED` by `yuantailing` (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4281319270)
- `2026-05-13T12:02:50Z` `APPROVED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4281319606)
- `2026-05-13T12:02:51Z` `COMMENTED` by `yuantailing` (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4281319726)
- `2026-05-13T12:03:10Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4281322476)

## Inline Comment Hotspots

- `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-05-13T03:19:56Z` `issue` by `coderabbitai`; signals: benchmark, cache, cuda, cute, hang, memory, nan, perf; excerpt: "📝 Walkthrough Walkthrough This PR refactors NVLink support checking to cache results per device and parameterizes device ID instead of using implicit CUDA state. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#issuecomment-4436856035)
- `2026-05-13T03:19:59Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, hang, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#pullrequestreview-4277974008)
- `2026-05-13T03:19:59Z` `inline` by `coderabbitai` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:446; signals: benchmark, hang, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Do not hardcode trust remote code=False in the benchmark runner. This removes support for models/configs that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#discussion_r3231271084)
- `2026-05-13T03:34:59Z` `inline` by `kaiyux` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:445; signals: benchmark, block, tensorrt; excerpt: "Why hardcoding trust remote code to False? Wondering if this would block the models that have remote code." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#discussion_r3231317478)
- `2026-05-13T12:03:10Z` `inline` by `coderabbitai` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:446; signals: benchmark, hang, tensorrt; excerpt: "@yuantailing Thanks for the update! Acknowledged — reverting the trust remote code changes resolves the concern. --- 🧠 Learnings used --- --- --- --- ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#discussion_r3233998570)
- `2026-05-13T12:02:48Z` `inline` by `yuantailing` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:445; signals: benchmark, tensorrt; excerpt: "Reverted trust remote code related code." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#discussion_r3233995822)
- `2026-05-13T12:02:50Z` `inline` by `yuantailing` `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`:446; signals: benchmark, tensorrt; excerpt: "Reverted trust remote code related code." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#discussion_r3233996288)
- `2026-05-13T05:54:45Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48088]( [ run ] completed with state SUCCESS. Commit: 379de45 [/LLM/main/L0 MergeRequest PR pipeline 37919]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#issuecomment-4437788442)
- `2026-05-13T16:02:56Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48175]( [ run ] completed with state FAILURE. Commit: 4485466 [/LLM/main/L0 MergeRequest PR pipeline 37995]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#issuecomment-4442908623)
- `2026-05-14T10:44:45Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48225]( [ run ] completed with state SUCCESS. Commit: 4485466 [/LLM/main/L0 MergeRequest PR pipeline 38043]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#issuecomment-4449956383)
- `2026-05-15T05:31:32Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48490]( [ run ] completed with state SUCCESS. Commit: 4485466 [/LLM/main/L0 MergeRequest PR pipeline 38286]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14070#issuecomment-4457158021)
