# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14165](https://github.com/NVIDIA/TensorRT-LLM/pull/14165)
- Source page: `sources/prs/tensorrt-llm/PR-14165.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14165`
- Generated at: `2026-05-20T15:19:04.160141+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-15T01:41:56Z`
- Merged: `2026-05-18T20:14:37Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: cascade812, coderabbitai, hyukn, tensorrt-cicd, yuzisun
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-15T11:51:01Z` `COMMENTED` by `yuzisun` (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#pullrequestreview-4297875509)
- `2026-05-15T18:07:24Z` `COMMENTED` by `cascade812` (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#pullrequestreview-4300273959)
- `2026-05-18T12:44:01Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#pullrequestreview-4310231009)
- `2026-05-18T12:45:31Z` `APPROVED` by `hyukn` - This might also affect perf when the LRU cache grows very large. the LRU look-up may introduce extra ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#pullrequestreview-4310242794)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-05-15T01:43:55Z` `issue` by `coderabbitai`; signals: autotune, block, cache, cute, fp8, gemm, hang, memory; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : Path: .coderabbit.yaml Review profile ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#issuecomment-4456159996)
- `2026-05-18T12:44:01Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1711; signals: cache, memory, tensorrt; excerpt: "Because the overall entries of the cache can be large in some cases. So the upper bound was removed. This fix reminds me that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#discussion_r3258973095)
- `2026-05-15T18:07:24Z` `inline` by `cascade812` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1711; signals: cache, hang, tensorrt; excerpt: "@hyukn The cache was changed to unbounded in this [PR]( , is there a specific reason for doing this?" (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#discussion_r3250042005)
- `2026-05-15T11:51:01Z` `inline` by `yuzisun` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1711; signals: cache, tensorrt; excerpt: "This fixes the constraint specs which helps the same request sending over again, would it still be a problem of variable inputs with the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#discussion_r3247975157)
- `2026-05-18T12:45:31Z` `review` `APPROVED` by `hyukn`; signals: cache, perf; excerpt: "This might also affect perf when the LRU cache grows very large. the LRU look-up may introduce extra overhead." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#pullrequestreview-4310242794)
- `2026-05-15T20:24:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48605]( [ run ] completed with state FAILURE. Commit: 4a26d1e [/LLM/main/L0 MergeRequest PR pipeline 38388]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#issuecomment-4463282865)
- `2026-05-16T17:12:12Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48702]( [ run ] completed with state FAILURE. Commit: 4a26d1e [/LLM/main/L0 MergeRequest PR pipeline 38473]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#issuecomment-4467562336)
- `2026-05-18T12:11:54Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48795]( [ run ] completed with state SUCCESS. Commit: 4a26d1e [/LLM/main/L0 MergeRequest PR pipeline 38558]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#issuecomment-4477523930)
- `2026-05-18T17:17:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48936]( [ run ] completed with state SUCCESS. Commit: 4a26d1e [/LLM/main/L0 MergeRequest PR pipeline 38682]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14165#issuecomment-4480085684)
