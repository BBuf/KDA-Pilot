# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1322](https://github.com/flashinfer-ai/flashinfer/pull/1322)
- Source page: `sources/prs/flashinfer/PR-1322.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1322`
- Generated at: `2026-05-20T15:22:18.612796+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-24T20:25:47Z`
- Merged: `2025-09-08T18:25:05Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: Edenzzzz, yyihuang, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-24T20:26:02Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Edenzzzz, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3053172958)
- `2025-07-24T20:27:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds k scale and v scale parameters to the BatchAttention.run method for scaling ... (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3053177146)
- `2025-07-25T11:17:44Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3055032828)
- `2025-08-02T16:32:44Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3081140752)
- `2025-09-08T03:02:12Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3194818429)
- `2025-09-08T03:18:13Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3194844646)
- `2025-09-08T18:24:52Z` `APPROVED` by `yzh119` - LGTM, thanks for the contribution. (https://github.com/flashinfer-ai/flashinfer/pull/1322#pullrequestreview-3197645809)

## Inline Comment Hotspots

- `flashinfer/attention.py`: 4 inline comment(s)
- `tests/test_batch_attention.py`: 2 inline comment(s)
- `csrc/batch_attention.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-25T11:17:37Z` `inline` by `yzh119` `flashinfer/attention.py`:179; signals: attention, bf16, dtype, flashinfer, fp8, kernel; excerpt: "Can you also implement fusing the multiply inside the kernel in the persistent kernel template? Also, it will be good to specify an out ..." (https://github.com/flashinfer-ai/flashinfer/pull/1322#discussion_r2230832944)
- `2025-09-08T03:02:12Z` `inline` by `Edenzzzz` `tests/test_batch_attention.py`:144; signals: attention, kernel, oom; excerpt: "when running the test, the prefill kernel allocator hit OOM, which seems unrelated to this PR (also hit on main), so I increased the ..." (https://github.com/flashinfer-ai/flashinfer/pull/1322#discussion_r2329028175)
- `2025-09-08T18:24:12Z` `inline` by `yzh119` `csrc/batch_attention.cu`:72; signals: attention, cuda, cudagraph; excerpt: "We should add the option of making this value (v scale) and sm scale on device to make sure we support dynamic scale in ..." (https://github.com/flashinfer-ai/flashinfer/pull/1322#discussion_r2331028736)
- `2025-08-02T16:32:44Z` `inline` by `Edenzzzz` `flashinfer/attention.py`:179; signals: attention, dtype, flashinfer; excerpt: "In that case we need to pass in out dtype during plan? Which can be troublesome" (https://github.com/flashinfer-ai/flashinfer/pull/1322#discussion_r2249313615)
- `2025-09-08T03:04:47Z` `issue` by `Edenzzzz`; signals: b200, kernel; excerpt: "Hi @yzh119 I fused v scale into the kernel and tests pass on b200" (https://github.com/flashinfer-ai/flashinfer/pull/1322#issuecomment-3264415903)
- `2025-09-08T03:18:13Z` `inline` by `yzh119` `tests/test_batch_attention.py`:144; signals: attention; excerpt: "Np, please go ahead with it." (https://github.com/flashinfer-ai/flashinfer/pull/1322#discussion_r2329045033)
- `2025-07-25T04:28:07Z` `issue` by `yyihuang`; signals: tma; excerpt: "I think it's better to keep only one pre-fused param as attn softmax scale, with some examples here:" (https://github.com/flashinfer-ai/flashinfer/pull/1322#issuecomment-3116347655)
