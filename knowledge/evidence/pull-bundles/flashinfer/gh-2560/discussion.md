# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2560](https://github.com/flashinfer-ai/flashinfer/pull/2560)
- Source page: `sources/prs/flashinfer/PR-2560.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2560`
- Generated at: `2026-05-20T15:25:04.674074+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-13T21:27:53Z`
- Merged: `2026-03-13T16:07:28Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: blake-snc, coderabbitai, eugr, yzh119
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-13T21:30:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses two issues. First, it removes SM12x support for the CUTLASS FMHA ... (https://github.com/flashinfer-ai/flashinfer/pull/2560#pullrequestreview-3799651355)
- `2026-02-19T02:22:09Z` `APPROVED` by `yzh119` - Make sense to me, thanks for the fix. (https://github.com/flashinfer-ai/flashinfer/pull/2560#pullrequestreview-3823182783)
- `2026-02-28T01:34:33Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2560#pullrequestreview-3869835472)

## Inline Comment Hotspots

- `flashinfer/prefill.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-13T21:28:45Z` `issue` by `coderabbitai`; signals: attention, compile, cuda, cutlass, flashinfer, hang, sm100; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3899586331)
- `2026-02-28T01:34:33Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, failing, flashinfer, hang, pipeline; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) flashinfer/prefill.py (1) ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#pullrequestreview-3869835472)
- `2026-02-13T23:23:40Z` `issue` by `blake-snc`; signals: cuda, flashinfer, hang, sm120; excerpt: "Regarding the suggestion to use get device capability()[0] != 12 instead of is sm120a supported() or is sm121a supported(): the is sm12xa supported() utility ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3900065580)
- `2026-02-17T20:39:07Z` `issue` by `blake-snc`; signals: gemm, mla, sm100, sm120; excerpt: "@eugr Good call. I just opened 2574 which adds is sm12x supported() to utils.py using a major == 12 check (matching the pattern of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3916977724)
- `2026-02-23T01:04:30Z` `issue` by `blake-snc`; signals: cutlass, hang, pipeline, sm100; excerpt: "The internal CI pipeline shows 9/20 passed — are the failures related to this PR or pre-existing? Our changes only narrow CUTLASS FMHA support ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3942061776)
- `2026-02-28T01:26:22Z` `issue` by `blake-snc`; signals: cuda, cutlass, hang, tcgen05; excerpt: "Hey @yzh119 — this PR now has merge conflicts with main. Here's what changed upstream since your approval: 1. CUTLASS FMHA : Main now ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3975973874)
- `2026-02-14T06:46:56Z` `issue` by `eugr`; signals: hang, sm120; excerpt: "That said, if a future SM122a variant appears, adding is sm122a supported() to the check is a one-line change. Happy to refactor if the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3901267028)
- `2026-02-28T01:32:40Z` `issue` by `blake-snc`; signals: cutlass, tcgen05; excerpt: "Update: resolved the merge conflicts and rebased onto main. PR is mergeable now. The resolution keeps our original intent: - CUTLASS FMHA guard: SM12x ..." (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3975985572)
- `2026-02-19T02:22:38Z` `issue` by `yzh119`; signals: flashinfer; excerpt: "@flashinfer-bot run" (https://github.com/flashinfer-ai/flashinfer/pull/2560#issuecomment-3924318590)
