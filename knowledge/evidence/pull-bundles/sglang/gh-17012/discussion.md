# PR Discussion Digest

- Source PR: [sgl-project/sglang#17012](https://github.com/sgl-project/sglang/pull/17012)
- Source page: `sources/prs/sglang/PR-17012.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17012`
- Generated at: `2026-05-20T15:28:25.284365+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-13T07:53:21Z`
- Merged: `2026-01-29T03:07:35Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 10 (approved=1, changes_requested=1, commented=8)
- Inline review comments: 21
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=13, outdated=5
- Human participants with discussion text: Duyi-Wang, HaiShaw, billishyahao, kkHuang-amd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-14T06:48:25Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3659118625)
- `2026-01-14T23:56:06Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3663345120)
- `2026-01-18T09:10:21Z` `COMMENTED` by `HaiShaw` - Consider to: - change Supports FP8 quantization via environment variable to server arg. - add performance and accuracy ... (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3675293300)
- `2026-01-19T01:22:46Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3675971931)
- `2026-01-19T01:24:48Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3675974669)
- `2026-01-19T12:09:10Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3677785226)
- `2026-01-20T02:46:30Z` `COMMENTED` by `Duyi-Wang` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3680109809)
- `2026-01-22T02:02:51Z` `COMMENTED` by `billishyahao` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3690236704)
- `2026-01-28T09:14:08Z` `CHANGES_REQUESTED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3715472159)
- `2026-01-28T09:24:39Z` `APPROVED` by `HaiShaw` - LGTM (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3715540564)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`: 9 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 6 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 4 inline comment(s)
- `python/sglang/srt/layers/moe/utils.py`: 1 inline comment(s)
- `docs/references/environment_variables.md`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-18T09:10:21Z` `review` `COMMENTED` by `HaiShaw`; signals: accuracy, fp4, fp8, hang, latency, moe, mxfp4, perf; excerpt: "Consider to: - change Supports FP8 quantization via environment variable to server arg. - add performance and accuracy readings from fp8 dispatch (MxFP4 dispatch ..." (https://github.com/sgl-project/sglang/pull/17012#pullrequestreview-3675293300)
- `2026-01-27T05:22:32Z` `issue` by `kkHuang-amd`; signals: accuracy, fp4, fp8, hang, latency, moe, mxfp4, perf; excerpt: "Consider to: change Supports FP8 quantization via environment variable to server arg. add performance and accuracy readings from fp8 dispatch (MxFP4 dispatch can be ..." (https://github.com/sgl-project/sglang/pull/17012#issuecomment-3803179621)
- `2026-01-18T08:50:40Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:236; signals: accuracy, fp4, moe, mxfp4; excerpt: "MxFP4 dispatch can be experimental, with accuracy study needed" (https://github.com/sgl-project/sglang/pull/17012#discussion_r2702233574)
- `2026-01-22T02:02:51Z` `inline` by `billishyahao` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:236; signals: fp4, moe, mxfp4; excerpt: "MXFP4 dispatch feature is on the MoRI roadmap but have not been supported" (https://github.com/sgl-project/sglang/pull/17012#discussion_r2715031660)
- `2026-01-19T01:22:46Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/moe/ep_moe/layer.py`:682; signals: latency, moe; excerpt: "In this commit, mori-ep does not still support low latency mode. The low latency mode will be enabled in TBO run" (https://github.com/sgl-project/sglang/pull/17012#discussion_r2702950642)
- `2026-01-14T23:56:06Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:114; signals: fp8, moe; excerpt: "The //128 is for FP8 DISPATCH function." (https://github.com/sgl-project/sglang/pull/17012#discussion_r2692478350)
- `2026-01-18T08:00:47Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/ep_moe/layer.py`:682; signals: latency, moe; excerpt: "low latency support?" (https://github.com/sgl-project/sglang/pull/17012#discussion_r2702205285)
- `2026-01-18T08:47:13Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:110; signals: moe; excerpt: "the hardcoded numbers below good/tuned for diff chips? coding wise, please define a group of symbols." (https://github.com/sgl-project/sglang/pull/17012#discussion_r2702231337)
- `2026-01-18T09:00:07Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:367; signals: moe; excerpt: "It is unclear to use DeepEPMode here, if MoriEP is meant to be orthogonal to DeepEP; otherwise migrate MoriEP to a backend to DeepEP." (https://github.com/sgl-project/sglang/pull/17012#discussion_r2702239263)
- `2026-01-19T12:09:10Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:367; signals: moe; excerpt: "DeepEPMode is used to decide what behavior of dispatch and combine should be used. Like other dispatch backend " also follow this definition to ..." (https://github.com/sgl-project/sglang/pull/17012#discussion_r2704503586)
- `2026-01-14T06:48:25Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`:114; signals: moe; excerpt: "sync it with "//128"" (https://github.com/sgl-project/sglang/pull/17012#discussion_r2689168543)
- `2026-01-18T07:14:31Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/ep_moe/layer.py`:590; signals: moe; excerpt: "Minimize global variable check, pass it in" (https://github.com/sgl-project/sglang/pull/17012#discussion_r2702181812)
