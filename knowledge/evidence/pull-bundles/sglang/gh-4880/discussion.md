# PR Discussion Digest

- Source PR: [sgl-project/sglang#4880](https://github.com/sgl-project/sglang/pull/4880)
- Source page: `sources/prs/sglang/PR-4880.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4880`
- Generated at: `2026-05-20T15:30:15.217930+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-29T07:24:41Z`
- Merged: `2025-04-10T06:23:24Z`

## Discussion Counts

- Issue comments: 75
- Review submissions: 20 (approved=1, commented=19)
- Inline review comments: 22
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=0, outdated=7
- Human participants with discussion text: ByronHsu, GaoYusong, Hongbosherlock, Huixxi, JensenFire, LJL36, RuixiangMa, ShangmingCai, XucSh, ZhengWG, Zhou-sx, liz-badada, orrorcol, stmatengss, whybeyoung, yansiyu550, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 53

## Review Decisions

- `2025-03-30T07:32:01Z` `COMMENTED` by `ByronHsu` - Awesome work! Left few comments and questions 1. The current design is based on send/recv, which needs a ... (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2727815927)
- `2025-03-31T01:18:26Z` `COMMENTED` by `XucSh` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2728096229)
- `2025-03-31T07:38:17Z` `COMMENTED` by `Zhou-sx` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2728443999)
- `2025-03-31T08:18:27Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2728530793)
- `2025-03-31T08:49:17Z` `COMMENTED` by `Zhou-sx` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2728598927)
- `2025-03-31T09:03:46Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2728631963)
- `2025-04-01T07:05:42Z` `COMMENTED` by `Huixxi` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2731657782)
- `2025-04-03T07:59:53Z` `COMMENTED` by `Zhou-sx` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2738868878)
- `2025-04-04T06:12:16Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2741872385)
- `2025-04-04T06:22:18Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2741886304)
- `2025-04-04T06:26:13Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2741891972)
- `2025-04-04T06:35:28Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2741907688)
- `2025-04-05T09:02:27Z` `COMMENTED` by `GaoYusong` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2744832539)
- `2025-04-05T12:45:06Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2744881958)
- `2025-04-05T13:21:49Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2744897391)
- `2025-04-05T16:44:39Z` `COMMENTED` by `stmatengss` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2744938460)
- `2025-04-07T06:26:42Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2745640229)
- `2025-04-10T06:20:53Z` `APPROVED` by `ByronHsu` (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2755463365)

## Inline Comment Hotspots

- `python/sglang/srt/disaggregation/conn.py`: 22 inline comment(s)

## High-Signal Discussion

- `2025-04-09T11:54:39Z` `issue` by `yansiyu550`; signals: dtype, memory, mla, race; excerpt: "MOONCAKE CONFIG PATH=./mooncake.json python -m sglang.launch server --model-path /workspace/data/DeepSeek-Coder-V2-Lite-Instruct --disaggregation-mode prefill --port 30000 --host 10.14.4.11 --trust-remote-code log： [2025-04-09 11:41:29 TP0] Only Deepseek V3/R1 can ..." (https://github.com/sgl-project/sglang/pull/4880#issuecomment-2789445449)
- `2025-04-09T13:14:14Z` `issue` by `stmatengss`; signals: dtype, memory, mla, race; excerpt: "MOONCAKE CONFIG PATH=./mooncake.json python -m sglang.launch server --model-path /workspace/data/DeepSeek-Coder-V2-Lite-Instruct --disaggregation-mode prefill --port 30000 --host 10.14.4.11 --trust-remote-code log： [2025-04-09 11:41:29 TP0] Only Deepseek V3/R1 can ..." (https://github.com/sgl-project/sglang/pull/4880#issuecomment-2789664326)
- `2025-04-09T15:50:34Z` `issue` by `stmatengss`; signals: latency, perf, performance, throughput; excerpt: "PD Disaggregation Performance We evaluated the current implementation on two A10 servers. By comparing the performance of a 1P1D configuration with that of two ..." (https://github.com/sgl-project/sglang/pull/4880#issuecomment-2790180538)
- `2025-04-10T06:20:20Z` `issue` by `ByronHsu`; signals: accuracy, deadlock, perf, performance; excerpt: "Thank you mooncake team for the fantastic work!! Let's merge the PR first and follow up with the following items: 1. Currently, the first ..." (https://github.com/sgl-project/sglang/pull/4880#issuecomment-2791674099)
- `2025-04-03T07:53:23Z` `issue` by `JensenFire`; signals: cache, kv cache, tma; excerpt: "Hi @stmatengss, it's amazing! One naive question here: Since you guys support the kv-cache saving in [send kv caches and hidden states]( and loading ..." (https://github.com/sgl-project/sglang/pull/4880#issuecomment-2774786963)
- `2025-04-01T07:05:42Z` `inline` by `Huixxi` `python/sglang/srt/disaggregation/conn.py`:84; signals: cache, kv cache; excerpt: "I met Transfer Return Error in this line. Can you give some advice? Hi, Could you please tell me how to run a sglang ..." (https://github.com/sgl-project/sglang/pull/4880#discussion_r2022270336)
- `2025-04-03T07:59:53Z` `inline` by `Zhou-sx` `python/sglang/srt/disaggregation/conn.py`:84; signals: cache, kv cache; excerpt: "I met Transfer Return Error in this line. Can you give some advice? Hi, Could you please tell me how to run a sglang ..." (https://github.com/sgl-project/sglang/pull/4880#discussion_r2026422056)
- `2025-04-05T13:21:48Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/conn.py`:367; signals: cache, race; excerpt: "@yuan-luo This is the first version which assumes p and d have the same TP size while implementing. Different TP support will be in ..." (https://github.com/sgl-project/sglang/pull/4880#discussion_r2029870935)
- `2025-04-05T09:02:27Z` `inline` by `GaoYusong` `python/sglang/srt/disaggregation/conn.py`:104; signals: overflow; excerpt: "Got an OverflowError, which was resolved by casting prefill index to np.int64(prefill index) and decode index to np.int64(decode index). The same fix is also ..." (https://github.com/sgl-project/sglang/pull/4880#discussion_r2029817847)
- `2025-04-05T12:45:06Z` `inline` by `yuan-luo` `python/sglang/srt/disaggregation/conn.py`:367; signals: layout; excerpt: "I think here has a problem, the self.kv mgr.kv args.engine rank is the decode's tp rank, instead of the prefill's. (Considering the special case: ..." (https://github.com/sgl-project/sglang/pull/4880#discussion_r2029860725)
- `2025-03-30T06:50:29Z` `inline` by `ByronHsu` `python/sglang/srt/disaggregation/conn.py`:145; signals: oom; excerpt: "should this checks if bootstrap room is enqueued first?" (https://github.com/sgl-project/sglang/pull/4880#discussion_r2020080358)
- `2025-03-30T07:32:01Z` `review` `COMMENTED` by `ByronHsu`; signals: general review; excerpt: "Awesome work! Left few comments and questions 1. The current design is based on send/recv, which needs a handshake step. IIUC, for read/write we ..." (https://github.com/sgl-project/sglang/pull/4880#pullrequestreview-2727815927)
