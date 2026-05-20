# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1821](https://github.com/flashinfer-ai/flashinfer/pull/1821)
- Source page: `sources/prs/flashinfer/PR-1821.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1821`
- Generated at: `2026-05-20T15:23:26.773223+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T21:33:50Z`
- Merged: `2025-10-01T00:16:32Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: chelsea0x3b, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-30T21:35:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly identifies and fixes an issue where having /usr/include in the system include ... (https://github.com/flashinfer-ai/flashinfer/pull/1821#pullrequestreview-3286784955)
- `2025-09-30T21:37:42Z` `COMMENTED` by `chelsea0x3b` (https://github.com/flashinfer-ai/flashinfer/pull/1821#pullrequestreview-3286789150)
- `2025-09-30T22:14:10Z` `APPROVED` by `yzh119` - Hi @coreylowman thanks for the fix, LGTM overall. Quick question: which installers installs CUDA under /usr? I'm used ... (https://github.com/flashinfer-ai/flashinfer/pull/1821#pullrequestreview-3286864110)

## Inline Comment Hotspots

- `flashinfer/jit/cpp_ext.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-09-30T21:37:42Z` `inline` by `chelsea0x3b` `flashinfer/jit/cpp_ext.py`:111; signals: flashinfer; excerpt: "I don't think we should do this personally, but open to maintainers chiming in. The issue resolved by this PR is that -isystem /usr/include ..." (https://github.com/flashinfer-ai/flashinfer/pull/1821#discussion_r2392889786)
- `2025-09-30T22:14:10Z` `review` `APPROVED` by `yzh119`; signals: cuda; excerpt: "Hi @coreylowman thanks for the fix, LGTM overall. Quick question: which installers installs CUDA under /usr? I'm used to seeing it under /usr/local/cuda. Not ..." (https://github.com/flashinfer-ai/flashinfer/pull/1821#pullrequestreview-3286864110)
- `2025-09-30T22:28:27Z` `issue` by `chelsea0x3b`; signals: cuda; excerpt: "Niche once’s afaik. /usr/local is definitely the default recommended location by nvidia. My guess is that low level systems people who are providing GPU ..." (https://github.com/flashinfer-ai/flashinfer/pull/1821#issuecomment-3353995159)
