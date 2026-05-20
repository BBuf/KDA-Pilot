# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2227](https://github.com/Dao-AILab/flash-attention/pull/2227)
- Source page: `sources/prs/flash-attention/PR-2227.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2227`
- Generated at: `2026-05-20T15:16:47.092905+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-04T02:14:16Z`
- Merged: `2026-03-09T03:12:50Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: chatgpt-codex-connector, drisspg, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-05T05:29:54Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: be07536c20 ℹ️ About ... (https://github.com/Dao-AILab/flash-attention/pull/2227#pullrequestreview-3754667206)
- `2026-02-05T05:46:46Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2227#pullrequestreview-3754705755)
- `2026-02-08T01:24:24Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: ce6827bf85 ℹ️ About ... (https://github.com/Dao-AILab/flash-attention/pull/2227#pullrequestreview-3768623671)
- `2026-03-07T05:27:23Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2227#pullrequestreview-3907538636)

## Inline Comment Hotspots

- `flash_attn/cute/interface.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-02-05T05:29:54Z` `inline` by `chatgpt-codex-connector` `flash_attn/cute/interface.py`:86; signals: cute, kernel, regression, sm100; excerpt: ", so inputs like head dim=128, head dim v=192 should be valid but will now raise before kernel selection. This is a regression for ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#discussion_r2767213382)
- `2026-02-08T01:24:24Z` `inline` by `chatgpt-codex-connector` `flash_attn/cute/interface.py`:81; signals: cute, hang, kernel, sm90; excerpt: "and were previously allowed by the interface. As a result, configurations such as head dim=head dim v=256 on SM90 will now raise before kernel ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#discussion_r2778335080)
- `2026-02-05T05:46:46Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:86; signals: cuda, cute, tmem; excerpt: "just checked again and no this is not true we either have tmem error or cudaErrorIllegalAddress" (https://github.com/Dao-AILab/flash-attention/pull/2227#discussion_r2767250263)
- `2026-02-05T05:29:54Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: be07536c20 ℹ️ About Codex in GitHub [Your team has ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#pullrequestreview-3754667206)
- `2026-02-08T01:24:24Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: ce6827bf85 ℹ️ About Codex in GitHub [Your team has ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#pullrequestreview-3768623671)
- `2026-02-08T00:53:12Z` `issue` by `tridao`; signals: sm90; excerpt: "Iirrc we support hdim 192-128 on Sm90, at least in the forward. Btw one should be able to round up the headdim, e.g. if ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#issuecomment-3865861638)
- `2026-02-08T01:44:38Z` `issue` by `chatgpt-codex-connector`; signals: general review; excerpt: "You have reached your Codex usage limits for code reviews. You can see your limits in the [Codex usage dashboard]( To continue using code ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#issuecomment-3865917136)
- `2026-02-08T02:39:47Z` `issue` by `chatgpt-codex-connector`; signals: general review; excerpt: "You have reached your Codex usage limits for code reviews. You can see your limits in the [Codex usage dashboard]( To continue using code ..." (https://github.com/Dao-AILab/flash-attention/pull/2227#issuecomment-3865983697)
