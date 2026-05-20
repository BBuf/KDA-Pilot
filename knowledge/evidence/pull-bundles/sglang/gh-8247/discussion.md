# PR Discussion Digest

- Source PR: [sgl-project/sglang#8247](https://github.com/sgl-project/sglang/pull/8247)
- Source page: `sources/prs/sglang/PR-8247.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8247`
- Generated at: `2026-05-20T15:31:23.667572+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-22T06:39:02Z`
- Merged: `2025-10-15T03:10:53Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 23 (approved=1, commented=22)
- Inline review comments: 31
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=20, outdated=19
- Human participants with discussion text: ayrnb, ch-wan, fzyzcjy, whybeyoung, yangsijia-celina
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-22T06:39:28Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ayrnb, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3041371697)
- `2025-07-22T06:41:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for w4a8 quantization in the DeepEP MoE layer, which is a ... (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3041376663)
- `2025-07-24T12:11:33Z` `COMMENTED` by `fzyzcjy` - not fully checked, only glance very quickly and there is a tiny nit (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3051395403)
- `2025-07-25T01:51:59Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3053855819)
- `2025-07-31T14:24:16Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3075657982)
- `2025-08-01T15:44:14Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3079714106)
- `2025-08-04T01:53:43Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3082491918)
- `2025-08-08T06:47:30Z` `COMMENTED` by `yangsijia-celina` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3099655266)
- `2025-08-17T14:17:10Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3126356374)
- `2025-08-18T02:39:41Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3126633594)
- `2025-08-18T02:43:25Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3126636985)
- `2025-08-18T02:45:07Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3126638534)
- `2025-08-21T09:41:16Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3139884227)
- `2025-08-21T09:42:34Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3139889721)
- `2025-09-05T09:40:52Z` `COMMENTED` by `yangsijia-celina` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3188678185)
- `2025-09-05T09:56:25Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3188720953)
- `2025-10-08T02:30:04Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3312548284)
- `2025-10-08T02:33:19Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3312552143)
- `2025-10-08T02:34:06Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3312553417)
- `2025-10-08T02:36:09Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3312555803)
- `2025-10-13T08:09:43Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3330399975)
- `2025-10-13T08:09:53Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3330400648)
- `2025-10-13T20:07:55Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8247#pullrequestreview-3332919276)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 13 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`: 7 inline comment(s)
- `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`: 7 inline comment(s)
- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 3 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-08T02:36:09Z` `inline` by `ch-wan` `python/sglang/srt/server_args.py`:1644; signals: cutlass, fp8, moe; excerpt: "MoE runner backend should be decoupled with quant methods. We will have --moe-runner-backend cutlass in the future. Check our roadmap: cutlass w4afp8." (https://github.com/sgl-project/sglang/pull/8247#discussion_r2412356627)
- `2025-09-05T09:40:52Z` `inline` by `yangsijia-celina` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:118; signals: cutlass, fp8, moe; excerpt: "seems duplicated local topk ids transfer logic in apply func in w4afp8.py and here?" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2324611068)
- `2025-10-08T02:34:06Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`:407; signals: alignment, cutlass, moe; excerpt: "could you explain why cutlass does not need expert alignment?" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2412354689)
- `2025-08-17T14:13:43Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/ep_moe/layer.py`; signals: hang, moe; excerpt: "we may need to rebase the PR to use @ch-wan's moe refactors (I will review again after the refactor, since that changes a lot)" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2280897518)
- `2025-08-17T14:14:21Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/ep_moe/layer.py`:364; signals: cutlass, moe; excerpt: "wondering whether we should do SGLANG USE W4A8 env var, or make it something like a "moe backend", say, --moe-runner-backend cutlass w4a8" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2280897649)
- `2025-07-31T14:22:57Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:222; signals: cutlass, moe; excerpt: "nit: maybe use elif mode is deepep" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2245551868)
- `2025-08-01T15:44:14Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:222; signals: cutlass, moe; excerpt: "Thx. Since there are some updates in the main branch, I'll also update the code again." (https://github.com/sgl-project/sglang/pull/8247#discussion_r2248299042)
- `2025-08-04T01:53:43Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:222; signals: cutlass, moe; excerpt: "nit: maybe use elif mode is deepep Done!" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2250254217)
- `2025-08-17T14:13:02Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:119; signals: cutlass, moe; excerpt: "would be great to avoid hardcoding a "8" here" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2280897270)
- `2025-08-18T02:43:25Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:119; signals: cutlass, moe; excerpt: "Ok, I will modify it to avoid hardcoding." (https://github.com/sgl-project/sglang/pull/8247#discussion_r2281177975)
- `2025-09-05T09:56:25Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:118; signals: cutlass, moe; excerpt: "done!" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2324643875)
- `2025-07-24T12:11:11Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`:261; signals: moe; excerpt: "nit: get bool env var("SGLANG USE W4A8") or sth like that" (https://github.com/sgl-project/sglang/pull/8247#discussion_r2228338447)
