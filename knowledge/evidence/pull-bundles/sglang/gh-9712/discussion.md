# PR Discussion Digest

- Source PR: [sgl-project/sglang#9712](https://github.com/sgl-project/sglang/pull/9712)
- Source page: `sources/prs/sglang/PR-9712.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9712`
- Generated at: `2026-05-20T15:31:39.825927+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-27T21:38:54Z`
- Merged: `2025-08-30T00:13:52Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Edwardf0t1, donglinz, pavanimajety, trevor-m, yiakwy-xpu-ml-framework-team
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 8

## Review Decisions

- `2025-08-27T21:39:11Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @pavanimajety, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9712#pullrequestreview-3161831135)
- `2025-08-27T22:40:52Z` `APPROVED` by `trevor-m` - LGTM (https://github.com/sgl-project/sglang/pull/9712#pullrequestreview-3161990196)
- `2025-08-28T01:27:31Z` `APPROVED` by `Edwardf0t1` - Thanks @pavanimajety for the fix. We didn't expect our new config could break weight loading of fp4 ckpts ... (https://github.com/sgl-project/sglang/pull/9712#pullrequestreview-3162635360)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-08-28T03:12:18Z` `issue` by `yiakwy-xpu-ml-framework-team`; signals: bf16, fp4, kernel, mxfp4; excerpt: "The previous ModelOpt quant method to mxfp4 from bf16 python script is extremely slow (no kernel, just pytorch codes to select closest value from ..." (https://github.com/sgl-project/sglang/pull/9712#issuecomment-3231639266)
- `2025-08-29T04:52:11Z` `issue` by `pavanimajety`; signals: fp4, hang, nvfp4; excerpt: "@yiakwy-xpu-ml-framework-team This is for nvfp4 models. Could you provide more code pointer into what is extremely slow? This PR changes weight loading logic for ..." (https://github.com/sgl-project/sglang/pull/9712#issuecomment-3235718030)
- `2025-08-28T01:27:31Z` `review` `APPROVED` by `Edwardf0t1`; signals: fp4; excerpt: "Thanks @pavanimajety for the fix. We didn't expect our new config could break weight loading of fp4 ckpts in SGLang." (https://github.com/sgl-project/sglang/pull/9712#pullrequestreview-3162635360)
