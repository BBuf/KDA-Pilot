# PR Discussion Digest

- Source PR: [vllm-project/vllm#28701](https://github.com/vllm-project/vllm/pull/28701)
- Source page: `sources/prs/vllm/PR-28701.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28701`
- Generated at: `2026-05-20T15:38:32.010064+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T04:39:00Z`
- Merged: `2025-11-19T19:59:31Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: SageMoore, chatgpt-codex-connector, gshtras, maleksan85, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-14T17:57:22Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3466103568)
- `2025-11-17T10:30:13Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3472047000)
- `2025-11-17T22:33:22Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3474800729)
- `2025-11-18T08:16:25Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3476089614)
- `2025-11-18T16:28:18Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3478692065)
- `2025-11-18T20:07:57Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3479598404)
- `2025-11-18T20:11:13Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3479617666)
- `2025-11-19T00:38:33Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3480228038)
- `2025-11-19T02:03:06Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3480428219)
- `2025-11-19T03:31:29Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3480669591)
- `2025-11-19T17:19:33Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3483919726)
- `2025-11-19T17:43:49Z` `APPROVED` by `gshtras` (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3484009043)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/triton_mla.py`: 8 inline comment(s)
- `vllm/v1/attention/backends/mla/aiter_triton_mla.py`: 2 inline comment(s)
- `vllm/platforms/rocm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-18T08:16:25Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/mla/aiter_triton_mla.py`:24; signals: accuracy, attention, flash attention, hang, mla, triton; excerpt: "Could I know if you are intending to use AITER's mla decode or vLLM's triton mla decode backend? From my understanding, what this PR ..." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2536789154)
- `2025-11-14T17:57:22Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/triton_mla.py`:103; signals: attention, mla, triton; excerpt: "and return only the attention output. The caller still expects a tuple and may crash or operate on a tensor without the LSE needed ..." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2528430790)
- `2025-11-18T16:28:18Z` `inline` by `maleksan85` `vllm/v1/attention/backends/mla/aiter_triton_mla.py`:24; signals: attention, mla, triton; excerpt: "no, added Trtiton MLA is particular for prefills in AITER MLA. In order to get alternative and upstream from internal fork." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2538880686)
- `2025-11-18T20:07:57Z` `inline` by `gshtras` `vllm/v1/attention/backends/mla/triton_mla.py`:44; signals: attention, mla, triton; excerpt: "Why not make it a separate backend class, since it's a separate implementation? Since there seem to now be: triton MLA AITER mla AITER ..." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2539563954)
- `2025-11-19T02:03:06Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/mla/triton_mla.py`:44; signals: attention, mla, triton; excerpt: "@maleksan85 Thank you for the consideration. To add on, vLLM offers an explicit backend selection feature through VLLM ATTENTION BACKEND (this is for all ..." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2540209902)
- `2025-11-17T10:30:13Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/mla/triton_mla.py`:62; signals: attention, mla, triton; excerpt: "Let's separate out into another class called aiter triton mla.py" (https://github.com/vllm-project/vllm/pull/28701#discussion_r2533538937)
- `2025-11-17T22:33:22Z` `inline` by `maleksan85` `vllm/v1/attention/backends/mla/triton_mla.py`:62; signals: attention, mla, triton; excerpt: "sure, extracted" (https://github.com/vllm-project/vllm/pull/28701#discussion_r2535713722)
- `2025-11-18T20:11:13Z` `inline` by `maleksan85` `vllm/v1/attention/backends/mla/triton_mla.py`:44; signals: attention, mla, triton; excerpt: "just tried to avoid adding new flag as upstream do not appreciate new flags." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2539581566)
- `2025-11-19T00:38:33Z` `inline` by `maleksan85` `vllm/v1/attention/backends/mla/triton_mla.py`:44; signals: attention, mla, triton; excerpt: "refactored" (https://github.com/vllm-project/vllm/pull/28701#discussion_r2540055509)
- `2025-11-19T17:19:33Z` `inline` by `maleksan85` `vllm/v1/attention/backends/mla/triton_mla.py`:44; signals: attention, mla, triton; excerpt: "yep, did that in the last revision, thanks!" (https://github.com/vllm-project/vllm/pull/28701#discussion_r2542925440)
- `2025-11-14T17:57:22Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28701#pullrequestreview-3466103568)
- `2025-11-14T17:57:22Z` `inline` by `chatgpt-codex-connector` `vllm/platforms/rocm.py`:240; signals: general review; excerpt: ". Useful? React with 👍 / 👎." (https://github.com/vllm-project/vllm/pull/28701#discussion_r2528430778)
