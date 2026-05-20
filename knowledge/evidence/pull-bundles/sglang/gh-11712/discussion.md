# PR Discussion Digest

- Source PR: [sgl-project/sglang#11712](https://github.com/sgl-project/sglang/pull/11712)
- Source page: `sources/prs/sglang/PR-11712.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11712`
- Generated at: `2026-05-20T15:27:25.294444+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-16T09:34:14Z`
- Merged: `2026-02-03T19:15:15Z`

## Discussion Counts

- Issue comments: 34
- Review submissions: 15 (approved=1, changes_requested=1, commented=13)
- Inline review comments: 16
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=0, outdated=10
- Human participants with discussion text: 1pikachu, Kangyan-Zhou, airMeng, chunyuan-w, mingfeima, ping1jing2
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-07T02:35:21Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431329760)
- `2025-11-07T02:39:33Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431342159)
- `2025-11-07T02:41:38Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431345503)
- `2025-11-07T02:44:58Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431350088)
- `2025-11-07T02:49:19Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431356593)
- `2025-11-07T02:49:34Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431357439)
- `2025-11-07T02:49:46Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431357944)
- `2025-11-07T02:51:13Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431361464)
- `2025-11-07T02:52:56Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431364302)
- `2025-11-07T02:56:03Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431370546)
- `2025-11-07T06:48:55Z` `CHANGES_REQUESTED` by `mingfeima` - generally LGTM, just some minor changes required. (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431762723)
- `2025-11-25T02:29:55Z` `COMMENTED` by `1pikachu` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3503035563)
- `2025-12-22T05:44:13Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3602759058)
- `2026-01-30T05:46:16Z` `COMMENTED` by `Kangyan-Zhou` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3726475556)
- `2026-01-30T06:02:11Z` `COMMENTED` by `1pikachu` (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3726520901)

## Inline Comment Hotspots

- `python/sglang/test/test_utils.py`: 8 inline comment(s)
- `test/registered/layers/mamba/test_causal_conv1d.py`: 4 inline comment(s)
- `test/registered/attention/test_create_kvindices.py`: 1 inline comment(s)
- `test/srt/test_get_weights_by_name.py`: 1 inline comment(s)
- `test/srt/layers/attention/mamba/test_causal_conv1d.py`: 1 inline comment(s)
- `test/srt/test_forward_split_prefill.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-07T02:49:18Z` `inline` by `chunyuan-w` `test/registered/layers/mamba/test_causal_conv1d.py`:158; signals: cuda, register; excerpt: "By removing this check, are we expecting this test to run on all devices, or only on cuda and xpu?" (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501503546)
- `2025-11-07T02:51:13Z` `inline` by `chunyuan-w` `test/registered/attention/test_create_kvindices.py`:19; signals: attention, register; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501506431)
- `2025-11-25T02:29:55Z` `inline` by `1pikachu` `test/registered/layers/mamba/test_causal_conv1d.py`:158; signals: cuda, register; excerpt: "This case is only in CUDA CI." (https://github.com/sgl-project/sglang/pull/11712#discussion_r2558352430)
- `2025-11-07T06:48:55Z` `review` `CHANGES_REQUESTED` by `mingfeima`; signals: hang; excerpt: "generally LGTM, just some minor changes required." (https://github.com/sgl-project/sglang/pull/11712#pullrequestreview-3431762723)
- `2025-11-07T02:56:03Z` `inline` by `chunyuan-w` `test/srt/layers/attention/mamba/test_causal_conv1d.py`:19; signals: attention; excerpt: "I feel like you could add a util function for this device setting in python/sglang/test/test utils.py and then you can reuse this util function ..." (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501512932)
- `2026-01-30T06:02:11Z` `inline` by `1pikachu` `python/sglang/test/test_utils.py`:1477; signals: hang; excerpt: "The main issue is here: This change here may not be ideal, but I think we should not fall back to CPU and should ..." (https://github.com/sgl-project/sglang/pull/11712#discussion_r2744771454)
- `2025-11-07T02:49:34Z` `inline` by `chunyuan-w` `test/registered/layers/mamba/test_causal_conv1d.py`:197; signals: register; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501504047)
- `2025-11-07T02:49:46Z` `inline` by `chunyuan-w` `test/registered/layers/mamba/test_causal_conv1d.py`:277; signals: register; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501504368)
- `2025-11-24T02:26:46Z` `issue` by `mingfeima`; signals: cache; excerpt: "this PR should be ready within for the current context. but is it possible to leverage for example torch.accelerator.empty cache(). The code would be ..." (https://github.com/sgl-project/sglang/pull/11712#issuecomment-3568720839)
- `2026-02-02T22:40:56Z` `issue` by `Kangyan-Zhou`; signals: hang; excerpt: "Hello, @Kangyan-Zhou Those PR issues aren’t caused by my change. Could you help review it? Yes I think the PR generally looks good, just ..." (https://github.com/sgl-project/sglang/pull/11712#issuecomment-3837662206)
- `2025-11-07T02:35:21Z` `inline` by `chunyuan-w` `python/sglang/test/test_utils.py`:1845; signals: general review; excerpt: "The function is getting device count, not the current rank or device index. I feel like it's better to name the function to something ..." (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501484749)
- `2025-11-07T02:52:56Z` `inline` by `chunyuan-w` `test/srt/test_get_weights_by_name.py`:25; signals: general review; excerpt: "You've added this util function in python/sglang/test/test utils.py in this PR. Can we directly reuse that one?" (https://github.com/sgl-project/sglang/pull/11712#discussion_r2501508699)
