# PR Discussion Digest

- Source PR: [sgl-project/sglang#13158](https://github.com/sgl-project/sglang/pull/13158)
- Source page: `sources/prs/sglang/PR-13158.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13158`
- Generated at: `2026-05-20T15:27:46.204609+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-12T15:06:30Z`
- Merged: `2026-02-25T00:55:20Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 10 (approved=3, commented=7)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=1, outdated=4
- Human participants with discussion text: OrangeRedeng, Vladimir221, iforgetmyname, ping1jing2, ssshinigami
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-12T15:08:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request optimizes the forward npu method for UnquantizedFusedMoEMethod by leveraging a more efficient NPU ... (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3453946085)
- `2025-11-17T12:45:49Z` `APPROVED` by `ssshinigami` - LGTM (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3472541526)
- `2025-11-27T02:25:39Z` `APPROVED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3513347907)
- `2026-01-22T10:14:01Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3691575784)
- `2026-01-22T11:46:44Z` `COMMENTED` by `Vladimir221` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3692054591)
- `2026-01-22T11:50:29Z` `COMMENTED` by `Vladimir221` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3692069682)
- `2026-01-29T14:25:57Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3723070533)
- `2026-01-29T14:27:21Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3723080802)
- `2026-01-29T15:56:50Z` `COMMENTED` by `Vladimir221` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3723594908)
- `2026-02-24T12:02:18Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/13158#pullrequestreview-3847308061)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/unquant.py`: 12 inline comment(s)

## High-Signal Discussion

- `2026-01-22T11:46:44Z` `inline` by `Vladimir221` `python/sglang/srt/layers/quantization/unquant.py`:609; signals: moe; excerpt: "It seems torch npu.npu moe init routing v2 returns expanded row idx in another format ([torch npu-npu moe finalize routing.doc]( so without drop pad ..." (https://github.com/sgl-project/sglang/pull/13158#discussion_r2716567791)
- `2026-01-22T11:50:29Z` `inline` by `Vladimir221` `python/sglang/srt/layers/quantization/unquant.py`:246; signals: hang; excerpt: "Will change after 15904 is merged" (https://github.com/sgl-project/sglang/pull/13158#discussion_r2716579710)
- `2026-01-22T09:53:21Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/quantization/unquant.py`:246; signals: general review; excerpt: "we have a utility function to do this operation here at srt.hardware backend.npu.utils.npu format cast" (https://github.com/sgl-project/sglang/pull/13158#discussion_r2716148037)
- `2026-01-22T10:13:41Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/quantization/unquant.py`:609; signals: general review; excerpt: "why we need this drop pad mode?" (https://github.com/sgl-project/sglang/pull/13158#discussion_r2716220329)
- `2026-01-29T14:25:57Z` `inline` by `OrangeRedeng` `python/sglang/srt/layers/quantization/unquant.py`:311; signals: general review; excerpt: "Please remove this strings" (https://github.com/sgl-project/sglang/pull/13158#discussion_r2741924337)
- `2026-01-29T14:27:20Z` `inline` by `OrangeRedeng` `python/sglang/srt/layers/quantization/unquant.py`:311; signals: general review; excerpt: "they are no longer needed after merge" (https://github.com/sgl-project/sglang/pull/13158#discussion_r2741932687)
- `2026-01-29T15:56:50Z` `inline` by `Vladimir221` `python/sglang/srt/layers/quantization/unquant.py`:311; signals: general review; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/13158#discussion_r2742359071)
