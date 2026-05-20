# PR Discussion Digest

- Source PR: [vllm-project/vllm#17139](https://github.com/vllm-project/vllm/pull/17139)
- Source page: `sources/prs/vllm/PR-17139.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17139`
- Generated at: `2026-05-20T15:35:06.298085+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-24T21:44:07Z`
- Merged: `2025-05-07T14:12:35Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 7
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: ProExpertProg, gshtras, houseroad, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-25T04:08:55Z` `COMMENTED` by `ProExpertProg` - 2 nits, and could we add this case to tests? (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2792946505)
- `2025-04-25T04:36:38Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2792970424)
- `2025-04-25T21:57:18Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2795387642)
- `2025-05-01T18:14:14Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2810384898)
- `2025-05-01T19:22:55Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2810529645)
- `2025-05-01T20:32:33Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2810665678)
- `2025-05-05T15:09:31Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2815157206)
- `2025-05-05T17:08:10Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2815487396)

## Inline Comment Hotspots

- `csrc/rocm/attention.cu`: 7 inline comment(s)

## High-Signal Discussion

- `2025-04-25T04:08:20Z` `inline` by `ProExpertProg` `csrc/rocm/attention.cu`:1637; signals: attention, fp8; excerpt: "Should the OUTT type be fp8 if scale is given? Is that captured automatically? Maybe we could assert this somewhere" (https://github.com/vllm-project/vllm/pull/17139#discussion_r2059530052)
- `2025-04-25T21:57:18Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:1637; signals: attention, fp8; excerpt: "Should the OUTT type be fp8 if scale is given? Is that captured automatically? Maybe we could assert this somewhere This is ensured at ..." (https://github.com/vllm-project/vllm/pull/17139#discussion_r2060942232)
- `2025-05-01T20:32:33Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:1243; signals: attention, kernel; excerpt: "It is actually used in the reduction kernel launched after either of the attention kernels. The dereferencing here is indeed not needed, but it'll ..." (https://github.com/vllm-project/vllm/pull/17139#discussion_r2070769849)
- `2025-04-25T04:36:37Z` `inline` by `ProExpertProg` `csrc/rocm/attention.cu`:1637; signals: attention, fp8; excerpt: "Also, should tmp output be the same type as output? So if output is fp8, is tmp output also fp8?" (https://github.com/vllm-project/vllm/pull/17139#discussion_r2059545330)
- `2025-04-25T04:07:05Z` `inline` by `ProExpertProg` `csrc/rocm/attention.cu`:1640; signals: attention; excerpt: "Nit: static cast?" (https://github.com/vllm-project/vllm/pull/17139#discussion_r2059529425)
- `2025-05-01T19:22:55Z` `inline` by `houseroad` `csrc/rocm/attention.cu`:1243; signals: attention; excerpt: "wondering where out scale is used here?" (https://github.com/vllm-project/vllm/pull/17139#discussion_r2070693161)
- `2025-05-05T15:09:31Z` `inline` by `ProExpertProg` `csrc/rocm/attention.cu`:1243; signals: attention; excerpt: "Could you just remove it in this PR?" (https://github.com/vllm-project/vllm/pull/17139#discussion_r2073638518)
- `2025-04-25T04:08:55Z` `review` `COMMENTED` by `ProExpertProg`; signals: general review; excerpt: "2 nits, and could we add this case to tests?" (https://github.com/vllm-project/vllm/pull/17139#pullrequestreview-2792946505)
