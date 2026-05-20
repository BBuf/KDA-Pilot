# PR Discussion Digest

- Source PR: [sgl-project/sglang#17353](https://github.com/sgl-project/sglang/pull/17353)
- Source page: `sources/prs/sglang/PR-17353.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17353`
- Generated at: `2026-05-20T15:28:29.134125+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-19T12:37:42Z`
- Merged: `2026-01-24T07:25:03Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 4 (approved=2, changes_requested=1, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: BBuf, Fridge003, johnnynunez, merrymercy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-19T12:50:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request moves the FlashAttention v4 implementation from sgl-kernel to a new jit kernel directory ... (https://github.com/sgl-project/sglang/pull/17353#pullrequestreview-3677961046)
- `2026-01-19T21:32:46Z` `CHANGES_REQUESTED` by `zhyncs` - This change looks good. In the future, we can evolve FA4 independently in the JIT kernel. Given that ... (https://github.com/sgl-project/sglang/pull/17353#pullrequestreview-3679668699)
- `2026-01-20T07:45:04Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/17353#pullrequestreview-3680788880)
- `2026-01-24T07:23:03Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/17353#pullrequestreview-3700938758)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/flash_attention_v4.py`: 1 inline comment(s)
- `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/flashattention_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-20T06:22:31Z` `issue` by `BBuf`; signals: attention, cute, flash attention, hang, kernel; excerpt: "This change looks good. In the future, we can evolve FA4 independently in the JIT kernel. Given that the new FA4 has a different ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3771230787)
- `2026-01-21T01:49:16Z` `issue` by `BBuf`; signals: cute, cutlass, hang, kernel; excerpt: "I think that at some point, we can move everything to cute dsl, so It would be nice to remove C++ FA from sglang ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3775744718)
- `2026-01-21T02:52:56Z` `issue` by `johnnynunez`; signals: cute, cutlass, hang, kernel; excerpt: "I think that at some point, we can move everything to cute dsl, so It would be nice to remove C++ FA from sglang ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3775893098)
- `2026-01-19T21:32:46Z` `review` `CHANGES_REQUESTED` by `zhyncs`; signals: hang, kernel; excerpt: "This change looks good. In the future, we can evolve FA4 independently in the JIT kernel. Given that the new FA4 has a different ..." (https://github.com/sgl-project/sglang/pull/17353#pullrequestreview-3679668699)
- `2026-01-20T07:49:52Z` `issue` by `merrymercy`; signals: hang, kernel, nan; excerpt: "We do not guarantee any backward compatbility of an experimental API (early FA4) in sgl kernel for other non-sglang projects, so I believe we ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3771502332)
- `2026-01-20T11:48:02Z` `issue` by `johnnynunez`; signals: cute, cutlass, hang; excerpt: "I think that at some point, we can move everything to cute dsl, so It would be nice to remove C++ FA from sglang ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3772479652)
- `2026-01-20T06:26:55Z` `issue` by `zhyncs`; signals: hang, kernel; excerpt: "@BBuf Thanks for the explanation. I agree that FA4 should evolve independently and should not be upgraded or released from sgl-kernel. My point about ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3771241443)
- `2026-01-20T09:04:13Z` `issue` by `BBuf`; signals: hang, kernel; excerpt: "@BBuf Thanks for the explanation. I agree that FA4 should evolve independently and should not be upgraded or released from sgl-kernel. My point about ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3771778019)
- `2026-01-21T12:31:03Z` `issue` by `johnnynunez`; signals: hang, kernel; excerpt: "The problem that I see here is that the API is still beta and not all features are available, so in sgl-kernel, we point ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3777873558)
- `2026-01-21T12:33:54Z` `issue` by `BBuf`; signals: hang, kernel; excerpt: "The problem that I see here is that the API is still beta and not all features are available, so in sgl-kernel, we point ..." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3777890199)
- `2026-01-19T12:44:58Z` `issue` by `Fridge003`; signals: block, kernel; excerpt: "Nice, we definitely need this. In this way the update of fa4 won't be blocked by sgl-kernel update" (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3768162797)
- `2026-01-24T07:18:07Z` `issue` by `BBuf`; signals: hang; excerpt: "@zhyncs The request change has been solved and ci passed too. Can you give me a approve? Thanks." (https://github.com/sgl-project/sglang/pull/17353#issuecomment-3794041203)
