# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1203](https://github.com/Dao-AILab/flash-attention/pull/1203)
- Source page: `sources/prs/flash-attention/PR-1203.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1203`
- Generated at: `2026-05-20T15:16:29.269179+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-09-04T12:32:16Z`
- Merged: `2024-12-06T01:38:53Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 2 (commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: TerminatorJ, dtrifiro, micmelesse, unclemusclez
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2024-09-12T11:07:29Z` `COMMENTED` by `dtrifiro` (https://github.com/Dao-AILab/flash-attention/pull/1203#pullrequestreview-2299976160)
- `2024-09-13T15:16:49Z` `COMMENTED` by `micmelesse` (https://github.com/Dao-AILab/flash-attention/pull/1203#pullrequestreview-2303414746)

## Inline Comment Hotspots

- `setup.py`: 2 inline comment(s)

## High-Signal Discussion

- `2024-10-30T15:46:07Z` `issue` by `micmelesse`; signals: compile, kernel, triton; excerpt: "will this work with CDNA 1? The kernels work on any architecture supported by the Triton compiler. Right now the Triton compiler does not ..." (https://github.com/Dao-AILab/flash-attention/pull/1203#issuecomment-2447599962)
- `2024-10-30T16:02:00Z` `issue` by `micmelesse`; signals: perf, performance, triton; excerpt: "Hi @tridao Hope you are doing well. I wanted to check if you have any feedback or suggestions regarding this PR. I've refreshed it ..." (https://github.com/Dao-AILab/flash-attention/pull/1203#issuecomment-2447643543)
- `2024-09-12T11:07:29Z` `inline` by `dtrifiro` `setup.py`:64; signals: kernel, triton; excerpt: "If USE TRITON ROCM is true, we can also skip the git submodule update command at line 137, as well as as the os.system ..." (https://github.com/Dao-AILab/flash-attention/pull/1203#discussion_r1756643708)
- `2024-09-13T15:16:49Z` `inline` by `micmelesse` `setup.py`:64; signals: general review; excerpt: "done" (https://github.com/Dao-AILab/flash-attention/pull/1203#discussion_r1759055590)
