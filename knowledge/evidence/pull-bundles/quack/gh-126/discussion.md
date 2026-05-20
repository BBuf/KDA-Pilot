# PR Discussion Digest

- Source PR: [Dao-AILab/quack#126](https://github.com/Dao-AILab/quack/pull/126)
- Source page: `sources/prs/quack/PR-126.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-126`
- Generated at: `2026-05-20T15:17:16.913458+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-29T23:10:41Z`
- Merged: `2026-05-01T13:40:43Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 13
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: rafacelente, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-30T02:49:45Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4202110430)
- `2026-04-30T02:50:31Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4202112628)
- `2026-04-30T02:51:17Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4202115432)
- `2026-04-30T02:56:10Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4202132634)
- `2026-04-30T02:58:32Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4202140381)
- `2026-04-30T14:05:27Z` `COMMENTED` by `rafacelente` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4205793597)
- `2026-04-30T14:07:05Z` `COMMENTED` by `rafacelente` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4205804281)
- `2026-04-30T14:08:23Z` `COMMENTED` by `rafacelente` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4205813609)
- `2026-04-30T14:15:40Z` `COMMENTED` by `rafacelente` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4205870971)
- `2026-04-30T14:20:08Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4205903203)
- `2026-04-30T14:21:18Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4205911560)
- `2026-04-30T15:33:26Z` `COMMENTED` by `rafacelente` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4206448878)
- `2026-04-30T15:34:00Z` `COMMENTED` by `rafacelente` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4206453199)
- `2026-05-01T13:40:35Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/126#pullrequestreview-4211359633)

## Inline Comment Hotspots

- `quack/cross_entropy.py`: 10 inline comment(s)
- `tests/test_cross_entropy_weight.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-30T14:20:08Z` `inline` by `tridao` `quack/cross_entropy.py`:746; signals: compile, cute, dtype; excerpt: "i see. The issue is that during compilation compile cross entropy backward we should construct dloss = cute.runtime.make fake tensor(dtype, batch sym int, stride=(cute.sym ..." (https://github.com/Dao-AILab/quack/pull/126#discussion_r3168597481)
- `2026-04-30T14:05:27Z` `inline` by `rafacelente` `quack/cross_entropy.py`:746; signals: kernel, memory; excerpt: "that's the only way I could make it work with reduction != "none". I think this is because when computing the grad of torch.mean(), ..." (https://github.com/Dao-AILab/quack/pull/126#discussion_r3168499385)
- `2026-04-30T14:15:40Z` `inline` by `rafacelente` `quack/cross_entropy.py`:270; signals: dtype, kernel; excerpt: "in the original kernel the logits are upcasted to fp32, so if we allow weight to be any other dtype we would need to ..." (https://github.com/Dao-AILab/quack/pull/126#discussion_r3168569242)
- `2026-04-30T14:21:18Z` `inline` by `tridao` `quack/cross_entropy.py`:270; signals: dtype; excerpt: "we could support any dtype just for generality (it doesn't add much / any code i think). You can pass in weight dtype, which ..." (https://github.com/Dao-AILab/quack/pull/126#discussion_r3168604661)
- `2026-04-30T02:49:45Z` `inline` by `tridao` `quack/cross_entropy.py`:270; signals: dtype; excerpt: "is weight dtype always fp32 or should we pass that in?" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3165356449)
- `2026-04-30T14:07:05Z` `inline` by `rafacelente` `quack/cross_entropy.py`:521; signals: hang; excerpt: "changed the wording slightly but added it back again" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3168509457)
- `2026-04-30T15:34:00Z` `inline` by `rafacelente` `quack/cross_entropy.py`:270; signals: dtype; excerpt: "done. Removed has weights in favor of weight dtype, all fp dtypes should work now" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3169078504)
- `2026-04-30T02:51:17Z` `inline` by `tridao` `tests/test_cross_entropy_weight.py`:1; signals: general review; excerpt: "ideally "has weight" is a test parameter so that we cover all the cases of cross entropy with / without weight" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3165359841)
- `2026-04-30T14:08:22Z` `inline` by `rafacelente` `tests/test_cross_entropy_weight.py`:1; signals: general review; excerpt: "removed the weighted tests file and added them to test cross entropy as a test parameter. I also included a new test in that ..." (https://github.com/Dao-AILab/quack/pull/126#discussion_r3168517125)
- `2026-04-30T02:50:31Z` `inline` by `tridao` `tests/test_cross_entropy_weight.py`:1; signals: general review; excerpt: "can you put this in test cross entropy.py?" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3165358157)
- `2026-04-30T02:56:10Z` `inline` by `tridao` `quack/cross_entropy.py`:521; signals: general review; excerpt: "let's keep this comment (Claude likes to delete comments)" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3165371674)
- `2026-04-30T02:58:32Z` `inline` by `tridao` `quack/cross_entropy.py`:746; signals: general review; excerpt: "do we need dloss.contigous()" (https://github.com/Dao-AILab/quack/pull/126#discussion_r3165377062)
