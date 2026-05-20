# PR Discussion Digest

- Source PR: [Dao-AILab/quack#82](https://github.com/Dao-AILab/quack/pull/82)
- Source page: `sources/prs/quack/PR-82.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-82`
- Generated at: `2026-05-20T15:17:24.924175+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T00:35:54Z`
- Merged: `2026-03-16T17:03:02Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 20 (approved=2, commented=18)
- Inline review comments: 18
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=8
- Human participants with discussion text: thakkarV, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-12T10:09:43Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935363782)
- `2026-03-12T10:32:13Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935506784)
- `2026-03-12T10:43:32Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935568602)
- `2026-03-12T11:26:24Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935817049)
- `2026-03-12T11:27:12Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935821739)
- `2026-03-12T11:30:53Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935844857)
- `2026-03-12T11:31:36Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3935849242)
- `2026-03-12T14:30:57Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3937115899)
- `2026-03-12T14:52:44Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3937287692)
- `2026-03-12T16:37:52Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3938099236)
- `2026-03-12T16:38:53Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3938108381)
- `2026-03-12T16:44:00Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3938149710)
- `2026-03-12T16:50:33Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3938195702)
- `2026-03-12T16:51:45Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3938204559)
- `2026-03-12T22:39:57Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3940232280)
- `2026-03-12T22:40:14Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3940234409)
- `2026-03-13T18:39:10Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3946232044)
- `2026-03-16T15:48:19Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3954839877)
- `2026-03-16T16:04:09Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3954977531)
- `2026-03-16T17:02:53Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/82#pullrequestreview-3955358935)

## Inline Comment Hotspots

- `quack/gemm_act.py`: 6 inline comment(s)
- `quack/gemm_default_epi.py`: 4 inline comment(s)
- `quack/rounding.py`: 4 inline comment(s)
- `quack/gemm_sm90.py`: 2 inline comment(s)
- `quack/copy_utils.py`: 1 inline comment(s)
- `quack/gemm_interface.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-12T16:50:33Z` `inline` by `tridao` `quack/gemm_default_epi.py`:205; signals: bf16, cutlass, epilogue, gemm; excerpt: "it's doing up-conversion, typically C is bf16, tRS rD is fp32, so we're converting from bf16 - fp32 here. I think this convention differs ..." (https://github.com/Dao-AILab/quack/pull/82#discussion_r2926005825)
- `2026-03-12T11:31:37Z` `inline` by `tridao` `quack/gemm_sm90.py`:1239; signals: gemm, sm90, tile; excerpt: "are these constants universal or are they dependent on tile size, epi tile etc?" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2923995048)
- `2026-03-12T14:30:57Z` `inline` by `thakkarV` `quack/gemm_sm90.py`:1239; signals: gemm, sm90, triton; excerpt: "they are seed constants. Following the triton impl here :" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2925075139)
- `2026-03-13T06:00:02Z` `issue` by `thakkarV`; signals: cuda, hang, kernel; excerpt: "@tridao one other change I want to push before merging this is to make the host side philox seed a device ptr instead of ..." (https://github.com/Dao-AILab/quack/pull/82#issuecomment-4052968745)
- `2026-03-12T10:43:32Z` `inline` by `tridao` `quack/copy_utils.py`:56; signals: bf16, dtype; excerpt: "should put assert here that that dtypes are fp32 and bf16" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2923739161)
- `2026-03-16T15:48:20Z` `inline` by `tridao` `quack/gemm_act.py`:339; signals: cutlass, gemm; excerpt: "This should be tRS rPostAct.element type == cutlass.Float32" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2941265210)
- `2026-03-12T10:32:13Z` `inline` by `tridao` `quack/rounding.py`:67; signals: perf; excerpt: "1. shouldn't we use mul.wide ? I've just checked that ptaxs is able to optimize mul.hi and mul.lo into IMAD.WIDE.U32 as well, but it's ..." (https://github.com/Dao-AILab/quack/pull/82#discussion_r2923681168)
- `2026-03-12T16:44:00Z` `inline` by `thakkarV` `quack/gemm_default_epi.py`:205; signals: gemm; excerpt: "@tridao can you help me understand if the .to(tRS rD.element type) are downconversions or not? if so, just wondering if we should add SR ..." (https://github.com/Dao-AILab/quack/pull/82#discussion_r2925968937)
- `2026-03-12T22:39:53Z` `inline` by `thakkarV` `quack/gemm_act.py`:303; signals: gemm; excerpt: "implemented now, please review for sanity. I added a hash salt for its counter so the entropy is unique." (https://github.com/Dao-AILab/quack/pull/82#discussion_r2927800268)
- `2026-03-12T10:09:43Z` `inline` by `tridao` `quack/gemm_default_epi.py`:9; signals: gemm; excerpt: "let's remove this Uint32 import as it's not used and linter is complaining" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2923561323)
- `2026-03-12T11:26:24Z` `inline` by `tridao` `quack/gemm_act.py`:275; signals: gemm; excerpt: "self.rounding mode == RoundingMode.RS" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2923966846)
- `2026-03-12T11:27:13Z` `inline` by `tridao` `quack/gemm_act.py`:303; signals: gemm; excerpt: "Should we do RS rounding for postact as well?" (https://github.com/Dao-AILab/quack/pull/82#discussion_r2923970953)
