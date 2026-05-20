# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2882](https://github.com/flashinfer-ai/flashinfer/pull/2882)
- Source page: `sources/prs/flashinfer/PR-2882.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2882`
- Generated at: `2026-05-20T15:25:48.702449+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T18:39:42Z`
- Merged: `2026-04-14T04:20:41Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: aleozlx, coderabbitai, danisereb
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-24T18:42:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request removes the restriction on using non-gated activations for FP8 per-tensor MoE configurations. However, ... (https://github.com/flashinfer-ai/flashinfer/pull/2882#pullrequestreview-4001504656)
- `2026-03-24T19:09:00Z` `COMMENTED` by `danisereb` (https://github.com/flashinfer-ai/flashinfer/pull/2882#pullrequestreview-4001664939)
- `2026-03-24T20:37:09Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2882#pullrequestreview-4002131218)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-24T18:39:51Z` `issue` by `coderabbitai`; signals: flashinfer, fp8, hang, kernel, moe; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/flashinfer-ai/flashinfer/pull/2882#issuecomment-4120563606)
- `2026-03-24T19:09:00Z` `inline` by `danisereb` `csrc/trtllm_fused_moe_kernel_launcher.cu`:2273; signals: flashinfer, hang, kernel, moe; excerpt: "This seems like a pre-existing bug from v0.6.4 In order to reduce the risk of changes, I will not fix this issue in this ..." (https://github.com/flashinfer-ai/flashinfer/pull/2882#discussion_r2983724769)
- `2026-04-13T04:19:28Z` `issue` by `aleozlx`; signals: block; excerpt: "CI was blocked on a known irrelevant nvshm compilation error. restarted CI and waiting for auto-merge" (https://github.com/flashinfer-ai/flashinfer/pull/2882#issuecomment-4233799827)
