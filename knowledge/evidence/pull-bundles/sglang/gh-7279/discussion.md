# PR Discussion Digest

- Source PR: [sgl-project/sglang#7279](https://github.com/sgl-project/sglang/pull/7279)
- Source page: `sources/prs/sglang/PR-7279.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7279`
- Generated at: `2026-05-20T15:31:09.071352+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-17T14:10:38Z`
- Merged: `2025-08-08T18:06:03Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 8 (approved=2, changes_requested=1, commented=5)
- Inline review comments: 10
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=6, outdated=2
- Human participants with discussion text: HaiShaw, kkHuang-amd, merrymercy, saienduri, valarLip
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-17T14:11:19Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @valarLip, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2935851927)
- `2025-06-17T14:12:09Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request refines the aiter backend and enables the aiter biased grouped topk kernel, primarily ... (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2935855354)
- `2025-06-19T12:20:15Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2942787121)
- `2025-06-19T15:18:10Z` `COMMENTED` by `valarLip` (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2943424422)
- `2025-06-21T08:52:57Z` `CHANGES_REQUESTED` by `HaiShaw` - @valarLip Pls split MTP to another PR, and we plan to have aiter biased grouped topk merged first ... (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2947697771)
- `2025-06-21T15:43:37Z` `COMMENTED` by `valarLip` (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2947800254)
- `2025-08-07T06:48:48Z` `APPROVED` by `HaiShaw` - LGTM (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-3095587691)
- `2025-08-08T18:05:53Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-3101772749)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/aiter_backend.py`: 8 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-18T12:06:31Z` `issue` by `valarLip`; signals: accuracy, attention, benchmark, latency, throughput; excerpt: "server launch: SGLANG USE AITER=1 \ python3 -m sglang.launch server \ --model-path deepseek-ai/DeepSeek-R1-0528 \ --attention-backend aiter \ --port 30000 --host 0.0.0.0 --trust-remote-code --tp-size 8 ..." (https://github.com/sgl-project/sglang/pull/7279#issuecomment-2983932300)
- `2025-06-21T15:43:37Z` `inline` by `valarLip` `python/sglang/srt/layers/attention/aiter_backend.py`:171; signals: attention, kernel; excerpt: "it's ok for this case, we fill the whole tensor in next few lines. using zeros we will have a addition fill kernel launch..." (https://github.com/sgl-project/sglang/pull/7279#discussion_r2160068407)
- `2025-06-19T12:20:14Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/quantization/fp8_utils.py`:49; signals: fp8; excerpt: "Below code does not use it, could we remove it" (https://github.com/sgl-project/sglang/pull/7279#discussion_r2156885118)
- `2025-06-19T15:18:10Z` `inline` by `valarLip` `python/sglang/srt/layers/quantization/fp8_utils.py`:49; signals: fp8; excerpt: "will use it later, just leave a placeholder for now" (https://github.com/sgl-project/sglang/pull/7279#discussion_r2157259416)
- `2025-06-21T07:58:03Z` `inline` by `HaiShaw` `python/sglang/srt/layers/attention/aiter_backend.py`:171; signals: attention; excerpt: "ROCm: torch.empty seems to be more troublesome than torch.zeros" (https://github.com/sgl-project/sglang/pull/7279#discussion_r2159971939)
- `2025-06-21T08:52:57Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: general review; excerpt: "@valarLip Pls split MTP to another PR, and we plan to have aiter biased grouped topk merged first - with that we expect the ..." (https://github.com/sgl-project/sglang/pull/7279#pullrequestreview-2947697771)
- `2025-06-19T15:15:55Z` `issue` by `valarLip`; signals: general review; excerpt: "@valarLip please cross-check 7240 for the 2nd enhancement. cc @kkHuang-amd this way is my old implementation... we can switch to this new one now" (https://github.com/sgl-project/sglang/pull/7279#issuecomment-2988461255)
- `2025-06-21T15:42:09Z` `issue` by `valarLip`; signals: general review; excerpt: "@valarLip Pls split MTP to another PR, and we plan to have aiter biased grouped topk merged first - with that we expect the ..." (https://github.com/sgl-project/sglang/pull/7279#issuecomment-2993641853)
