# PR Discussion Digest

- Source PR: [vllm-project/vllm#37887](https://github.com/vllm-project/vllm/pull/37887)
- Source page: `sources/prs/vllm/PR-37887.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37887`
- Generated at: `2026-05-20T15:40:26.405655+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T12:29:23Z`
- Merged: `2026-03-31T23:22:23Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: MatthewBonanni, gronsti-amd, mergify
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T12:35:34Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix an issue with speculative decoding for DeepSeek v3.2 on ROCm. ... (https://github.com/vllm-project/vllm/pull/37887#pullrequestreview-3991413077)
- `2026-03-23T15:22:51Z` `COMMENTED` by `gronsti-amd` (https://github.com/vllm-project/vllm/pull/37887#pullrequestreview-3992579481)
- `2026-03-23T15:50:23Z` `COMMENTED` by `gronsti-amd` (https://github.com/vllm-project/vllm/pull/37887#pullrequestreview-3992761150)
- `2026-03-30T13:58:31Z` `APPROVED` by `MatthewBonanni` - LGTM, thanks for the fix! Could you fix this earlier call with the same bug? (https://github.com/vllm-project/vllm/pull/37887#pullrequestreview-4030782093)
- `2026-03-30T14:03:16Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/37887#pullrequestreview-4030839124)

## Inline Comment Hotspots

- `vllm/v1/spec_decode/eagle.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-03-31T07:41:50Z` `issue` by `gronsti-amd`; signals: attention, hang; excerpt: "There was a conflict with a change on main, breaking out the attention building loop into a function. I moved my changes into the ..." (https://github.com/vllm-project/vllm/pull/37887#issuecomment-4160584240)
- `2026-03-23T15:22:51Z` `inline` by `gronsti-amd` `vllm/v1/spec_decode/eagle.py`:523; signals: attention; excerpt: "I don't quite agree that the proposed alternative is better. per layer attn metadata is of type dict[str, object], so values are of type ..." (https://github.com/vllm-project/vllm/pull/37887#discussion_r2975758639)
- `2026-03-23T15:50:23Z` `inline` by `gronsti-amd` `vllm/v1/spec_decode/eagle.py`:523; signals: attention; excerpt: "I resolved the issue in a cleaner way, by introducing a new variable draft attn metadata per group. Pros: - Self-contained and simple. The ..." (https://github.com/vllm-project/vllm/pull/37887#discussion_r2975928224)
- `2026-03-30T14:03:16Z` `inline` by `MatthewBonanni` `vllm/v1/spec_decode/eagle.py`:436; signals: general review; excerpt: "nit: could we rename for consistency?" (https://github.com/vllm-project/vllm/pull/37887#discussion_r3010030963)
- `2026-03-31T06:33:12Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @gronsti-amd." (https://github.com/vllm-project/vllm/pull/37887#issuecomment-4160266513)
