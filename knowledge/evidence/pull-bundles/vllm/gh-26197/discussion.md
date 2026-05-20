# PR Discussion Digest

- Source PR: [vllm-project/vllm#26197](https://github.com/vllm-project/vllm/pull/26197)
- Source page: `sources/prs/vllm/PR-26197.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26197`
- Generated at: `2026-05-20T15:38:06.385736+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-03T21:31:02Z`
- Merged: `2025-10-08T07:33:56Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: benchislett, bnellnm, djmmoss, mgoin, yewentao256, youkaichao
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-10-03T21:32:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables E8M0 by default on Hopper for DeepGEMM by unifying the environment variables ... (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3301050604)
- `2025-10-07T15:40:14Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3310745106)
- `2025-10-07T15:40:22Z` `APPROVED` by `bnellnm` - LGTM (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3310745522)
- `2025-10-07T18:20:35Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3311375531)
- `2025-10-07T18:30:51Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3311406414)
- `2025-10-07T19:08:50Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3311516170)
- `2025-10-08T07:33:45Z` `APPROVED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/26197#pullrequestreview-3313396067)

## Inline Comment Hotspots

- `vllm/utils/deep_gemm.py`: 5 inline comment(s)
- `vllm/transformers_utils/config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-03T23:27:27Z` `issue` by `benchislett`; signals: deepgemm, gemm, hang, hopper, speedup; excerpt: "What does this flag actually do on hopper? Looking through the DeepGEMM code at a glance, it seems like E8M0/disabled doesn't change any behaviour. ..." (https://github.com/vllm-project/vllm/pull/26197#issuecomment-3367533243)
- `2025-10-04T15:02:41Z` `issue` by `yewentao256`; signals: deepgemm, gemm, hang, hopper, speedup; excerpt: "What does this flag actually do on hopper? Looking through the DeepGEMM code at a glance, it seems like E8M0/disabled doesn't change any behaviour. ..." (https://github.com/vllm-project/vllm/pull/26197#issuecomment-3368322203)
- `2025-10-07T15:40:14Z` `inline` by `bnellnm` `vllm/utils/deep_gemm.py`:36; signals: deepgemm, flashinfer, gemm, hopper; excerpt: "Was the flashinfer check meant to give flashinfer priority over DeepGEMM or was it to fill the gap on hopper?" (https://github.com/vllm-project/vllm/pull/26197#discussion_r2411076308)
- `2025-10-07T18:20:31Z` `inline` by `yewentao256` `vllm/utils/deep_gemm.py`:36; signals: flashinfer, fp8, gemm, moe; excerpt: "VLLM USE FLASHINFER MOE FP8 has the higher priority" (https://github.com/vllm-project/vllm/pull/26197#discussion_r2411518041)
- `2025-10-04T15:00:49Z` `issue` by `yewentao256`; signals: aligned, hang, hopper, tma; excerpt: "How does this work on Hopper? I think return get mn major tma aligned tensor(sf); doesn't change the e8m0, it just make the TMA-aligned ..." (https://github.com/vllm-project/vllm/pull/26197#issuecomment-3368320946)
- `2025-10-03T23:26:58Z` `issue` by `djmmoss`; signals: hopper, layout; excerpt: "How does this work on Hopper? If I'm not mistaken: and disable the ue8m0 layout on hopper regardless of the flag." (https://github.com/vllm-project/vllm/pull/26197#issuecomment-3367532331)
- `2025-10-07T18:30:51Z` `inline` by `bnellnm` `vllm/utils/deep_gemm.py`:36; signals: gemm; excerpt: "Does that need to go back into the condition then or is it handled elsewhere?" (https://github.com/vllm-project/vllm/pull/26197#discussion_r2411541096)
- `2025-10-07T19:08:48Z` `inline` by `yewentao256` `vllm/utils/deep_gemm.py`:36; signals: gemm; excerpt: "It is handled in We have a double check so this PR removes that" (https://github.com/vllm-project/vllm/pull/26197#discussion_r2411626154)
