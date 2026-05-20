# PR Discussion Digest

- Source PR: [vllm-project/vllm#35271](https://github.com/vllm-project/vllm/pull/35271)
- Source page: `sources/prs/vllm/PR-35271.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35271`
- Generated at: `2026-05-20T15:39:59.981010+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-25T08:19:14Z`
- Merged: `2026-02-28T10:12:01Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 13
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=5
- Human participants with discussion text: LucasWilkinson, chaunceyjiang, haosdent
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-25T08:22:02Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces PyTorch-based fallback implementations for fp8 mqa logits and fp8 paged mqa logits, ... (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3852610997)
- `2026-02-25T09:08:23Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3852833917)
- `2026-02-25T09:14:27Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3852866122)
- `2026-02-26T02:03:57Z` `COMMENTED` by `chaunceyjiang` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3857985978)
- `2026-02-26T03:30:11Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3858204568)
- `2026-02-26T03:32:03Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3858207790)
- `2026-02-26T03:32:39Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3858208884)
- `2026-02-26T03:40:17Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3858222651)
- `2026-02-26T07:01:28Z` `COMMENTED` by `chaunceyjiang` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3858863428)
- `2026-02-26T07:06:18Z` `COMMENTED` by `haosdent` (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3858878523)
- `2026-02-28T04:12:43Z` `APPROVED` by `LucasWilkinson` - LGTM, thanks for doing this! (https://github.com/vllm-project/vllm/pull/35271#pullrequestreview-3870042008)

## Inline Comment Hotspots

- `vllm/model_executor/layers/sparse_attn_indexer.py`: 8 inline comment(s)
- `vllm/utils/deep_gemm.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-02-26T03:32:03Z` `inline` by `haosdent` `vllm/model_executor/layers/sparse_attn_indexer.py`:304; signals: gemm, sm90; excerpt: "And we may need to distinguish 2 different cases. For sm90+ that support deep gemm, still need to show a warning instead of a ..." (https://github.com/vllm-project/vllm/pull/35271#discussion_r2856693792)
- `2026-02-26T03:32:39Z` `inline` by `haosdent` `vllm/utils/deep_gemm.py`:453; signals: cuda, gemm; excerpt: "May use device=q.device instead of device="cuda"" (https://github.com/vllm-project/vllm/pull/35271#discussion_r2856694982)
- `2026-02-25T09:08:23Z` `inline` by `haosdent` `vllm/model_executor/layers/sparse_attn_indexer.py`:111; signals: gemm; excerpt: "I think use is deep gemm supported is better, because has deep gemm would be true if the package is installed, even if sm80 ..." (https://github.com/vllm-project/vllm/pull/35271#discussion_r2851745743)
- `2026-02-26T03:30:11Z` `inline` by `haosdent` `vllm/model_executor/layers/sparse_attn_indexer.py`:304; signals: gemm; excerpt: "Should we update the warning as well? Because in A100, even deep gemm is installed, it would not work." (https://github.com/vllm-project/vllm/pull/35271#discussion_r2856690450)
- `2026-02-26T03:40:17Z` `inline` by `haosdent` `vllm/model_executor/layers/sparse_attn_indexer.py`:176; signals: fp8; excerpt: "Maybe we could do the fallback inside fp8 paged mqa logits like this capsuled internally Same to fp8 mqa logits, but I am fine ..." (https://github.com/vllm-project/vllm/pull/35271#discussion_r2856709266)
- `2026-02-26T07:01:27Z` `inline` by `chaunceyjiang` `vllm/model_executor/layers/sparse_attn_indexer.py`:176; signals: gemm; excerpt: "That was actually how I wrote it at first, but I felt it wasn’t consistent with the style of the other deep gemm functions. ..." (https://github.com/vllm-project/vllm/pull/35271#discussion_r2857288432)
- `2026-02-25T09:14:26Z` `inline` by `haosdent` `vllm/model_executor/layers/sparse_attn_indexer.py`:111; signals: general review; excerpt: "May need to update as well" (https://github.com/vllm-project/vllm/pull/35271#discussion_r2851776477)
- `2026-02-26T02:03:57Z` `inline` by `chaunceyjiang` `vllm/model_executor/layers/sparse_attn_indexer.py`:111; signals: general review; excerpt: "Done." (https://github.com/vllm-project/vllm/pull/35271#discussion_r2856486137)
- `2026-02-26T07:06:18Z` `inline` by `haosdent` `vllm/model_executor/layers/sparse_attn_indexer.py`:176; signals: general review; excerpt: "I see" (https://github.com/vllm-project/vllm/pull/35271#discussion_r2857302822)
