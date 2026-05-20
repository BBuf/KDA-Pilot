# PR Discussion Digest

- Source PR: [sgl-project/sglang#18442](https://github.com/sgl-project/sglang/pull/18442)
- Source page: `sources/prs/sglang/PR-18442.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18442`
- Generated at: `2026-05-20T15:28:38.532598+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-08T08:53:54Z`
- Merged: `2026-03-02T01:12:19Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=7
- Human participants with discussion text: BBuf, Kangyan-Zhou, Ratish1, ShangmingCai, b8zhong, mmangkad, zwang86
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-08T08:56:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces paged KV cache support for FlashAttention 4 on SM90 (Hopper) GPUs, which ... (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3769253714)
- `2026-02-15T04:55:08Z` `APPROVED` by `BBuf` - Looks good. (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3803413803)
- `2026-02-15T18:28:00Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3805290274)
- `2026-02-15T18:28:46Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3805290979)
- `2026-02-19T03:05:21Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3823270581)
- `2026-02-19T03:05:51Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3823271806)
- `2026-02-19T03:06:19Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3823272622)
- `2026-02-19T03:06:46Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3823273582)
- `2026-02-19T03:07:33Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18442#pullrequestreview-3823275036)

## Inline Comment Hotspots

- `docs/advanced_features/attention_backend.md`: 6 inline comment(s)
- `python/sglang/jit_kernel/flash_attention/cute/interface.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-11T08:58:54Z` `issue` by `zwang86`; signals: benchmark, block, cache, cute, fp8, h100, hang, kernel; excerpt: "@mmangkad @b8zhong Per your request, I benchmarked FA3 vs FA4 on H100 (SM90) using Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 with output lengths from 512 to 16384 tokens. Key ..." (https://github.com/sgl-project/sglang/pull/18442#issuecomment-3883124945)
- `2026-02-15T09:13:27Z` `issue` by `zwang86`; signals: attention, b200, compile, cute, flash attention, hang, kernel, perf; excerpt: "Changes in this PR - python/sglang/jit kernel/flash attention/cute/flash fwd.py — paged KV support for FA4 SM90 - python/sglang/jit kernel/flash attention/cute/interface.py — page size validation ..." (https://github.com/sgl-project/sglang/pull/18442#issuecomment-3903886346)
- `2026-02-15T18:28:46Z` `inline` by `b8zhong` `docs/advanced_features/attention_backend.md`:61; signals: attention, sm90; excerpt: "You could delete For MHA models on SM90+, FA4 can also handle both prefill and decode natively with --attention-backend fa4 --page-size 128., as you ..." (https://github.com/sgl-project/sglang/pull/18442#discussion_r2809794207)
- `2026-02-15T18:28:00Z` `inline` by `b8zhong` `docs/advanced_features/attention_backend.md`:52; signals: attention, sm100; excerpt: "Hi, I believe SM100 FA4 supports page size = 1" (https://github.com/sgl-project/sglang/pull/18442#discussion_r2809793586)
- `2026-03-01T21:10:43Z` `issue` by `zwang86`; signals: failing, regression; excerpt: "@Kangyan-Zhou test lora tp.py is failing consistently on main as well (partition 2 in stage-b-test-large-2-gpu), this probably is a pre-existing regression unrelated to this ..." (https://github.com/sgl-project/sglang/pull/18442#issuecomment-3981034200)
- `2026-03-01T22:54:46Z` `issue` by `Kangyan-Zhou`; signals: failing, regression; excerpt: "@Kangyan-Zhou test lora tp.py is failing consistently on main as well (partition 2 in stage-b-test-large-2-gpu), this probably is a pre-existing regression unrelated to this ..." (https://github.com/sgl-project/sglang/pull/18442#issuecomment-3981222623)
- `2026-03-01T06:08:37Z` `issue` by `Kangyan-Zhou`; signals: hang; excerpt: "seems to be a consistent failure after this change" (https://github.com/sgl-project/sglang/pull/18442#issuecomment-3979227157)
- `2026-02-09T21:15:54Z` `issue` by `b8zhong`; signals: general review; excerpt: "Yes I agree with @mmangkad , I found that the decoding phase would slow down a lot at 2048 output (and beyond) You can ..." (https://github.com/sgl-project/sglang/pull/18442#issuecomment-3873906936)
