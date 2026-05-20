# PR Discussion Digest

- Source PR: [sgl-project/sglang#13264](https://github.com/sgl-project/sglang/pull/13264)
- Source page: `sources/prs/sglang/PR-13264.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13264`
- Generated at: `2026-05-20T15:27:46.210427+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T07:05:39Z`
- Merged: `2025-11-18T00:13:28Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Fridge003, Kangyan-Zhou, kaixih, zhyncs
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-14T07:19:54Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3463204007)
- `2025-11-15T07:14:29Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3467815283)
- `2025-11-15T08:37:26Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3467861935)
- `2025-11-15T09:38:06Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3467891705)
- `2025-11-17T21:21:33Z` `COMMENTED` by `Kangyan-Zhou` (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3474605636)
- `2025-11-17T22:47:51Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3474832525)
- `2025-11-17T23:05:29Z` `COMMENTED` by `Kangyan-Zhou` - Can we add deepseek-ai/DeepSeek-R1-0528 to scripts/ci/validate and download models.py under 8-gpu-b200? (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3474865041)

## Inline Comment Hotspots

- `test/srt/test_deepseek_r1_fp8_trtllm_backend.py`: 2 inline comment(s)
- `test/srt/run_suite.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-15T08:37:25Z` `inline` by `kaixih` `test/srt/test_deepseek_r1_fp8_trtllm_backend.py`:1; signals: blackwell, fp8, h200, hang; excerpt: "File name changed. Didn't move it to H200 since this trtllm backend only works with blackwell for now." (https://github.com/sgl-project/sglang/pull/13264#discussion_r2529706499)
- `2025-11-14T07:29:08Z` `issue` by `Fridge003`; signals: fp8, mla, moe; excerpt: "@kaixih Can we add a nightly test for dpsk fp8 w/ trtllm moe & trtllm mla attn" (https://github.com/sgl-project/sglang/pull/13264#issuecomment-3531298813)
- `2025-11-14T22:57:28Z` `issue` by `kaixih`; signals: fp8, mla, moe; excerpt: "@kaixih Can we add a nightly test for dpsk fp8 w/ trtllm moe & trtllm mla attn Done, PTAL." (https://github.com/sgl-project/sglang/pull/13264#issuecomment-3534977453)
- `2025-11-15T07:13:38Z` `inline` by `Fridge003` `test/srt/test_deepseek_r1_fp8_trtllm_backend.py`:1; signals: fp8, h200; excerpt: "Maybe renaming this test to test deepseek r1 fp8 trtllm backend.py Can we move it to 8-gpu H200 nightly test, since this is an ..." (https://github.com/sgl-project/sglang/pull/13264#discussion_r2529665973)
- `2025-11-17T23:05:29Z` `review` `COMMENTED` by `Kangyan-Zhou`; signals: b200; excerpt: "Can we add deepseek-ai/DeepSeek-R1-0528 to scripts/ci/validate and download models.py under 8-gpu-b200?" (https://github.com/sgl-project/sglang/pull/13264#pullrequestreview-3474865041)
- `2025-11-17T21:21:34Z` `inline` by `Kangyan-Zhou` `test/srt/run_suite.py`:181; signals: b200; excerpt: "Can we add this to the nightly test instead? We only have one 8-gpu-b200 runner and this would slow down the pr merge process" (https://github.com/sgl-project/sglang/pull/13264#discussion_r2535551439)
- `2025-11-17T22:47:51Z` `inline` by `Fridge003` `test/srt/run_suite.py`:181; signals: block; excerpt: "Sure, I can move it back if it can be blocker" (https://github.com/sgl-project/sglang/pull/13264#discussion_r2535741915)
- `2025-11-15T22:18:03Z` `issue` by `Fridge003`; signals: b200; excerpt: "@kaixih we just added a 8-gpu b200 runner. I just moved this test there, and also we can move it from nightly to per-commit ..." (https://github.com/sgl-project/sglang/pull/13264#issuecomment-3536970184)
- `2025-11-14T07:06:22Z` `issue` by `kaixih`; signals: race; excerpt: "@gracehonv @Fridge003" (https://github.com/sgl-project/sglang/pull/13264#issuecomment-3531215590)
- `2025-11-17T23:15:05Z` `issue` by `Fridge003`; signals: general review; excerpt: "@Kangyan-Zhou We can just use deepseek-v3. I don't find any specific reason for using dpsk-r1 rather than dpsk-v3. Just updated" (https://github.com/sgl-project/sglang/pull/13264#issuecomment-3544246261)
