# PR Discussion Digest

- Source PR: [vllm-project/vllm#13321](https://github.com/vllm-project/vllm/pull/13321)
- Source page: `sources/prs/vllm/PR-13321.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13321`
- Generated at: `2026-05-20T15:34:01.256880+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-15T05:52:44Z`
- Merged: `2025-03-11T00:12:40Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=2
- Human participants with discussion text: GreyZzzzzzXh, LagPixelLOL, jinzhen-lin, lizongyao123, mgoin, sunjianxide
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-02-28T04:10:17Z` `COMMENTED` by `mgoin` - Nice work keeping the kernel clean! I do think we definitely need to refactor fused moe.py to give ... (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2649646759)
- `2025-02-28T05:18:31Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2649753183)
- `2025-02-28T05:19:37Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2649754296)
- `2025-02-28T05:21:25Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2649756052)
- `2025-02-28T05:28:11Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2649763053)
- `2025-02-28T16:09:04Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2651187602)
- `2025-03-11T00:12:28Z` `APPROVED` by `mgoin` - Excellent work, thank you (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2672434884)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 6 inline comment(s)
- `csrc/moe/moe_wna16.cu`: 3 inline comment(s)
- `CMakeLists.txt`: 2 inline comment(s)

## High-Signal Discussion

- `2025-02-18T07:01:14Z` `issue` by `jinzhen-lin`; signals: gemm, memory, mla, moe, perf, performance; excerpt: "@sunjianxide try to run with VLLM MLA DISABLE=1 and reduce max model len, increase gpu memory utilization. This PR only optimizes moe gemm operator, ..." (https://github.com/vllm-project/vllm/pull/13321#issuecomment-2664772332)
- `2025-02-28T05:28:11Z` `inline` by `jinzhen-lin` `csrc/moe/moe_wna16.cu`:310; signals: cuda, gemm, moe, perf, performance; excerpt: "The first version of the moe wna16 gemm supports int4 only, so the should moe wna16 use cuda does a check bit == 4. ..." (https://github.com/vllm-project/vllm/pull/13321#discussion_r1974803297)
- `2025-02-28T16:09:04Z` `inline` by `jinzhen-lin` `csrc/moe/moe_wna16.cu`:310; signals: cuda, kernel, moe, perf, triton; excerpt: "@mgoin My test result shows that the triton kernel perform well for int8 (even slightly better than cuda kernel). So it would be better ..." (https://github.com/vllm-project/vllm/pull/13321#discussion_r1975664260)
- `2025-02-28T03:48:52Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:746; signals: kernel, moe, triton; excerpt: "Why do you need to copy the config? I assume this config applies to the triton kernel as well and we don't rollback" (https://github.com/vllm-project/vllm/pull/13321#discussion_r1974721192)
- `2025-02-28T03:59:02Z` `inline` by `mgoin` `csrc/moe/moe_wna16.cu`:310; signals: cuda, moe, perf; excerpt: "should moe wna16 use cuda checks for bit == 4 only, is it not as performant for 8bit?" (https://github.com/vllm-project/vllm/pull/13321#discussion_r1974727399)
- `2025-02-28T04:10:17Z` `review` `COMMENTED` by `mgoin`; signals: kernel, moe; excerpt: "Nice work keeping the kernel clean! I do think we definitely need to refactor fused moe.py to give a better interface to plug in ..." (https://github.com/vllm-project/vllm/pull/13321#pullrequestreview-2649646759)
- `2025-02-18T06:31:16Z` `issue` by `sunjianxide`; signals: memory, moe, speedup; excerpt: "can you show you run command with vllm ? I run on on 8 A800 + deepseek-r1-awq ，but the speedup ratio typically ranges from ..." (https://github.com/vllm-project/vllm/pull/13321#issuecomment-2664732753)
- `2025-02-28T05:18:31Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:746; signals: block, moe; excerpt: "The gate up proj and down proj have different N and K, so the optimal BLOCK SIZE N and BLOCK SIZE K may differ. ..." (https://github.com/vllm-project/vllm/pull/13321#discussion_r1974796740)
- `2025-03-10T03:10:41Z` `issue` by `GreyZzzzzzXh`; signals: correctness, kernel; excerpt: "Hi @jinzhen-lin , the writes to output in these two places cannot guarantee the order of execution, which may lead to potential correctness issues. ..." (https://github.com/vllm-project/vllm/pull/13321#issuecomment-2709320512)
- `2025-03-10T03:34:08Z` `issue` by `jinzhen-lin`; signals: correctness, kernel; excerpt: "Hi @jinzhen-lin , the writes to output in these two places cannot guarantee the order of execution, which may lead to potential correctness issues. ..." (https://github.com/vllm-project/vllm/pull/13321#issuecomment-2709345106)
- `2025-02-28T04:06:25Z` `inline` by `mgoin` `CMakeLists.txt`:561; signals: cuda; excerpt: "We might want to put this source in a if(VLLM GPU LANG STREQUAL "CUDA") section - I'm not sure if this might accidentally get ..." (https://github.com/vllm-project/vllm/pull/13321#discussion_r1974732221)
- `2025-02-28T03:52:59Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:915; signals: moe; excerpt: "What is "int4 w8a16"? Is this just a typo for int4 w4a16?" (https://github.com/vllm-project/vllm/pull/13321#discussion_r1974723807)
