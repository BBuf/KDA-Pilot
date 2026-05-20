# PR Discussion Digest

- Source PR: [sgl-project/sglang#5370](https://github.com/sgl-project/sglang/pull/5370)
- Source page: `sources/prs/sglang/PR-5370.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5370`
- Generated at: `2026-05-20T15:30:23.005612+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-14T09:21:08Z`
- Merged: `2025-04-14T19:35:43Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: Alcanderian, BBuf, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-04-14T09:52:18Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5370#pullrequestreview-2763786192)
- `2025-04-14T10:12:56Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/5370#pullrequestreview-2763848567)
- `2025-04-14T10:30:52Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5370#pullrequestreview-2763889794)
- `2025-04-14T13:58:24Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5370#pullrequestreview-2764446771)
- `2025-04-14T15:02:32Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/5370#pullrequestreview-2764676446)
- `2025-04-14T19:33:54Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5370#pullrequestreview-2765470428)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 3 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_kernel.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-14T10:12:56Z` `inline` by `Alcanderian` `python/sglang/srt/models/deepseek_v2.py`:851; signals: kernel, triton; excerpt: "Great work, can you fuse transpose and contiguous into Triton kernel too? Fusing transpose and contiguous with 3d-tensor is not a common case and ..." (https://github.com/sgl-project/sglang/pull/5370#discussion_r2041844422)
- `2025-04-14T13:58:24Z` `inline` by `BBuf` `python/sglang/srt/layers/quantization/fp8_kernel.py`:970; signals: fp8, kernel; excerpt: "I would like to know why this kernel is not equivalent to the [per-tensor quant in the sgl-kernel]( ?" (https://github.com/sgl-project/sglang/pull/5370#discussion_r2042203090)
- `2025-04-14T15:02:31Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/fp8_kernel.py`:970; signals: fp8, kernel; excerpt: "I would like to know why this kernel is not equivalent to the , but the underlying storage size is (num seq, num head, ..." (https://github.com/sgl-project/sglang/pull/5370#discussion_r2042344006)
- `2025-04-14T09:52:18Z` `inline` by `BBuf` `python/sglang/srt/models/deepseek_v2.py`:851; signals: kernel, triton; excerpt: "Great work, can you fuse transpose and contiguous into Triton kernel too?" (https://github.com/sgl-project/sglang/pull/5370#discussion_r2041810401)
- `2025-04-14T11:11:38Z` `issue` by `Alcanderian`; signals: accuracy, mla; excerpt: "Can you add gsm8k acc test too? Ok, I will post the accuracy report by TestMLADeepseekV3 at after I fully finish this PR" (https://github.com/sgl-project/sglang/pull/5370#issuecomment-2801356118)
- `2025-04-14T13:04:25Z` `issue` by `Alcanderian`; signals: fp8, mla; excerpt: "Can you add gsm8k acc test too? Done. The failed ci cases are not related to deepseek fp8. Acc cmd: python3 test mla deepseek ..." (https://github.com/sgl-project/sglang/pull/5370#issuecomment-2801648782)
- `2025-04-14T17:36:31Z` `issue` by `Alcanderian`; signals: fp8, mla; excerpt: "per tensor quant fp8 has been removed and per tensor quant mla fp8 has been optimized(boost 64-batch case from 8000token/s to 8600 token/s). Please ..." (https://github.com/sgl-project/sglang/pull/5370#issuecomment-2802417738)
- `2025-04-14T10:30:52Z` `inline` by `BBuf` `python/sglang/srt/models/deepseek_v2.py`:851; signals: general review; excerpt: "That's ok." (https://github.com/sgl-project/sglang/pull/5370#discussion_r2041870413)
