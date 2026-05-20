# PR Discussion Digest

- Source PR: [sgl-project/sglang#12543](https://github.com/sgl-project/sglang/pull/12543)
- Source page: `sources/prs/sglang/PR-12543.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12543`
- Generated at: `2026-05-20T15:27:39.742333+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-03T08:37:38Z`
- Merged: `2025-11-13T11:44:44Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: FlamingoPg, Fridge003, samuellees, yizhang2077
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-03T08:40:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables the Flashinfer TRTLLM-GEN-MoE FP8 blockwise kernel, specifically for Qwen3-Next on Blackwell hardware, ... (https://github.com/sgl-project/sglang/pull/12543#pullrequestreview-3409929081)
- `2025-11-03T08:40:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables the Flashinfer TRTLLM-GEN-MoE FP8 blockwise kernel for Qwen3-Next models on Blackwell hardware, ... (https://github.com/sgl-project/sglang/pull/12543#pullrequestreview-3409929345)
- `2025-11-07T07:15:49Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/12543#pullrequestreview-3432021665)
- `2025-11-08T13:17:38Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/12543#pullrequestreview-3438349188)
- `2025-11-12T07:24:32Z` `APPROVED` by `yizhang2077` - LGTM (https://github.com/sgl-project/sglang/pull/12543#pullrequestreview-3451988586)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8.py`: 2 inline comment(s)
- `python/sglang/srt/models/qwen2_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-07T07:15:40Z` `inline` by `yizhang2077` `python/sglang/srt/models/qwen2_moe.py`:170; signals: b200, moe; excerpt: "could you add a ut? Ref test qwen3 next models.py, you need split a separate file and add it into run suite.py b200 part." (https://github.com/sgl-project/sglang/pull/12543#discussion_r2501942030)
- `2025-11-08T13:17:38Z` `inline` by `samuellees` `python/sglang/srt/models/qwen2_moe.py`:170; signals: moe; excerpt: "Done." (https://github.com/sgl-project/sglang/pull/12543#discussion_r2506915373)
- `2025-11-08T19:11:20Z` `issue` by `Fridge003`; signals: b200; excerpt: "@samuellees Please move the test to nightly-4-gpu-b200 suite" (https://github.com/sgl-project/sglang/pull/12543#issuecomment-3506810771)
- `2025-11-09T10:04:39Z` `issue` by `samuellees`; signals: b200; excerpt: "@samuellees Please move the test to nightly-4-gpu-b200 suite Done" (https://github.com/sgl-project/sglang/pull/12543#issuecomment-3507884627)
