# PR Discussion Digest

- Source PR: [vllm-project/vllm#38990](https://github.com/vllm-project/vllm/pull/38990)
- Source page: `sources/prs/vllm/PR-38990.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38990`
- Generated at: `2026-05-20T15:40:40.509142+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-04T17:59:02Z`
- Merged: `2026-04-05T14:28:32Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: milesial, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-04-04T18:01:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request modifies the determine shared experts order method in shared experts.py to prioritize multi-stream ... (https://github.com/vllm-project/vllm/pull/38990#pullrequestreview-4058720900)
- `2026-04-05T14:28:29Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38990#pullrequestreview-4059525230)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-05T05:59:24Z` `issue` by `milesial`; signals: b200, fp8, nan, race, regression; excerpt: "Confirming I saw the same issue, impact is 15 to 20% E2E regression on nemotron nano 3, B200 FP8. Top trace is from yesterday's ..." (https://github.com/vllm-project/vllm/pull/38990#issuecomment-4188357067)
- `2026-04-04T19:08:25Z` `issue` by `robertgshaw2-redhat`; signals: general review; excerpt: "to be clear, 0.19.1 is not a release yet. I dont think the offending commit is in a release unless I am mistaken" (https://github.com/vllm-project/vllm/pull/38990#issuecomment-4187597102)
