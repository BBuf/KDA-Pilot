# PR Discussion Digest

- Source PR: [vllm-project/vllm#37880](https://github.com/vllm-project/vllm/pull/37880)
- Source page: `sources/prs/vllm/PR-37880.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37880`
- Generated at: `2026-05-20T15:40:24.598181+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T10:37:29Z`
- Merged: `2026-03-25T14:31:53Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=2, changes_requested=2, commented=4)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: askliar, benchislett, hmellor, mergify
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T10:42:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a moe backend option within SpeculativeConfig to enable distinct MoE kernel backends ... (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-3990840719)
- `2026-03-23T14:48:23Z` `CHANGES_REQUESTED` by `benchislett` - Does not seem to apply to all LLM speculators, only draft models. Why? (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-3992334802)
- `2026-03-23T16:42:30Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-3993098600)
- `2026-03-24T11:46:14Z` `COMMENTED` by `askliar` (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-3998460964)
- `2026-03-24T22:30:22Z` `APPROVED` by `benchislett` - LGTM (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-4002751822)
- `2026-03-25T12:04:07Z` `CHANGES_REQUESTED` by `hmellor` - Please use vllm.config.utils.replace instead of dataclasses.replace. dataclasses.replace is not guaranteed to work on Pydantic dataclasses (which all our ... (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-4006137080)
- `2026-03-25T13:43:39Z` `COMMENTED` by `hmellor` - Thanks for making the change! (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-4006803321)
- `2026-03-25T13:44:04Z` `APPROVED` by `hmellor` (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-4006806115)

## Inline Comment Hotspots

- `vllm/v1/spec_decode/utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-25T13:43:39Z` `review` `COMMENTED` by `hmellor`; signals: hang; excerpt: "Thanks for making the change!" (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-4006803321)
- `2026-03-23T16:42:30Z` `inline` by `benchislett` `vllm/v1/spec_decode/utils.py`:260; signals: hang; excerpt: "Can you consolidate this into create vllm config for spec decode and then have create vllm config for draft model extend it? Probably this ..." (https://github.com/vllm-project/vllm/pull/37880#discussion_r2976239436)
- `2026-03-25T12:04:07Z` `review` `CHANGES_REQUESTED` by `hmellor`; signals: general review; excerpt: "Please use vllm.config.utils.replace instead of dataclasses.replace. dataclasses.replace is not guaranteed to work on Pydantic dataclasses (which all our config classes are)." (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-4006137080)
- `2026-03-23T14:48:23Z` `review` `CHANGES_REQUESTED` by `benchislett`; signals: general review; excerpt: "Does not seem to apply to all LLM speculators, only draft models. Why?" (https://github.com/vllm-project/vllm/pull/37880#pullrequestreview-3992334802)
- `2026-03-24T11:46:14Z` `inline` by `askliar` `vllm/v1/spec_decode/utils.py`:260; signals: general review; excerpt: "Done, lmk what you think!" (https://github.com/vllm-project/vllm/pull/37880#discussion_r2980946106)
- `2026-03-24T22:12:09Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @askliar." (https://github.com/vllm-project/vllm/pull/37880#issuecomment-4121741695)
