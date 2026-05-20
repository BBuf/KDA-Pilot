# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2148](https://github.com/tile-ai/tilelang/pull/2148)
- Source page: `sources/prs/tilelang/PR-2148.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2148`
- Generated at: `2026-05-20T15:33:03.874781+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-04T17:28:22Z`
- Merged: `2026-05-07T04:05:30Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: LeiWang1999, Rachmanino, coderabbitai
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-04T17:36:26Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4222133843)
- `2026-05-04T17:57:01Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4222256844)
- `2026-05-06T05:42:17Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4233500765)
- `2026-05-06T05:52:47Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (4) examples/deepseek v4/act quant.py (3) 32-32: 💤 Low value Inconsistent round scale defaults between kernel ... (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4233553244)
- `2026-05-07T04:05:23Z` `APPROVED` by `LeiWang1999` (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4241171174)

## Inline Comment Hotspots

- `examples/deepseek_v4/sparse_attn_fwd_sm90.py`: 4 inline comment(s)
- `examples/deepseek_v4/act_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-06T05:52:47Z` `review` `COMMENTED` by `coderabbitai`; signals: block, correctness, cuda, fp4, fp8, hang, kernel, mla; excerpt: "🧹 Nitpick comments (4) examples/deepseek v4/act quant.py (3) 32-32: 💤 Low value Inconsistent round scale defaults between kernel and wrapper. fp8 quant kernel defaults ..." (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4233553244)
- `2026-05-04T17:28:36Z` `issue` by `coderabbitai`; signals: attention, benchmark, block, correctness, cuda, cute, fp4, fp8; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/tile-ai/tilelang/pull/2148#issuecomment-4373069041)
- `2026-05-04T17:36:25Z` `inline` by `coderabbitai` `examples/deepseek_v4/sparse_attn_fwd_sm90.py`:104; signals: correctness, gemm, memory, nan, perf, sm90, tma; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Unconditional KV gather reads invalid memory when idx == -1 (padding case). The comment on line ..." (https://github.com/tile-ai/tilelang/pull/2148#discussion_r3183328992)
- `2026-05-04T17:36:25Z` `inline` by `coderabbitai` `examples/deepseek_v4/sparse_attn_fwd_sm90.py`:200; signals: benchmark, compile, correctness, dtype, sm90, tile; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win dtype type mismatch between test correctness and benchmark fwd. test correctness converts dtype str to a ..." (https://github.com/tile-ai/tilelang/pull/2148#discussion_r3183328995)
- `2026-05-06T05:42:17Z` `inline` by `coderabbitai` `examples/deepseek_v4/sparse_attn_fwd_sm90.py`:276; signals: attention, benchmark, correctness, oom, sm90; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win CLI default sizes will OOM the PyTorch reference path. The CLI defaults (h=128, n ctx=4096, n ..." (https://github.com/tile-ai/tilelang/pull/2148#discussion_r3193259881)
- `2026-05-06T05:42:17Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, mla, sm90, tile; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4233500765)
- `2026-05-04T17:36:25Z` `inline` by `coderabbitai` `examples/deepseek_v4/sparse_attn_fwd_sm90.py`:61; signals: block, cute, sm90, tile; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: tile-ai/tilelang Length of output: 42 --- 🏁 Script executed: ..." (https://github.com/tile-ai/tilelang/pull/2148#discussion_r3183328986)
- `2026-05-04T17:57:00Z` `inline` by `coderabbitai` `examples/deepseek_v4/act_quant.py`:267; signals: cute, dtype, fp4, tile; excerpt: "⚠️ Potential issue 🔴 Critical 💤 Low value 🧩 Analysis chain 🌐 Web query: PyTorch float4 e2m1fn x2 dtype availability version 💡 Result: The ..." (https://github.com/tile-ai/tilelang/pull/2148#discussion_r3183438639)
- `2026-05-04T17:36:26Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, mla, sm90; excerpt: "Actionable comments posted: 3 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4222133843)
- `2026-05-04T17:57:01Z` `review` `COMMENTED` by `coderabbitai`; signals: hang; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2148#pullrequestreview-4222256844)
- `2026-05-06T05:46:55Z` `issue` by `Rachmanino`; signals: perf, regression; excerpt: "@regression-perf" (https://github.com/tile-ai/tilelang/pull/2148#issuecomment-4385452567)
