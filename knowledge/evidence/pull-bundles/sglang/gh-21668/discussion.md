# PR Discussion Digest

- Source PR: [sgl-project/sglang#21668](https://github.com/sgl-project/sglang/pull/21668)
- Source page: `sources/prs/sglang/PR-21668.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21668`
- Generated at: `2026-05-20T15:29:17.037251+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T06:57:37Z`
- Merged: `2026-05-18T06:59:20Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 11 (approved=2, changes_requested=2, commented=7)
- Inline review comments: 15
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: Xia-Weiwen, mingfeima
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-13T11:39:15Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4098359591)
- `2026-05-06T09:05:59Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4234682191)
- `2026-05-06T09:07:02Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4234689368)
- `2026-05-07T04:48:12Z` `CHANGES_REQUESTED` by `mingfeima` - let's check ci first, and also some small refactoring is needed to simplify the code. (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4240901184)
- `2026-05-08T08:30:17Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4250778618)
- `2026-05-08T08:30:27Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4250779593)
- `2026-05-08T08:30:35Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4250780481)
- `2026-05-08T08:32:28Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4250792541)
- `2026-05-08T08:32:37Z` `COMMENTED` by `Xia-Weiwen` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4250793446)
- `2026-05-13T05:05:31Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4278458361)
- `2026-05-18T02:52:24Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/21668#pullrequestreview-4306943140)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`: 7 inline comment(s)
- `test/registered/attention/test_chunk_gated_delta_rule.py`: 4 inline comment(s)
- `docs_new/docs/hardware-platforms/xpu.mdx`: 2 inline comment(s)
- `python/sglang/bench_one_batch.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-15T03:08:07Z` `issue` by `mingfeima`; signals: attention, benchmark, perf, performance; excerpt: "i suggest that we remove benchmark/bench linear attention/bench fwd h.py in this PR and keeps performance info internal. this is mostly for performance debugging. ..." (https://github.com/sgl-project/sglang/pull/21668#issuecomment-4456541088)
- `2026-05-15T03:27:13Z` `issue` by `Xia-Weiwen`; signals: attention, benchmark, perf, performance; excerpt: "i suggest that we remove benchmark/bench linear attention/bench fwd h.py in this PR and keeps performance info internal. this is mostly for performance debugging. ..." (https://github.com/sgl-project/sglang/pull/21668#issuecomment-4456628023)
- `2026-05-15T06:52:24Z` `issue` by `mingfeima`; signals: attention, cuda, kernel, triton; excerpt: "The major issue brought up by this pull request is that "existing triton kernels does not fit into non-CUDA gpu arch". for intel gpus, ..." (https://github.com/sgl-project/sglang/pull/21668#issuecomment-4457645698)
- `2026-05-15T08:11:19Z` `issue` by `Xia-Weiwen`; signals: attention, cuda, kernel, triton; excerpt: "The major issue brought up by this pull request is that "existing triton kernels does not fit into non-CUDA gpu arch". for intel gpus, ..." (https://github.com/sgl-project/sglang/pull/21668#issuecomment-4458138014)
- `2026-05-06T09:07:02Z` `inline` by `Xia-Weiwen` `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`:230; signals: attention, hang, triton; excerpt: "Triton-xpu has fixed this bug in their latest wheel, so this change is no longer needed. I have also updated the installation doc to ..." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3194214909)
- `2026-04-13T11:39:10Z` `inline` by `mingfeima` `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`:230; signals: attention, block; excerpt: "also any place else that uses block ptr? if there are multiple places that use block ptr, better put use block ptr in a ..." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3072719287)
- `2026-05-07T04:42:23Z` `inline` by `mingfeima` `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`:328; signals: attention, kernel; excerpt: "16 if is intel else 32 is used multiple times. we can put something like the following in sglang.srt.layers.attention.fla.utils ``` other vendors may also ..." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3198978495)
- `2026-05-07T02:54:23Z` `inline` by `mingfeima` `test/registered/attention/test_chunk_gated_delta_rule.py`:75; signals: attention, register; excerpt: "use: from sglang.srt.utils import get device ... device = get device()" (https://github.com/sgl-project/sglang/pull/21668#discussion_r3198687912)
- `2026-05-08T08:30:27Z` `inline` by `Xia-Weiwen` `test/registered/attention/test_chunk_gated_delta_rule.py`:75; signals: attention, register; excerpt: "Thanks. Updated." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3207415627)
- `2026-05-08T08:30:35Z` `inline` by `Xia-Weiwen` `test/registered/attention/test_chunk_gated_delta_rule.py`:19; signals: attention, register; excerpt: "Thanks. Updated." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3207416326)
- `2026-04-13T11:33:27Z` `inline` by `mingfeima` `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`:365; signals: attention; excerpt: "what is 16 or 32 here link to the HW config? leaving magic number like this is going to be confusing." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3072692715)
- `2026-05-06T09:05:59Z` `inline` by `Xia-Weiwen` `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`:365; signals: attention; excerpt: "Yes, it is related to HW specs. However, it cannot be derived from HW properties. It is a result of tuning. It was hard-coded ..." (https://github.com/sgl-project/sglang/pull/21668#discussion_r3194207633)
