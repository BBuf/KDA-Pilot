# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2087](https://github.com/tile-ai/tilelang/pull/2087)
- Source page: `sources/prs/tilelang/PR-2087.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2087`
- Generated at: `2026-05-20T15:32:57.905272+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-22T16:22:50Z`
- Merged: `2026-04-22T16:36:54Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LeiWang1999, coderabbitai
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-22T16:28:11Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) src/tl templates/cuda/copy sm90.h (1) 23-247: Factor the 7 repeated if/ ... (https://github.com/tile-ai/tilelang/pull/2087#pullrequestreview-4156291853)
- `2026-04-22T16:36:46Z` `APPROVED` by `LeiWang1999` (https://github.com/tile-ai/tilelang/pull/2087#pullrequestreview-4156354336)

## Inline Comment Hotspots

- `src/target/ptx.cc`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-22T16:28:10Z` `inline` by `coderabbitai` `src/target/ptx.cc`:1443; signals: blackwell, block, cuda, h100, hang, hopper, memory, ptx; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🌐 Web query: Which PTX ISA version introduced the shared::cta state space for cp.async.bulk and cp.async.bulk.tensor, ..." (https://github.com/tile-ai/tilelang/pull/2087#discussion_r3125438429)
- `2026-04-22T16:28:11Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cuda, hang, ptx, sm90, tile, tma; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) src/tl templates/cuda/copy sm90.h (1) 23-247: Factor the 7 repeated if/ else/ endif blocks into a single ..." (https://github.com/tile-ai/tilelang/pull/2087#pullrequestreview-4156291853)
- `2026-04-22T16:23:03Z` `issue` by `coderabbitai`; signals: compile, cuda, hang, ptx, sm90, tile, tma; excerpt: "📝 Walkthrough Walkthrough This PR introduces CUDA compiler version-specific conditional compilation to emit different PTX instruction mnemonics for cp.async.bulk operations. The changes switch synchronization ..." (https://github.com/tile-ai/tilelang/pull/2087#issuecomment-4297987381)
