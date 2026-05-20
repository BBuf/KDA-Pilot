# PR Discussion Digest

- Source PR: [sgl-project/sglang#10281](https://github.com/sgl-project/sglang/pull/10281)
- Source page: `sources/prs/sglang/PR-10281.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10281`
- Generated at: `2026-05-20T15:27:16.571056+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-10T21:38:34Z`
- Merged: `2025-09-22T22:54:00Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 5 (commented=5)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Fridge003, fzyzcjy, pavanimajety, pranavm-nvidia, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-09-10T21:38:46Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @pranavm-nvidia, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/10281#pullrequestreview-3207925267)
- `2025-09-10T21:40:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables the TRT-LLM backend for the target verify step in multi-token prediction, which ... (https://github.com/sgl-project/sglang/pull/10281#pullrequestreview-3207928734)
- `2025-09-10T23:43:34Z` `COMMENTED` by `fzyzcjy` - hi, could you please run (1) math500 w/ 64k gen 3 times (3) gpqa diamond w/ 32k gen ... (https://github.com/sgl-project/sglang/pull/10281#pullrequestreview-3208188798)
- `2025-09-21T06:36:45Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/10281#pullrequestreview-3249413901)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-09-22T13:24:05Z` `issue` by `fzyzcjy`; signals: b200, cuda, dtype, fp4, fp8; excerpt: "Test command Results (the "strict-match" part in lm-eval) baseline: 946,937,942,939,942,946,943,943,942,943,947,950,942,948,941,945,938,944,936,939 before commit: 89.5,88.8,88.3,88.9,89.5,89.4,89.0 after commit: 94.5,94.1,94.9,94.1,94.5,94.5,945,942,948,949,943,942,948,944 for more subtle checks, I will need to ..." (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3319015408)
- `2025-09-21T06:36:45Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:672; signals: attention, mla; excerpt: "btw curious why we make o sf scale -1.0 while the original one is +1.0" (https://github.com/sgl-project/sglang/pull/10281#discussion_r2365972715)
- `2025-09-22T13:53:25Z` `issue` by `fzyzcjy`; signals: fp8, hang; excerpt: "UPDATE: Support of fp8 test command results (strict-match in lm-eval) baseline: not tested before change: error when starting server after change: 94.3, 94.8, 94.5, ..." (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3319184971)
- `2025-09-10T23:43:34Z` `review` `COMMENTED` by `fzyzcjy`; signals: general review; excerpt: "hi, could you please run (1) math500 w/ 64k gen 3 times (3) gpqa diamond w/ 32k gen for at least 16 times (preferably ..." (https://github.com/sgl-project/sglang/pull/10281#pullrequestreview-3208188798)
- `2025-09-11T01:36:47Z` `issue` by `pranavm-nvidia`; signals: benchmark; excerpt: "GPQA benchmark with MTP=off: Server command: Results: Category evaluation mode num entries avg tokens gen seconds symbolic correct no answer ------------------------------------------- ----------------- ------------- ------------ ..." (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3277067897)
- `2025-09-22T01:31:57Z` `issue` by `fzyzcjy`; signals: flashinfer; excerpt: "I want to have a quick test and see the following launch error. may I know what is your env? (I tried both stable ..." (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3316466259)
- `2025-09-22T13:28:23Z` `issue` by `fzyzcjy`; signals: b200; excerpt: "cc @zhyncs shall we merge this first (if I find subtle issues in gb200 settings will post separately)" (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3319043727)
- `2025-09-22T02:45:44Z` `issue` by `fzyzcjy`; signals: b200; excerpt: "My full reproduction on B200 Results p.s. version is correct" (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3316582355)
- `2025-09-22T13:02:29Z` `issue` by `fzyzcjy`; signals: accuracy; excerpt: "hi @pranavm-nvidia, @zhyncs let me to help fix accuracy issues, my fix is WIP in" (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3318874085)
- `2025-09-11T05:35:35Z` `issue` by `fzyzcjy`; signals: general review; excerpt: "would be great to try R1-0528 and get 80% for this number also need to repeat e.g. 10 times since it has huge randomness" (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3277933929)
- `2025-09-14T04:44:23Z` `issue` by `fzyzcjy`; signals: general review; excerpt: "looking forward to this PR, if it is hard to do the testing maybe merge first and I will test it in my case ..." (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3289183896)
- `2025-09-17T23:49:41Z` `issue` by `zhyncs`; signals: general review; excerpt: "We need to ensure that this PR does not break the above two commands. Thanks! @pranavm-nvidia @kushanam" (https://github.com/sgl-project/sglang/pull/10281#issuecomment-3304876756)
