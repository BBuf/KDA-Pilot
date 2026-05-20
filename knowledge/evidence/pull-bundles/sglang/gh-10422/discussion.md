# PR Discussion Digest

- Source PR: [sgl-project/sglang#10422](https://github.com/sgl-project/sglang/pull/10422)
- Source page: `sources/prs/sglang/PR-10422.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10422`
- Generated at: `2026-05-20T15:27:18.324706+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-14T10:25:11Z`
- Merged: `2025-10-02T10:04:36Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (commented=6)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=1
- Human participants with discussion text: ch-wan, fzyzcjy
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-14T10:25:36Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @fzyzcjy, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3221975152)
- `2025-09-14T10:33:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for single-batch overlap to improve performance, primarily for MoE layers using ... (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3221978546)
- `2025-09-15T02:46:28Z` `COMMENTED` by `ch-wan` - server arguments.md needs to be updated. Also, a new CI test is needed to cover this new feature. ... (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3222747190)
- `2025-09-15T06:56:42Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3223151472)
- `2025-09-15T06:57:38Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3223153970)
- `2025-09-15T06:59:32Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3223159443)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`: 2 inline comment(s)
- `python/sglang/srt/managers/schedule_batch.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-15T07:19:44Z` `issue` by `fzyzcjy`; signals: accuracy, fp4, nvfp4, speedup; excerpt: "tested just now using latest code, I can confirm this has both correct accuracy and correct speedup on nvfp4 code path" (https://github.com/sgl-project/sglang/pull/10422#issuecomment-3290803764)
- `2025-09-15T02:37:36Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`:181; signals: cute, flashinfer, moe; excerpt: "Can we make the code cleaner? Also, is it needed to add assertion like down sm count is None == down signals is None?" (https://github.com/sgl-project/sglang/pull/10422#discussion_r2347767615)
- `2025-09-15T06:57:38Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`:181; signals: cute, flashinfer, moe; excerpt: "we cannot do it now to allow old flashinfer release, but can do that in the future when flashinfer releases new versions and we ..." (https://github.com/sgl-project/sglang/pull/10422#discussion_r2348043959)
- `2025-09-15T02:42:35Z` `inline` by `ch-wan` `python/sglang/srt/managers/schedule_batch.py`:91; signals: moe; excerpt: "Abuse of GLOBAL SERVER ARGS KEYS is likely to incur circular import. We can add IS SBO ENABLED in srt/layers/moe/utils.py." (https://github.com/sgl-project/sglang/pull/10422#discussion_r2347770979)
- `2025-09-23T02:24:28Z` `issue` by `fzyzcjy`; signals: b200, cuda; excerpt: "excluding the b200 which is known to have issues, cuda ci is green now" (https://github.com/sgl-project/sglang/pull/10422#issuecomment-3322140168)
- `2025-09-15T02:31:32Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`:317; signals: moe; excerpt: "quotes are not needed here" (https://github.com/sgl-project/sglang/pull/10422#discussion_r2347763090)
- `2025-09-15T02:46:28Z` `review` `COMMENTED` by `ch-wan`; signals: general review; excerpt: "server arguments.md needs to be updated. Also, a new CI test is needed to cover this new feature. I guess we cannot merge this ..." (https://github.com/sgl-project/sglang/pull/10422#pullrequestreview-3222747190)
- `2025-09-15T06:56:42Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`:317; signals: moe; excerpt: "it is if TYPE CHECKING" (https://github.com/sgl-project/sglang/pull/10422#discussion_r2348042274)
- `2025-09-15T06:59:32Z` `inline` by `fzyzcjy` `python/sglang/srt/managers/schedule_batch.py`:91; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/10422#discussion_r2348047594)
