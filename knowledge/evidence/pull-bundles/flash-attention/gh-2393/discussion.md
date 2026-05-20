# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2393](https://github.com/Dao-AILab/flash-attention/pull/2393)
- Source page: `sources/prs/flash-attention/PR-2393.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2393`
- Generated at: `2026-05-20T15:16:56.087120+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T19:53:04Z`
- Merged: `2026-04-02T01:41:39Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 28 (approved=1, commented=27)
- Inline review comments: 27
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=12, outdated=8
- Human participants with discussion text: Johnsonms, drisspg
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-31T01:50:32Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4034157032)
- `2026-03-31T19:44:14Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4039697584)
- `2026-03-31T23:54:40Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040896408)
- `2026-03-31T23:55:11Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040898372)
- `2026-03-31T23:59:04Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040913621)
- `2026-04-01T00:00:38Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040920070)
- `2026-04-01T00:01:23Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040923297)
- `2026-04-01T00:05:40Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040937168)
- `2026-04-01T00:06:34Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040939927)
- `2026-04-01T00:15:37Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4040969854)
- `2026-04-01T04:50:25Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041655121)
- `2026-04-01T04:51:24Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041659383)
- `2026-04-01T04:53:12Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041664758)
- `2026-04-01T04:55:29Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041671651)
- `2026-04-01T05:05:37Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041696185)
- `2026-04-01T05:09:58Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041706702)
- `2026-04-01T05:23:34Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041744122)
- `2026-04-01T05:30:24Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4041765348)
- `2026-04-01T22:07:52Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4047349511)
- `2026-04-01T22:52:45Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4047500695)
- `2026-04-01T22:53:58Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4047504053)
- `2026-04-01T22:54:16Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4047504885)
- `2026-04-01T22:56:23Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4047510770)
- `2026-04-01T23:42:37Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2393#pullrequestreview-4047639005)
- ... 4 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tools/ci/run_fa4_ci.py`: 9 inline comment(s)
- `.github/workflows/ci.yml`: 6 inline comment(s)
- `AI/CI_SETUP.md`: 4 inline comment(s)
- `tools/ci/docker/Dockerfile`: 4 inline comment(s)
- `flash_attn/cute/cache_utils.py`: 2 inline comment(s)
- `tools/ci/build_sif.sh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-01T05:09:58Z` `inline` by `Johnsonms` `tools/ci/docker/Dockerfile`:20; signals: b200, cuda, sm100; excerpt: "This is intentional — CUDA 13.0 (cu130) isn't available in a stable PyTorch release yet, so nightly is currently the only option for B200/SM100 ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3019799023)
- `2026-04-01T23:42:37Z` `inline` by `Johnsonms` `.github/workflows/ci.yml`:13; signals: b200, compile, kernel; excerpt: "Yes—this is just a smoke test for the initial CI bring-up: a single case(for faster test) to verify that the kernel compiles and runs ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3025185006)
- `2026-04-01T22:54:16Z` `inline` by `drisspg` `flash_attn/cute/cache_utils.py`:35; signals: cache, cute, hang; excerpt: "can oyu rebase I just changed this" (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3025050019)
- `2026-03-31T01:50:32Z` `inline` by `drisspg` `AI/CI_SETUP.md`:36; signals: correctness, perf; excerpt: "There is unfortunately a large delta in perf (depending on cases) between the 12.9. I dont think this effects correctness in any way fwiw ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3013016436)
- `2026-03-31T19:44:14Z` `inline` by `Johnsonms` `AI/CI_SETUP.md`:36; signals: b200, cuda; excerpt: "Thanks for the note! The target CI machine is running driver 575.57 with CUDA 13.0 (B200) after upgrading last Friday, so we can upgrade ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3017970915)
- `2026-04-01T00:06:34Z` `inline` by `drisspg` `.github/workflows/ci.yml`:8; signals: perf, performance; excerpt: "can pin FA4 IMAGE by full image digest, e.g. togethercomputer/training-performance@sha256:..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3019062503)
- `2026-04-01T23:53:46Z` `inline` by `Johnsonms` `flash_attn/cute/cache_utils.py`:35; signals: cache, cute; excerpt: "Done. Thanks @drisspg" (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3025211708)
- `2026-04-01T05:30:24Z` `inline` by `Johnsonms` `tools/ci/run_fa4_ci.py`:88; signals: benchmark; excerpt: "Not easily right now — the benchmark script only outputs a human-readable ASCII table. I'd like to add --json output to benchmark attn.py and ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3019854708)
- `2026-04-01T22:53:58Z` `inline` by `drisspg` `AI/CI_SETUP.md`:2; signals: hang; excerpt: "nit I think this has deviated a little bit from source of ruth; Also do we think its helpful to have, amybe just trim ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3025049243)
- `2026-04-01T22:56:23Z` `inline` by `drisspg` `tools/ci/build_sif.sh`:36; signals: cache; excerpt: "I dont know too much about apptainer, but 1 other thing is that since we are using hosted runner I imagine that the cache ..." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3025056198)
- `2026-04-01T04:53:12Z` `inline` by `Johnsonms` `tools/ci/run_fa4_ci.py`:149; signals: correctness; excerpt: "Fixed in run fa4 ci.py. Was a real correctness issue if paths ever contain spaces." (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3019756304)
- `2026-04-01T00:00:38Z` `inline` by `drisspg` `tools/ci/run_fa4_ci.py`:76; signals: general review; excerpt: "do we even need two modes? this file is only expected to run in apptainer right? maybe this was for testing" (https://github.com/Dao-AILab/flash-attention/pull/2393#discussion_r3019048299)
