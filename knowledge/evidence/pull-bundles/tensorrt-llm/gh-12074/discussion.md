# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12074](https://github.com/NVIDIA/TensorRT-LLM/pull/12074)
- Source page: `sources/prs/tensorrt-llm/PR-12074.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12074`
- Generated at: `2026-05-20T15:18:04.472650+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-10T07:01:13Z`
- Merged: `2026-04-30T08:17:05Z`

## Discussion Counts

- Issue comments: 116
- Review submissions: 18 (approved=8, changes_requested=1, commented=9)
- Inline review comments: 18
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=4
- Human participants with discussion text: QiJune, StanleySun639, chang-l, coderabbitai, kaiyux, liji-nv, peaceh-nv, pengbowang-nv, tensorrt-cicd, xinhe-nv, xxi-nv, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-10T07:16:05Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 🧹 Nitpick comments (2) tensorrt llm/ torch/custom ops/cute dsl custom ops.py (1) 323-324: For ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-3920280905)
- `2026-03-13T09:32:58Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-3942747503)
- `2026-03-20T08:03:05Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-3980064524)
- `2026-03-23T01:40:08Z` `APPROVED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-3988929413)
- `2026-04-01T03:25:48Z` `APPROVED` by `zongfeijing` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4041450484)
- `2026-04-07T09:12:56Z` `APPROVED` by `pengbowang-nv` - Attention changes LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4066984237)
- `2026-04-08T08:10:33Z` `CHANGES_REQUESTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4073664562)
- `2026-04-09T01:43:42Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4079266979)
- `2026-04-13T08:23:54Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4097327119)
- `2026-04-14T09:48:55Z` `APPROVED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4104931179)
- `2026-04-14T09:57:14Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4105019362)
- `2026-04-15T02:15:16Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4110379289)
- `2026-04-20T08:31:47Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4138418769)
- `2026-04-20T08:32:00Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4138420370)
- `2026-04-21T05:13:59Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4145186990)
- `2026-04-21T09:08:28Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4146454686)
- `2026-04-21T10:04:50Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4146803288)
- `2026-04-30T05:48:20Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-4202701846)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/attention.py`: 5 inline comment(s)
- `tensorrt_llm/llmapi/llm_args.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 3 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_gemm_persistent.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-10T07:16:05Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, blackwell, cute, gemm, hang, kernel, race; excerpt: "Actionable comments posted: 6 🧹 Nitpick comments (2) tensorrt llm/ torch/custom ops/cute dsl custom ops.py (1) 323-324: For new imports, follow the module-namespace rule. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#pullrequestreview-3920280905)
- `2026-03-10T07:16:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_gemm_persistent.py`:129; signals: blackwell, cute, epilogue, gemm, kernel, layout, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major Fail fast when use tma store is false. The constructor exposes a non-TMA epilogue mode, but the rest of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r2909809833)
- `2026-03-10T07:16:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/attention.py`:2223; signals: attention, bf16, blackwell, cute, cutlass, register, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard the CuTe BF16 path on op registration, not just SM. cute dsl bf16 bmm blackwell is only registered ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r2909809839)
- `2026-04-14T09:57:14Z` `inline` by `peaceh-nv` `tensorrt_llm/_torch/modules/attention.py`:2439; signals: attention, b200, bf16, cute, fp4, gemm, perf, regression; excerpt: "The perf result is in the description, Perf result on GB200 1k/1k 1ctx + 2gen DEP8 bs512 DeepSeek-FP4 tps/user: native bf16 bmm + gemm ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r3078624811)
- `2026-03-10T07:16:04Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:1999; signals: accuracy, bf16, blackwell, cute, kernel, memory, sm100; excerpt: "⚠️ Potential issue 🟡 Minor Gate these tests to SM100f so they actually hit the CuteDSL BF16 path. This feature is runtime-gated by is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r2909809848)
- `2026-04-14T09:48:52Z` `inline` by `kaiyux` `tensorrt_llm/_torch/modules/attention.py`:2439; signals: attention, bf16, blackwell, cute, perf, performance, tensorrt; excerpt: "What's the performance status of cute dsl bf16 bmm blackwell when comparing with bmm out? Just thinking if we can make the default performance ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r3078577929)
- `2026-03-10T07:16:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_gemm_persistent.py`:14; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Update the Apache header year to 2026. This file is being added/meaningfully modified in this March 2026 PR, so ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r2909809827)
- `2026-03-10T07:16:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3864; signals: cute, layout, memory, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 950 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r2909809812)
- `2026-04-30T05:48:20Z` `inline` by `peaceh-nv` `tensorrt_llm/llmapi/llm_args.py`:3825; signals: bf16, cute, fp8, tensorrt; excerpt: "Done, added bf16 cute dsl configs section comment to separate from fp8 configs." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r3165877287)
- `2026-04-14T09:42:45Z` `inline` by `kaiyux` `tensorrt_llm/_torch/modules/attention.py`:2436; signals: attention, block, tensorrt; excerpt: "since it appears repeatedly, is it better to be a function? Or should we even make the whole block a function?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r3078541325)
- `2026-04-21T05:11:22Z` `inline` by `chang-l` `tensorrt_llm/llmapi/llm_args.py`:3825; signals: cute, fp8, tensorrt; excerpt: "Nit: can we have the similar comment (as above for fp8) to separate from fp8 cute dsl configs?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r3115172570)
- `2026-04-08T08:10:28Z` `inline` by `liji-nv` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:5652; signals: cute, tensorrt; excerpt: "Any specific reason to use mutated output? If not, avoid use mutated output. If mutated output is must have, the custom op need to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12074#discussion_r3049998946)
