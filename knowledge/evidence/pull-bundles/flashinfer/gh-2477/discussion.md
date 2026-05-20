# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2477](https://github.com/flashinfer-ai/flashinfer/pull/2477)
- Source page: `sources/prs/flashinfer/PR-2477.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2477`
- Generated at: `2026-05-20T15:24:54.397263+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-03T12:56:32Z`
- Merged: `2026-02-11T16:37:33Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 16 (approved=3, commented=13)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=2
- Human participants with discussion text: DomBrown, PerkzZheng, bkryu, coderabbitai, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-03T12:58:48Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Skip-Softmax attention for Blackwell GPUs in TRTLLM-Gen kernels, which is ... (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3745115930)
- `2026-02-03T13:02:30Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3745132758)
- `2026-02-03T13:54:24Z` `APPROVED` by `PerkzZheng` - The changes LGTM. thanks! (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3745417771)
- `2026-02-03T16:10:04Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3746175257)
- `2026-02-09T18:27:31Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774719047)
- `2026-02-09T18:28:36Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774724026)
- `2026-02-09T18:28:52Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774725232)
- `2026-02-09T18:31:09Z` `COMMENTED` by `bkryu` - Thank you @DomBrown. Confirmed that the CI failures are unrelated. Left a minor comment about docstrings. (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774735530)
- `2026-02-09T19:40:01Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774962992)
- `2026-02-09T19:42:33Z` `APPROVED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774970259)
- `2026-02-09T19:48:42Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774987964)
- `2026-02-09T21:44:25Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3775544171)
- `2026-02-09T21:51:20Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3775582195)
- `2026-02-09T21:51:51Z` `COMMENTED` by `DomBrown` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3775583997)
- `2026-02-09T22:23:54Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3775710898)
- `2026-02-09T22:24:05Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3775711512)

## Inline Comment Hotspots

- `tests/attention/test_trtllm_gen_attention.py`: 6 inline comment(s)
- `flashinfer/decode.py`: 3 inline comment(s)
- `flashinfer/prefill.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-03T12:56:43Z` `issue` by `coderabbitai`; signals: attention, dtype, flashinfer, hang, kernel, mla, tma; excerpt: "📝 Walkthrough Walkthrough Adds optional softmax-skipping controls (bool and threshold scale factor) across FMHA: launcher, kernel params, kernel hash, and Python prefill/decode APIs; propagates ..." (https://github.com/flashinfer-ai/flashinfer/pull/2477#issuecomment-3841155906)
- `2026-02-09T18:27:31Z` `inline` by `bkryu` `flashinfer/decode.py`:1252; signals: accuracy, flashinfer, kernel, perf, performance; excerpt: "Can you provide a bit more detail in the docstring here for the user? What should the user takeaway from this? Perhaps providing the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2783981528)
- `2026-02-09T21:51:20Z` `inline` by `DomBrown` `tests/attention/test_trtllm_gen_attention.py`:571; signals: attention, hang, kernel, tile; excerpt: "We would have to write an entire reference kernel in torch. It's something I intend to come back to later. It's non trivial because ..." (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2784697692)
- `2026-02-09T19:48:42Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, kernel, tma; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (4) flashinfer/prefill.py (1) ..." (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774987964)
- `2026-02-03T16:10:04Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, tma; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3746175257)
- `2026-02-09T21:44:25Z` `inline` by `yzh119` `tests/attention/test_trtllm_gen_attention.py`:571; signals: attention, tma; excerpt: "This means we didn't test the case where skip softmax threshold scale factor is not 0 right? Is there a way we can test ..." (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2784671694)
- `2026-02-03T13:02:30Z` `inline` by `DomBrown` `tests/attention/test_trtllm_gen_attention.py`:1339; signals: attention; excerpt: "This is deliberate and will be enabled at a later time." (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2758961270)
- `2026-02-09T18:28:36Z` `inline` by `bkryu` `flashinfer/decode.py`:2236; signals: flashinfer; excerpt: "Ditto" (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2783986236)
- `2026-02-09T18:28:52Z` `inline` by `bkryu` `flashinfer/prefill.py`:3628; signals: flashinfer; excerpt: "Ditto" (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2783987374)
- `2026-02-09T18:31:09Z` `review` `COMMENTED` by `bkryu`; signals: general review; excerpt: "Thank you @DomBrown. Confirmed that the CI failures are unrelated. Left a minor comment about docstrings." (https://github.com/flashinfer-ai/flashinfer/pull/2477#pullrequestreview-3774735530)
- `2026-02-09T19:40:00Z` `inline` by `DomBrown` `flashinfer/decode.py`:1252; signals: flashinfer; excerpt: "Updated" (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2784203800)
- `2026-02-09T21:51:51Z` `inline` by `DomBrown` `tests/attention/test_trtllm_gen_attention.py`:571; signals: attention; excerpt: "This is currently tested very robustly in trtllm-gen, I think it's safe for now" (https://github.com/flashinfer-ai/flashinfer/pull/2477#discussion_r2784699494)
