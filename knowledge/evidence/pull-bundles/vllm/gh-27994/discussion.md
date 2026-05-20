# PR Discussion Digest

- Source PR: [vllm-project/vllm#27994](https://github.com/vllm-project/vllm/pull/27994)
- Source page: `sources/prs/vllm/PR-27994.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27994`
- Generated at: `2026-05-20T15:38:23.825175+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-03T17:41:05Z`
- Merged: `2025-11-05T17:25:33Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: MengqingCao, heheda12345, pavanimajety, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-04T03:31:19Z` `COMMENTED` by `MengqingCao` (https://github.com/vllm-project/vllm/pull/27994#pullrequestreview-3413844192)
- `2025-11-04T05:42:31Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/27994#pullrequestreview-3414146126)
- `2025-11-04T05:50:02Z` `COMMENTED` by `MengqingCao` (https://github.com/vllm-project/vllm/pull/27994#pullrequestreview-3414161966)
- `2025-11-05T17:24:23Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/27994#pullrequestreview-3423459579)
- `2025-11-05T17:25:25Z` `APPROVED` by `pavanimajety` - LGTM, we can undo the change once flashinfer is fixed. (https://github.com/vllm-project/vllm/pull/27994#pullrequestreview-3423464163)

## Inline Comment Hotspots

- `vllm/model_executor/models/config.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-11-04T03:31:19Z` `inline` by `MengqingCao` `vllm/model_executor/models/config.py`:378; signals: alignment, attention, block, kernel; excerpt: "nit: How about make the logic of kernel block alignment size into each attention backends? Actually this is need in vllm-ascend, too. If this ..." (https://github.com/vllm-project/vllm/pull/27994#discussion_r2488545691)
- `2025-11-04T05:42:31Z` `inline` by `heheda12345` `vllm/model_executor/models/config.py`:378; signals: alignment, block, kernel; excerpt: "Yes it make sense. Help wanted on it. And I think the alignment can be inferred from get supported kernel block size" (https://github.com/vllm-project/vllm/pull/27994#discussion_r2488794329)
- `2025-11-05T17:24:23Z` `inline` by `pavanimajety` `vllm/model_executor/models/config.py`:378; signals: alignment, block, kernel; excerpt: "For my knowledge, what is kernel block alignment size?" (https://github.com/vllm-project/vllm/pull/27994#discussion_r2495481197)
- `2025-11-05T17:25:25Z` `review` `APPROVED` by `pavanimajety`; signals: flashinfer, hang; excerpt: "LGTM, we can undo the change once flashinfer is fixed." (https://github.com/vllm-project/vllm/pull/27994#pullrequestreview-3423464163)
- `2025-11-04T05:50:02Z` `inline` by `MengqingCao` `vllm/model_executor/models/config.py`:378; signals: general review; excerpt: "Okay, I'll work on it then." (https://github.com/vllm-project/vllm/pull/27994#discussion_r2488806295)
- `2025-11-04T07:50:55Z` `issue` by `MengqingCao`; signals: general review; excerpt: "@MengqingCao are you talking about something like I did in 27704 Yes, thanks for the context! I'll take a look at your pr" (https://github.com/vllm-project/vllm/pull/27994#issuecomment-3484352820)
