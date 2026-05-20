# PR Discussion Digest

- Source PR: [sgl-project/sglang#18070](https://github.com/sgl-project/sglang/pull/18070)
- Source page: `sources/prs/sglang/PR-18070.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18070`
- Generated at: `2026-05-20T15:28:33.116947+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-01T14:11:18Z`
- Merged: `2026-02-19T08:56:06Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=3
- Human participants with discussion text: ispobock, shaharmor98, yizhang2077
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-01T14:14:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a dispatcher for Mamba's selective state update kernel, adding support for a ... (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3735802122)
- `2026-02-09T08:55:21Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3771963541)
- `2026-02-09T13:06:38Z` `COMMENTED` by `shaharmor98` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3773190545)
- `2026-02-09T13:32:38Z` `COMMENTED` by `shaharmor98` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3773319389)
- `2026-02-09T14:44:37Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3773720641)
- `2026-02-10T08:16:12Z` `COMMENTED` by `shaharmor98` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3777376919)
- `2026-02-11T05:22:56Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3782871509)
- `2026-02-12T04:54:51Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3788730966)
- `2026-02-18T01:28:39Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/18070#pullrequestreview-3817177096)

## Inline Comment Hotspots

- `python/sglang/srt/managers/scheduler.py`: 5 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/pyproject.toml`: 2 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/mamba/ops/ssu_dispatch.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-11T09:12:49Z` `issue` by `yizhang2077`; signals: attention, bf16, flashinfer, hang, kernel, nan; excerpt: "Could we integrate this into models like nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16? We need to make sure it will be used. Or will it be integrated in the ..." (https://github.com/sgl-project/sglang/pull/18070#issuecomment-3883183188)
- `2026-02-11T09:21:06Z` `issue` by `shaharmor98`; signals: attention, bf16, flashinfer, hang, kernel, nan; excerpt: "Could we integrate this into models like nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16? We need to make sure it will be used. Or will it be integrated in the ..." (https://github.com/sgl-project/sglang/pull/18070#issuecomment-3883218714)
- `2026-02-12T04:54:34Z` `issue` by `yizhang2077`; signals: attention, bf16, flashinfer, hang, kernel, nan; excerpt: "Could we integrate this into models like nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16? We need to make sure it will be used. Or will it be integrated in the ..." (https://github.com/sgl-project/sglang/pull/18070#issuecomment-3888683010)
- `2026-02-10T08:16:11Z` `inline` by `shaharmor98` `python/sglang/srt/managers/scheduler.py`:499; signals: attention, flashinfer, hang, kernel, triton; excerpt: "Hi @yizhang2077 I'm sorry, but after taking a deeper look, it seems like my proposal won't work. triton is the default mamba-backend kernel, and ..." (https://github.com/sgl-project/sglang/pull/18070#discussion_r2786444915)
- `2026-02-11T07:19:26Z` `issue` by `shaharmor98`; signals: bf16, flashinfer, hang, kernel, nan; excerpt: "Could we integrate this into models like nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16? We need to make sure it will be used. Or will it be integrated in the ..." (https://github.com/sgl-project/sglang/pull/18070#issuecomment-3882770290)
- `2026-02-11T05:26:33Z` `issue` by `yizhang2077`; signals: bf16, nan; excerpt: "Could we integrate this into models like nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16? We need to make sure it will be used. Or will it be integrated in the ..." (https://github.com/sgl-project/sglang/pull/18070#issuecomment-3882246743)
- `2026-02-09T13:32:38Z` `inline` by `shaharmor98` `python/sglang/srt/managers/scheduler.py`:499; signals: hang; excerpt: "Hi @yizhang2077 Thank you for your comment. As I see it, we have two alternatives The first: This is more "rigorous" testing, which ensures ..." (https://github.com/sgl-project/sglang/pull/18070#discussion_r2782657891)
- `2026-02-11T14:11:18Z` `issue` by `ispobock`; signals: flashinfer, hang; excerpt: "@shaharmor98 What flashinfer version is needed for this change? Could you also add a ci test for it?" (https://github.com/sgl-project/sglang/pull/18070#issuecomment-3884680727)
- `2026-02-09T08:54:41Z` `inline` by `yizhang2077` `python/sglang/srt/managers/scheduler.py`:499; signals: general review; excerpt: "maybe we need to rename it maybe xxx, and models which do not use mamba backend do not need to update backend" (https://github.com/sgl-project/sglang/pull/18070#discussion_r2781385969)
- `2026-02-09T08:51:03Z` `inline` by `yizhang2077` `python/pyproject.toml`:24; signals: general review; excerpt: "remove space" (https://github.com/sgl-project/sglang/pull/18070#discussion_r2781370098)
- `2026-02-09T13:06:38Z` `inline` by `shaharmor98` `python/pyproject.toml`:24; signals: general review; excerpt: "My bad" (https://github.com/sgl-project/sglang/pull/18070#discussion_r2782537322)
- `2026-02-09T14:44:37Z` `inline` by `yizhang2077` `python/sglang/srt/managers/scheduler.py`:499; signals: general review; excerpt: "I think the second is ok for me" (https://github.com/sgl-project/sglang/pull/18070#discussion_r2783037420)
