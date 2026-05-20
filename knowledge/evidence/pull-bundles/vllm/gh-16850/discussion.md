# PR Discussion Digest

- Source PR: [vllm-project/vllm#16850](https://github.com/vllm-project/vllm/pull/16850)
- Source page: `sources/prs/vllm/PR-16850.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16850`
- Generated at: `2026-05-20T15:35:02.452777+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-18T15:46:46Z`
- Merged: `2025-05-05T16:39:31Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 19 (approved=1, commented=18)
- Inline review comments: 38
- Review threads observed: 23
- Resolved/outdated thread markers: resolved=22, outdated=13
- Human participants with discussion text: ElizaWszola, jinzhen-lin, mergify, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-04-23T02:36:41Z` `COMMENTED` by `mgoin` - This does increase the wheel size by about 10MB to 313MB, so we should try to trim down ... (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785670546)
- `2025-04-23T03:01:55Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785818793)
- `2025-04-23T03:03:34Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785806276)
- `2025-04-23T03:05:16Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785821563)
- `2025-04-23T05:17:28Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785957357)
- `2025-04-23T05:18:22Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785958380)
- `2025-04-23T05:21:04Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785962077)
- `2025-04-23T05:25:20Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785967477)
- `2025-04-23T06:05:32Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2786031951)
- `2025-04-23T06:07:02Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2786035172)
- `2025-04-23T06:09:50Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2786041774)
- `2025-04-23T07:55:50Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2786317727)
- `2025-04-23T08:02:13Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2786336077)
- `2025-04-23T11:59:04Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2787036187)
- `2025-04-23T12:02:17Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2787045785)
- `2025-04-29T06:45:36Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2802228199)
- `2025-04-29T06:56:12Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2802274898)
- `2025-04-29T07:18:24Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2802325423)
- `2025-05-05T16:14:55Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2815341032)

## Inline Comment Hotspots

- `csrc/moe/marlin_moe_wna16/ops.cu`: 9 inline comment(s)
- `csrc/moe/marlin_moe_wna16/marlin_template.h`: 5 inline comment(s)
- `CMakeLists.txt`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/marlin_utils.py`: 4 inline comment(s)
- `csrc/quantization/gptq_marlin/generate_kernels.py`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/marlin_utils_fp8.py`: 3 inline comment(s)
- `vllm/scalar_type.py`: 3 inline comment(s)
- `csrc/moe/marlin_moe_wna16/generate_kernels.py`: 2 inline comment(s)
- `csrc/quantization/gptq_marlin/gptq_marlin.cu`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-04-29T07:18:23Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/marlin_template.h`:1835; signals: block, memory, moe, shared memory; excerpt: "This optimization aims to minimize redundant reads of matrix A by utilizing the remaining shared memory to store a half-precision matrix of size moe ..." (https://github.com/vllm-project/vllm/pull/16850#discussion_r2065678722)
- `2025-04-19T13:49:13Z` `issue` by `jinzhen-lin`; signals: benchmark, moe, perf, performance; excerpt: "moe marlin benchmark tests (on A800) ( NOTE1 : The optimization methods introduced in this PR have already been implemented in for cases where ..." (https://github.com/vllm-project/vllm/pull/16850#issuecomment-2816716194)
- `2025-04-23T07:55:50Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/utils/marlin_utils.py`:394; signals: kernel, memory, moe; excerpt: "It seems that gptq/awq marlin does not support using in-place operations here to reduce redundant memory usage. My main goal is to keep the ..." (https://github.com/vllm-project/vllm/pull/16850#discussion_r2055471772)
- `2025-04-23T12:02:17Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/ops.cu`:196; signals: memory, moe, shared memory; excerpt: "I miscalculated the shared memory size occupied by scale. Indeed, there's no need to add 1 here. Updated." (https://github.com/vllm-project/vllm/pull/16850#discussion_r2055897104)
- `2025-04-23T02:54:58Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/marlin_utils_fp8.py`:120; signals: block, fp8; excerpt: "Please add comments for the operations here, as this answered a question I had with how to support block quant with group quant support ..." (https://github.com/vllm-project/vllm/pull/16850#discussion_r2055169047)
- `2025-04-23T08:02:13Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/utils/marlin_utils.py`:192; signals: block, kernel; excerpt: "Yes. In previous, marlin kernel have (size m / block size m) (size n / block size n) output blocks, so we need a ..." (https://github.com/vllm-project/vllm/pull/16850#discussion_r2055483093)
- `2025-04-29T06:56:12Z` `inline` by `ElizaWszola` `csrc/moe/marlin_moe_wna16/ops.cu`:361; signals: cute, moe; excerpt: "Does this mean that the code in hqq marlin.py will not be able to execute? Or is there some fallback in place?" (https://github.com/vllm-project/vllm/pull/16850#discussion_r2065647336)
- `2025-04-23T00:30:38Z` `inline` by `mgoin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:59; signals: kernel, moe; excerpt: "Please add a comment for this case" (https://github.com/vllm-project/vllm/pull/16850#discussion_r2055078524)
- `2025-04-23T00:30:51Z` `inline` by `mgoin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:73; signals: kernel, moe; excerpt: "Please add a comment for this case" (https://github.com/vllm-project/vllm/pull/16850#discussion_r2055078642)
- `2025-04-23T02:36:41Z` `review` `COMMENTED` by `mgoin`; signals: compile; excerpt: "This does increase the wheel size by about 10MB to 313MB, so we should try to trim down a bit. I think there may ..." (https://github.com/vllm-project/vllm/pull/16850#pullrequestreview-2785670546)
- `2025-04-19T14:10:43Z` `issue` by `jinzhen-lin`; signals: benchmark, hang; excerpt: "@mgoin @LucasWilkinson The benchmark results is posted. BTW, should we change the default value of VLLM MARLIN USE ATOMIC ADD to 1 now ? ..." (https://github.com/vllm-project/vllm/pull/16850#issuecomment-2816722820)
- `2025-05-04T14:16:28Z` `issue` by `jinzhen-lin`; signals: failing, moe; excerpt: "Looks like several of the failing tests are related to the merge 😞 @mgoin The error seems introduced by rebase. FIxed now (The content ..." (https://github.com/vllm-project/vllm/pull/16850#issuecomment-2849245302)
