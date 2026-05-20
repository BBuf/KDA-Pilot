# PR Discussion Digest

- Source PR: [vllm-project/vllm#29352](https://github.com/vllm-project/vllm/pull/29352)
- Source page: `sources/prs/vllm/PR-29352.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29352`
- Generated at: `2026-05-20T15:38:42.716720+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-24T21:52:29Z`
- Merged: `2025-12-02T18:48:09Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 8
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: LucasWilkinson, MatthewBonanni, mergify, tdoublep
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-26T21:01:13Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3512743772)
- `2025-11-27T09:05:19Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3514145082)
- `2025-11-27T16:12:29Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3516270922)
- `2025-11-27T16:12:34Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3516271144)
- `2025-12-01T16:06:26Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3525807077)
- `2025-12-01T18:21:22Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3526408952)
- `2025-12-01T18:59:45Z` `APPROVED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3526538993)
- `2025-12-01T18:59:51Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/29352#pullrequestreview-3526539242)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mamba1_attn.py`: 3 inline comment(s)
- `vllm/v1/attention/backends/mamba2_attn.py`: 3 inline comment(s)
- `vllm/v1/attention/backends/gdn_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-27T16:12:29Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/mamba1_attn.py`:142; signals: attention, nan; excerpt: "I think we can; can you try @MatthewBonanni ?" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2569429022)
- `2025-11-27T16:12:34Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/mamba2_attn.py`:311; signals: attention, nan; excerpt: "I think we can; can you try @MatthewBonanni ?" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2569429204)
- `2025-11-27T09:02:00Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba1_attn.py`:142; signals: attention; excerpt: "Are we sure this is OK to remove? I will check the prefix caching logic to see if it is really necessary to fill ..." (https://github.com/vllm-project/vllm/pull/29352#discussion_r2567683343)
- `2025-12-01T16:06:26Z` `inline` by `MatthewBonanni` `vllm/v1/attention/backends/mamba1_attn.py`:142; signals: attention; excerpt: "I tested it with pytest tests/models/language/generation -m hybrid model with that line removed and it seemed to work fine" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2577710168)
- `2025-11-26T21:01:13Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/gdn_attn.py`:272; signals: attention; excerpt: "im not sure if this is needed anymore? this should already be respected in the model runner" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2566483210)
- `2025-11-27T09:03:08Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba2_attn.py`:311; signals: attention; excerpt: "I guess this line is now redundant? Or is num decodes not padded?" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2567686780)
- `2025-12-01T18:21:21Z` `inline` by `MatthewBonanni` `vllm/v1/attention/backends/gdn_attn.py`:272; signals: attention; excerpt: "Removed in [3cd6cdb](" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2578170830)
- `2025-12-01T18:59:50Z` `inline` by `MatthewBonanni` `vllm/v1/attention/backends/mamba2_attn.py`:311; signals: attention; excerpt: "Yes, removed in [97d50c9]( works fine" (https://github.com/vllm-project/vllm/pull/29352#discussion_r2578273978)
- `2025-11-24T21:58:27Z` `issue` by `mergify`; signals: nan; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @MatthewBonanni." (https://github.com/vllm-project/vllm/pull/29352#issuecomment-3572884492)
