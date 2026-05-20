# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2385](https://github.com/Dao-AILab/flash-attention/pull/2385)
- Source page: `sources/prs/flash-attention/PR-2385.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2385`
- Generated at: `2026-05-20T15:16:56.080571+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T22:30:25Z`
- Merged: `2026-04-02T21:08:46Z`

## Discussion Counts

- Issue comments: 31
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: 0xDELUXA, ScottTodd, astrelsky, m-gallus, micmelesse, tianwyan, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-24T23:17:37Z` `COMMENTED` by `astrelsky` (https://github.com/Dao-AILab/flash-attention/pull/2385#pullrequestreview-4002985934)
- `2026-03-24T23:21:58Z` `COMMENTED` by `ScottTodd` (https://github.com/Dao-AILab/flash-attention/pull/2385#pullrequestreview-4002997491)
- `2026-03-24T23:47:40Z` `COMMENTED` by `micmelesse` (https://github.com/Dao-AILab/flash-attention/pull/2385#pullrequestreview-4003100968)
- `2026-03-25T15:30:23Z` `COMMENTED` by `m-gallus` (https://github.com/Dao-AILab/flash-attention/pull/2385#pullrequestreview-4007643210)
- `2026-04-02T16:09:17Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2385#pullrequestreview-4051693566)

## Inline Comment Hotspots

- `setup.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-26T12:39:41Z` `issue` by `0xDELUXA`; signals: attention, benchmark, latency, perf, performance, regression, speedup, throughput; excerpt: "I ran some benchmarks by checking out locally, building it, and comparing it against aiter FA (on Windows). Here are the results: Key Observations ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4134381791)
- `2026-03-26T13:00:36Z` `issue` by `tianwyan`; signals: attention, benchmark, latency, perf, performance, regression, speedup, throughput; excerpt: "I ran some benchmarks by checking out 2217 locally, building it, and comparing it against aiter FA. Here are the results: Key Observations Significant ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4134557926)
- `2026-03-25T12:52:53Z` `issue` by `0xDELUXA`; signals: attention, block, flash attention, hang; excerpt: "@astrelsky I removed the IS WINDOWS error in cpp extension.py. This is the command that I am used to get the message above. You ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4126372117)
- `2026-03-25T15:30:23Z` `inline` by `m-gallus` `setup.py`:621; signals: attention, hang, triton; excerpt: "We recently introduced TheRock's Windows builds to produce wheels named triton (instead of triton-windows) for cross-platform consistency. However, this creates a mismatch with the ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#discussion_r2989068337)
- `2026-03-24T23:53:22Z` `issue` by `micmelesse`; signals: attention, flash attention, triton; excerpt: "@astrelsky I removed the IS WINDOWS error in cpp extension.py. This is the command that I am used to get the message above. You ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4122169017)
- `2026-03-25T07:04:51Z` `issue` by `astrelsky`; signals: attention, flash attention, triton; excerpt: "@astrelsky I removed the IS WINDOWS error in cpp extension.py. This is the command that I am used to get the message above. You ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4124266333)
- `2026-04-02T15:26:15Z` `issue` by `0xDELUXA`; signals: attention, flash attention, hang; excerpt: "@tridao Would love to see this merged when you get a chance. Without this PR's changes, Windows ROCm users cannot build or use Flash ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4178678036)
- `2026-03-24T23:21:16Z` `issue` by `astrelsky`; signals: hang, triton; excerpt: "Unfortunately, unless I'm missing changes, I'm not seeing that at all. If I try to run pytest directly I get a ton of errors. ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4122049012)
- `2026-03-25T17:09:02Z` `issue` by `0xDELUXA`; signals: attention, triton; excerpt: "As a side note, for anyone who wants to experiment, from aiter.ops.triton.attention.mha import flash attn func also works on Windows if we place a ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4128280896)
- `2026-03-26T18:10:00Z` `issue` by `0xDELUXA`; signals: attention, flash attention; excerpt: "I would like to point out that Windows users must use the --no-deps flag when building Flash Attention from source. Failure to do so ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4137148672)
- `2026-03-26T22:40:50Z` `issue` by `0xDELUXA`; signals: hang, triton; excerpt: "@0xDELUXA Added the distributed.py fix. Thanks! I was quite determined to address this distributed support issue on Windows ROCm: - - - Even - ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4138786289)
- `2026-03-27T08:11:55Z` `issue` by `astrelsky`; signals: compile, triton; excerpt: "@0xDELUXA Added the distributed.py fix. For --no-deps, that's a triton vs triton-windows naming issue that needs to get resolved first. According to the conversation, ..." (https://github.com/Dao-AILab/flash-attention/pull/2385#issuecomment-4140892151)
