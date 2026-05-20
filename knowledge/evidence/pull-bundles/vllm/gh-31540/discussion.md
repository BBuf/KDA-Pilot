# PR Discussion Digest

- Source PR: [vllm-project/vllm#31540](https://github.com/vllm-project/vllm/pull/31540)
- Source page: `sources/prs/vllm/PR-31540.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31540`
- Generated at: `2026-05-20T15:39:21.722911+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-30T18:31:16Z`
- Merged: `2026-01-02T03:32:31Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: benchislett, copilot-pull-request-reviewer, mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-30T18:33:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a critical bug in the EAGLE speculative decoding implementation where a globally ... (https://github.com/vllm-project/vllm/pull/31540#pullrequestreview-3618979378)
- `2025-12-30T18:34:03Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR fixes a bug in EAGLE's slot mapping computation for hybrid models that use ... (https://github.com/vllm-project/vllm/pull/31540#pullrequestreview-3618979655)
- `2025-12-30T18:42:02Z` `APPROVED` by `pavanimajety` - LGTM, thank you. (https://github.com/vllm-project/vllm/pull/31540#pullrequestreview-3618991534)
- `2025-12-30T20:36:47Z` `APPROVED` by `mgoin` - Seems reasonable to me. @benchislett have you seen this improve Qwen3-Next results? (https://github.com/vllm-project/vllm/pull/31540#pullrequestreview-3619265591)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-12-30T18:34:03Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: attention, block, cache, hang, kv cache; excerpt: "Pull request overview This PR fixes a bug in EAGLE's slot mapping computation for hybrid models that use different block sizes for linear and ..." (https://github.com/vllm-project/vllm/pull/31540#pullrequestreview-3618979655)
- `2025-12-30T21:28:13Z` `issue` by `benchislett`; signals: attention, block, nan; excerpt: "This bugfix came about when fixing issues in a WIP branch for specdec support of NVIDIA Nemotron Nano V3 + EAGLE. I'm not sure ..." (https://github.com/vllm-project/vllm/pull/31540#issuecomment-3700602518)
- `2025-12-30T22:30:08Z` `issue` by `benchislett`; signals: block, cache, kv cache; excerpt: "Update, does not fix 31186. It seems that Qwen3-Next actually uses the larger block size when allocating KV-Cache for the MTP module, and in ..." (https://github.com/vllm-project/vllm/pull/31540#issuecomment-3700695906)
- `2025-12-30T21:29:58Z` `issue` by `benchislett`; signals: cuda; excerpt: "31186 remains open, but I can rerun it later this week to check if this fix applies. Given that the crash in that issue ..." (https://github.com/vllm-project/vllm/pull/31540#issuecomment-3700605626)
