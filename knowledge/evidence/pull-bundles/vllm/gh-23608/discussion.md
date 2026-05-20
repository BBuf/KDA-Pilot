# PR Discussion Digest

- Source PR: [vllm-project/vllm#23608](https://github.com/vllm-project/vllm/pull/23608)
- Source page: `sources/prs/vllm/PR-23608.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23608`
- Generated at: `2026-05-20T15:37:33.480395+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-26T02:25:30Z`
- Merged: `2025-08-27T21:33:22Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 15 (approved=2, commented=13)
- Inline review comments: 15
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=1, outdated=7
- Human participants with discussion text: bnellnm, mergify, mgoin, varun-sundar-rabindranath, weireweire, zyongye
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-08-26T02:27:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds Data Parallelism and Expert Parallelism support for GPT-OSS models, particularly with the ... (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3153635852)
- `2025-08-26T11:02:56Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155105948)
- `2025-08-26T11:06:01Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155114731)
- `2025-08-26T14:31:10Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155932462)
- `2025-08-26T14:36:36Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155957944)
- `2025-08-26T14:36:54Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155959557)
- `2025-08-26T14:37:01Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155960047)
- `2025-08-26T14:37:56Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3155964495)
- `2025-08-26T14:45:29Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3156000557)
- `2025-08-26T15:42:41Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3156264945)
- `2025-08-26T16:26:43Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3156434429)
- `2025-08-26T20:24:56Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3157198914)
- `2025-08-26T20:32:24Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3157217897)
- `2025-08-26T20:32:53Z` `APPROVED` by `bnellnm` - LGTM. All the layer arguments could be torch.nn.Module instead of Any (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3157219310)
- `2025-08-27T21:33:02Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23608#pullrequestreview-3160050909)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/trtllm_moe.py`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/mxfp4.py`: 3 inline comment(s)
- `vllm/distributed/device_communicators/base_device_communicator.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-26T14:45:28Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/mxfp4.py`:458; signals: fp4, mxfp4, race; excerpt: "If we want a graceful fallback instead of an error you could overload maybe make prepare finalize and make it return None for the ..." (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301243104)
- `2025-08-26T20:32:23Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/mxfp4.py`:458; signals: fp4, kernel, mxfp4; excerpt: "The fallback would basically be disabling the all2all communication for this layer and using the non-batched kernels but maybe erroring out would be better." (https://github.com/vllm-project/vllm/pull/23608#discussion_r2302076107)
- `2025-08-26T20:37:18Z` `issue` by `zyongye`; signals: b200, benchmark, perf, performance; excerpt: "Done with the nit fix. I will run some performance benchmarks tonight after the B200 is freed." (https://github.com/vllm-project/vllm/pull/23608#issuecomment-3225656098)
- `2025-08-26T15:42:40Z` `inline` by `zyongye` `vllm/model_executor/layers/quantization/mxfp4.py`:458; signals: fp4, kernel, mxfp4; excerpt: "what can we fall back to? I don't know if there's any other kernel has batched mxfp4?" (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301414991)
- `2025-08-26T11:02:56Z` `inline` by `varun-sundar-rabindranath` `vllm/distributed/device_communicators/base_device_communicator.py`:258; signals: hang; excerpt: "@bnellnm This PR makes the change to pass the layer as an argument to init prepare finalize can you take a look please. Thanks." (https://github.com/vllm-project/vllm/pull/23608#discussion_r2300623349)
- `2025-08-26T14:37:56Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:16; signals: moe; excerpt: "Can you pass the individual components here instead of the entire layer? Using the layer makes it harder to test." (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301218993)
- `2025-08-26T11:06:00Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:36; signals: moe; excerpt: "This should be True ." (https://github.com/vllm-project/vllm/pull/23608#discussion_r2300630113)
- `2025-08-26T14:31:10Z` `inline` by `bnellnm` `vllm/distributed/device_communicators/base_device_communicator.py`:258; signals: hang; excerpt: "I think this is fine. I made the same change in one of my PRs" (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301197859)
- `2025-08-26T14:36:36Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:203; signals: moe; excerpt: "The layer should have torch.nn.Module type." (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301214827)
- `2025-08-26T14:36:54Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:224; signals: moe; excerpt: "ditto" (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301215941)
- `2025-08-26T14:37:01Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:277; signals: moe; excerpt: "ditto" (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301216287)
- `2025-08-26T16:26:43Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:16; signals: moe; excerpt: "done" (https://github.com/vllm-project/vllm/pull/23608#discussion_r2301525814)
