# PR Discussion Digest

- Source PR: [vllm-project/vllm#16859](https://github.com/vllm-project/vllm/pull/16859)
- Source page: `sources/prs/vllm/PR-16859.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16859`
- Generated at: `2026-05-20T15:35:02.457271+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-18T16:55:05Z`
- Merged: `2025-04-30T02:08:04Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 16
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=3, outdated=5
- Human participants with discussion text: DogeFlow, cliffwoolley, drisspg, huydhn, jessiewiswjc, mergify, mgoin, simon-mo, vadimkantorov, zhanglianjie-163, zou3519
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 9

## Review Decisions

- `2025-04-23T17:27:33Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2788189103)
- `2025-04-23T17:28:07Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2788190446)
- `2025-04-25T10:11:03Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2793649919)
- `2025-04-26T00:30:45Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2795564541)
- `2025-04-26T00:52:21Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2795596011)
- `2025-04-26T02:00:38Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2795647990)
- `2025-04-26T04:09:40Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2795729547)
- `2025-04-26T15:39:18Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2792257509)
- `2025-04-26T18:30:35Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2796336987)
- `2025-04-26T18:31:51Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2796337192)
- `2025-04-30T01:00:26Z` `COMMENTED` by `cliffwoolley` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2805471804)
- `2025-04-30T01:05:09Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2805476640)
- `2025-04-30T02:07:56Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/16859#pullrequestreview-2805535396)

## Inline Comment Hotspots

- `docker/Dockerfile`: 11 inline comment(s)
- `examples/online_serving/chart-helm/values.yaml`: 3 inline comment(s)
- `requirements/cuda.txt`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-23T17:27:32Z` `inline` by `drisspg` `docker/Dockerfile`:83; signals: blackwell, ptx, sm100; excerpt: "for blackwell support we will wnat to add sm100 here, although the +PTX should handle this.." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2056561373)
- `2025-04-26T18:30:35Z` `inline` by `huydhn` `docker/Dockerfile`:239; signals: cuda, hang; excerpt: "Yeah, you're right, this needs to change depending on CUDA VERSION, let me add that check to cover 11.8, 12.6, and 12.8 matching those ..." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061536268)
- `2025-04-26T15:38:08Z` `inline` by `mgoin` `docker/Dockerfile`:239; signals: cuda, hang; excerpt: "It seems like this should changed based on CUDA VERSION, as this won't work for CUDA VERSION=12.6" (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061405908)
- `2025-04-26T00:29:46Z` `inline` by `simon-mo` `docker/Dockerfile`:233; signals: compile; excerpt: "How long does this take to compile xformers? If it's too long I don't want to slow down our CI time for this." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061060613)
- `2025-04-26T00:52:21Z` `inline` by `huydhn` `docker/Dockerfile`:233; signals: cache; excerpt: "Let me dig out the number for this once the build finish. Without caching, it would be significant from what I see locally, but ..." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061084367)
- `2025-04-26T02:00:37Z` `inline` by `huydhn` `examples/online_serving/chart-helm/values.yaml`:11; signals: dtype; excerpt: "This is a curious issue that I have seen on CI where cpu build fails on that dtype. I look around and see a ..." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061112929)
- `2025-04-26T04:09:40Z` `inline` by `huydhn` `examples/online_serving/chart-helm/values.yaml`:11; signals: hang; excerpt: "Here is the full server log when serving vllm serve facebook/opt-125m on the CPU docker image The change you see here is only to ..." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061149936)
- `2025-04-30T01:00:26Z` `inline` by `cliffwoolley` `docker/Dockerfile`:83; signals: ptx; excerpt: "Yes 10.0 as well as 12.0. +PTX is not enough. (Same comment in the several places this sequence appears.) cc @kushanam" (https://github.com/vllm-project/vllm/pull/16859#discussion_r2067693346)
- `2025-04-30T01:05:09Z` `inline` by `huydhn` `docker/Dockerfile`:83; signals: hang; excerpt: "As the size of this PR is relative big already and its signals are ready, let me add this change to a subsequent PR. ..." (https://github.com/vllm-project/vllm/pull/16859#discussion_r2067696546)
- `2025-04-26T15:39:09Z` `inline` by `mgoin` `requirements/cuda.txt`:9; signals: cuda; excerpt: "ditto on hardcoding cu128 here" (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061406076)
- `2025-04-26T18:31:50Z` `inline` by `huydhn` `requirements/cuda.txt`:9; signals: cuda; excerpt: "I'll move the check to the Dockerfile to match the CUDA VERSION there" (https://github.com/vllm-project/vllm/pull/16859#discussion_r2061536453)
- `2025-04-27T17:12:35Z` `issue` by `huydhn`; signals: compile; excerpt: "@youkaichao @zou3519 I think some of the failed tests are pointing to a real torch.compile compatibility issue with 2.7.0 I can reproduce it with ..." (https://github.com/vllm-project/vllm/pull/16859#issuecomment-2833553764)
