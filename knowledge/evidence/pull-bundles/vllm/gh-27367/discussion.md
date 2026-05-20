# PR Discussion Digest

- Source PR: [vllm-project/vllm#27367](https://github.com/vllm-project/vllm/pull/27367)
- Source page: `sources/prs/vllm/PR-27367.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27367`
- Generated at: `2026-05-20T15:38:15.315575+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-22T19:32:32Z`
- Merged: `2025-10-28T17:55:10Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: LucasWilkinson, amirai21, benchislett, chatgpt-codex-connector, ganyi1996ppo, heheda12345, sarckk
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 13

## Review Decisions

- `2025-10-22T19:33:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the batch reordering logic to classify requests into decode, extend, and prefill ... (https://github.com/vllm-project/vllm/pull/27367#pullrequestreview-3367273822)
- `2025-10-22T19:34:44Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/27367#pullrequestreview-3367277043)
- `2025-10-28T04:05:19Z` `APPROVED` by `heheda12345` - LGTM! Can you add some unit tests like the order of decode requests are not changed? (https://github.com/vllm-project/vllm/pull/27367#pullrequestreview-3386473859)
- `2025-10-28T12:10:06Z` `APPROVED` by `benchislett` - LGTM (https://github.com/vllm-project/vllm/pull/27367#pullrequestreview-3388461894)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/utils.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-10-22T19:34:44Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/utils.py`:835; signals: attention, hang; excerpt: ", so the function will crash instead of leaving the batch unchanged. Useful? React with 👍 / 👎." (https://github.com/vllm-project/vllm/pull/27367#discussion_r2453157114)
- `2025-10-22T19:34:44Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub [Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/27367#pullrequestreview-3367277043)
- `2025-10-28T04:05:19Z` `review` `APPROVED` by `heheda12345`; signals: hang; excerpt: "LGTM! Can you add some unit tests like the order of decode requests are not changed?" (https://github.com/vllm-project/vllm/pull/27367#pullrequestreview-3386473859)
