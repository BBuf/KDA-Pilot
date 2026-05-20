# PR Discussion Digest

- Source PR: [Dao-AILab/quack#118](https://github.com/Dao-AILab/quack/pull/118)
- Source page: `sources/prs/quack/PR-118.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-118`
- Generated at: `2026-05-20T15:17:15.363226+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-23T17:25:28Z`
- Merged: `2026-04-25T17:04:51Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 21 (approved=1, commented=20)
- Inline review comments: 20
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=13, outdated=13
- Human participants with discussion text: alecco, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T10:49:32Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169878840)
- `2026-04-24T10:49:55Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169880523)
- `2026-04-24T10:50:09Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169881635)
- `2026-04-24T10:50:42Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169884189)
- `2026-04-24T10:50:51Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169884925)
- `2026-04-24T10:51:15Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169886738)
- `2026-04-24T10:51:23Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169887351)
- `2026-04-24T10:51:56Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169889822)
- `2026-04-24T10:52:36Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169892969)
- `2026-04-24T10:53:16Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169895999)
- `2026-04-24T10:54:03Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4169900097)
- `2026-04-24T12:46:35Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4170519337)
- `2026-04-24T12:55:07Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4170568372)
- `2026-04-24T12:58:38Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4170589876)
- `2026-04-24T13:39:37Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4170875325)
- `2026-04-24T13:39:46Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4170876485)
- `2026-04-25T16:00:53Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4175818757)
- `2026-04-25T16:01:17Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4175819068)
- `2026-04-25T16:20:34Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4175835093)
- `2026-04-25T16:30:35Z` `COMMENTED` by `alecco` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4175847375)
- `2026-04-25T17:04:12Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/118#pullrequestreview-4175895002)

## Inline Comment Hotspots

- `quack/gemm_interface.py`: 9 inline comment(s)
- `quack/linear.py`: 4 inline comment(s)
- `quack/gemm_config.py`: 2 inline comment(s)
- `quack/gemm_sm120.py`: 2 inline comment(s)
- `benchmarks/benchmark_sm120_gemm_epilogues.py`: 2 inline comment(s)
- `README.md`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-24T08:24:01Z` `issue` by `tridao`; signals: compile, epilogue, gemm, sm120, tile, warp; excerpt: "keep SM120 heavy epilogues within the 99 KB SMEM budget using resource-aware config selection Is there evidence for this? Does it actually go out ..." (https://github.com/Dao-AILab/quack/pull/118#issuecomment-4311726413)
- `2026-04-24T08:29:02Z` `issue` by `alecco`; signals: compile, epilogue, sm120, tile, warp; excerpt: "keep SM120 heavy epilogues within the 99 KB SMEM budget using resource-aware config selection Is there evidence for this? Does it actually go out ..." (https://github.com/Dao-AILab/quack/pull/118#issuecomment-4311753263)
- `2026-04-24T10:54:03Z` `inline` by `tridao` `benchmarks/benchmark_sm120_gemm_epilogues.py`:2; signals: benchmark, epilogue, gemm, sm120; excerpt: "this file isn't specific to sm120?" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137206021)
- `2026-04-24T12:58:38Z` `inline` by `alecco` `benchmarks/benchmark_sm120_gemm_epilogues.py`:2; signals: benchmark, epilogue, gemm, sm120; excerpt: "Indeed. Will rename and reword it." (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137831745)
- `2026-04-25T16:55:38Z` `issue` by `alecco`; signals: compile, gemm, hang, sm120; excerpt: "1. Removed commit "Fix torch.compile ops dispatch in linear wrappers" So quack/linear.py is back to how it was before. 2. Removed quack/gemm interface.py get ..." (https://github.com/Dao-AILab/quack/pull/118#issuecomment-4320113885)
- `2026-04-24T10:50:42Z` `inline` by `tridao` `quack/gemm_interface.py`:1742; signals: correctness, gemm, perf; excerpt: "pruning isn't for perf, it's for correctness" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137190728)
- `2026-04-24T10:53:16Z` `inline` by `tridao` `README.md`:34; signals: blackwell, sm100, sm120; excerpt: "I would separate out Blackwell and Blackwell Geforce (sm120, which is quite different from Sm100)" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137202215)
- `2026-04-24T10:49:55Z` `inline` by `tridao` `quack/gemm_interface.py`:304; signals: gemm, hang; excerpt: "why change the default?" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137187177)
- `2026-04-24T10:50:09Z` `inline` by `tridao` `quack/gemm_interface.py`:374; signals: gemm, hang; excerpt: "why change the default?" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137188275)
- `2026-04-24T10:50:52Z` `inline` by `tridao` `quack/gemm_interface.py`:1777; signals: gemm, hang; excerpt: "why change the default?" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137191407)
- `2026-04-24T10:51:15Z` `inline` by `tridao` `quack/gemm_interface.py`:1954; signals: gemm, perf; excerpt: "pruning isn't for perf. That's what autotuning is for" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137193169)
- `2026-04-24T10:51:23Z` `inline` by `tridao` `quack/gemm_interface.py`:2006; signals: gemm, hang; excerpt: "why change the default?" (https://github.com/Dao-AILab/quack/pull/118#discussion_r3137193864)
