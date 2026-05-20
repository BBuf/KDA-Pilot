# PR Discussion Digest

- Source PR: [vllm-project/vllm#23696](https://github.com/vllm-project/vllm/pull/23696)
- Source page: `sources/prs/vllm/PR-23696.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23696`
- Generated at: `2026-05-20T15:37:38.135171+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-27T00:23:43Z`
- Merged: `2025-09-11T21:04:57Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 18 (approved=1, commented=16, dismissed=1)
- Inline review comments: 21
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=7, outdated=12
- Human participants with discussion text: IwakuraRein, djmmoss, mergify, mgoin, nvpohanh, robertgshaw2-redhat, zyongye
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-27T00:26:13Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for mxfp4 fused MoE kernels using CUTLASS for Hopper and Blackwell ... (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3157764773)
- `2025-08-27T01:56:51Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3158031977)
- `2025-08-27T03:09:03Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3158133159)
- `2025-08-27T17:34:32Z` `COMMENTED` by `IwakuraRein` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3160980044)
- `2025-08-27T22:16:14Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3161904940)
- `2025-08-27T22:21:10Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3161913601)
- `2025-09-04T13:50:55Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3185432958)
- `2025-09-04T13:54:26Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3185452285)
- `2025-09-04T14:01:45Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3185491072)
- `2025-09-04T14:04:01Z` `DISMISSED` by `robertgshaw2-redhat` - This will break ROCm. Please ensure that we select the Triton kernels for ROCm backend. Per discussion offline. ... (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3185505873)
- `2025-09-04T17:34:14Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3186371289)
- `2025-09-04T17:34:32Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3186372556)
- `2025-09-04T22:24:01Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3186678182)
- `2025-09-05T08:30:02Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3188473902)
- `2025-09-05T14:35:24Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3189634847)
- `2025-09-05T14:35:29Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3189635080)
- `2025-09-10T23:10:27Z` `COMMENTED` by `mgoin` - Looks reasonable to me, although the process weights after loading and apply functions are getting gnarly (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3208089815)
- `2025-09-11T21:04:19Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23696#pullrequestreview-3213637820)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/mxfp4.py`: 19 inline comment(s)
- `examples/offline_inference/basic/basic.py`: 1 inline comment(s)
- `tests/kernels/moe/test_mxfp4_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-04T13:50:39Z` `inline` by `zyongye` `vllm/model_executor/layers/quantization/mxfp4.py`:56; signals: flashinfer, fp4, kernel, mxfp4, perf, performance, sm90, triton; excerpt: "Can you not make it default when having flashinfer? and use triton kernel on SM90 instead? We can still benefit topk and top-p sampling ..." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2322249966)
- `2025-08-27T01:56:51Z` `inline` by `nvpohanh` `vllm/model_executor/layers/quantization/mxfp4.py`:67; signals: cutlass, flashinfer, fp4, fp8, moe, mxfp4; excerpt: "Can we put this elif before the elif at line 59? This is such that VLLM USE FLASHINFER MOE MXFP4 MXFP8 CUTLASS take precedence ..." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2302645135)
- `2025-08-27T22:21:10Z` `inline` by `djmmoss` `vllm/model_executor/layers/quantization/mxfp4.py`:69; signals: cutlass, fp4, layout, mxfp4, perf, performance; excerpt: "Due to the different weight layouts runtime switching is going to need some additional though. We could be potentially make the switch at startup ..." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2305410992)
- `2025-09-05T08:30:02Z` `inline` by `nvpohanh` `vllm/model_executor/layers/quantization/mxfp4.py`:93; signals: fp4, hopper, kernel, mxfp4, triton; excerpt: "This doesn't match the original logic and breaks GPT-OSS + Hopper when no env vars are set. The original logic says that on Hopper ..." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2324456382)
- `2025-09-04T14:01:45Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/quantization/mxfp4.py`:54; signals: cuda, fp4, kernel, mxfp4, triton; excerpt: "This will break ROCm. We need to select the triton kernel for non-CUDA backends." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2322291622)
- `2025-08-27T17:25:25Z` `inline` by `IwakuraRein` `vllm/model_executor/layers/quantization/mxfp4.py`:762; signals: fp4, hopper, kernel, mxfp4; excerpt: "The autotuning is already handled by [kernel warmup]( but you may need to update the condition to support hopper." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2304782981)
- `2025-09-04T18:42:28Z` `inline` by `zyongye` `vllm/model_executor/layers/quantization/mxfp4.py`:85; signals: blackwell, fp4, hang, mxfp4; excerpt: "Can we change this log to Blackwell only?" (https://github.com/vllm-project/vllm/pull/23696#discussion_r2323138506)
- `2025-08-27T17:30:51Z` `inline` by `IwakuraRein` `vllm/model_executor/layers/quantization/mxfp4.py`:69; signals: cutlass, fp4, mxfp4; excerpt: "Maybe pass in the batch size and add a basic heuristic here to select between trtllm-gen and cutlass?" (https://github.com/vllm-project/vllm/pull/23696#discussion_r2304803133)
- `2025-08-29T01:21:13Z` `issue` by `nvpohanh`; signals: flashinfer, fp4, mxfp4; excerpt: "@djmmoss There is one should use flashinfer mxfp4() you probably missed:" (https://github.com/vllm-project/vllm/pull/23696#issuecomment-3235407533)
- `2025-08-27T03:09:03Z` `inline` by `djmmoss` `vllm/model_executor/layers/quantization/mxfp4.py`:67; signals: fp4, mxfp4; excerpt: "sure, done" (https://github.com/vllm-project/vllm/pull/23696#discussion_r2302727694)
- `2025-08-27T22:16:14Z` `inline` by `djmmoss` `vllm/model_executor/layers/quantization/mxfp4.py`:762; signals: fp4, mxfp4; excerpt: "ah, I see. I moved it." (https://github.com/vllm-project/vllm/pull/23696#discussion_r2305405115)
- `2025-09-04T13:54:26Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/quantization/mxfp4.py`:69; signals: fp4, mxfp4; excerpt: "+1 to @djmmoss" (https://github.com/vllm-project/vllm/pull/23696#discussion_r2322263392)
