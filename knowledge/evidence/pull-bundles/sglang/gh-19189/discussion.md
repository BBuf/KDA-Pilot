# PR Discussion Digest

- Source PR: [sgl-project/sglang#19189](https://github.com/sgl-project/sglang/pull/19189)
- Source page: `sources/prs/sglang/PR-19189.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19189`
- Generated at: `2026-05-20T15:28:47.229970+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-23T18:50:05Z`
- Merged: `2026-03-06T23:15:04Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, nvpohanh, wenscarl
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T18:53:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix an issue with the flashinfer autotuner by ensuring the hidden ... (https://github.com/sgl-project/sglang/pull/19189#pullrequestreview-3842917652)
- `2026-02-24T08:03:21Z` `APPROVED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/19189#pullrequestreview-3845843368)
- `2026-03-06T00:11:39Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19189#pullrequestreview-3900403314)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-02T07:09:25Z` `issue` by `nvpohanh`; signals: block, flashinfer; excerpt: "@wenscarl Could you update the PR description? Credits to @danisereb. Depends on flashinfer fix: This line makes me wonder if this is blocked by ..." (https://github.com/sgl-project/sglang/pull/19189#issuecomment-3982552407)
- `2026-03-02T07:09:55Z` `issue` by `nvpohanh`; signals: hang, moe; excerpt: "@Fridge003 Could you assign this to the MoE expert for review? This is a small change. Thanks!" (https://github.com/sgl-project/sglang/pull/19189#issuecomment-3982554001)
- `2026-02-24T08:04:13Z` `issue` by `nvpohanh`; signals: flashinfer; excerpt: "@wenscarl Should we mark this PR as DRAFT until FlashInfer PR has been merged and SGLang has upgraded to a new FlashInfer version containing ..." (https://github.com/sgl-project/sglang/pull/19189#issuecomment-3949902059)
- `2026-02-25T13:06:26Z` `issue` by `wenscarl`; signals: flashinfer; excerpt: "@nvpohanh Actually this PR doesn't rely on flashinfer fix or update which add coverage to the cases when the first dim is not power ..." (https://github.com/sgl-project/sglang/pull/19189#issuecomment-3959141703)
