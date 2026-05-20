# PR Discussion Digest

- Source PR: [vllm-project/vllm#26891](https://github.com/vllm-project/vllm/pull/26891)
- Source page: `sources/prs/vllm/PR-26891.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26891`
- Generated at: `2026-05-20T15:38:09.858013+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-15T07:47:16Z`
- Merged: `2025-10-15T17:06:18Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-15T07:49:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables tensor parallelism for nv-fp4 MoE layers by removing several assertions in ModelOptNvFp4FusedMoE.process ... (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3338893012)
- `2025-10-15T14:46:05Z` `APPROVED` by `mgoin` - It looks like these asserts aren't present in the compressed-tensors backend and I was able to run vllm ... (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3340821781)
- `2025-10-15T17:04:15Z` `COMMENTED` by `pavanimajety` - Agree, it's the weight that should be divisble by 16, not the weight scale. Why are we removing ... (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3341471300)
- `2025-10-15T17:05:37Z` `APPROVED` by `pavanimajety` - It seems like the dtype check is happening in swizzle blockscale. (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3341476777)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-10-15T17:04:15Z` `review` `COMMENTED` by `pavanimajety`; signals: dtype; excerpt: "Agree, it's the weight that should be divisble by 16, not the weight scale. Why are we removing the dtype assertion?" (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3341471300)
- `2025-10-15T14:46:05Z` `review` `APPROVED` by `mgoin`; signals: fp4, nvfp4; excerpt: "It looks like these asserts aren't present in the compressed-tensors backend and I was able to run vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 -tp 2 fine, so ..." (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3340821781)
- `2025-10-15T17:05:37Z` `review` `APPROVED` by `pavanimajety`; signals: block, dtype; excerpt: "It seems like the dtype check is happening in swizzle blockscale." (https://github.com/vllm-project/vllm/pull/26891#pullrequestreview-3341476777)
