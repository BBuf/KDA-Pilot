# PR Discussion Digest

- Source PR: [vllm-project/vllm#19717](https://github.com/vllm-project/vllm/pull/19717)
- Source page: `sources/prs/vllm/PR-19717.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19717`
- Generated at: `2026-05-20T15:35:33.386771+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-16T22:45:33Z`
- Merged: `2025-06-25T06:22:58Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bnellnm, tdoublep, tlrmchlsmth, yeqcharlotte, zou3519
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 9

## Review Decisions

- `2025-06-24T19:56:37Z` `COMMENTED` by `tlrmchlsmth` - To document somewhere in the PR description why we change from .shape to .size(), pasting from a DM ... (https://github.com/vllm-project/vllm/pull/19717#pullrequestreview-2955130144)
- `2025-06-24T19:59:15Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/19717#pullrequestreview-2955136719)

## Inline Comment Hotspots

- `tests/kernels/moe/test_cutlass_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-24T19:56:37Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: compile, hang; excerpt: "To document somewhere in the PR description why we change from .shape to .size(), pasting from a DM between me and @bnellnm: i was ..." (https://github.com/vllm-project/vllm/pull/19717#pullrequestreview-2955130144)
- `2025-06-17T21:46:44Z` `issue` by `bnellnm`; signals: compile, hang; excerpt: "After updating the unit tests with mark dynamic, I'm running into torch.compile problems. At this point, I'm going to back off on some of ..." (https://github.com/vllm-project/vllm/pull/19717#issuecomment-2981930480)
- `2025-06-17T23:03:16Z` `issue` by `zou3519`; signals: compile, hang; excerpt: "After updating the unit tests with mark dynamic, I'm running into torch.compile problems. At this point, I'm going to back off on some of ..." (https://github.com/vllm-project/vllm/pull/19717#issuecomment-2982067083)
- `2025-06-18T17:00:05Z` `issue` by `bnellnm`; signals: compile, hang; excerpt: "After updating the unit tests with mark dynamic, I'm running into torch.compile problems. At this point, I'm going to back off on some of ..." (https://github.com/vllm-project/vllm/pull/19717#issuecomment-2985050408)
