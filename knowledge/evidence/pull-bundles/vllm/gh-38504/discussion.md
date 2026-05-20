# PR Discussion Digest

- Source PR: [vllm-project/vllm#38504](https://github.com/vllm-project/vllm/pull/38504)
- Source page: `sources/prs/vllm/PR-38504.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38504`
- Generated at: `2026-05-20T15:40:34.903235+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T04:44:16Z`
- Merged: `2026-04-07T02:57:09Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: AndreasKaratzas, claude, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-30T04:46:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the MoE routing logic to handle bitmatrix-based routing and introduces a mechanism ... (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4027985158)
- `2026-03-30T17:11:10Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4032085844)
- `2026-03-31T14:20:50Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4037781992)
- `2026-03-31T18:33:42Z` `COMMENTED` by `AndreasKaratzas` (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4039313254)
- `2026-04-03T09:28:11Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4055004489)
- `2026-04-03T21:42:56Z` `COMMENTED` by `AndreasKaratzas` (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4057415874)
- `2026-04-07T02:57:01Z` `APPROVED` by `tjtanaa` - LGTM (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4065513047)

## Inline Comment Hotspots

- `vllm/v1/core/sched/scheduler.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-05T06:54:58Z` `issue` by `AndreasKaratzas`; signals: accuracy, benchmark, bf16, fp4, fp8, mxfp4, throughput, triton; excerpt: "GPQA accuracy (amd/gpt-oss-20b-w-mxfp4-a-bf16, TP=2, gfx950, threshold=0.568, tol=0.05) Config main PR branch -------- ------ ----------- mxfp4-bf16-aiter PASSED (0.5739) PASSED (0.5600) mxfp4-bf16-triton PASSED (0.5701) PASSED (0.5726) ..." (https://github.com/vllm-project/vllm/pull/38504#issuecomment-4188419723)
- `2026-04-03T09:28:11Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:191; signals: accuracy, kernel, moe, triton; excerpt: "after you remove this legacy routing from sparsematrix is not used any more. Let's remove it. Moreover, please disclose the accuracy of the models. ..." (https://github.com/vllm-project/vllm/pull/38504#discussion_r3032164982)
- `2026-04-03T21:42:56Z` `inline` by `AndreasKaratzas` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:191; signals: accuracy, kernel, moe, triton; excerpt: "I removed that legacy routing logic. I enabled also GPQA Eval tests too for GPT-OSS accuracy." (https://github.com/vllm-project/vllm/pull/38504#discussion_r3034506971)
- `2026-04-04T02:48:44Z` `issue` by `tjtanaa`; signals: perf, performance; excerpt: "Does it affect performance?" (https://github.com/vllm-project/vllm/pull/38504#issuecomment-4186099774)
- `2026-03-30T17:11:10Z` `review` `COMMENTED` by `claude`; signals: general review; excerpt: "Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer can comment @claude review to run ..." (https://github.com/vllm-project/vllm/pull/38504#pullrequestreview-4032085844)
- `2026-03-31T14:20:51Z` `inline` by `tjtanaa` `vllm/v1/core/sched/scheduler.py`:1863; signals: hang; excerpt: "are these changes from the other PR ?" (https://github.com/vllm-project/vllm/pull/38504#discussion_r3016250909)
- `2026-04-04T02:52:12Z` `issue` by `AndreasKaratzas`; signals: accuracy; excerpt: "@tjtanaa Actually I was about to cite the tests regarding accuracy, but think I got to rebase first to get clean logs:" (https://github.com/vllm-project/vllm/pull/38504#issuecomment-4186108845)
- `2026-03-31T18:33:42Z` `inline` by `AndreasKaratzas` `vllm/v1/core/sched/scheduler.py`:1863; signals: general review; excerpt: "Yep, you're right, I reverted that." (https://github.com/vllm-project/vllm/pull/38504#discussion_r3017628976)
