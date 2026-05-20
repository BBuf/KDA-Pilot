# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13975](https://github.com/NVIDIA/TensorRT-LLM/pull/13975)
- Source page: `sources/prs/tensorrt-llm/PR-13975.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13975`
- Generated at: `2026-05-20T15:19:00.102724+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T07:23:23Z`
- Merged: `2026-05-18T07:22:23Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: lfr-0531, liji-nv, mingyangHao, qiaoxj07, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-12T08:58:44Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#pullrequestreview-4270744729)
- `2026-05-14T05:38:43Z` `COMMENTED` by `mingyangHao` (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#pullrequestreview-4287559169)
- `2026-05-18T07:22:13Z` `APPROVED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#pullrequestreview-4308037059)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/attention.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-12T08:58:40Z` `inline` by `liji-nv` `tensorrt_llm/_torch/modules/attention.py`:1672; signals: attention, cuda, tensorrt; excerpt: "Dispatching according to q.is cuda may have issue for dynamo(Although currently the whole dsv 4 op is under a custom op and cannot be ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#discussion_r3225059910)
- `2026-05-14T05:38:42Z` `inline` by `mingyangHao` `tensorrt_llm/_torch/modules/attention.py`:1672; signals: attention, kernel, tensorrt; excerpt: "Fixed -- only new norm kernel is enabled and removed all those branches." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#discussion_r3239317220)
- `2026-05-11T11:23:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47698]( [ run ] completed with state SUCCESS. Commit: 2b6494d [/LLM/main/L0 MergeRequest PR pipeline 37594]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4420222373)
- `2026-05-11T17:53:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47771]( [ run ] completed with state SUCCESS. Commit: 2b6494d [/LLM/main/L0 MergeRequest PR pipeline 37663]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4423356191)
- `2026-05-14T19:58:46Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48363]( [ run ] completed with state SUCCESS. Commit: a53999f [/LLM/main/L0 MergeRequest PR pipeline 38169]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4454256321)
- `2026-05-15T08:11:58Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48508]( [ run ] completed with state SUCCESS. Commit: 7099307 [/LLM/main/L0 MergeRequest PR pipeline 38303]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4458141345)
- `2026-05-15T11:47:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48566]( [ run ] completed with state SUCCESS. Commit: 7099307 [/LLM/main/L0 MergeRequest PR pipeline 38354]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4459476458)
- `2026-05-17T06:11:58Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48737]( [ run ] completed with state SUCCESS. Commit: 7099307 [/LLM/main/L0 MergeRequest PR pipeline 38503]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4469559748)
- `2026-05-17T16:32:50Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48774]( [ run ] completed with state FAILURE. Commit: 7099307 [/LLM/main/L0 MergeRequest PR pipeline 38537]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4471409650)
- `2026-05-18T07:00:08Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48826]( [ run ] completed with state SUCCESS. Commit: 2145cdc [/LLM/main/L0 MergeRequest PR pipeline 38586]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13975#issuecomment-4475186322)
