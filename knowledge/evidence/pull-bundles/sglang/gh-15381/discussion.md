# PR Discussion Digest

- Source PR: [sgl-project/sglang#15381](https://github.com/sgl-project/sglang/pull/15381)
- Source page: `sources/prs/sglang/PR-15381.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15381`
- Generated at: `2026-05-20T15:28:11.125570+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-18T07:15:11Z`
- Merged: `2026-01-26T12:42:38Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 20 (approved=2, commented=17, dismissed=1)
- Inline review comments: 26
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=13, outdated=12
- Human participants with discussion text: Alcanderian, ZhengdQin, iforgetmyname, lawtherWu, ping1jing2
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-18T15:17:59Z` `DISMISSED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3593529525)
- `2025-12-19T07:02:31Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3597210844)
- `2025-12-19T07:02:39Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3597211452)
- `2025-12-31T05:26:00Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3611806447)
- `2026-01-04T02:44:04Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3624639499)
- `2026-01-04T02:45:54Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3624639903)
- `2026-01-04T02:46:30Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3624640043)
- `2026-01-04T02:48:33Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3624640526)
- `2026-01-09T03:31:33Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3641909448)
- `2026-01-09T08:29:55Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3642890590)
- `2026-01-09T08:32:07Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3642897847)
- `2026-01-09T08:34:42Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3642906238)
- `2026-01-14T08:29:26Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3659470688)
- `2026-01-14T09:25:17Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3659702059)
- `2026-01-14T09:25:24Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3659702640)
- `2026-01-14T09:25:30Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3659703112)
- `2026-01-14T09:41:07Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3659778452)
- `2026-01-14T09:48:09Z` `COMMENTED` by `lawtherWu` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3659809055)
- `2026-01-15T07:24:11Z` `APPROVED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3664244794)
- `2026-01-26T12:29:56Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/15381#pullrequestreview-3705826675)

## Inline Comment Hotspots

- `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`: 8 inline comment(s)
- `python/sglang/srt/layers/linear.py`: 6 inline comment(s)
- `python/sglang/srt/layers/quantization/unquant.py`: 4 inline comment(s)
- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 4 inline comment(s)
- `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`: 2 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-09T03:31:17Z` `inline` by `iforgetmyname` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:15; signals: attention, hang, mla, perf, performance; excerpt: "this postprocess looks great but introducing q lora rank as input is hardly acceptable, i think of two ways to avoid changing interface: 1. ..." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2674698212)
- `2025-12-25T03:51:16Z` `inline` by `ping1jing2` `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`:615; signals: attention, cache, kv cache, mla; excerpt: "\ MLAPO and MLAPROLOG do save kv cache" (https://github.com/sgl-project/sglang/pull/15381#discussion_r2646503146)
- `2026-01-04T02:46:30Z` `inline` by `lawtherWu` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:476; signals: attention, cache, mla; excerpt: "In the elif branch, the custom mlaprolog operator fuses all preparatory computations prior to the MLA. In the else branch, npu kv rmsnorm rope ..." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2659279317)
- `2025-12-31T03:44:36Z` `inline` by `ping1jing2` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:470; signals: attention, mla; excerpt: "14424 we will support different frameworks such as gptq/awq, so please ensure this condition can work properly in this scenario?" (https://github.com/sgl-project/sglang/pull/15381#discussion_r2654754482)
- `2026-01-04T02:45:54Z` `inline` by `lawtherWu` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:470; signals: attention, mla; excerpt: "Thank you for your review comments. Line 465 indicates that NPUFusedMLAPreprocess.forward() is exclusively triggered for modelslim quantization frameworks. We revised the conditional judgment to ..." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2659279180)
- `2025-12-31T03:48:42Z` `inline` by `ping1jing2` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:476; signals: attention, mla; excerpt: "what's the difference between elif and else? and do we need else branch now?" (https://github.com/sgl-project/sglang/pull/15381#discussion_r2654757459)
- `2026-01-09T01:19:40Z` `inline` by `iforgetmyname` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:115; signals: attention, mla; excerpt: "suggest: keep the naming convention for better readability" (https://github.com/sgl-project/sglang/pull/15381#discussion_r2674458705)
- `2026-01-09T08:29:55Z` `inline` by `lawtherWu` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:115; signals: attention, mla; excerpt: "done" (https://github.com/sgl-project/sglang/pull/15381#discussion_r2675296410)
- `2026-01-09T08:34:42Z` `inline` by `lawtherWu` `python/sglang/srt/hardware_backend/npu/attention/mla_preprocess.py`:15; signals: attention, mla; excerpt: "I have modified it according to the first way." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2675308751)
- `2026-01-04T02:48:33Z` `inline` by `lawtherWu` `python/sglang/srt/models/deepseek_v2.py`:1334; signals: mla; excerpt: "Thank you for your review comments. The mlaprolog operator’s input parameters comprise the q a proj and kv a proj weights, while the q ..." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2659280100)
- `2026-01-09T01:56:34Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/linear.py`:269; signals: hang; excerpt: "this is not a good modification imo it needs to change all apply methods for all quantizations, not only unquant and linear method npu, ..." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2674541378)
- `2026-01-14T08:28:37Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/linear.py`:259; signals: hang; excerpt: "follows above change, (q lora, dynamic scale) will pass in as x here and there's on more accesses/changes towards x but only pass it ..." (https://github.com/sgl-project/sglang/pull/15381#discussion_r2689459158)
