# PR Discussion Digest

- Source PR: [sgl-project/sglang#5086](https://github.com/sgl-project/sglang/pull/5086)
- Source page: `sources/prs/sglang/PR-5086.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5086`
- Generated at: `2026-05-20T15:30:20.003894+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-05T15:48:28Z`
- Merged: `2025-04-10T00:59:36Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 22
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=6
- Human participants with discussion text: BBuf, FlamingoPg, fzyzcjy, merrymercy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-04-09T10:34:37Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2752996164)
- `2025-04-09T11:09:14Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753096601)
- `2025-04-09T11:11:38Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753102197)
- `2025-04-09T11:12:57Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753105292)
- `2025-04-09T11:13:29Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753106579)
- `2025-04-09T11:13:37Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753106923)
- `2025-04-09T11:14:18Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753108776)
- `2025-04-09T12:46:26Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753352124)
- `2025-04-09T12:49:57Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753363704)
- `2025-04-09T12:50:19Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753364889)
- `2025-04-09T15:36:49Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753929239)
- `2025-04-09T15:37:18Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2753930613)
- `2025-04-09T16:37:53Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/5086#pullrequestreview-2754106603)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/moe_align_kernel.cu`: 13 inline comment(s)
- `sgl-kernel/benchmark/bench_moe_align_block_size.py`: 9 inline comment(s)

## High-Signal Discussion

- `2025-04-06T13:49:55Z` `issue` by `BBuf`; signals: benchmark, block, h200, hang, kernel, moe, perf, performance; excerpt: "@zhyncs @merrymercy Now, I have fixed all the bug and performace bug in sgl kernel moe align block size kernel. It can be seen ..." (https://github.com/sgl-project/sglang/pull/5086#issuecomment-2781434388)
- `2025-04-09T11:11:38Z` `inline` by `BBuf` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:200; signals: kernel, memory, moe, perf, race; excerpt: "After removing this previously, we found that if synchronization is not performed after writing, there will be illegal memory access after running fused MoE ..." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035142195)
- `2025-04-09T10:30:54Z` `inline` by `fzyzcjy` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:384; signals: benchmark, block, hang, kernel, moe; excerpt: "nit: curious why do we change the defaults (seems 256 experts w/ 8 topk is the value for deepseek)" (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035080599)
- `2025-04-09T10:30:53Z` `inline` by `fzyzcjy` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:301; signals: benchmark, block, kernel, moe; excerpt: "nit: maybe I do not get it, it seems it is a torch.empty instead of torch.zeros, so wondering whether the name is "with empty" ..." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035080561)
- `2025-04-09T15:36:49Z` `inline` by `BBuf` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:123; signals: benchmark, kernel, moe, speedup; excerpt: "That makes sense, done! I have gained some speedup in small batch expert mode, and the benchmark has been updated above." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035640594)
- `2025-04-09T10:31:03Z` `inline` by `fzyzcjy` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:391; signals: benchmark, block, kernel, moe; excerpt: "(same as above)" (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035080826)
- `2025-04-09T10:31:08Z` `inline` by `fzyzcjy` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:391; signals: benchmark, block, kernel, moe; excerpt: "(same as above)" (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035080926)
- `2025-04-09T11:12:56Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:301; signals: benchmark, block, kernel, moe; excerpt: "Make sense, I will fix it." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035144169)
- `2025-04-09T11:13:29Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:384; signals: benchmark, block, kernel, moe; excerpt: "I'll revert it." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035144991)
- `2025-04-09T11:13:37Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:391; signals: benchmark, block, kernel, moe; excerpt: "I'll revert it too." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035145206)
- `2025-04-09T11:14:18Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:391; signals: benchmark, block, kernel, moe; excerpt: "I'll revert it too." (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035146240)
- `2025-04-09T12:50:19Z` `inline` by `fzyzcjy` `sgl-kernel/benchmark/bench_moe_align_block_size.py`:391; signals: benchmark, block, kernel, moe; excerpt: "(ignore this - dnk why my comment is repeated twice for L391...)" (https://github.com/sgl-project/sglang/pull/5086#discussion_r2035302671)
