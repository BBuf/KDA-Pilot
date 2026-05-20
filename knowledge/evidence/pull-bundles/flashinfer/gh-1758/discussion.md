# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1758](https://github.com/flashinfer-ai/flashinfer/pull/1758)
- Source page: `sources/prs/flashinfer/PR-1758.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1758`
- Generated at: `2026-05-20T15:23:21.461298+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T08:39:58Z`
- Merged: `2025-09-25T05:06:46Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: elvischenv, weireweire, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-09-23T08:44:02Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces tests for sink attention and refactors some of the existing test setup ... (https://github.com/flashinfer-ai/flashinfer/pull/1758#pullrequestreview-3256893475)
- `2025-09-23T09:17:14Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1758#pullrequestreview-3257005561)
- `2025-09-23T16:59:27Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1758#pullrequestreview-3258902012)
- `2025-09-24T01:34:57Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1758#pullrequestreview-3260305555)
- `2025-09-24T05:57:08Z` `APPROVED` by `yzh119` - LGTM, thanks for the fix! (https://github.com/flashinfer-ai/flashinfer/pull/1758#pullrequestreview-3261119978)

## Inline Comment Hotspots

- `tests/test_trtllm_gen_attention.py`: 2 inline comment(s)
- `flashinfer/artifacts.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-24T01:34:57Z` `inline` by `weireweire` `flashinfer/artifacts.py`:72; signals: accuracy, attention, flashinfer, regression; excerpt: "fix sink attention accuracy regression，caused by adding the sink twice." (https://github.com/flashinfer-ai/flashinfer/pull/1758#discussion_r2373831818)
- `2025-09-23T16:59:11Z` `inline` by `yzh119` `flashinfer/artifacts.py`:72; signals: flashinfer, hang; excerpt: "what's this change about?" (https://github.com/flashinfer-ai/flashinfer/pull/1758#discussion_r2372944807)
- `2025-09-23T09:19:03Z` `issue` by `weireweire`; signals: attention, blackwell; excerpt: "The added test can be a replacement of test attention sink blackwell.py but I didn't remove it yet. cc @IwakuraRein @joker-eph" (https://github.com/flashinfer-ai/flashinfer/pull/1758#issuecomment-3323101461)
- `2025-09-23T09:17:14Z` `inline` by `weireweire` `tests/test_trtllm_gen_attention.py`:204; signals: attention; excerpt: "solved. thanks" (https://github.com/flashinfer-ai/flashinfer/pull/1758#discussion_r2371679832)
