# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12322](https://github.com/NVIDIA/TensorRT-LLM/pull/12322)
- Source page: `sources/prs/tensorrt-llm/PR-12322.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12322`
- Generated at: `2026-05-20T15:18:08.001319+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-18T16:22:52Z`
- Merged: `2026-03-21T05:53:27Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: QiJune, chang-l, coderabbitai, hyukn, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-18T16:32:20Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (2) tensorrt llm/ torch/attention backend/sparse/kernel.py (1) 2027-2028: Consider a larger BLOCK ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#pullrequestreview-3969224045)
- `2026-03-19T20:00:11Z` `APPROVED` by `chang-l` - Overall, LGTM with a few minor comments. (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#pullrequestreview-3977648907)
- `2026-03-20T01:49:40Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#pullrequestreview-3978902818)
- `2026-03-20T01:49:53Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#pullrequestreview-3978903151)
- `2026-03-20T16:10:07Z` `APPROVED` by `QiJune` (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#pullrequestreview-3982542673)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/attention_backend/sparse/kernel.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 2 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-18T16:32:20Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, block, cache, coalesc, fp8, hang, kernel; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (2) tensorrt llm/ torch/attention backend/sparse/kernel.py (1) 2027-2028: Consider a larger BLOCK TOKENS for better GPU utilization. BLOCK ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#pullrequestreview-3969224045)
- `2026-03-18T16:32:16Z` `issue` by `coderabbitai`; signals: accuracy, attention, cache, cuda, fp4, fp8, hang, kernel; excerpt: "📝 Walkthrough Walkthrough A new fused Triton kernel is introduced to gather K cache data efficiently, replacing multi-step PyTorch operations. The sparse attention DSA ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#issuecomment-4083910225)
- `2026-03-18T16:32:18Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:3271; signals: accuracy, benchmark, block, cuda, fp4, nvfp4; excerpt: "⚠️ Potential issue 🔴 Critical Remove duplicated test method definition (currently overwriting the earlier one). test nvfp4 multi gpus piecewise cuda graph is defined ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#discussion_r2954737526)
- `2026-03-19T19:59:12Z` `inline` by `chang-l` `tensorrt_llm/_torch/attention_backend/sparse/kernel.py`:2001; signals: attention, kernel, tensorrt, triton; excerpt: "Can we add an unit test for this triton function?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#discussion_r2962403344)
- `2026-03-20T01:49:40Z` `inline` by `hyukn` `tensorrt_llm/_torch/attention_backend/sparse/kernel.py`:2001; signals: attention, kernel, tensorrt, triton; excerpt: "Sure. I will add the test and rename the function to follow the name pattern of triton kernel" (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#discussion_r2963579848)
- `2026-03-19T19:59:41Z` `inline` by `chang-l` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1515; signals: attention, cache, tensorrt; excerpt: "Do we still need the old self. gather k cache for chunk function?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#discussion_r2962405716)
- `2026-03-20T01:49:53Z` `inline` by `hyukn` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1515; signals: attention, tensorrt; excerpt: "I shall remove it." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#discussion_r2963580242)
- `2026-03-19T20:05:19Z` `issue` by `chang-l`; signals: perf, performance; excerpt: "BTW, what are the performance implications? Could we add some data points to the PR description for record?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#issuecomment-4092984496)
- `2026-03-20T08:38:39Z` `issue` by `hyukn`; signals: perf, performance; excerpt: "BTW, what are the performance implications? Could we add some data points to the PR description for record? I have updated the perf number ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#issuecomment-4096604045)
- `2026-03-18T22:08:24Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39483]( [ run ] completed with state SUCCESS. Commit: ff401d4 [/LLM/main/L0 MergeRequest PR pipeline 30704]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#issuecomment-4085868012)
- `2026-03-19T04:28:12Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39520]( [ run ] completed with state SUCCESS. Commit: ff401d4 [/LLM/main/L0 MergeRequest PR pipeline 30741]( completed with status: 'SUCCESS' Pipeline passed with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#issuecomment-4087740333)
- `2026-03-19T10:24:29Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39557]( [ run ] completed with state SUCCESS. Commit: 6f73053 [/LLM/main/L0 MergeRequest PR pipeline 30774]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12322#issuecomment-4089132523)
