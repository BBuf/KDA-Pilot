# PR Discussion Digest

- Source PR: [sgl-project/sglang#14162](https://github.com/sgl-project/sglang/pull/14162)
- Source page: `sources/prs/sglang/PR-14162.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14162`
- Generated at: `2026-05-20T15:27:57.043721+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-30T07:40:26Z`
- Merged: `2026-03-30T14:27:29Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=2, changes_requested=1, commented=5)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=0, outdated=4
- Human participants with discussion text: BBuf
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-30T07:43:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant performance optimization for DeepSeek-R1-0528-W4AFP8 models by enabling FP8 communication for ... (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-3521144812)
- `2026-03-25T03:12:13Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4003635882)
- `2026-03-25T03:12:24Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4003636303)
- `2026-03-25T03:13:05Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4003637782)
- `2026-03-25T03:13:27Z` `CHANGES_REQUESTED` by `BBuf` - The direction makes sense, but I think this still needs a pass on compatibility and shared-path safety. In ... (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4003638499)
- `2026-03-25T03:14:30Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4003640669)
- `2026-03-26T08:10:38Z` `APPROVED` by `BBuf` - Can you add more acc tests such as mmlu? (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4012162456)
- `2026-03-27T03:38:41Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4018680908)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 1 inline comment(s)
- `python/sglang/srt/environ.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-25T03:13:27Z` `review` `CHANGES_REQUESTED` by `BBuf`; signals: blackwell, fp4, fp8, kernel, nvfp4; excerpt: "The direction makes sense, but I think this still needs a pass on compatibility and shared-path safety. In particular: the env var rename breaks ..." (https://github.com/sgl-project/sglang/pull/14162#pullrequestreview-4003638499)
- `2026-03-25T03:12:13Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`:620; signals: fp4, fp8, moe, nvfp4; excerpt: "I don't think use fp8 should be unconditional here. When input global scale is set we also pass use nvfp4=True, so this ends up ..." (https://github.com/sgl-project/sglang/pull/14162#discussion_r2985473223)
- `2026-03-25T03:13:05Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:1423; signals: blackwell, kernel, latency, moe; excerpt: "This assumes x scale is a regular fp scale. In the Blackwell path low-latency dispatch may hand back ue8m0/e8m0-style scales, so we probably need ..." (https://github.com/sgl-project/sglang/pull/14162#discussion_r2985475221)
- `2026-03-25T03:12:24Z` `inline` by `BBuf` `python/sglang/srt/environ.py`:379; signals: bf16, fp8, hang; excerpt: "Renaming the env var here will break existing configs unless we keep a compatibility alias. There are still tests/docs using SGLANG DEEPEP BF16 DISPATCH, ..." (https://github.com/sgl-project/sglang/pull/14162#discussion_r2985473645)
- `2026-03-25T03:14:30Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:1386; signals: cuda, kernel, moe; excerpt: "It might be better to implement this kernel under the jit kernel directory. We could also consider writing a simple CUDA kernel for it." (https://github.com/sgl-project/sglang/pull/14162#discussion_r2985478312)
