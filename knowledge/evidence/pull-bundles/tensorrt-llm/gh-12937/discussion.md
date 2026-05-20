# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12937](https://github.com/NVIDIA/TensorRT-LLM/pull/12937)
- Source page: `sources/prs/tensorrt-llm/PR-12937.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12937`
- Generated at: `2026-05-20T15:18:26.295982+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-10T15:49:48Z`
- Merged: `2026-04-23T08:02:25Z`

## Discussion Counts

- Issue comments: 74
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 7
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: chang-l, coderabbitai, tensorrt-cicd, xrq-phys, zhenhuaw-me
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-10T15:58:47Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4090879635)
- `2026-04-10T16:42:33Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4091168697)
- `2026-04-10T16:43:04Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4091171422)
- `2026-04-11T05:51:35Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4093465449)
- `2026-04-11T05:52:39Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4093466278)
- `2026-04-21T01:42:17Z` `APPROVED` by `zhenhuaw-me` (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4144527729)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/common/attentionOp.cpp`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/multiHeadAttentionCommon.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-10T15:58:42Z` `issue` by `coderabbitai`; signals: attention, bf16, block, cuda, fp8, hang, kernel, perf; excerpt: "📝 Walkthrough Walkthrough Integrates SageAttention quantization support into TensorRT-LLM's attention operator. Adds new CUDA quantization kernels for Q/K/V, extends workspace management for FP8/INT8 buffers, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#issuecomment-4225054841)
- `2026-04-10T15:58:47Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, hang, kernel, sm100, tensorrt, tma; excerpt: "Actionable comments posted: 3 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#pullrequestreview-4090879635)
- `2026-04-11T05:52:39Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/common/attentionOp.cpp`:824; signals: attention, block, fp8, mla, tensorrt; excerpt: "@xrq-phys, you're right — there's no direct total kv len parameter in getWorkspaceSizeForContext. However, there are two available building blocks: 1. kv seq length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3067662369)
- `2026-04-10T15:58:45Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/common/attentionOp.cpp`:824; signals: attention, fp8, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical These SageAttention workspace sizes are keyed off Q length, but the kernel writes K/V using KV length. fp8 k ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3065367216)
- `2026-04-10T15:58:45Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:62; signals: attention, benchmark, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical dataTypeV is dropped here, so the INT8 SageAttention path becomes (K=int8, V=int8). AttentionOp now sets SageAttention as dataTypeKv = ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3065367226)
- `2026-04-10T15:58:46Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/multiHeadAttentionCommon.h`:80; signals: attention, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 3225 --- Add the missing include. The unpack ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3065367255)
- `2026-04-10T16:43:04Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/common/attentionOp.cpp`:824; signals: attention, kernel, tensorrt; excerpt: "@xrq-phys, sounds good — thanks for the acknowledgment! Just a quick reminder to also update sage k sfs buffer size (keyed off input seq ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3065591911)
- `2026-04-11T05:51:35Z` `inline` by `xrq-phys` `cpp/tensorrt_llm/common/attentionOp.cpp`:824; signals: attention, tensorrt; excerpt: "Question: IIUC, input seq length stands for max num of tokens among the Q batches, but we don't seem to have such a member ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3067661329)
- `2026-04-10T16:42:32Z` `inline` by `xrq-phys` `cpp/tensorrt_llm/common/attentionOp.cpp`:824; signals: attention, tensorrt; excerpt: "CR is right. Will fix." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#discussion_r3065589567)
- `2026-04-12T06:47:07Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42844]( [ run ] completed with state SUCCESS. Commit: c1d64f7 [/LLM/main/L0 MergeRequest PR pipeline 33510]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#issuecomment-4230940671)
- `2026-04-12T08:52:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42855]( [ run ] completed with state SUCCESS. Commit: c1d64f7 [/LLM/main/L0 MergeRequest PR pipeline 33521]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#issuecomment-4231152456)
- `2026-04-12T19:24:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42890]( [ run ] completed with state SUCCESS. Commit: d3727fe [/LLM/main/L0 MergeRequest PR pipeline 33553]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12937#issuecomment-4232567685)
