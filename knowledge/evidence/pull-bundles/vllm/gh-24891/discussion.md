# PR Discussion Digest

- Source PR: [vllm-project/vllm#24891](https://github.com/vllm-project/vllm/pull/24891)
- Source page: `sources/prs/vllm/PR-24891.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-24891`
- Generated at: `2026-05-20T15:37:52.177151+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-15T16:37:18Z`
- Merged: `2025-09-15T20:21:53Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: ProExpertProg, alexm-redhat, mgoin
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-15T16:40:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request removes two redundant .clone() calls on the q nope and q pe tensors ... (https://github.com/vllm-project/vllm/pull/24891#pullrequestreview-3225490401)
- `2025-09-15T16:44:33Z` `APPROVED` by `mgoin` - Nice find (https://github.com/vllm-project/vllm/pull/24891#pullrequestreview-3225503356)
- `2025-09-15T16:51:26Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24891#pullrequestreview-3225524362)
- `2025-09-15T18:46:44Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24891#pullrequestreview-3225871553)
- `2025-09-15T18:55:01Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/24891#pullrequestreview-3225896333)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/cutlass_mla.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-15T18:46:28Z` `inline` by `mgoin` `vllm/v1/attention/backends/mla/cutlass_mla.py`:218; signals: attention, cutlass, mla; excerpt: "I understand putting this in a conditional, but why can we remove the contiguous for out if we can't for lse?" (https://github.com/vllm-project/vllm/pull/24891#discussion_r2349828060)
- `2025-09-15T18:55:01Z` `inline` by `alexm-redhat` `vllm/v1/attention/backends/mla/cutlass_mla.py`:218; signals: attention, cutlass, mla; excerpt: "Most likely lse as well, I was just on the safe side, since I don't know how to test it." (https://github.com/vllm-project/vllm/pull/24891#discussion_r2349845442)
- `2025-09-15T18:12:20Z` `issue` by `alexm-redhat`; signals: cutlass, mla, sm100; excerpt: "Removed the contiguous() call in sm100 cutlass mla decode(), gets additional 0.8%, for a total of 2.4% improvement. TPOT 18.7ms vs 19.15ms." (https://github.com/vllm-project/vllm/pull/24891#issuecomment-3293370589)
