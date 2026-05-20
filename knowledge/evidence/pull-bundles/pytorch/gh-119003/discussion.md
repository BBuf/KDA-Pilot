# PR Discussion Digest

- Source PR: [pytorch/pytorch#119003](https://github.com/pytorch/pytorch/pull/119003)
- Source page: `sources/prs/pytorch/PR-119003.md`
- Evidence bundle: `evidence/pull-bundles/pytorch/gh-119003`
- Generated at: `2026-05-20T15:26:53.243518+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-02-02T14:13:53Z`
- Merged: `2024-02-07T16:05:47Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 9 (approved=1, changes_requested=1, commented=7)
- Inline review comments: 10
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: jansel, kadeng
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2024-02-04T18:07:01Z` `CHANGES_REQUESTED` by `jansel` - Add tests (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1861534355)
- `2024-02-05T12:45:54Z` `COMMENTED` by `kadeng` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1862683279)
- `2024-02-05T13:16:09Z` `COMMENTED` by `kadeng` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1862765916)
- `2024-02-05T13:29:38Z` `COMMENTED` by `kadeng` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1862804441)
- `2024-02-05T20:41:09Z` `COMMENTED` by `kadeng` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1863775964)
- `2024-02-05T21:14:25Z` `COMMENTED` by `jansel` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1863822561)
- `2024-02-06T10:24:11Z` `COMMENTED` by `kadeng` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1864781733)
- `2024-02-06T10:32:07Z` `COMMENTED` by `kadeng` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1864798313)
- `2024-02-06T16:52:41Z` `APPROVED` by `jansel` (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1865851141)

## Inline Comment Hotspots

- `torch/_inductor/config.py`: 5 inline comment(s)
- `torch/_inductor/codecache.py`: 3 inline comment(s)
- `torch/_inductor/select_algorithm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2024-02-05T13:16:09Z` `inline` by `kadeng` `torch/_inductor/select_algorithm.py`:788; signals: compile, deadlock, perf, performance, race; excerpt: "Several reasons: 1.) Threads are relatively lightweight to construct but (a bit) costly to keep alive, so there's no real benefit but a downside ..." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1478231430)
- `2024-02-05T15:34:09Z` `issue` by `kadeng`; signals: autotune, compile, perf, performance; excerpt: "Add tests Add tests This is actually on the default codepath for all unit tests that involve max autotune. So while there were no ..." (https://github.com/pytorch/pytorch/pull/119003#issuecomment-1927271034)
- `2024-02-04T18:03:55Z` `inline` by `jansel` `torch/_inductor/codecache.py`:295; signals: cache, compile; excerpt: "This comment seems important. I think we do want consistent numbers from the same machine. If you mix old numbers with new numbers it ..." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1477414838)
- `2024-02-05T12:45:54Z` `inline` by `kadeng` `torch/_inductor/codecache.py`:295; signals: cache, hang; excerpt: "I will change that back if you like. It will literally mean that we run the same code again on the same machine, just ..." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1478174017)
- `2024-02-04T18:06:55Z` `inline` by `jansel` `torch/_inductor/select_algorithm.py`:788; signals: compile; excerpt: "Why not reuse the same threadpool and infra for parallel compiles? This seems like it is doing the same thing as async compile..." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1477415280)
- `2024-02-05T13:29:38Z` `inline` by `kadeng` `torch/_inductor/config.py`:210; signals: hang; excerpt: "Yes, negative values are allowed, in that case we simply don't have parallel precompilation. The idea is to leave at least 8 CPUs unused ..." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1478253311)
- `2024-02-05T20:41:09Z` `inline` by `kadeng` `torch/_inductor/codecache.py`:295; signals: cache; excerpt: "done" (https://github.com/pytorch/pytorch/pull/119003#discussion_r1478887020)
- `2024-02-04T18:07:01Z` `review` `CHANGES_REQUESTED` by `jansel`; signals: general review; excerpt: "Add tests" (https://github.com/pytorch/pytorch/pull/119003#pullrequestreview-1861534355)
- `2024-02-06T10:24:11Z` `inline` by `kadeng` `torch/_inductor/config.py`:210; signals: general review; excerpt: "The idea is to leave 8 CPUs unused under the assumption that these are required for whatever else is happening on the system. But ..." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1479539581)
- `2024-02-04T18:05:46Z` `inline` by `jansel` `torch/_inductor/config.py`:210; signals: general review; excerpt: "Why -8? This could be negative on some machines." (https://github.com/pytorch/pytorch/pull/119003#discussion_r1477415114)
- `2024-02-05T21:14:25Z` `inline` by `jansel` `torch/_inductor/config.py`:210; signals: general review; excerpt: "Why not use just use torch.get num threads()?" (https://github.com/pytorch/pytorch/pull/119003#discussion_r1478915854)
- `2024-02-06T10:32:06Z` `inline` by `kadeng` `torch/_inductor/config.py`:210; signals: general review; excerpt: "done" (https://github.com/pytorch/pytorch/pull/119003#discussion_r1479550013)
