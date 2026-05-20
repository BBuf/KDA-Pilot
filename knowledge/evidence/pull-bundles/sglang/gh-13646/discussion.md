# PR Discussion Digest

- Source PR: [sgl-project/sglang#13646](https://github.com/sgl-project/sglang/pull/13646)
- Source page: `sources/prs/sglang/PR-13646.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13646`
- Generated at: `2026-05-20T15:27:49.570137+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-20T10:28:13Z`
- Merged: `2025-11-30T23:59:24Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: Fridge003, YAMY1234, llc-kc, xu-yfei
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-20T10:31:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables pure Tensor Parallelism (TP) for DeepSeekV3.2 models. My review focuses on correctness ... (https://github.com/sgl-project/sglang/pull/13646#pullrequestreview-3486970149)
- `2025-11-27T15:36:21Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13646#pullrequestreview-3516102573)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa_backend.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-25T10:11:23Z` `issue` by `YAMY1234`; signals: attention, hang, layout, mla, perf, performance, sm100, sm90; excerpt: "In forward flashmla sparse(...), pad q’s head dimension to the required multiple (64 on SM90, 128 on SM100+) @YAMY1234 For the Hxx device, the ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3574841204)
- `2025-11-25T08:29:30Z` `issue` by `xu-yfei`; signals: mla, perf, performance, sm100, sm90; excerpt: "In forward flashmla sparse(...), pad q’s head dimension to the required multiple (64 on SM90, 128 on SM100+) @YAMY1234 For the Hxx device, the ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3574339915)
- `2025-11-30T19:06:21Z` `issue` by `YAMY1234`; signals: attention, benchmark, perf, performance; excerpt: "@YAMY1234 Can you add a benchmark for bs=1? Expectedly pure TP should be faster than DP+TP @Fridge003 Added in the PR description Oh I ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3593129499)
- `2025-11-20T18:45:44Z` `issue` by `Fridge003`; signals: block, kernel, mla; excerpt: "Thanks @YAMY1234 If your PR is blocked on FlashMLA side, you can create a new branch at The flashmla kernel now integrated in sglang ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3559540532)
- `2025-11-29T22:10:20Z` `issue` by `Fridge003`; signals: benchmark, perf, performance; excerpt: "@YAMY1234 Can you add a benchmark for bs=1? Expectedly pure TP should be faster than DP+TP @Fridge003 Added in the PR description Oh I ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3591981064)
- `2025-11-28T18:13:33Z` `issue` by `YAMY1234`; signals: benchmark; excerpt: "@YAMY1234 Can you add a benchmark for bs=1? Expectedly pure TP should be faster than DP+TP @Fridge003 Added in the PR description" (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3590076121)
- `2025-11-30T19:19:54Z` `issue` by `Fridge003`; signals: hang; excerpt: "@YAMY1234 Thanks Since this PR will break the usage of deepseek v32, can you please change all the related usage (appending --dp argument) in ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3593157901)
- `2025-11-27T15:01:08Z` `issue` by `Fridge003`; signals: benchmark; excerpt: "@YAMY1234 Can you add a benchmark for bs=1? Expectedly pure TP should be faster than DP+TP" (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3586331897)
- `2025-11-25T11:37:36Z` `issue` by `llc-kc`; signals: general review; excerpt: "@YAMY1234 Hi, I use your branch ( and get some error in PD: I launced prefill as decode as TP16 DP16 EP16 Can you ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3575217550)
- `2025-11-25T18:30:05Z` `issue` by `YAMY1234`; signals: general review; excerpt: "@YAMY1234 Hi, I use your branch ( and get some error in PD: Thanks for pointing this out! For now this PR is mainly ..." (https://github.com/sgl-project/sglang/pull/13646#issuecomment-3576998260)
