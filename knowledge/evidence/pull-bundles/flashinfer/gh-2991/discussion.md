# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2991](https://github.com/flashinfer-ai/flashinfer/pull/2991)
- Source page: `sources/prs/flashinfer/PR-2991.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2991`
- Generated at: `2026-05-20T15:26:02.015335+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-06T07:34:46Z`
- Merged: `2026-04-08T03:53:11Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 9 (approved=2, changes_requested=1, commented=6)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: bkryu, coderabbitai, harrisonlimh, nv-yunzheq, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-06T07:37:18Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the supported compute capabilities for the mm M1 16 K7168 N256 shape ... (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4060843959)
- `2026-04-06T07:37:56Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) flashinfer/gemm/routergemm.py (1) 218-219: Minor: Docstring mentions only "compute capability 10.0" but 10.3 is now ... (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4060846461)
- `2026-04-06T16:28:14Z` `CHANGES_REQUESTED` by `bkryu` - Hi @harrisonlimh, thank you for contributing this PR. The addition in this PR is probably valid, but it ... (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4063097043)
- `2026-04-06T17:52:04Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4063547650)
- `2026-04-06T17:54:21Z` `COMMENTED` by `harrisonlimh` (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4063559044)
- `2026-04-06T17:59:45Z` `COMMENTED` by `nv-yunzheq` (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4063586950)
- `2026-04-06T20:12:39Z` `COMMENTED` by `harrisonlimh` (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4064281666)
- `2026-04-07T01:15:16Z` `APPROVED` by `bkryu` - Thanks for the updates @harrisonlimh LGTM (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4065278171)
- `2026-04-07T05:39:33Z` `APPROVED` by `nv-yunzheq` - LGTM, thanks for contributing! (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4065962415)

## Inline Comment Hotspots

- `flashinfer/gemm/routergemm.py`: 3 inline comment(s)
- `tests/model_optimizations/test_dsv3_router_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-06T07:37:56Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, flashinfer, gemm, hang; excerpt: "🧹 Nitpick comments (1) flashinfer/gemm/routergemm.py (1) 218-219: Minor: Docstring mentions only "compute capability 10.0" but 10.3 is now also supported. The Note section still ..." (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4060846461)
- `2026-04-06T17:52:04Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, gemm, hang, sm100; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) tests/model optimizations/test ..." (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4063547650)
- `2026-04-06T07:35:03Z` `issue` by `coderabbitai`; signals: cuda, flashinfer, gemm, hang, sm100; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/flashinfer-ai/flashinfer/pull/2991#issuecomment-4190941084)
- `2026-04-06T16:28:14Z` `review` `CHANGES_REQUESTED` by `bkryu`; signals: gemm, sm100; excerpt: "Hi @harrisonlimh, thank you for contributing this PR. The addition in this PR is probably valid, but it would be a good idea to ..." (https://github.com/flashinfer-ai/flashinfer/pull/2991#pullrequestreview-4063097043)
- `2026-04-06T16:25:31Z` `inline` by `bkryu` `flashinfer/gemm/routergemm.py`:82; signals: flashinfer, gemm; excerpt: "Should we add 103 here as well?" (https://github.com/flashinfer-ai/flashinfer/pull/2991#discussion_r3040444869)
- `2026-04-06T17:54:21Z` `inline` by `harrisonlimh` `flashinfer/gemm/routergemm.py`:82; signals: flashinfer, gemm; excerpt: "Updated to expand the support for mm M1 16 K7168 N128 and and also the test coverage! PTAL." (https://github.com/flashinfer-ai/flashinfer/pull/2991#discussion_r3040833958)
- `2026-04-06T16:44:05Z` `issue` by `nv-yunzheq`; signals: gemm, sm100; excerpt: "Moreover, there is a test dsv3 router gemm.py file which only tests the function against sm100 right now, we want to expand that to ..." (https://github.com/flashinfer-ai/flashinfer/pull/2991#issuecomment-4193561788)
- `2026-04-06T17:59:45Z` `inline` by `nv-yunzheq` `tests/model_optimizations/test_dsv3_router_gemm.py`:243; signals: gemm; excerpt: "Maybe also here?" (https://github.com/flashinfer-ai/flashinfer/pull/2991#discussion_r3040859595)
- `2026-04-06T20:12:39Z` `inline` by `harrisonlimh` `tests/model_optimizations/test_dsv3_router_gemm.py`:243; signals: gemm; excerpt: "Done." (https://github.com/flashinfer-ai/flashinfer/pull/2991#discussion_r3041458070)
