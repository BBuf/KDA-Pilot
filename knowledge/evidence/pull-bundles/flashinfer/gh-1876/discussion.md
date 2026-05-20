# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1876](https://github.com/flashinfer-ai/flashinfer/pull/1876)
- Source page: `sources/prs/flashinfer/PR-1876.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1876`
- Generated at: `2026-05-20T15:23:31.586686+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-06T17:46:43Z`
- Merged: `2025-10-20T07:13:23Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=1
- Human participants with discussion text: ChristinaZ, pavanimajety, wenscarl, yzh119
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-06T18:02:58Z` `COMMENTED` by `pavanimajety` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3306363711)
- `2025-10-09T22:27:23Z` `COMMENTED` by `pavanimajety` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3320816475)
- `2025-10-09T22:32:57Z` `COMMENTED` by `pavanimajety` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3320827538)
- `2025-10-09T22:36:32Z` `COMMENTED` by `pavanimajety` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3320835456)
- `2025-10-10T12:45:07Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3323198862)
- `2025-10-10T12:45:12Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3323199514)
- `2025-10-10T12:58:43Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3323288273)
- `2025-10-10T12:59:23Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3323293027)
- `2025-10-10T16:54:26Z` `COMMENTED` by `pavanimajety` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3324783736)
- `2025-10-10T16:55:40Z` `APPROVED` by `pavanimajety` - LGTM, thanks @wenscarl and @ChristinaZ for making the required changes! (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3324789154)
- `2025-10-20T07:13:21Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3355249625)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 7 inline comment(s)
- `csrc/trtllm_fused_moe_runner.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-10T12:58:43Z` `inline` by `ChristinaZ` `csrc/trtllm_fused_moe_kernel_launcher.cu`:194; signals: block, fp4, fp8, kernel, moe, mxfp4, nvfp4; excerpt: "I think use deep seek fp8=True means the blockscale fp8. We set use deep seek fp8=False for all other cases like per-tensor FP8, nvfp4, ..." (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2420033018)
- `2025-10-06T18:02:58Z` `inline` by `pavanimajety` `csrc/trtllm_fused_moe_kernel_launcher.cu`:113; signals: dtype, kernel, moe; excerpt: "When would routing bias not have value? Can we combine the statements and ensure that we always follow the dtype specified as the routing ..." (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2407747531)
- `2025-10-09T22:32:57Z` `inline` by `pavanimajety` `csrc/trtllm_fused_moe_kernel_launcher.cu`:194; signals: fp8, kernel, moe; excerpt: "does use deep seek fp8=False mean per-tensor FP8?" (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2418095410)
- `2025-10-09T22:36:33Z` `inline` by `pavanimajety` `csrc/trtllm_fused_moe_kernel_launcher.cu`:459; signals: fp8, kernel, moe; excerpt: "Nit: Can we mention use routing scales on input and use deep seek fp8 here as well as comments?" (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2418100036)
- `2025-10-10T12:45:12Z` `inline` by `ChristinaZ` `csrc/trtllm_fused_moe_kernel_launcher.cu`:113; signals: kernel, moe; excerpt: "When the routing method is not deepseek (for example, renormalize routing method), the routing bias does not have value." (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2419954810)
- `2025-10-10T16:54:25Z` `inline` by `pavanimajety` `csrc/trtllm_fused_moe_kernel_launcher.cu`:194; signals: kernel, moe; excerpt: "Does it make more sense to make it more explicit by making it an Enum? Probably for future, not in this PR" (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2421236141)
- `2025-10-10T12:45:07Z` `inline` by `ChristinaZ` `csrc/trtllm_fused_moe_runner.cu`:66; signals: kernel, moe; excerpt: "For the routing part, it's the output data type of the routing kernel." (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2419954260)
- `2025-10-10T12:59:23Z` `inline` by `ChristinaZ` `csrc/trtllm_fused_moe_kernel_launcher.cu`:459; signals: kernel, moe; excerpt: "Yes, agree. It's better that we can add comments on them." (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2420037299)
- `2025-10-09T22:39:59Z` `issue` by `pavanimajety`; signals: hang, moe; excerpt: "@ChristinaZ Thanks for making changes across all MOE runners!" (https://github.com/flashinfer-ai/flashinfer/pull/1876#issuecomment-3387699607)
- `2025-10-09T22:27:23Z` `inline` by `pavanimajety` `csrc/trtllm_fused_moe_runner.cu`:66; signals: moe; excerpt: "what is expW?" (https://github.com/flashinfer-ai/flashinfer/pull/1876#discussion_r2418088631)
- `2025-10-10T16:55:40Z` `review` `APPROVED` by `pavanimajety`; signals: hang; excerpt: "LGTM, thanks @wenscarl and @ChristinaZ for making the required changes!" (https://github.com/flashinfer-ai/flashinfer/pull/1876#pullrequestreview-3324789154)
