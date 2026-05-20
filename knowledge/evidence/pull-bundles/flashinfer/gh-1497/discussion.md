# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1497](https://github.com/flashinfer-ai/flashinfer/pull/1497)
- Source page: `sources/prs/flashinfer/PR-1497.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1497`
- Generated at: `2026-05-20T15:22:46.765841+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-15T18:47:10Z`
- Merged: `2025-08-18T20:46:08Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: bkryu, nv-yunzheq, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-15T18:47:34Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @nv-yunzheq, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3124823727)
- `2025-08-15T18:49:05Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds Mixture-of-Experts (MoE) benchmark routines to the FlashInfer benchmark suite. The changes include ... (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3124827232)
- `2025-08-15T20:31:58Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3125070846)
- `2025-08-15T20:34:34Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3125077571)
- `2025-08-15T20:37:30Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3125085208)
- `2025-08-18T15:51:44Z` `APPROVED` by `yzh119` - LGTM overall, thanks @nv-yunzheq @bkryu ! (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3128947264)
- `2025-08-18T16:53:57Z` `COMMENTED` by `nv-yunzheq` (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3129173973)
- `2025-08-18T17:45:06Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1497#pullrequestreview-3129329135)

## Inline Comment Hotspots

- `benchmarks/routines/moe.py`: 7 inline comment(s)
- `benchmarks/routines/flashinfer_benchmark_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-15T20:31:58Z` `inline` by `bkryu` `benchmarks/routines/flashinfer_benchmark_utils.py`:44; signals: attention, benchmark, flashinfer, moe; excerpt: "Can you actually move the backend in "moe" and "attention" to "general" to avoid redundancy?" (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2279836431)
- `2025-08-15T20:37:30Z` `inline` by `bkryu` `benchmarks/routines/moe.py`:986; signals: benchmark, hang, moe; excerpt: "Since cur res is a defaultdict, I'm finding that it is okay to remove these lines for brevity. I'll also be making that change ..." (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2279844248)
- `2025-08-15T20:34:34Z` `inline` by `bkryu` `benchmarks/routines/moe.py`:370; signals: benchmark, moe; excerpt: "I'm generally not familiar with the MOE operation. Were the FLOPs and TB/s calculations brought over from existing benchmark files? If not, let's ask ..." (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2279840171)
- `2025-08-18T15:51:06Z` `inline` by `yzh119` `benchmarks/routines/moe.py`:446; signals: benchmark, moe; excerpt: "This means we will not skip expert weights if they are not activated (in small batch size case), is that correct?" (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2282800995)
- `2025-08-18T16:53:57Z` `inline` by `nv-yunzheq` `benchmarks/routines/moe.py`:446; signals: benchmark, moe; excerpt: "No. We will skip expert weights if they are not activated. The code below uses num active experts weight bytes per expert. So, only ..." (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2282947017)
- `2025-08-18T15:49:42Z` `inline` by `yzh119` `benchmarks/routines/moe.py`:370; signals: benchmark, moe; excerpt: "The moe tflops calculation looks correct to me." (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2282797149)
- `2025-08-18T17:45:06Z` `inline` by `yzh119` `benchmarks/routines/moe.py`:446; signals: benchmark, moe; excerpt: "Got it, so the num active experts need to be specified explicitly." (https://github.com/flashinfer-ai/flashinfer/pull/1497#discussion_r2283056381)
