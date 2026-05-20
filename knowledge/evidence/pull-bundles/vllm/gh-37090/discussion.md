# PR Discussion Digest

- Source PR: [vllm-project/vllm#37090](https://github.com/vllm-project/vllm/pull/37090)
- Source page: `sources/prs/vllm/PR-37090.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37090`
- Generated at: `2026-05-20T15:40:17.881586+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-15T03:08:51Z`
- Merged: `2026-03-16T17:03:10Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: haosdent, mergify, orozery
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-15T03:20:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug causing garbage output with MLA models when KV offloading is ... (https://github.com/vllm-project/vllm/pull/37090#pullrequestreview-3949640103)
- `2026-03-16T10:49:18Z` `APPROVED` by `orozery` - Thanks again @haosdent ! (https://github.com/vllm-project/vllm/pull/37090#pullrequestreview-3952989107)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-03-16T07:18:05Z` `issue` by `orozery`; signals: block, cache, kernel, kv cache, mla; excerpt: "Hi, @orozery, I checked again, and this approach does not seem to work. The identity permutation still allocates a single cross-layer tensor. Slicing tensor[i] ..." (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4065602193)
- `2026-03-16T06:43:59Z` `issue` by `orozery`; signals: hang, kernel, mla; excerpt: "@haosdent thanks for this fix! I was able to reproduce the issue. I was not aware that MLA kernels did not support cross layers. ..." (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4065443443)
- `2026-03-16T06:53:22Z` `issue` by `haosdent`; signals: block, kernel, mla; excerpt: "However, instead of returning NotImplementedError, I think we should return the identity permutation (e.g. (0, 1, 2, ...)). This will yield contiguous per-layer tensors. ..." (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4065476524)
- `2026-03-16T08:41:23Z` `issue` by `orozery`; signals: cache, kv cache, layout; excerpt: "@haosdent LGTM! Can we just move the new unit tests to a new e.g. tests/v1/kv connector/unit/test kv cache layout.py ?" (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4066012645)
- `2026-03-16T09:20:08Z` `issue` by `haosdent`; signals: cache, kv cache, layout; excerpt: "Can we just move the new unit tests to a new e.g. tests/v1/kv connector/unit/test kv cache layout.py ? Done, thanks @orozery" (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4066218378)
- `2026-03-15T15:39:00Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @haosdent, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4063246648)
- `2026-03-16T06:47:30Z` `issue` by `haosdent`; signals: general review; excerpt: "However, instead of returning NotImplementedError, I think we should return the identity permutation (e.g. (0, 1, 2, ...)). This will yield contiguous per-layer tensors. ..." (https://github.com/vllm-project/vllm/pull/37090#issuecomment-4065456177)
