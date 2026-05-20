# PR Discussion Digest

- Source PR: [vllm-project/vllm#14570](https://github.com/vllm-project/vllm/pull/14570)
- Source page: `sources/prs/vllm/PR-14570.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14570`
- Generated at: `2026-05-20T15:34:28.841892+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-10T15:40:03Z`
- Merged: `2025-03-20T05:14:20Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: JaheimLee, LucasWilkinson, NickLucche, mergify, mickaelseznec
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-03-11T18:18:50Z` `COMMENTED` by `LucasWilkinson` - Thanks for the contribution! Looks clean 😄, ill approve once we can get it updated to use vllm ... (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2675648284)
- `2025-03-12T19:31:17Z` `COMMENTED` by `mickaelseznec` (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2679666384)
- `2025-03-12T19:33:26Z` `COMMENTED` by `mickaelseznec` (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2679670580)
- `2025-03-13T01:27:18Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2680216894)
- `2025-03-14T11:07:32Z` `COMMENTED` by `mickaelseznec` (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2685177512)
- `2025-03-20T05:14:19Z` `APPROVED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2701221441)

## Inline Comment Hotspots

- `vllm/platforms/cuda.py`: 4 inline comment(s)
- `tests/kernels/test_flash_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-13T01:27:18Z` `inline` by `LucasWilkinson` `vllm/platforms/cuda.py`:243; signals: attention, cuda, mla; excerpt: "Do you prefer if I move that function in another file? vllm/attention/backends/versions.py for example? sure, maybe move it to: for now, since there is ..." (https://github.com/vllm-project/vllm/pull/14570#discussion_r1992512223)
- `2025-03-11T18:16:47Z` `inline` by `LucasWilkinson` `vllm/platforms/cuda.py`:243; signals: attention, cuda; excerpt: "we should keep this check but restrict it to FA2, i.e. check get flash attn version() != 2 (get flash attn version() is in ..." (https://github.com/vllm-project/vllm/pull/14570#discussion_r1989887561)
- `2025-03-12T19:33:25Z` `inline` by `mickaelseznec` `vllm/platforms/cuda.py`:243; signals: attention, cuda; excerpt: "Agree that this might be improved, but I can't directly import get flash attn version because of circular dependency. Do you prefer if I ..." (https://github.com/vllm-project/vllm/pull/14570#discussion_r1992174757)
- `2025-03-14T11:07:32Z` `inline` by `mickaelseznec` `vllm/platforms/cuda.py`:243; signals: attention, cuda; excerpt: "I had to move it to vllm/fa utils.py because of how vllm/attention/ init .py imports a bunch of stuff for convenience." (https://github.com/vllm-project/vllm/pull/14570#discussion_r1995357476)
- `2025-03-11T09:30:52Z` `issue` by `mickaelseznec`; signals: accuracy, failing; excerpt: "CI failing because vllm/tests/entrypoints/openai/test accuracy.py from" (https://github.com/vllm-project/vllm/pull/14570#issuecomment-2713332992)
- `2025-03-12T19:31:17Z` `inline` by `mickaelseznec` `tests/kernels/test_flash_attn.py`:282; signals: kernel; excerpt: "I can add tests here, but these type of scaling isn't supported by vLLM for the moment. I believe that whenever we add support ..." (https://github.com/vllm-project/vllm/pull/14570#discussion_r1992172268)
- `2025-03-15T22:35:26Z` `issue` by `LucasWilkinson`; signals: failing, kernel; excerpt: "apologies for the delay, the CI should be working now. There appears to be failing kernel tests" (https://github.com/vllm-project/vllm/pull/14570#issuecomment-2727036513)
- `2025-03-11T18:10:34Z` `inline` by `LucasWilkinson` `tests/kernels/test_flash_attn.py`:282; signals: kernel; excerpt: "nit: could we maybe test per-head scales here too?, i.e. also test with non-zero strides" (https://github.com/vllm-project/vllm/pull/14570#discussion_r1989878063)
- `2025-03-11T18:18:50Z` `review` `COMMENTED` by `LucasWilkinson`; signals: general review; excerpt: "Thanks for the contribution! Looks clean 😄, ill approve once we can get it updated to use vllm flash attn, added a couple comments" (https://github.com/vllm-project/vllm/pull/14570#pullrequestreview-2675648284)
- `2025-03-11T18:05:41Z` `issue` by `LucasWilkinson`; signals: cache; excerpt: "@mickaelseznec apologies for the delay, has been merged, you can now point to vllm flash attn We will need to populate the sccache on ..." (https://github.com/vllm-project/vllm/pull/14570#issuecomment-2715260777)
- `2025-03-11T11:43:04Z` `issue` by `NickLucche`; signals: block; excerpt: "This is a known issue, PR addressing it here It won't block your PR." (https://github.com/vllm-project/vllm/pull/14570#issuecomment-2713837191)
- `2025-03-14T10:59:30Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @mickaelseznec." (https://github.com/vllm-project/vllm/pull/14570#issuecomment-2724327911)
