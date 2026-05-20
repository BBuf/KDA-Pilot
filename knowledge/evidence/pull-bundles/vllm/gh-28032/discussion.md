# PR Discussion Digest

- Source PR: [vllm-project/vllm#28032](https://github.com/vllm-project/vllm/pull/28032)
- Source page: `sources/prs/vllm/PR-28032.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28032`
- Generated at: `2026-05-20T15:38:25.496066+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-04T08:21:37Z`
- Merged: `2025-11-25T02:15:02Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: ganyi1996ppo, gbyu-amd, mergify, tjtanaa, wuhuikx, xaguilar-amd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-04T08:24:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables fp8 support for MLA decode on ROCm by adding q scale and ... (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3414682333)
- `2025-11-18T03:18:21Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3475312015)
- `2025-11-18T03:23:07Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3475319007)
- `2025-11-18T03:31:17Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3475330060)
- `2025-11-20T11:13:53Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3487218077)
- `2025-11-20T11:16:03Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3487232606)
- `2025-11-24T07:58:40Z` `APPROVED` by `tjtanaa` - LGTM (https://github.com/vllm-project/vllm/pull/28032#pullrequestreview-3498768108)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-11-19T13:31:30Z` `issue` by `xaguilar-amd`; signals: accuracy, bf16, fp8, kernel, mla, perf, performance, triton; excerpt: "We have been testing this as well, and we noticed that when MLA FP8 is in use it introduces three extra 4-5us GPU kernels ..." (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3552735060)
- `2025-11-18T03:43:31Z` `issue` by `gbyu-amd`; signals: bf16, fp8, hang, kernel, mla, perf, performance; excerpt: "PR description updated. But one thing confused me here, that is without , no performance gain should observed from that changes My suggestion is ..." (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3544891654)
- `2025-11-18T03:15:38Z` `issue` by `ganyi1996ppo`; signals: bf16, fp8, hang, kernel, perf, performance; excerpt: "PR description updated. But one thing confused me here, that is without , no performance gain should observed from that changes My suggestion is ..." (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3544841841)
- `2025-11-20T11:16:03Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:60; signals: attention, cache, memory, mla, perf; excerpt: "Yes. It reduces KVCache memory requirement, we can fix the perf in coming PR." (https://github.com/vllm-project/vllm/pull/28032#discussion_r2545567277)
- `2025-11-14T13:43:02Z` `issue` by `gbyu-amd`; signals: bf16, fp8, mla, perf, performance; excerpt: "@gbyu-amd can you provide performance improvement ratio bf16 vs fp8, and include the lm-eval score of bf16 (baseline) and fp8 (this PR). PR description ..." (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3532874183)
- `2025-11-18T03:23:07Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:60; signals: attention, fp8, hang, mla; excerpt: "I don't think we should change those 2 class variable, QueryLenSupport.VARLEN and AttentionCGSupport.UNIFORM BATCH are used only for MTP case, since your PR only ..." (https://github.com/vllm-project/vllm/pull/28032#discussion_r2536173235)
- `2025-11-18T03:31:17Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:60; signals: attention, mla, perf, performance; excerpt: "Even without performance improvement, I think this is still a important functionality feature for ROCm's MLA backend, and worth to merge. What do you ..." (https://github.com/vllm-project/vllm/pull/28032#discussion_r2536183673)
- `2025-11-12T06:16:51Z` `issue` by `tjtanaa`; signals: bf16, fp8, perf, performance; excerpt: "@gbyu-amd can you provide performance improvement ratio bf16 vs fp8, and include the lm-eval score of bf16 (baseline) and fp8 (this PR)." (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3520225275)
- `2025-11-12T06:18:42Z` `issue` by `gbyu-amd`; signals: bf16, fp8, perf, performance; excerpt: "@gbyu-amd can you provide performance improvement ratio bf16 vs fp8, and include the lm-eval score of bf16 (baseline) and fp8 (this PR). sure, will ..." (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3520231261)
- `2025-11-18T03:18:21Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:274; signals: attention, dtype, mla; excerpt: "I wonder if we have better solution than hardcode this to bfloat16, maybe self.model config.dtype ? What's your thought @tjtanaa @gshtras ?" (https://github.com/vllm-project/vllm/pull/28032#discussion_r2536166938)
- `2025-11-20T11:13:53Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:274; signals: attention, dtype, mla; excerpt: "Great suggestion. It is better to set it to the model dtype." (https://github.com/vllm-project/vllm/pull/28032#discussion_r2545555927)
- `2025-11-05T07:17:44Z` `issue` by `wuhuikx`; signals: accuracy, perf, performance; excerpt: "Could you please attach the accuracy result and the performance improvement ratio?" (https://github.com/vllm-project/vllm/pull/28032#issuecomment-3489703245)
