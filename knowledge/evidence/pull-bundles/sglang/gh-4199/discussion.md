# PR Discussion Digest

- Source PR: [sgl-project/sglang#4199](https://github.com/sgl-project/sglang/pull/4199)
- Source page: `sources/prs/sglang/PR-4199.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4199`
- Generated at: `2026-05-20T15:30:07.132616+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-08T07:36:02Z`
- Merged: `2025-03-11T07:38:37Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 6 (approved=1, changes_requested=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: merrymercy, sleepcoo, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-10T07:43:59Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2670036692)
- `2025-03-10T08:20:19Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2670110820)
- `2025-03-10T08:31:52Z` `COMMENTED` by `sleepcoo` (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2670137631)
- `2025-03-10T10:40:04Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2670498541)
- `2025-03-10T21:28:43Z` `CHANGES_REQUESTED` by `zhyncs` - - ut can't pass on H200 - torch compile not compatible python3 -m sglang.launch server --model deepseek-ai/DeepSeek-R1 --tp ... (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2672244937)
- `2025-03-11T07:38:00Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2673191199)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_kernel.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-03-10T08:31:52Z` `inline` by `sleepcoo` `python/sglang/srt/layers/quantization/fp8_kernel.py`:21; signals: deepgemm, fp8, gemm, hang, kernel; excerpt: "Currently, installing deepgemm via 3rd party is quite tricky. Could we change it to import deep gemm from sgl kernel? In your opinion, which ..." (https://github.com/sgl-project/sglang/pull/4199#discussion_r1986817771)
- `2025-03-10T08:20:12Z` `inline` by `merrymercy` `python/sglang/srt/layers/quantization/fp8_kernel.py`:21; signals: fp8, gemm, kernel; excerpt: "is it possible to do from sgl kernel import deep gemm?" (https://github.com/sgl-project/sglang/pull/4199#discussion_r1986801542)
- `2025-03-10T21:28:43Z` `review` `CHANGES_REQUESTED` by `zhyncs`; signals: compile, h200; excerpt: "- ut can't pass on H200 - torch compile not compatible python3 -m sglang.launch server --model deepseek-ai/DeepSeek-R1 --tp 8 --trust-remote-code --enable-torch-compile --torch-compile-max-bs 1" (https://github.com/sgl-project/sglang/pull/4199#pullrequestreview-2672244937)
- `2025-03-10T07:43:59Z` `inline` by `zhyncs` `python/sglang/srt/layers/quantization/fp8_kernel.py`:733; signals: fp8, kernel; excerpt: "This is a duplicate. Please delete line 726 of the code." (https://github.com/sgl-project/sglang/pull/4199#discussion_r1986755934)
- `2025-03-10T10:40:03Z` `inline` by `merrymercy` `python/sglang/srt/layers/quantization/fp8_kernel.py`:21; signals: fp8, kernel; excerpt: "Getting better speed has a higher priority" (https://github.com/sgl-project/sglang/pull/4199#discussion_r1987030459)
- `2025-03-10T10:40:36Z` `issue` by `merrymercy`; signals: block, kernel; excerpt: "I tried to release a new version of sgl kernel to unblock this. But I hit some errors Will need @zhyncs 's help." (https://github.com/sgl-project/sglang/pull/4199#issuecomment-2710138619)
- `2025-03-11T04:45:07Z` `issue` by `sleepcoo`; signals: compile, h200; excerpt: "ut can't pass on H200 torch compile not compatible python3 -m sglang.launch server --model deepseek-ai/DeepSeek-R1 --tp 8 --trust-remote-code --enable-torch-compile --torch-compile-max-bs 1 wait this" (https://github.com/sgl-project/sglang/pull/4199#issuecomment-2712609172)
- `2025-03-11T07:36:41Z` `issue` by `zhyncs`; signals: hopper, oom; excerpt: "There are still many issues to be fixed in this PR, such as the condition of arch older than hopper, oom of ut, etc., ..." (https://github.com/sgl-project/sglang/pull/4199#issuecomment-2712991159)
