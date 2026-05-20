# PR Discussion Digest

- Source PR: [sgl-project/sglang#3785](https://github.com/sgl-project/sglang/pull/3785)
- Source page: `sources/prs/sglang/PR-3785.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3785`
- Generated at: `2026-05-20T15:30:02.473001+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-22T09:15:49Z`
- Merged: `2025-02-24T12:07:26Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 11 (commented=11)
- Inline review comments: 14
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: Fridge003, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-23T16:25:30Z` `COMMENTED` by `yzh119` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635663935)
- `2025-02-23T19:14:47Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635720799)
- `2025-02-23T22:08:37Z` `COMMENTED` by `yzh119` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635775216)
- `2025-02-23T22:37:47Z` `COMMENTED` by `yzh119` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635792487)
- `2025-02-23T22:58:31Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635804351)
- `2025-02-23T22:58:37Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635804384)
- `2025-02-23T22:58:43Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635804413)
- `2025-02-23T22:59:47Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635806539)
- `2025-02-23T23:00:51Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635807132)
- `2025-02-23T23:45:41Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635824246)
- `2025-02-24T01:21:15Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3785#pullrequestreview-2635876054)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`: 13 inline comment(s)
- `python/sglang/srt/configs/model_config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-23T22:37:47Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:74; signals: attention, correctness, flashinfer, hang, mla; excerpt: "btw, the correctness issue for DeepSeek-V2-Lite-Chat can be resolved by changing the sm scale:" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966913547)
- `2025-02-23T22:59:47Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:74; signals: attention, flashinfer, hang, mla; excerpt: "The former code is tested only on deepseek v3 and used a lot magic numbers like 512 and 128. This PR has changed these ..." (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966921462)
- `2025-02-23T16:25:30Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:492; signals: attention, flashinfer, kernel, mla; excerpt: "It's not required here as we add boundary check inside flashinfer mla kernel." (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966828096)
- `2025-02-23T22:08:04Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:112; signals: attention, flashinfer, hopper, mla; excerpt: "As get merged (in , you can try "auto" which will select FA3 for hopper architecture." (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966904164)
- `2025-02-23T23:00:51Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:74; signals: attention, flashinfer, hang, mla; excerpt: "I'm trying the effect of changing sm scale" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966921732)
- `2025-02-23T23:45:41Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:74; signals: accuracy, attention, flashinfer, mla; excerpt: "@yzh119 Thanks for your hint! The accuracy issue is solved！" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966933474)
- `2025-02-23T22:06:26Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:74; signals: attention, flashinfer, mla; excerpt: "Is there any fundamental reason that we cannot use flashinfer MLA for earlier models? I suppose DeepSeek-V2-Lite-Chat has the same lora rank and rope ..." (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966903641)
- `2025-02-23T19:14:46Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:492; signals: attention, flashinfer, mla; excerpt: "modified" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966860762)
- `2025-02-23T22:08:22Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:121; signals: attention, flashinfer, mla; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966904373)
- `2025-02-23T22:08:28Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:201; signals: attention, flashinfer, mla; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966904426)
- `2025-02-23T22:58:31Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:112; signals: attention, flashinfer, mla; excerpt: "fixed" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966921129)
- `2025-02-23T22:58:37Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:201; signals: attention, flashinfer, mla; excerpt: "fixed" (https://github.com/sgl-project/sglang/pull/3785#discussion_r1966921149)
