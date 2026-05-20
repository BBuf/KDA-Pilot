# PR Discussion Digest

- Source PR: [vllm-project/vllm#42810](https://github.com/vllm-project/vllm/pull/42810)
- Source page: `sources/prs/vllm/PR-42810.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-42810`
- Generated at: `2026-05-20T15:41:00.988204+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-16T03:23:07Z`
- Merged: `2026-05-17T16:18:50Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: mergify, tjtanaa, zyongye
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-16T03:24:15Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4302565063)
- `2026-05-16T03:25:26Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4302566938)
- `2026-05-16T03:26:07Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4302567884)
- `2026-05-16T03:26:35Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4302568338)
- `2026-05-16T03:26:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request disables the aiter implementation for MHC layers due to accuracy issues and refactors ... (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4302568422)
- `2026-05-16T03:27:34Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4302569135)
- `2026-05-16T15:22:19Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4303821220)
- `2026-05-17T16:18:36Z` `APPROVED` by `zyongye` (https://github.com/vllm-project/vllm/pull/42810#pullrequestreview-4305750722)

## Inline Comment Hotspots

- `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`: 5 inline comment(s)
- `vllm/model_executor/layers/sparse_attn_indexer.py`: 1 inline comment(s)
- `vllm/model_executor/layers/mhc.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-16T03:24:15Z` `inline` by `tjtanaa` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:545; signals: aligned, attention, mla; excerpt: "This is a fixed to the reference topk indices torch so that it is aligned with the torch.ops. C.top k per row prefill implementation." (https://github.com/vllm-project/vllm/pull/42810#discussion_r3251930729)
- `2026-05-16T03:26:07Z` `inline` by `tjtanaa` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:590; signals: attention, cuda, mla; excerpt: "I have cleaned up the function interface following the CUDA's sparse attn indexer fake and sparse attn indexer implementation." (https://github.com/vllm-project/vllm/pull/42810#discussion_r3251932735)
- `2026-05-16T03:25:26Z` `inline` by `tjtanaa` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:583; signals: attention, mla; excerpt: "Since torch.ops. C.top k per row prefill supports general values of topk tokens, we can call it all the time. Not just when topk ..." (https://github.com/vllm-project/vllm/pull/42810#discussion_r3251932022)
- `2026-05-16T03:26:35Z` `inline` by `tjtanaa` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:841; signals: attention, mla; excerpt: "Chores: We don't need another layer of wrapper." (https://github.com/vllm-project/vllm/pull/42810#discussion_r3251933340)
- `2026-05-16T15:31:44Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @tjtanaa, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/42810#issuecomment-4467276439)
- `2026-05-16T15:22:19Z` `inline` by `tjtanaa` `vllm/model_executor/layers/mhc.py`:82; signals: compile; excerpt: "It is not very slow as right now with graph mode and torch compile, this op is optimized to be better than regular torch." (https://github.com/vllm-project/vllm/pull/42810#discussion_r3253004744)
- `2026-05-16T03:27:34Z` `inline` by `tjtanaa` `vllm/model_executor/layers/sparse_attn_indexer.py`:525; signals: kernel; excerpt: "Right now, DSA is only supported using AITER kernels." (https://github.com/vllm-project/vllm/pull/42810#discussion_r3251934289)
