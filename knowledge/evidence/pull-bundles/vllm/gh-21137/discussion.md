# PR Discussion Digest

- Source PR: [vllm-project/vllm#21137](https://github.com/vllm-project/vllm/pull/21137)
- Source page: `sources/prs/vllm/PR-21137.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21137`
- Generated at: `2026-05-20T15:36:30.074447+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-17T20:31:02Z`
- Merged: `2025-07-24T10:21:46Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LucasWilkinson, WoosukKwon, fhl2000, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-17T20:32:50Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request is a significant and well-executed refactoring of the attention backend infrastructure. The primary ... (https://github.com/vllm-project/vllm/pull/21137#pullrequestreview-3030930021)
- `2025-07-18T04:50:12Z` `COMMENTED` by `WoosukKwon` - BTW why don't we use Numpy instead of PyTorch CPU tensors? Except for some edge cases, Numpy is ... (https://github.com/vllm-project/vllm/pull/21137#pullrequestreview-3031793497)
- `2025-07-23T16:31:34Z` `APPROVED` by `mgoin` - Looks good to me, thanks! After review the amount of work we have to do on the CPU ... (https://github.com/vllm-project/vllm/pull/21137#pullrequestreview-3048211522)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-07-18T12:14:58Z` `issue` by `LucasWilkinson`; signals: attention, block, cache, cuda, cudagraph, flashinfer; excerpt: "Could we still pass the device tensors to Flashinfer's plan() rather than host tensors? Because we might want to support full cudagraph of Flashinfer ..." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3089290704)
- `2025-07-18T13:00:07Z` `issue` by `fhl2000`; signals: cache, cuda, cudagraph, flashinfer; excerpt: "If I remember correctly, Sglang's implementation overrides the plan functions that still pass host-side persistent buffers, Oh my bad! Sorry, I was saying they ..." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3089413100)
- `2025-07-18T14:16:07Z` `issue` by `LucasWilkinson`; signals: cache, cuda, cudagraph, flashinfer; excerpt: "If I remember correctly, Sglang's implementation overrides the plan functions that still pass host-side persistent buffers, Oh my bad! Sorry, I was saying they ..." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3089625567)
- `2025-07-18T09:48:50Z` `issue` by `fhl2000`; signals: cuda, cudagraph, flashinfer; excerpt: "Could we still pass the device tensors to Flashinfer's plan() rather than host tensors? Because we might want to support full cudagraph of Flashinfer ..." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3088842427)
- `2025-07-18T04:50:12Z` `review` `COMMENTED` by `WoosukKwon`; signals: general review; excerpt: "BTW why don't we use Numpy instead of PyTorch CPU tensors? Except for some edge cases, Numpy is usually faster in my experience." (https://github.com/vllm-project/vllm/pull/21137#pullrequestreview-3031793497)
- `2025-07-18T11:18:20Z` `issue` by `LucasWilkinson`; signals: flashinfer; excerpt: "BTW why don't we use Numpy instead of PyTorch CPU tensors? Except for some edge cases, Numpy is usually faster in my experience. Ive ..." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3089133617)
- `2025-07-18T16:06:29Z` `issue` by `mgoin`; signals: flashinfer; excerpt: "Could you make sure to test the trtllm case in the flashinfer backend as well? Just want to make sure this choice is preferable ..." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3089956617)
- `2025-07-17T20:31:38Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @LucasWilkinson." (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3085381710)
- `2025-07-23T15:43:29Z` `issue` by `LucasWilkinson`; signals: general review; excerpt: "@mgoin looks good 👍 I think we should land this since its a win and I can follow up if using numpy helps" (https://github.com/vllm-project/vllm/pull/21137#issuecomment-3109179985)
- `2025-07-23T16:31:34Z` `review` `APPROVED` by `mgoin`; signals: general review; excerpt: "Looks good to me, thanks! After review the amount of work we have to do on the CPU is more than I expected, so ..." (https://github.com/vllm-project/vllm/pull/21137#pullrequestreview-3048211522)
