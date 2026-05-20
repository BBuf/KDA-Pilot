# PR Discussion Digest

- Source PR: [sgl-project/sglang#11664](https://github.com/sgl-project/sglang/pull/11664)
- Source page: `sources/prs/sglang/PR-11664.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11664`
- Generated at: `2026-05-20T15:27:25.290803+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-15T08:59:31Z`
- Merged: `2025-10-21T03:42:09Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: Qiaolin-Yu, cicirori, ispobock
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-10-16T05:18:31Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/11664#pullrequestreview-3343091827)
- `2025-10-20T05:58:57Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/11664#pullrequestreview-3355089739)
- `2025-10-20T07:51:55Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/11664#pullrequestreview-3355341857)
- `2025-10-20T07:52:10Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/11664#pullrequestreview-3355342456)
- `2025-10-20T07:52:20Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/11664#pullrequestreview-3355342835)
- `2025-10-21T02:41:37Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/11664#pullrequestreview-3358566542)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 8 inline comment(s)

## High-Signal Discussion

- `2025-10-20T05:57:42Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:735; signals: attention, mla, perf, performance; excerpt: "We can also parallelize it on head num and head dim to achieve better performance." (https://github.com/sgl-project/sglang/pull/11664#discussion_r2443876817)
- `2025-10-20T05:58:50Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:735; signals: attention, correctness, kernel, mla; excerpt: "It's better to have an unit test on this kernel in somewhere to make sure the correctness." (https://github.com/sgl-project/sglang/pull/11664#discussion_r2443878210)
- `2025-10-16T05:17:09Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:949; signals: attention, cuda, mla; excerpt: "can we move this update to the init metadata (normal/cuda graph)?" (https://github.com/sgl-project/sglang/pull/11664#discussion_r2434602960)
- `2025-10-20T05:53:07Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:573; signals: attention, mla; excerpt: "the item() will cause additional cpu sync, which will affect the cpu/gpu overlap we can use accept length cpu tensor in forward batch to ..." (https://github.com/sgl-project/sglang/pull/11664#discussion_r2443871638)
- `2025-10-20T07:51:55Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:573; signals: attention, mla; excerpt: "somehow accept length cpu is not consistent with accept length. I found extend seq lens cpu is correct." (https://github.com/sgl-project/sglang/pull/11664#discussion_r2444067838)
- `2025-10-20T05:53:44Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:572; signals: attention, mla; excerpt: "tensor.max() is much faster than max(tensor)" (https://github.com/sgl-project/sglang/pull/11664#discussion_r2443872441)
- `2025-10-20T07:52:10Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:572; signals: attention, mla; excerpt: "but extend seq lens cpu is a list" (https://github.com/sgl-project/sglang/pull/11664#discussion_r2444068347)
- `2025-10-20T07:52:20Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:735; signals: attention, mla; excerpt: "done" (https://github.com/sgl-project/sglang/pull/11664#discussion_r2444068650)
