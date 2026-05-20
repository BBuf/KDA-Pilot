# PR Discussion Digest

- Source PR: [sgl-project/sglang#19089](https://github.com/sgl-project/sglang/pull/19089)
- Source page: `sources/prs/sglang/PR-19089.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19089`
- Generated at: `2026-05-20T15:28:45.380073+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-20T22:28:49Z`
- Merged: `2026-03-28T22:55:49Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: Fridge003, hlu1
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-20T22:31:16Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for skip-softmax attention by adding two new environment variables for prefill ... (https://github.com/sgl-project/sglang/pull/19089#pullrequestreview-3834483603)
- `2026-03-09T06:14:31Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19089#pullrequestreview-3912778462)
- `2026-03-10T18:00:42Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19089#pullrequestreview-3924375934)
- `2026-03-23T20:42:51Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19089#pullrequestreview-3994578991)

## Inline Comment Hotspots

- `python/sglang/srt/environ.py`: 2 inline comment(s)
- `python/sglang/benchmark/datasets/longbench_v2.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/nsa_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-09T04:13:18Z` `inline` by `Fridge003` `python/sglang/srt/environ.py`:346; signals: attention, tma; excerpt: "Just for checking, setting None here means disabling skip softmax attention?" (https://github.com/sgl-project/sglang/pull/19089#discussion_r2903099687)
- `2026-02-24T20:33:03Z` `issue` by `hlu1`; signals: benchmark, perf; excerpt: "Using longbench for perf benchmark isn't reliable because the number of output tokens varies from run to run. It's better to do standard perf ..." (https://github.com/sgl-project/sglang/pull/19089#issuecomment-3954566301)
- `2026-03-09T05:58:54Z` `issue` by `Fridge003`; signals: accuracy, hang; excerpt: "Please post the accuracy results on longbench-v2 as the sparsity changes, and probably draw curves (similar to those in [trtllm]( if time permits" (https://github.com/sgl-project/sglang/pull/19089#issuecomment-4021351079)
- `2026-03-09T05:58:01Z` `inline` by `Fridge003` `python/sglang/benchmark/datasets/longbench_v2.py`:1; signals: benchmark; excerpt: "Agree with maybe we don't need the longbench benchmark?" (https://github.com/sgl-project/sglang/pull/19089#discussion_r2903370501)
- `2026-03-10T18:00:42Z` `inline` by `Fridge003` `python/sglang/benchmark/datasets/longbench_v2.py`:1; signals: benchmark; excerpt: "Oh I misunderstood, can close this right now" (https://github.com/sgl-project/sglang/pull/19089#discussion_r2913520175)
- `2026-03-09T06:14:27Z` `inline` by `Fridge003` `python/sglang/srt/environ.py`:341; signals: general review; excerpt: "Please also update document docs/references/environment variables.md" (https://github.com/sgl-project/sglang/pull/19089#discussion_r2903416419)
