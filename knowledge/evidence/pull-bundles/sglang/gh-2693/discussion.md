# PR Discussion Digest

- Source PR: [sgl-project/sglang#2693](https://github.com/sgl-project/sglang/pull/2693)
- Source page: `sources/prs/sglang/PR-2693.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-2693`
- Generated at: `2026-05-20T15:29:55.951769+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-01T07:59:42Z`
- Merged: `2025-02-24T05:56:30Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: Edenzzzz, Ying1123, gmlwns2000, lambert0312, merrymercy, msharmavikram, shensimeteor, wangyibin-gh, xiezhq-hermann, zhaohaidao, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 10

## Review Decisions

- `2025-01-02T22:46:55Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/2693#pullrequestreview-2528320370)
- `2025-01-04T09:25:14Z` `COMMENTED` by `zhaohaidao` (https://github.com/sgl-project/sglang/pull/2693#pullrequestreview-2530488820)
- `2025-01-15T08:41:55Z` `COMMENTED` by `xiezhq-hermann` (https://github.com/sgl-project/sglang/pull/2693#pullrequestreview-2551882191)
- `2025-02-24T05:44:43Z` `APPROVED` by `Ying1123` (https://github.com/sgl-project/sglang/pull/2693#pullrequestreview-2636049219)

## Inline Comment Hotspots

- `python/sglang/srt/mem_cache/radix_cache.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-01-22T03:05:02Z` `issue` by `msharmavikram`; signals: attention, block, cache, cuda, kernel, kv cache, memory, perf; excerpt: "Hi, Thanks for the great work. I am leaving a comment because my team is working on something similar. As I understand your PR, ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2606187846)
- `2025-01-10T13:08:47Z` `issue` by `gmlwns2000`; signals: attention, block, cuda, kernel, perf, performance, throughput; excerpt: "Hi, Thanks for the great work. I am leaving a comment because my team is working on something similar. As I understand your PR, ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2582677770)
- `2025-01-15T08:18:11Z` `issue` by `xiezhq-hermann`; signals: attention, block, cuda, kernel, perf, performance, throughput; excerpt: "Hi, Thanks for the great work. I am leaving a comment because my team is working on something similar. As I understand your PR, ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2591906951)
- `2025-01-28T06:40:17Z` `issue` by `xiezhq-hermann`; signals: benchmark, cache, latency, perf, performance, throughput; excerpt: "After code cleaning and basic performance benchmark, this PR is ready to merge. You can add --enable-hierarchical-cache option when starting a SGLang server to ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2618050205)
- `2025-01-22T06:14:30Z` `issue` by `gmlwns2000`; signals: attention, cache, kv cache, memory; excerpt: "@msharmavikram Thanks for advice! I was planning to make a new PR (Adding HiP attention, Support training-free context extension, Support UVM KV cache offloading ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2606384154)
- `2025-01-26T15:43:59Z` `issue` by `gmlwns2000`; signals: cache, cuda, latency; excerpt: "@Edenzzzz Yes, I used cudaMemAdvise to make the pages stay mostly in the CPU. So, if what I understand is correct, the latency should ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2614474909)
- `2025-01-07T08:33:55Z` `issue` by `xiezhq-hermann`; signals: perf, performance; excerpt: "While collecting performance numbers, I am breaking this PR into multiple small ones for easier reviewing (WIP): ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2574681412)
- `2025-01-26T14:32:59Z` `issue` by `Edenzzzz`; signals: cache, cuda; excerpt: "Hierarchical caching and UVM caching are not the same. Hierarchical caching can use UVM caching as a mechanism or can do without UVM. What ..." (https://github.com/sgl-project/sglang/pull/2693#issuecomment-2614449434)
- `2025-01-04T09:03:37Z` `inline` by `zhaohaidao` `python/sglang/srt/mem_cache/radix_cache.py`:572; signals: cache; excerpt: "I'm not sure if I understand it correctly, based on the function naming, shouldn't it return not self.loading?" (https://github.com/sgl-project/sglang/pull/2693#discussion_r1902888361)
- `2025-01-02T22:46:49Z` `inline` by `merrymercy` `python/sglang/srt/mem_cache/radix_cache.py`:356; signals: cache; excerpt: "move this to a separate file?" (https://github.com/sgl-project/sglang/pull/2693#discussion_r1901325750)
- `2025-01-04T08:50:32Z` `inline` by `zhaohaidao` `python/sglang/srt/mem_cache/radix_cache.py`:59; signals: cache; excerpt: "If I understand correctly, self.writing = False here shouldn't be commented?" (https://github.com/sgl-project/sglang/pull/2693#discussion_r1902866946)
- `2025-01-15T08:41:55Z` `inline` by `xiezhq-hermann` `python/sglang/srt/mem_cache/radix_cache.py`:572; signals: cache; excerpt: "it's correct thanks for the catch!" (https://github.com/sgl-project/sglang/pull/2693#discussion_r1916147093)
