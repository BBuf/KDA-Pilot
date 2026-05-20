# PR Discussion Digest

- Source PR: [pytorch/pytorch#170486](https://github.com/pytorch/pytorch/pull/170486)
- Source page: `sources/prs/pytorch/PR-170486.md`
- Evidence bundle: `evidence/pull-bundles/pytorch/gh-170486`
- Generated at: `2026-05-20T15:27:05.785615+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-16T00:14:28Z`
- Merged: `2026-01-05T17:28:43Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 16 (approved=1, commented=15)
- Inline review comments: 14
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=2, outdated=5
- Human participants with discussion text: atalman, drisspg, howardzhang-cv
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-12-18T03:14:47Z` `COMMENTED` by `drisspg` - Looks good, can we also add some sanity numeric checks to the test flex attention which use SQNR ... (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3590548830)
- `2025-12-21T22:46:56Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3602046652)
- `2025-12-21T22:47:04Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3602046681)
- `2025-12-21T22:48:08Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3602047028)
- `2025-12-21T22:49:15Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3602047431)
- `2025-12-21T22:50:18Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3602047824)
- `2025-12-21T22:50:31Z` `APPROVED` by `drisspg` - Looks great, some small nits/comments (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3602047895)
- `2025-12-22T23:15:54Z` `COMMENTED` by `howardzhang-cv` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606051166)
- `2025-12-22T23:31:24Z` `COMMENTED` by `howardzhang-cv` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606076533)
- `2025-12-22T23:39:42Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606085179)
- `2025-12-22T23:40:07Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606085610)
- `2025-12-22T23:51:09Z` `COMMENTED` by `howardzhang-cv` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606097845)
- `2025-12-22T23:54:39Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606102531)
- `2025-12-22T23:58:36Z` `COMMENTED` by `howardzhang-cv` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606108067)
- `2025-12-23T00:08:42Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606124697)
- `2025-12-23T01:13:30Z` `COMMENTED` by `howardzhang-cv` (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3606215334)

## Inline Comment Hotspots

- `torch/_higher_order_ops/flex_attention.py`: 8 inline comment(s)
- `test/inductor/test_flex_attention.py`: 5 inline comment(s)
- `test/inductor/test_flex_flash.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-18T03:14:47Z` `review` `COMMENTED` by `drisspg`; signals: attention, cache, fp8, kv cache; excerpt: "Looks good, can we also add some sanity numeric checks to the test flex attention which use SQNR and test against this. I think ..." (https://github.com/pytorch/pytorch/pull/170486#pullrequestreview-3590548830)
- `2025-12-21T22:50:18Z` `inline` by `drisspg` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention, dtype, kernel; excerpt: "Can you write a note somehwere on the dtype casts we do in this kernel and leave somehwere in this file near the eager ..." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2638168276)
- `2025-12-23T01:13:30Z` `inline` by `howardzhang-cv` `test/inductor/test_flex_attention.py`:2807; signals: attention, bf16, dtype; excerpt: "Looked into it for a long while and to be honest, not quite sure why the written version is better than quantize tensorwise? From ..." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641647517)
- `2025-12-22T23:31:24Z` `inline` by `howardzhang-cv` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention, dtype; excerpt: "Checked and value is not cast in math inner. It also isn't used at all in math inner and is not passed back so ..." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641517507)
- `2025-12-22T23:39:42Z` `inline` by `drisspg` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention, dtype; excerpt: "Ohh sorry I was confusing, for q@k I was surprised I didnt see q @ k.to(q.dtype), I imagine (know but didnt look) this is ..." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641526772)
- `2025-12-22T23:58:36Z` `inline` by `howardzhang-cv` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention, dtype; excerpt: "Q and K are both cast to working precision right before q @ k to get scores. scores and value are both cast to ..." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641550464)
- `2025-12-21T22:49:15Z` `inline` by `drisspg` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention, dtype; excerpt: "do we do the dtype casts already in math inner?" (https://github.com/pytorch/pytorch/pull/170486#discussion_r2638167606)
- `2025-12-22T23:54:39Z` `inline` by `drisspg` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention, dtype; excerpt: "and then cast down to q.dtype right before q @ k right?" (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641545330)
- `2025-12-22T23:15:54Z` `inline` by `howardzhang-cv` `test/inductor/test_flex_attention.py`:2807; signals: attention; excerpt: "I see a quantize tensorwise and quantize rowwise from torch.testing internal.inductor utils. But for some reason when I use that instead the SNR drops ..." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641494433)
- `2025-12-22T23:51:09Z` `inline` by `howardzhang-cv` `torch/_higher_order_ops/flex_attention.py`:270; signals: attention; excerpt: "Yeah, we pick a working precision first (float64 if q is float64 and float32 otherwise) and cast K to that." (https://github.com/pytorch/pytorch/pull/170486#discussion_r2641540052)
- `2025-12-21T22:46:57Z` `inline` by `drisspg` `test/inductor/test_flex_attention.py`:2829; signals: attention; excerpt: "Nit: we might have this somewhere in torch.testing" (https://github.com/pytorch/pytorch/pull/170486#discussion_r2638166619)
- `2025-12-21T22:47:05Z` `inline` by `drisspg` `test/inductor/test_flex_attention.py`:2807; signals: attention; excerpt: "same for this quant scheme" (https://github.com/pytorch/pytorch/pull/170486#discussion_r2638166656)
