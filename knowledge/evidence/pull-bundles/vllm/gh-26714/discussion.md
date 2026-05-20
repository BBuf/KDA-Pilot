# PR Discussion Digest

- Source PR: [vllm-project/vllm#26714](https://github.com/vllm-project/vllm/pull/26714)
- Source page: `sources/prs/vllm/PR-26714.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26714`
- Generated at: `2026-05-20T15:38:08.235587+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-13T16:21:31Z`
- Merged: `2025-10-16T23:20:25Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: benchislett, jiahanc, mgoin
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-14T17:49:59Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/26714#pullrequestreview-3336829600)
- `2025-10-15T02:29:50Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26714#pullrequestreview-3338140469)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/trtllm_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-14T17:49:59Z` `inline` by `jiahanc` `vllm/model_executor/layers/fused_moe/trtllm_moe.py`:68; signals: flashinfer, moe, tile; excerpt: "Removed the get tile tokens dim because this logic is now in flashinfer, passing None to let flashinfer calculate automatically" (https://github.com/vllm-project/vllm/pull/26714#discussion_r2429992857)
- `2025-10-14T18:28:55Z` `issue` by `jiahanc`; signals: benchmark, flashinfer, kernel; excerpt: "flashinfer kernel benchmark:" (https://github.com/vllm-project/vllm/pull/26714#issuecomment-3403110635)
- `2025-10-16T22:17:42Z` `issue` by `mgoin`; signals: flashinfer; excerpt: "Yes thanks for the ping, just had to restart it to pick up the flashinfer-cubin==0.4.1 release that wasn't available before. Running gpt-oss eval now ..." (https://github.com/vllm-project/vllm/pull/26714#issuecomment-3413040733)
- `2025-10-13T16:35:54Z` `issue` by `jiahanc`; signals: benchmark; excerpt: "E2E benchmark on random 1024/1024 dataset using vllm serve + vllm bench serve on GPT-OSS-120B" (https://github.com/vllm-project/vllm/pull/26714#issuecomment-3398232525)
- `2025-10-16T06:24:56Z` `issue` by `jiahanc`; signals: general review; excerpt: "@mgoin the failed test is a 400 Bad request. looks like the request has some error rather than the vLLM server. It seems not ..." (https://github.com/vllm-project/vllm/pull/26714#issuecomment-3409358064)
