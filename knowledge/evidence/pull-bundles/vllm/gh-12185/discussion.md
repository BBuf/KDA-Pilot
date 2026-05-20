# PR Discussion Digest

- Source PR: [vllm-project/vllm#12185](https://github.com/vllm-project/vllm/pull/12185)
- Source page: `sources/prs/vllm/PR-12185.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12185`
- Generated at: `2026-05-20T15:33:40.774406+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-18T11:21:09Z`
- Merged: `2025-01-29T14:07:10Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=5
- Human participants with discussion text: casper-hansen, jeejeelee, jinzhen-lin, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-01-20T17:10:48Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2562691945)
- `2025-01-20T17:13:44Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2562855361)
- `2025-01-21T03:21:23Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2563392372)
- `2025-01-21T03:34:01Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2563410024)
- `2025-01-21T03:34:53Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2563410602)
- `2025-01-21T03:38:33Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2563413006)
- `2025-01-22T09:33:50Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2566669547)
- `2025-01-22T10:39:19Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2566831769)
- `2025-01-22T11:58:11Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2567004891)
- `2025-01-22T17:39:05Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2567874895)
- `2025-01-29T14:07:04Z` `APPROVED` by `mgoin` - Thanks for getting this over the line! (https://github.com/vllm-project/vllm/pull/12185#pullrequestreview-2581155915)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/moe_quant_int.py`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/moe_wna16.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-01-22T17:11:37Z` `issue` by `mgoin`; signals: benchmark, h100, kernel, moe, perf; excerpt: "Thank you, it seems to work fine now. I ran a 128/128 benchmark at 10QPS for the mixtral awq model on H100 and found ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2607808316)
- `2025-01-21T03:34:01Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/moe_quant_int.py`:116; signals: kernel, moe, nan, triton; excerpt: "I considered this before, but I created a new quantization method finally. The reasons are 1. This quantization method can be combined all gptq/awq ..." (https://github.com/vllm-project/vllm/pull/12185#discussion_r1923027385)
- `2025-01-21T06:15:51Z` `issue` by `jinzhen-lin`; signals: hang, kernel, moe, triton; excerpt: "Considering that this is allowing for "another option" to run quantized moe models, maybe we should consider writing a documentation page specifically for moe ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2603750929)
- `2025-01-22T15:29:41Z` `issue` by `mgoin`; signals: benchmark, kernel, moe, triton; excerpt: "I test with small moe model ( just now, triton kernel seems much faster than marlin kernel too. Besides, marlin kernel seems generate wrong ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2607557090)
- `2025-01-22T17:19:47Z` `issue` by `casper-hansen`; signals: benchmark, h100, kernel, perf; excerpt: "Thank you, it seems to work fine now. I ran a 128/128 benchmark at 10QPS for the mixtral awq model on H100 and found ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2607826461)
- `2025-01-20T16:58:23Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/fused_moe.py`:23; signals: block, kernel, moe; excerpt: "There's quite a bit of code duplication between this and fused moe kernel - Not necessarily a blocker for this PR but IMO we ..." (https://github.com/vllm-project/vllm/pull/12185#discussion_r1922675219)
- `2025-01-20T19:20:40Z` `issue` by `mgoin`; signals: kernel, moe, triton; excerpt: "Considering that this is allowing for "another option" to run quantized moe models, maybe we should consider writing a documentation page specifically for moe ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2603109191)
- `2025-01-20T17:06:58Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/moe_quant_int.py`:20; signals: hang, moe; excerpt: "Update this comment Is there any more specific name we could use for this method? I also feel that --quantization moe quant int is ..." (https://github.com/vllm-project/vllm/pull/12185#discussion_r1922685225)
- `2025-01-21T03:38:33Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:23; signals: kernel, moe; excerpt: "At the beginning I tried to modify the fused moe kernel, and found that this made this origin code very complex (with many complex ..." (https://github.com/vllm-project/vllm/pull/12185#discussion_r1923029453)
- `2025-01-21T03:21:23Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/moe_quant_int.py`:20; signals: hang, moe; excerpt: "moe wNa16 is a better name, I would change it." (https://github.com/vllm-project/vllm/pull/12185#discussion_r1923016992)
- `2025-01-20T12:51:39Z` `issue` by `jinzhen-lin`; signals: block, moe; excerpt: "@mgoin @robertgshaw2-redhat Could we expedite this PR + 12036 (not sure if 12204 is needed too or has overlap) now that DeepSeek has released ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2602350547)
- `2025-01-20T15:04:38Z` `issue` by `jinzhen-lin`; signals: perf, performance; excerpt: "I think this PR could be closed in favor of 12222. Thanks for your work @jinzhen-lin is an optimiztion over or it can be ..." (https://github.com/vllm-project/vllm/pull/12185#issuecomment-2602654454)
