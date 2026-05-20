# PR Discussion Digest

- Source PR: [vllm-project/vllm#19346](https://github.com/vllm-project/vllm/pull/19346)
- Source page: `sources/prs/vllm/PR-19346.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19346`
- Generated at: `2026-05-20T15:35:27.387218+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-09T04:05:26Z`
- Merged: `2025-07-18T18:10:21Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: ProExpertProg, houseroad, mergify, zou3519
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-09T04:05:47Z` `COMMENTED` by `gemini-code-assist` - Hello @zou3519, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2908870023)
- `2025-06-09T04:06:11Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively addresses the issue of the torch.Tag.needs fixed stride order being applied unnecessarily ... (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2908870534)
- `2025-06-10T00:33:54Z` `APPROVED` by `houseroad` - The PR looks good to me. For torch, should we support at least two major versions? like torch ... (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2911673662)
- `2025-06-10T01:52:02Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2911757545)
- `2025-06-18T19:58:43Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2940503968)
- `2025-06-25T18:05:23Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2959163042)
- `2025-06-25T19:52:33Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2959454543)
- `2025-06-25T19:52:44Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2959454912)

## Inline Comment Hotspots

- `vllm/attention/ops/rocm_aiter_mla.py`: 3 inline comment(s)
- `csrc/torch_bindings.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-25T18:05:23Z` `inline` by `zou3519` `vllm/attention/ops/rocm_aiter_mla.py`:99; signals: attention, mla; excerpt: "I don't really want to do this if we're just going to use it in two places and we are moving to PyTorch 2.8 ..." (https://github.com/vllm-project/vllm/pull/19346#discussion_r2167311944)
- `2025-06-18T19:58:43Z` `inline` by `ProExpertProg` `vllm/attention/ops/rocm_aiter_mla.py`:99; signals: attention, mla; excerpt: "Could we extract this into a common variable in utils?" (https://github.com/vllm-project/vllm/pull/19346#discussion_r2155394901)
- `2025-06-25T19:52:33Z` `inline` by `ProExpertProg` `vllm/attention/ops/rocm_aiter_mla.py`:99; signals: attention, mla; excerpt: "Yeah that's fair!" (https://github.com/vllm-project/vllm/pull/19346#discussion_r2167497830)
- `2025-06-10T00:29:11Z` `inline` by `houseroad` `csrc/torch_bindings.cpp`:29; signals: hang; excerpt: "So only ==6 or should be <=6? Do we know when the behavior got changed?" (https://github.com/vllm-project/vllm/pull/19346#discussion_r2136707984)
- `2025-06-10T15:04:24Z` `issue` by `zou3519`; signals: failing; excerpt: "@houseroad as far as I can tell those tests are failing for me locally (on the base revision before my commit). Should I try ..." (https://github.com/vllm-project/vllm/pull/19346#issuecomment-2959617312)
- `2025-06-10T18:11:28Z` `issue` by `zou3519`; signals: failing; excerpt: "Some data points: 1. It looks like the spec decoding tests are failing on main too, it's just that they don't seem to run ..." (https://github.com/vllm-project/vllm/pull/19346#issuecomment-2960195982)
- `2025-06-16T13:31:57Z` `issue` by `zou3519`; signals: memory; excerpt: "Rebased. I think what's going on with the lora tests is that they require the GPU to be empty. Some previously run test is ..." (https://github.com/vllm-project/vllm/pull/19346#issuecomment-2976677650)
- `2025-06-10T01:52:02Z` `inline` by `zou3519` `csrc/torch_bindings.cpp`:29; signals: general review; excerpt: "Only in 2.6 is the default "requires contiguous". In 2.5 and 2.7 the default is needs fixed stride order." (https://github.com/vllm-project/vllm/pull/19346#discussion_r2136768153)
- `2025-06-10T00:33:54Z` `review` `APPROVED` by `houseroad`; signals: general review; excerpt: "The PR looks good to me. For torch, should we support at least two major versions? like torch 2.7 + 2.6?" (https://github.com/vllm-project/vllm/pull/19346#pullrequestreview-2911673662)
- `2025-07-11T03:25:50Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @zou3519." (https://github.com/vllm-project/vllm/pull/19346#issuecomment-3060229892)
