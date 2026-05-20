# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2387](https://github.com/flashinfer-ai/flashinfer/pull/2387)
- Source page: `sources/prs/flashinfer/PR-2387.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2387`
- Generated at: `2026-05-20T15:24:43.764589+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-20T22:06:08Z`
- Merged: `2026-01-22T06:28:56Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 21
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=7
- Human participants with discussion text: coderabbitai, ishovkun, yzh119
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-20T22:08:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a Blackwell-optimized version of the selective state update kernel, specifically targeting SM100+ ... (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3684502680)
- `2026-01-20T22:13:26Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3684518502)
- `2026-01-20T22:13:38Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) include/flashinfer/mamba/selective state update.cuh ... (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3684519155)
- `2026-01-20T22:15:10Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3684524180)
- `2026-01-20T22:42:48Z` `COMMENTED` by `yzh119` - Hi @ishovkun can you explain a little bit about the optimization? What specific feature did you use for ... (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3684616052)
- `2026-01-21T01:59:39Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685018942)
- `2026-01-21T02:00:24Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685020516)
- `2026-01-21T02:07:34Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) include/flashinfer/mamba/selective state update.cuh ... (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685036052)
- `2026-01-21T02:47:45Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685127317)
- `2026-01-21T02:47:58Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685128013)
- `2026-01-21T02:48:38Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685129630)
- `2026-01-21T02:48:40Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685129687)
- `2026-01-21T02:50:57Z` `COMMENTED` by `ishovkun` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685134337)
- `2026-01-21T02:51:47Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685136472)
- `2026-01-22T06:28:47Z` `APPROVED` by `yzh119` - LGTM, the performance of horizontal kernel looks impressive! (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3690801067)

## Inline Comment Hotspots

- `include/flashinfer/mamba/selective_state_update.cuh`: 9 inline comment(s)
- `.zed/tasks.json`: 6 inline comment(s)
- `flashinfer/jit/mamba/selective_state_update.py`: 5 inline comment(s)
- `0`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-20T22:06:28Z` `issue` by `coderabbitai`; signals: alignment, blackwell, cuda, flashinfer, hang, hopper, kernel, memory; excerpt: "[!NOTE] Other AI code review bot(s) detected CodeRabbit has detected other AI code review bot(s) in this pull request and will avoid duplicating their ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#issuecomment-3775174650)
- `2026-01-20T22:13:38Z` `inline` by `coderabbitai` `include/flashinfer/mamba/selective_state_update.cuh`:1090; signals: benchmark, cuda, cute, flashinfer, perf, performance, regression; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 936 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710256807)
- `2026-01-20T22:13:38Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, layout, perf, performance, throughput; excerpt: "Actionable comments posted: 2 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) include/flashinfer/mamba/selective state update.cuh (1) 693-699: Add rationale for the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3684519155)
- `2026-01-20T23:38:44Z` `issue` by `ishovkun`; signals: blackwell, compile, h200, hopper, kernel; excerpt: "Hi @ishovkun can you explain a little bit about the optimization? What specific feature did you use for sm 100/110/120 acceleration compared to sm ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#issuecomment-3775451910)
- `2026-01-20T22:13:37Z` `inline` by `coderabbitai` `include/flashinfer/mamba/selective_state_update.cuh`:843; signals: benchmark, flashinfer, kernel, sm100; excerpt: "⚠️ Potential issue 🟠 Major Fix z indexing to respect z stride batch. The SM100 horizontal path indexes z assuming a contiguous batch nheads ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710256798)
- `2026-01-21T02:07:33Z` `inline` by `coderabbitai` `.zed/tasks.json`:19; signals: benchmark, cute, flashinfer, overflow; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 85 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710695796)
- `2026-01-21T02:07:33Z` `inline` by `coderabbitai` `.zed/tasks.json`:38; signals: cute, flashinfer, race; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 2234 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710695799)
- `2026-01-21T02:00:24Z` `inline` by `ishovkun` `flashinfer/jit/mamba/selective_state_update.py`:41; signals: flashinfer, perf, performance; excerpt: "I added the performance images in the PR description and the corresponding code comments." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710683662)
- `2026-01-21T02:07:34Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, sm100; excerpt: "Actionable comments posted: 4 🤖 Fix all issues with AI agents 🧹 Nitpick comments (1) include/flashinfer/mamba/selective state update.cuh (1) 688-724: Hoist dA computation out ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3685036052)
- `2026-01-21T02:07:33Z` `inline` by `coderabbitai` `flashinfer/jit/mamba/selective_state_update.py`:39; signals: flashinfer, sm90; excerpt: "⚠️ Potential issue 🟡 Minor Fix typos in the SM90 note. Minor spelling/grammar issues make the comment harder to read. ✏️ Suggested edit 🤖 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710695805)
- `2026-01-22T06:28:47Z` `review` `APPROVED` by `yzh119`; signals: kernel, perf, performance; excerpt: "LGTM, the performance of horizontal kernel looks impressive!" (https://github.com/flashinfer-ai/flashinfer/pull/2387#pullrequestreview-3690801067)
- `2026-01-21T02:51:47Z` `inline` by `coderabbitai` `flashinfer/jit/mamba/selective_state_update.py`:39; signals: flashinfer; excerpt: "@ishovkun, thank you for fixing the typos! 🎉 --- 🧠 Learnings used --- --- --- If you found this review helpful, would you consider ..." (https://github.com/flashinfer-ai/flashinfer/pull/2387#discussion_r2710768128)
