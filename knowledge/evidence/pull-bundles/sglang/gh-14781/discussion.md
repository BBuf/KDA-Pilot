# PR Discussion Digest

- Source PR: [sgl-project/sglang#14781](https://github.com/sgl-project/sglang/pull/14781)
- Source page: `sources/prs/sglang/PR-14781.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14781`
- Generated at: `2026-05-20T15:28:03.100406+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-10T03:23:39Z`
- Merged: `2025-12-18T21:48:28Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 8 (approved=1, changes_requested=1, commented=6)
- Inline review comments: 16
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=11
- Human participants with discussion text: Fridge003, Johnsonms
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-10T03:26:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant performance optimization for multi-step speculative decoding in the NSA backend. ... (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3560544992)
- `2025-12-13T08:40:54Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3574260390)
- `2025-12-16T02:33:48Z` `COMMENTED` by `Johnsonms` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3580963095)
- `2025-12-16T02:34:37Z` `COMMENTED` by `Johnsonms` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3580964412)
- `2025-12-16T02:34:48Z` `COMMENTED` by `Johnsonms` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3580964669)
- `2025-12-16T02:35:08Z` `COMMENTED` by `Johnsonms` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3580965277)
- `2025-12-16T02:35:26Z` `COMMENTED` by `Johnsonms` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3580965794)
- `2025-12-18T07:01:14Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14781#pullrequestreview-3591096725)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa_backend.py`: 16 inline comment(s)

## High-Signal Discussion

- `2025-12-11T22:14:24Z` `issue` by `Johnsonms`; signals: accuracy, attention, benchmark, perf, performance; excerpt: "1. Accuracy Test with gsm8k python3 benchmark/gsm8k/bench sglang.py --num-shots 8 --num-questions 1319 --parallel 1319 2. Accuracy Test with gpqa-diamond Service: python -m sglang.launch server ..." (https://github.com/sgl-project/sglang/pull/14781#issuecomment-3644011342)
- `2025-12-11T06:31:14Z` `issue` by `Fridge003`; signals: hang, perf, performance, throughput; excerpt: "@Johnsonms Thanks for your codes Do you have any e2e performance data. Like what's the change of decode throughput of a bs=1 isl=osl=1024, before ..." (https://github.com/sgl-project/sglang/pull/14781#issuecomment-3640444704)
- `2025-12-16T02:33:48Z` `inline` by `Johnsonms` `python/sglang/srt/layers/attention/nsa_backend.py`:1945; signals: attention, oom; excerpt: "This is currently only for draft decoding. I’ll work on the verify / draft-extend metadata next, but since it’s a single pass, there may ..." (https://github.com/sgl-project/sglang/pull/14781#discussion_r2621535623)
- `2025-12-13T08:11:40Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:242; signals: attention, speedup; excerpt: "What's the baseline of 3-5x speedup? Add some description here" (https://github.com/sgl-project/sglang/pull/14781#discussion_r2616165669)
- `2025-12-13T08:12:03Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:909; signals: attention, hang; excerpt: "Maybe remove 175us here since the number changes" (https://github.com/sgl-project/sglang/pull/14781#discussion_r2616165822)
- `2025-12-11T22:15:31Z` `issue` by `Johnsonms`; signals: accuracy, benchmark; excerpt: "Also can you post the accuracy result of GPQA/AIME benchmark? Added the test result, Thanks @Fridge003" (https://github.com/sgl-project/sglang/pull/14781#issuecomment-3644014615)
- `2025-12-16T21:41:49Z` `issue` by `Johnsonms`; signals: cuda, hang; excerpt: "Do you have data of acceptance length? Will it drop after this PR? I verified this and confirmed there is no change in the ..." (https://github.com/sgl-project/sglang/pull/14781#issuecomment-3662501252)
- `2025-12-11T07:03:17Z` `issue` by `Fridge003`; signals: accuracy, benchmark; excerpt: "Also can you post the accuracy result of GPQA/AIME benchmark?" (https://github.com/sgl-project/sglang/pull/14781#issuecomment-3640534220)
- `2025-12-13T07:56:11Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:234; signals: attention; excerpt: "Can we create a new file nsa backend mtp precompute.py, and put all the precompute related codes there? Seems all the precomputation logics are ..." (https://github.com/sgl-project/sglang/pull/14781#discussion_r2616159546)
- `2025-12-13T08:23:26Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:1951; signals: attention; excerpt: "Please add an environ that controls the precomputing of metadata, and put it under python/sglang/srt/layers/attention/nsa/utils.py" (https://github.com/sgl-project/sglang/pull/14781#discussion_r2616170154)
- `2025-12-13T08:30:19Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:1945; signals: attention; excerpt: "It's correct to fix the forward mode to decode here. But since it's the only place for precomputing metadata, will be the verify/draft extend ..." (https://github.com/sgl-project/sglang/pull/14781#discussion_r2616172988)
- `2025-12-13T08:35:02Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:1175; signals: attention; excerpt: "Also remove the hardcoded data here" (https://github.com/sgl-project/sglang/pull/14781#discussion_r2616174818)
