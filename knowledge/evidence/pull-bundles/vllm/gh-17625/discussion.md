# PR Discussion Digest

- Source PR: [vllm-project/vllm#17625](https://github.com/vllm-project/vllm/pull/17625)
- Source page: `sources/prs/vllm/PR-17625.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17625`
- Generated at: `2026-05-20T15:35:12.608473+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-04T07:37:39Z`
- Merged: `2025-06-04T04:40:26Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: LucasWilkinson, houseroad, kaixih, mergify, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-04T18:27:35Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2813531755)
- `2025-05-05T17:38:53Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2815577217)
- `2025-05-06T14:21:32Z` `COMMENTED` by `LucasWilkinson` - The perf is looking really good! thanks for the contribution! Do you mind doing accuracy checks (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2818451094)
- `2025-05-06T16:42:52Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2818988927)
- `2025-05-06T22:33:27Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2819854506)
- `2025-05-08T18:59:24Z` `APPROVED` by `LucasWilkinson` - LGTM, other than I do think we should turn it on by default for Blackwell: Any reason not ... (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2826104014)
- `2025-05-12T17:44:51Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2834016958)
- `2025-05-12T17:48:10Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2834024138)
- `2025-05-12T19:07:15Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2834221541)
- `2025-05-12T22:00:06Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2834728153)
- `2025-05-13T17:49:13Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2837655730)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/common.py`: 7 inline comment(s)
- `vllm/v1/attention/backends/mla/cutlass_mla.py`: 3 inline comment(s)
- `vllm/platforms/cuda.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-09T03:28:09Z` `issue` by `LucasWilkinson`; signals: attention, blackwell, block, cutlass, kernel, mla, race, triton; excerpt: "other than I do think we should turn it on by default for Blackwell, Any reason not to? My main concern is that the ..." (https://github.com/vllm-project/vllm/pull/17625#issuecomment-2864978012)
- `2025-05-08T22:21:26Z` `issue` by `kaixih`; signals: blackwell, cutlass, kernel, mla, triton; excerpt: "other than I do think we should turn it on by default for Blackwell, Any reason not to? My main concern is that the ..." (https://github.com/vllm-project/vllm/pull/17625#issuecomment-2864561850)
- `2025-05-11T07:19:17Z` `issue` by `kaixih`; signals: attention, block, cache, hang, race; excerpt: "we plan to eventually handle this more gracefully (i.e. better support of the attention backend being able to specify the block size it wants ..." (https://github.com/vllm-project/vllm/pull/17625#issuecomment-2869555891)
- `2025-05-04T18:27:35Z` `inline` by `mgoin` `vllm/v1/attention/backends/mla/cutlass_mla.py`:67; signals: attention, cutlass, mla; excerpt: "Make sure to update the messages for CutlassMLA" (https://github.com/vllm-project/vllm/pull/17625#discussion_r2072679002)
- `2025-05-05T17:38:53Z` `inline` by `kaixih` `vllm/v1/attention/backends/mla/cutlass_mla.py`:67; signals: attention, cutlass, mla; excerpt: "Done. PTAL." (https://github.com/vllm-project/vllm/pull/17625#discussion_r2073887790)
- `2025-05-06T14:13:30Z` `inline` by `LucasWilkinson` `vllm/platforms/cuda.py`:170; signals: blackwell, cuda, perf; excerpt: "the perf looks really good! I think we should turn this on by default for blackwell" (https://github.com/vllm-project/vllm/pull/17625#discussion_r2075575324)
- `2025-05-06T14:17:25Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/mla/cutlass_mla.py`:84; signals: attention, cutlass, mla; excerpt: "does this need to be torch.zeros? or does torch.empty work (faster)" (https://github.com/vllm-project/vllm/pull/17625#discussion_r2075584291)
- `2025-05-12T22:00:06Z` `inline` by `kaixih` `vllm/v1/attention/backends/mla/common.py`:352; signals: attention, hang, mla; excerpt: "Do I need to make any further changes, or is this good to go now?" (https://github.com/vllm-project/vllm/pull/17625#discussion_r2085598985)
- `2025-05-06T14:21:32Z` `review` `COMMENTED` by `LucasWilkinson`; signals: accuracy, perf; excerpt: "The perf is looking really good! thanks for the contribution! Do you mind doing accuracy checks" (https://github.com/vllm-project/vllm/pull/17625#pullrequestreview-2818451094)
- `2025-05-06T22:33:27Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/mla/common.py`:356; signals: attention, mla; excerpt: "oh sorry ya aot schedule is not actually used, aot schedule stands for ahead-of-time schedule and was meant to indicate if we should use ..." (https://github.com/vllm-project/vllm/pull/17625#discussion_r2076437871)
- `2025-05-12T17:48:10Z` `inline` by `kaixih` `vllm/v1/attention/backends/mla/common.py`:352; signals: attention, mla; excerpt: "See comment [here]( My understanding is that this aot schedule is irrelevant here. @LucasWilkinson can correct me." (https://github.com/vllm-project/vllm/pull/17625#discussion_r2085164806)
- `2025-05-06T14:13:02Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/mla/common.py`:356; signals: attention, mla; excerpt: "we should leave and updated: to" (https://github.com/vllm-project/vllm/pull/17625#discussion_r2075574280)
