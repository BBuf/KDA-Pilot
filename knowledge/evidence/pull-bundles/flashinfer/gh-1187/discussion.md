# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1187](https://github.com/flashinfer-ai/flashinfer/pull/1187)
- Source page: `sources/prs/flashinfer/PR-1187.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1187`
- Generated at: `2026-05-20T15:21:52.674312+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-27T17:20:47Z`
- Merged: `2025-07-01T02:38:52Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 14
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=4
- Human participants with discussion text: Anerudhan, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-27T17:22:07Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Anerudhan, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2967350245)
- `2025-06-27T17:23:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces cuDNN-based attention kernels for prefill and decode, with support for dynamic cubin ... (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2967353982)
- `2025-06-30T17:05:29Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972028246)
- `2025-06-30T17:19:45Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972072838)
- `2025-06-30T17:20:58Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972075683)
- `2025-06-30T17:46:19Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972142061)
- `2025-06-30T18:01:10Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972183162)
- `2025-06-30T18:01:24Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972183682)
- `2025-06-30T20:26:31Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972533168)
- `2025-06-30T20:28:43Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2972542769)
- `2025-06-30T23:46:15Z` `COMMENTED` by `Anerudhan` (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2973078836)
- `2025-06-30T23:51:57Z` `APPROVED` by `yzh119` - LGTM, thanks again for the effort @Anerudhan ! (https://github.com/flashinfer-ai/flashinfer/pull/1187#pullrequestreview-2973085397)

## Inline Comment Hotspots

- `pyproject.toml`: 5 inline comment(s)
- `tests/test_cudnn_prefill_deepseek.py`: 4 inline comment(s)
- `flashinfer/cudnn/decode.py`: 3 inline comment(s)
- `csrc/cudnn_sdpa_utils.h`: 1 inline comment(s)
- `csrc/cudnn_sdpa_kernel_launcher.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-30T17:04:09Z` `inline` by `yzh119` `flashinfer/cudnn/decode.py`:51; signals: flashinfer, kernel; excerpt: "Does the cudnn decode kernel support returning lse as well?" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175533246)
- `2025-06-30T17:20:57Z` `inline` by `Anerudhan` `tests/test_cudnn_prefill_deepseek.py`:122; signals: kernel; excerpt: "I added this as a check, - To make sure both the cudnn and reference kernel ran succesfully without errors - The output and ..." (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175557532)
- `2025-06-30T17:19:45Z` `inline` by `Anerudhan` `flashinfer/cudnn/decode.py`:51; signals: flashinfer; excerpt: "No. Decode does not generate lse stats, right?" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175555687)
- `2025-06-30T20:26:31Z` `inline` by `yzh119` `flashinfer/cudnn/decode.py`:51; signals: flashinfer; excerpt: "We usually don't need lse for decode." (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175834776)
- `2025-06-30T20:28:43Z` `inline` by `yzh119` `tests/test_cudnn_prefill_deepseek.py`:122; signals: general review; excerpt: "Yes it could be used for debugging purpose but we should remove it here considering the test get passed. User will not explicitly call ..." (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175838474)
- `2025-06-30T17:02:37Z` `inline` by `yzh119` `tests/test_cudnn_prefill_deepseek.py`:122; signals: general review; excerpt: "Is it necessary?" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175530931)
- `2025-06-30T17:46:04Z` `inline` by `yzh119` `pyproject.toml`:53; signals: general review; excerpt: "Remove this." (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175594326)
- `2025-06-30T17:46:09Z` `inline` by `yzh119` `pyproject.toml`:62; signals: general review; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175594426)
- `2025-06-30T17:46:14Z` `inline` by `yzh119` `pyproject.toml`:82; signals: general review; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175594527)
- `2025-06-30T18:01:09Z` `inline` by `Anerudhan` `pyproject.toml`:53; signals: general review; excerpt: "Done" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175618186)
- `2025-06-30T18:01:24Z` `inline` by `Anerudhan` `pyproject.toml`:62; signals: general review; excerpt: "Done" (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2175618489)
- `2025-06-30T23:46:14Z` `inline` by `Anerudhan` `tests/test_cudnn_prefill_deepseek.py`:122; signals: general review; excerpt: "Removed from this and other test file." (https://github.com/flashinfer-ai/flashinfer/pull/1187#discussion_r2176150753)
