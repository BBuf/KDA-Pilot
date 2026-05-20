# PR Discussion Digest

- Source PR: [sgl-project/sglang#10183](https://github.com/sgl-project/sglang/pull/10183)
- Source page: `sources/prs/sglang/PR-10183.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10183`
- Generated at: `2026-05-20T15:27:16.565211+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-08T23:00:33Z`
- Merged: `2025-11-04T08:20:56Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 11 (approved=5, changes_requested=1, commented=5)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: ch-wan, elfiegg, kushanam, pavanimajety, trevor-m, zhyncs
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-08T23:00:52Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @trevor-m, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3198433951)
- `2025-09-08T23:02:45Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new server argument --speculative-moe-runner-backend to allow separate configuration for the Mixture-of-Experts ... (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3198436227)
- `2025-09-15T23:37:39Z` `APPROVED` by `pavanimajety` - LGTM, thanks for the changes (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3226609904)
- `2025-09-16T20:29:25Z` `APPROVED` by `elfiegg` - LGTM (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3231595412)
- `2025-09-16T23:27:30Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3231992210)
- `2025-09-18T18:19:12Z` `APPROVED` by `kushanam` (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3241379567)
- `2025-09-18T21:32:22Z` `CHANGES_REQUESTED` by `ch-wan` - Could update server arguments.md? (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3242170715)
- `2025-09-22T01:49:45Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3250307734)
- `2025-11-02T05:26:03Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3408164871)
- `2025-11-03T21:03:49Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3412923535)
- `2025-11-04T08:18:41Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3414644521)

## Inline Comment Hotspots

- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-10T01:59:13Z` `issue` by `pavanimajety`; signals: accuracy, cutlass, flashinfer, fp8, moe; excerpt: "@trevor-m Could you try different backends for both? Eg: --moe-runner flashinfer trtllm and --speculative-moe-runner-backend cutlass fp8 and get accuracy numbers?" (https://github.com/sgl-project/sglang/pull/10183#issuecomment-3272924208)
- `2025-09-15T21:17:26Z` `issue` by `trevor-m`; signals: cutlass, flashinfer, fp8, moe; excerpt: "@pavanimajety moe-runner=flashinfer trtllm speculative-moe-runner=cutlass fp8 moe-runner=cutlass fp8 speculative-moe-runner=flashinfer trtllm" (https://github.com/sgl-project/sglang/pull/10183#issuecomment-3293987722)
- `2025-11-02T05:26:03Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/utils.py`:58; signals: cutlass, moe; excerpt: "I'm going to merge this PR. Could you use CUTLASS here? I don't think we need a new backend name here." (https://github.com/sgl-project/sglang/pull/10183#discussion_r2484227890)
- `2025-11-03T21:03:49Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/utils.py`:58; signals: moe; excerpt: "Thanks, fixed" (https://github.com/sgl-project/sglang/pull/10183#discussion_r2487847699)
- `2025-09-18T21:32:22Z` `review` `CHANGES_REQUESTED` by `ch-wan`; signals: general review; excerpt: "Could update server arguments.md?" (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3242170715)
- `2025-10-30T22:06:27Z` `issue` by `trevor-m`; signals: accuracy; excerpt: "Thanks @ch-wan After rebasing, seems there is an accuracy issue affecting this model even on the main branch. I will need to bisect that ..." (https://github.com/sgl-project/sglang/pull/10183#issuecomment-3470436263)
- `2025-09-15T23:37:39Z` `review` `APPROVED` by `pavanimajety`; signals: hang; excerpt: "LGTM, thanks for the changes" (https://github.com/sgl-project/sglang/pull/10183#pullrequestreview-3226609904)
- `2025-10-31T21:24:47Z` `issue` by `trevor-m`; signals: accuracy; excerpt: "@ch-wan Can you please take a look? Updated test/accuracy results" (https://github.com/sgl-project/sglang/pull/10183#issuecomment-3474943621)
- `2025-09-16T23:27:30Z` `inline` by `ch-wan` `python/sglang/srt/server_args.py`:2737; signals: general review; excerpt: "server arguments.md is not updated" (https://github.com/sgl-project/sglang/pull/10183#discussion_r2353863938)
