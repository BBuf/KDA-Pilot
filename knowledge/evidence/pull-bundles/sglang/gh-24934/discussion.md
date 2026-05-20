# PR Discussion Digest

- Source PR: [sgl-project/sglang#24934](https://github.com/sgl-project/sglang/pull/24934)
- Source page: `sources/prs/sglang/PR-24934.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-24934`
- Generated at: `2026-05-20T15:29:45.685173+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T03:48:23Z`
- Merged: `2026-05-19T23:51:32Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 1 (commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, Paiiiiiiiiiiiiii
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-11T05:46:59Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/24934#pullrequestreview-4260983051)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v4_nextn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-11T05:43:20Z` `issue` by `Fridge003`; signals: b200, fp4, register; excerpt: "Can we add a test for CP+MTP, possibly under test/registered/dsv4/test deepseek v4 flash fp4 b200.py with flash model. We can test it with larger ..." (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4417878041)
- `2026-05-11T05:46:14Z` `issue` by `Paiiiiiiiiiiiiii`; signals: b200, fp4, register; excerpt: "Can we add a test for CP+MTP, possibly under test/registered/dsv4/test deepseek v4 flash fp4 b200.py with flash model. We can test it with larger ..." (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4417889564)
- `2026-05-11T05:46:54Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v4_nextn.py`:240; signals: attention; excerpt: "should be get attention cp size() and get attention cp rank() here" (https://github.com/sgl-project/sglang/pull/24934#discussion_r3216582298)
- `2026-05-13T07:30:55Z` `issue` by `Fridge003`; signals: hopper; excerpt: "@Paiiiiiiiiiiiiii Please check this failure (I guess it can also be reproduced on hopper gpus)" (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4438454128)
- `2026-05-11T05:45:02Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v4_nextn.py`:168; signals: general review; excerpt: "This flag has been deprecated on main" (https://github.com/sgl-project/sglang/pull/24934#discussion_r3216575463)
- `2026-05-18T08:08:58Z` `issue` by `Paiiiiiiiiiiiiii`; signals: b200, fp4; excerpt: "/rerun-test test deepseek v4 flash fp4 b200.py" (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4475665833)
- `2026-05-19T07:54:16Z` `issue` by `Fridge003`; signals: b200, fp4; excerpt: "/rerun-test test deepseek v4 flash fp4 b200.py" (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4485595166)
- `2026-05-19T11:45:47Z` `issue` by `Paiiiiiiiiiiiiii`; signals: b200, fp4; excerpt: "/rerun-test test deepseek v4 flash fp4 b200.py @Fridge003 Now this CI has passed，can merge the pr ？" (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4487398173)
- `2026-05-13T09:24:31Z` `issue` by `Fridge003`; signals: general review; excerpt: "@Paiiiiiiiiiiiiii Latest main. You can try nightly image like this one docker pull lmsysorg/sglang:nightly-dev-20260513-4fb40bff" (https://github.com/sgl-project/sglang/pull/24934#issuecomment-4439391849)
