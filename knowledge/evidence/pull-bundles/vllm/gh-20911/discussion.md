# PR Discussion Digest

- Source PR: [vllm-project/vllm#20911](https://github.com/vllm-project/vllm/pull/20911)
- Source page: `sources/prs/vllm/PR-20911.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20911`
- Generated at: `2026-05-20T15:36:16.617257+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-14T07:58:58Z`
- Merged: `2025-07-18T04:34:44Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: djmmoss, mgoin, shixianc
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-14T07:59:42Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @shixianc, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3015164934)
- `2025-07-14T08:02:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces an optimization to swap A and B matrices in CUTLASS MoE grouped ... (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3015172323)
- `2025-07-17T18:49:33Z` `APPROVED` by `djmmoss` - @shixianc can you also run these please? if those looks good then I am happy (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3030638472)
- `2025-07-17T19:04:11Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3030674341)
- `2025-07-17T19:52:50Z` `COMMENTED` by `shixianc` (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3030833197)
- `2025-07-17T20:38:20Z` `COMMENTED` by `shixianc` (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3030950563)
- `2025-07-17T20:45:01Z` `APPROVED` by `mgoin` - LGTM, nice work! Evals and benchmarks look good (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3030965906)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x.cu`: 5 inline comment(s)
- `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`: 3 inline comment(s)

## High-Signal Discussion

- `2025-07-17T19:52:50Z` `inline` by `shixianc` `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x.cu`:39; signals: cutlass, moe, tile; excerpt: "yup, the requirement on tile n only has to be multiple of 16, and tuning shows it's actually better .." (https://github.com/vllm-project/vllm/pull/20911#discussion_r2214171465)
- `2025-07-17T19:01:05Z` `inline` by `mgoin` `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x.cu`:39; signals: cutlass, moe; excerpt: "I did not know you could go down to 16 😲" (https://github.com/vllm-project/vllm/pull/20911#discussion_r2214074796)
- `2025-07-17T19:02:46Z` `inline` by `mgoin` `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x.cu`:143; signals: cutlass, moe; excerpt: "I assume the ordering is intentional to enforce swap ab. Could you leave a comment for this?" (https://github.com/vllm-project/vllm/pull/20911#discussion_r2214077578)
- `2025-07-17T20:38:20Z` `inline` by `shixianc` `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x.cu`:143; signals: cutlass, moe; excerpt: "Added" (https://github.com/vllm-project/vllm/pull/20911#discussion_r2214250101)
- `2025-07-17T20:35:53Z` `issue` by `shixianc`; signals: cutlass, moe; excerpt: "@shixianc can you also run these please? if those looks good then I am happy test cutlass moe.py was run in the PR description. ..." (https://github.com/vllm-project/vllm/pull/20911#issuecomment-3085397002)
- `2025-07-18T03:34:44Z` `issue` by `shixianc`; signals: hang; excerpt: "@mgoin I took a look at the error msgs [distributed-tests-4-gpus]( and doesn't seem to be related to my change. might need your help for ..." (https://github.com/vllm-project/vllm/pull/20911#issuecomment-3086587679)
- `2025-07-17T20:45:01Z` `review` `APPROVED` by `mgoin`; signals: benchmark; excerpt: "LGTM, nice work! Evals and benchmarks look good" (https://github.com/vllm-project/vllm/pull/20911#pullrequestreview-3030965906)
