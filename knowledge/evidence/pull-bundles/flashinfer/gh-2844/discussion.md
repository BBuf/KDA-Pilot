# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2844](https://github.com/flashinfer-ai/flashinfer/pull/2844)
- Source page: `sources/prs/flashinfer/PR-2844.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2844`
- Generated at: `2026-05-20T15:25:43.504610+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-20T22:40:45Z`
- Merged: `2026-04-01T17:43:58Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: coderabbitai, saltyminty, sychen52
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-20T22:42:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly adds support for reading the actual strides from key/value block scale tensors ... (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-3984428020)
- `2026-03-20T22:44:27Z` `COMMENTED` by `sychen52` (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-3984431411)
- `2026-03-20T22:47:16Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (2) flashinfer/prefill.py (1) 3712-3715: Consider enforcing these documented stride constraints at ... (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-3984438142)
- `2026-03-24T18:23:06Z` `COMMENTED` by `saltyminty` (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-4001381378)
- `2026-03-24T18:23:31Z` `APPROVED` by `saltyminty` - Approved conditional on merge conflict and CI (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-4001384170)
- `2026-03-24T18:23:39Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-4001385004)
- `2026-03-31T17:26:36Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) csrc/trtllm fmha kernel launcher.cu (1) 90-91: Narrowing conversion from int64 t to int when ... (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-4038922286)

## Inline Comment Hotspots

- `include/flashinfer/trtllm/fmha/kernelParams.h`: 3 inline comment(s)
- `csrc/trtllm_fmha_kernel_launcher.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-20T22:41:00Z` `issue` by `coderabbitai`; signals: attention, block, flashinfer, fp4, hang, kernel, layout, nvfp4; excerpt: "📝 Walkthrough Walkthrough Added four explicit key/value scale-tensor stride fields through the FMHA runner and launcher call chain; KernelParams now uses those fields for ..." (https://github.com/flashinfer-ai/flashinfer/pull/2844#issuecomment-4101311890)
- `2026-03-20T22:47:16Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel, tma; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (2) flashinfer/prefill.py (1) 3712-3715: Consider enforcing these documented stride constraints at runtime. These are hard kernel/TMA requirements; ..." (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-3984438142)
- `2026-03-24T18:23:39Z` `inline` by `coderabbitai` `include/flashinfer/trtllm/fmha/kernelParams.h`:485; signals: flashinfer, kernel, regression, tma; excerpt: "@saltyminty, you're correct — the // FIXME: assume K and V uses the same shape. comment confirms this was a pre-existing known limitation before ..." (https://github.com/flashinfer-ai/flashinfer/pull/2844#discussion_r2983498939)
- `2026-03-31T17:26:36Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel; excerpt: "🧹 Nitpick comments (1) csrc/trtllm fmha kernel launcher.cu (1) 90-91: Narrowing conversion from int64 t to int when assigning to runner params. The launcher ..." (https://github.com/flashinfer-ai/flashinfer/pull/2844#pullrequestreview-4038922286)
- `2026-03-20T22:47:15Z` `inline` by `coderabbitai` `include/flashinfer/trtllm/fmha/kernelParams.h`:485; signals: flashinfer, kernel, tma; excerpt: "⚠️ Potential issue 🔴 Critical V scale-factor TMA descriptor still risks using K strides. You now read kSfStride /vSfStride separately here, but at Line ..." (https://github.com/flashinfer-ai/flashinfer/pull/2844#discussion_r2968271674)
- `2026-03-24T18:23:06Z` `inline` by `saltyminty` `include/flashinfer/trtllm/fmha/kernelParams.h`:485; signals: flashinfer, kernel, regression; excerpt: "Not a new regression I believe (this was already an issue as indicated by the comment on kernelParams.h:732" (https://github.com/flashinfer-ai/flashinfer/pull/2844#discussion_r2983496086)
- `2026-03-20T22:44:27Z` `inline` by `sychen52` `csrc/trtllm_fmha_kernel_launcher.cu`:318; signals: kernel; excerpt: "duplicate twice should be fine. I don't see this being reuse in many places." (https://github.com/flashinfer-ai/flashinfer/pull/2844#discussion_r2968266317)
