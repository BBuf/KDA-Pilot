# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1904](https://github.com/Dao-AILab/flash-attention/pull/1904)
- Source page: `sources/prs/flash-attention/PR-1904.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1904`
- Generated at: `2026-05-20T15:16:35.884883+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T08:19:55Z`
- Merged: `2025-09-25T08:22:48Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: janeyx99, johnnynunez, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-09-23T12:16:29Z` `COMMENTED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3257707337)
- `2025-09-23T12:18:52Z` `COMMENTED` by `johnnynunez` (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3257716121)
- `2025-09-23T12:45:05Z` `COMMENTED` by `johnnynunez` (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3257832326)
- `2025-09-23T13:55:47Z` `COMMENTED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3258160111)
- `2025-09-23T14:03:01Z` `COMMENTED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3258193552)
- `2025-09-23T14:08:38Z` `APPROVED` by `janeyx99` - Looks okay tho I’d feel better if you’re able to download a torch nightly after September and verify ... (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3258215831)
- `2025-09-23T14:20:57Z` `COMMENTED` by `johnnynunez` (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3258265948)

## Inline Comment Hotspots

- `hopper/flash_api.cpp`: 4 inline comment(s)
- `hopper/flash_api_stable.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-23T12:16:28Z` `inline` by `janeyx99` `hopper/flash_api.cpp`:1466; signals: hang, hopper; excerpt: "Please also make a similar change to flash api stable.cpp! Please use torch::stable::accelerator::DeviceIndex" (https://github.com/Dao-AILab/flash-attention/pull/1904#discussion_r2372124927)
- `2025-09-23T12:18:52Z` `inline` by `johnnynunez` `hopper/flash_api.cpp`:1466; signals: hopper; excerpt: "Got it" (https://github.com/Dao-AILab/flash-attention/pull/1904#discussion_r2372130533)
- `2025-09-23T12:45:05Z` `inline` by `johnnynunez` `hopper/flash_api.cpp`:1466; signals: hopper; excerpt: "@janeyx99 do you mean following lines?:" (https://github.com/Dao-AILab/flash-attention/pull/1904#discussion_r2372207703)
- `2025-09-23T13:55:47Z` `inline` by `janeyx99` `hopper/flash_api.cpp`:48; signals: hopper; excerpt: "Looks like this api is not needed?" (https://github.com/Dao-AILab/flash-attention/pull/1904#discussion_r2372430378)
- `2025-09-23T14:03:01Z` `inline` by `janeyx99` `hopper/flash_api_stable.cpp`:35; signals: hopper; excerpt: "Same here" (https://github.com/Dao-AILab/flash-attention/pull/1904#discussion_r2372452991)
- `2025-09-24T11:57:20Z` `issue` by `janeyx99`; signals: hopper; excerpt: "The screenshots looks like FA2, but you’re modifying FA3 right? So should be building from the hopper directory. Also can you verify that the ..." (https://github.com/Dao-AILab/flash-attention/pull/1904#issuecomment-3328055750)
- `2025-09-24T12:00:55Z` `issue` by `johnnynunez`; signals: hopper; excerpt: "The screenshots looks like FA2, but you’re modifying FA3 right? So should be building from the hopper directory. Also can you verify that the ..." (https://github.com/Dao-AILab/flash-attention/pull/1904#issuecomment-3328068561)
- `2025-09-24T18:32:11Z` `issue` by `johnnynunez`; signals: hopper; excerpt: "The screenshots looks like FA2, but you’re modifying FA3 right? So should be building from the hopper directory. Also can you verify that the ..." (https://github.com/Dao-AILab/flash-attention/pull/1904#issuecomment-3330178864)
- `2025-09-24T11:08:46Z` `issue` by `johnnynunez`; signals: h200; excerpt: "@tridao @janeyx99 it is working in my GH200" (https://github.com/Dao-AILab/flash-attention/pull/1904#issuecomment-3327829234)
- `2025-09-23T14:08:38Z` `review` `APPROVED` by `janeyx99`; signals: general review; excerpt: "Looks okay tho I’d feel better if you’re able to download a torch nightly after September and verify that fa3 still builds" (https://github.com/Dao-AILab/flash-attention/pull/1904#pullrequestreview-3258215831)
- `2025-09-23T14:20:57Z` `inline` by `johnnynunez` `hopper/flash_api_stable.cpp`:35; signals: hopper; excerpt: "thanks!" (https://github.com/Dao-AILab/flash-attention/pull/1904#discussion_r2372503201)
