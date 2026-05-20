# PR Discussion Digest

- Source PR: [vllm-project/vllm#18596](https://github.com/vllm-project/vllm/pull/18596)
- Source page: `sources/prs/vllm/PR-18596.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18596`
- Generated at: `2026-05-20T15:35:21.083777+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-23T06:49:18Z`
- Merged: `2025-06-18T15:46:52Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 24 (approved=3, commented=21)
- Inline review comments: 22
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=0, outdated=5
- Human participants with discussion text: HAIAI, SageMoore, Zzz9990, fsx950223, gshtras, houseroad, maleksan85, mergify, tjtanaa, tjtanaavllm, vllmellm
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-26T08:14:14Z` `COMMENTED` by `tjtanaavllm` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2867638929)
- `2025-05-27T02:44:50Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2869408128)
- `2025-05-27T17:01:02Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2871874964)
- `2025-05-28T14:26:50Z` `COMMENTED` by `SageMoore` - Thanks for the contribution. The FP8 speedups look good! It looks like you can clean up the backend ... (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2875323965)
- `2025-05-28T14:42:31Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2875387656)
- `2025-05-28T14:42:56Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2875389146)
- `2025-05-28T15:12:06Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2875498501)
- `2025-05-28T16:56:29Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2875808777)
- `2025-05-29T05:14:23Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2877079545)
- `2025-05-30T02:38:51Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2880049438)
- `2025-05-30T07:27:11Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2880140676)
- `2025-05-31T09:06:48Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2883742027)
- `2025-05-31T13:49:36Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2884120315)
- `2025-06-02T17:05:14Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2889283181)
- `2025-06-04T02:55:42Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2894797921)
- `2025-06-04T08:40:28Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2895827833)
- `2025-06-05T13:02:55Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2900250449)
- `2025-06-05T18:30:43Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2901626689)
- `2025-06-13T05:50:36Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2923490781)
- `2025-06-16T15:43:54Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2932650132)
- `2025-06-16T15:50:56Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2932678770)
- `2025-06-17T07:14:02Z` `APPROVED` by `houseroad` - Accept to unblock. Since only touch AMD related logic, should be safe on other platform. Could @HAIAI or ... (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2934419705)
- `2025-06-17T07:39:46Z` `APPROVED` by `HAIAI` - LGTM (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2934495943)
- `2025-06-17T20:11:32Z` `APPROVED` by `SageMoore` - Looks reasonable. If you can delete some more of the cascade attention code in the builder/metadata that would ... (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2936962458)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/rocm_aiter_fa.py`: 18 inline comment(s)
- `vllm/model_executor/layers/layernorm.py`: 2 inline comment(s)
- `vllm/platforms/rocm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-31T09:18:16Z` `issue` by `fsx950223`; signals: accuracy, attention, bf16, cache, dtype, fp8, kernel, perf; excerpt: "@Zzz9990 can we have more holistic evaluation of whether this AITER MHA benefits most models in general when compared with chunckedprefill attention before we ..." (https://github.com/vllm-project/vllm/pull/18596#issuecomment-2924753471)
- `2025-06-02T09:30:47Z` `issue` by `tjtanaa`; signals: attention, benchmark, flash attention, latency, memory, perf, performance, throughput; excerpt: "Having another backend especially AITER Flash Attention Backend is important opens up for vLLM to benefit from the future optimization that AITER team done ..." (https://github.com/vllm-project/vllm/pull/18596#issuecomment-2929671334)
- `2025-06-02T09:59:31Z` `issue` by `tjtanaa`; signals: accuracy, attention, bf16, cache, dtype, fp8, kernel, perf; excerpt: "@Zzz9990 can we have more holistic evaluation of whether this AITER MHA benefits most models in general when compared with chunckedprefill attention before we ..." (https://github.com/vllm-project/vllm/pull/18596#issuecomment-2929785370)
- `2025-05-30T04:22:23Z` `inline` by `vllmellm` `vllm/v1/attention/backends/rocm_aiter_fa.py`:132; signals: attention, hang, kernel, mla, perf, performance; excerpt: "@fsx950223 can we know why min seqlen q=1 while the default value is set to 0 in aiter package?. would changing this min value ..." (https://github.com/vllm-project/vllm/pull/18596#discussion_r2115113052)
- `2025-05-30T07:09:53Z` `issue` by `tjtanaa`; signals: attention, bf16, cache, dtype, fp8, kernel; excerpt: "@Zzz9990 can we have more holistic evaluation of whether this AITER MHA benefits most models in general when compared with chunckedprefill attention before we ..." (https://github.com/vllm-project/vllm/pull/18596#issuecomment-2921434953)
- `2025-05-31T09:06:48Z` `inline` by `fsx950223` `vllm/v1/attention/backends/rocm_aiter_fa.py`:132; signals: attention, block, hang, moe; excerpt: "@fsx950223 can you add this bug fix for vLLM as AITER commit: 648764942e552a8bb5fe16026703716a81f05374 has changes in the enum of fused moe vllm/model executor/layers/fused moe/rocm ..." (https://github.com/vllm-project/vllm/pull/18596#discussion_r2117590349)
- `2025-05-28T14:26:50Z` `review` `COMMENTED` by `SageMoore`; signals: attention, fp8, speedup; excerpt: "Thanks for the contribution. The FP8 speedups look good! It looks like you can clean up the backend a bit by removing the cascade ..." (https://github.com/vllm-project/vllm/pull/18596#pullrequestreview-2875323965)
- `2025-05-31T09:23:07Z` `issue` by `fsx950223`; signals: bf16, cache, kv cache, triton; excerpt: "In the PR, fa only supports bf16 and fp16 kv cache. We tested the implementation on Llama3 models and get large improvements than triton ..." (https://github.com/vllm-project/vllm/pull/18596#issuecomment-2924759318)
- `2025-05-30T02:38:51Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:132; signals: attention, hang, moe; excerpt: "@fsx950223 can you add this bug fix for vLLM as AITER commit: 648764942e552a8bb5fe16026703716a81f05374 has changes in the enum of fused moe vllm/model executor/layers/fused moe/rocm ..." (https://github.com/vllm-project/vllm/pull/18596#discussion_r2115044847)
- `2025-05-31T13:49:36Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:132; signals: attention, kernel, mla; excerpt: "To use this PR, the AITER commit needs to be upgraded to 648764942e552a8bb5fe16026703716a81f05374 which will break other AITER kernels as VLLM ROCM USE AITER ..." (https://github.com/vllm-project/vllm/pull/18596#discussion_r2117870448)
- `2025-05-28T14:42:31Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:424; signals: attention, block; excerpt: "Can you update this to "AiterFlashAttention does not support block-sparse attention"? Can you do this for this whole file to make the error message ..." (https://github.com/vllm-project/vllm/pull/18596#discussion_r2112094967)
- `2025-05-27T17:01:02Z` `inline` by `maleksan85` `vllm/v1/attention/backends/rocm_aiter_fa.py`:528; signals: attention; excerpt: "did you mean max query len here to check that there are prefills in batch to process in flash attn varlen func?" (https://github.com/vllm-project/vllm/pull/18596#discussion_r2109721216)
