# PR Discussion Digest

- Source PR: [vllm-project/vllm#28133](https://github.com/vllm-project/vllm/pull/28133)
- Source page: `sources/prs/vllm/PR-28133.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28133`
- Generated at: `2026-05-20T15:38:25.503754+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-05T14:48:47Z`
- Merged: `2025-12-23T20:57:00Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=1
- Human participants with discussion text: Josephasafg, mergify, tdoublep
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-18T11:26:47Z` `COMMENTED` by `tdoublep` - Awesome work, this will make things much more maintainable. I have a few minor suggestions/questions. (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3592283709)
- `2025-12-18T13:29:28Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3593017340)
- `2025-12-18T13:43:39Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3593076069)
- `2025-12-18T13:43:48Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3593076608)
- `2025-12-18T13:49:33Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3593097844)
- `2025-12-18T13:54:53Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3593117908)
- `2025-12-18T14:32:10Z` `APPROVED` by `tdoublep` - LGTM (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3593299343)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mamba_attn.py`: 7 inline comment(s)
- `vllm/v1/attention/backends/mamba2_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-18T14:05:05Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @Josephasafg, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/28133#issuecomment-3670444151)
- `2025-12-18T11:17:51Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba_attn.py`:40; signals: attention; excerpt: "state indices tensor is used for both prefill and decode right? It might be good to group has initial states p and query start ..." (https://github.com/vllm-project/vllm/pull/28133#discussion_r2630639080)
- `2025-12-18T11:18:58Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba_attn.py`:45; signals: attention; excerpt: "Should we add a note that these tensors are used for prefix caching (and None if prefix caching is disabled)?" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2630642529)
- `2025-12-18T11:25:45Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba2_attn.py`:249; signals: attention; excerpt: "Won't common have type BaseMambaAttentionMetadata or is the type hint of M that the child class override is enough?" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2630664031)
- `2025-12-18T13:54:53Z` `inline` by `Josephasafg` `vllm/v1/attention/backends/mamba2_attn.py`:249; signals: attention; excerpt: "Yes, the type hint of M that the child class overrides is enough. common will have type Mamba2AttentionMetadata and not just the base class ..." (https://github.com/vllm-project/vllm/pull/28133#discussion_r2631196913)
- `2025-12-18T11:18:33Z` `inline` by `tdoublep` `vllm/v1/attention/backends/mamba_attn.py`:45; signals: attention; excerpt: "Should we group this with the other int above?" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2630641354)
- `2025-12-18T11:26:47Z` `review` `COMMENTED` by `tdoublep`; signals: general review; excerpt: "Awesome work, this will make things much more maintainable. I have a few minor suggestions/questions." (https://github.com/vllm-project/vllm/pull/28133#pullrequestreview-3592283709)
- `2025-12-18T13:29:28Z` `inline` by `Josephasafg` `vllm/v1/attention/backends/mamba_attn.py`:40; signals: attention; excerpt: "Makes sense. Done" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2631112971)
- `2025-12-18T13:43:39Z` `inline` by `Josephasafg` `vllm/v1/attention/backends/mamba_attn.py`:40; signals: attention; excerpt: "I also added num computed tokens p to this group" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2631159992)
- `2025-12-18T13:43:48Z` `inline` by `Josephasafg` `vllm/v1/attention/backends/mamba_attn.py`:45; signals: attention; excerpt: "Sounds good" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2631160509)
- `2025-12-18T13:49:32Z` `inline` by `Josephasafg` `vllm/v1/attention/backends/mamba_attn.py`:45; signals: attention; excerpt: "Good point. Done" (https://github.com/vllm-project/vllm/pull/28133#discussion_r2631179086)
- `2025-12-04T09:39:24Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @Josephasafg." (https://github.com/vllm-project/vllm/pull/28133#issuecomment-3611123633)
