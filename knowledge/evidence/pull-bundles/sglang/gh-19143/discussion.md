# PR Discussion Digest

- Source PR: [sgl-project/sglang#19143](https://github.com/sgl-project/sglang/pull/19143)
- Source page: `sources/prs/sglang/PR-19143.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19143`
- Generated at: `2026-05-20T15:28:47.218660+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-22T06:09:53Z`
- Merged: `2026-04-16T23:51:33Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 16
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=0, outdated=7
- Human participants with discussion text: BowenBao, HaiShaw, bingxche, chatgpt-codex-connector, fengli1702, haohui, yctseng0211
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-02-22T06:14:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for MXFP4 quantized models on AMD GPUs by leveraging the Petit ... (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-3836824342)
- `2026-02-22T06:16:03Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: 600bb8594e ℹ️ About ... (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-3836824971)
- `2026-02-22T15:23:01Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-3838109211)
- `2026-02-22T15:23:53Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-3838111636)
- `2026-02-22T15:24:28Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-3838113338)
- `2026-03-27T01:15:22Z` `COMMENTED` by `BowenBao` - Thank you for contribution! I'm not sure if is the model mentioned in the PR description. It is ... (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4018276629)
- `2026-04-03T16:05:45Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4056279696)
- `2026-04-03T16:06:25Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4056281644)
- `2026-04-03T16:06:48Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4056282847)
- `2026-04-04T01:18:23Z` `APPROVED` by `BowenBao` - Looks good overall, thank you! cc @kkHuang-amd , @HaiShaw (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4057843271)
- `2026-04-04T04:38:45Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4058088636)
- `2026-04-04T04:39:09Z` `COMMENTED` by `fengli1702` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4058088962)
- `2026-04-16T23:50:13Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4125131738)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/petit_utils.py`: 6 inline comment(s)
- `python/sglang/srt/layers/quantization/petit_mxfp4.py`: 4 inline comment(s)
- `python/sglang/srt/layers/quantization/petit.py`: 4 inline comment(s)
- `python/sglang/srt/configs/model_config.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-22T06:16:03Z` `inline` by `chatgpt-codex-connector` `python/sglang/srt/layers/quantization/petit_mxfp4.py`:94; signals: fp4, moe, mxfp4; excerpt: ". In this commit, PetitMxfp4Config.get quant method only handles LinearBase, while MXFP4 MoE handling is implemented in mxfp4.py, so auto-switching all MXFP4 models here ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2837203530)
- `2026-02-22T15:23:53Z` `inline` by `fengli1702` `python/sglang/srt/layers/quantization/petit_mxfp4.py`:94; signals: fp4, moe, mxfp4; excerpt: "I gated PetitMxfp4Config.override quantization method to only auto-select when the user explicitly sets quantization=petit mxfp4, preserving existing MXFP4/MoE flows." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2838115327)
- `2026-03-27T00:57:17Z` `inline` by `BowenBao` `python/sglang/srt/configs/model_config.py`:880; signals: fp4, moe, mxfp4; excerpt: "probably only "quark" is the compatible quant method, I'm not sure if there are modelopt mxfp4 models? "mxfp4" quant method supports moe only at ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2998447868)
- `2026-03-27T00:59:55Z` `inline` by `BowenBao` `python/sglang/srt/layers/quantization/petit.py`:39; signals: fp4, mxfp4, nvfp4; excerpt: "if this also supports MXFP4, should the config class be renamed? e.g. PetitNvFp4Config - PetitFp4Config What's the relation of this with python/sglang/srt/layers/quantization/petit mxfp4.py? both ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2998453496)
- `2026-04-03T16:05:45Z` `inline` by `fengli1702` `python/sglang/srt/configs/model_config.py`:880; signals: aligned, fp4, mxfp4; excerpt: "Thanks for the review. Yes, the target model is amd/Llama-3.3-70B-Instruct-MXFP4-Preview, and its quant method is quark. To clarify, amd/Llama-3.3-70B-Instruct-MXFP4-Preview is an MXFP4 checkpoint, while ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r3033415839)
- `2026-04-03T16:06:25Z` `inline` by `fengli1702` `python/sglang/srt/layers/quantization/petit.py`:39; signals: fp4, mxfp4, nvfp4; excerpt: "I refactored this to make the boundary explicit: - petit nvfp4.py: NVFP4-only implementation (PetitNvFp4Config). - petit mxfp4.py: MXFP4-only implementation. - petit.py: now only a ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r3033417895)
- `2026-04-04T04:38:45Z` `inline` by `fengli1702` `python/sglang/srt/layers/quantization/petit_utils.py`:145; signals: fp4, hang, mxfp4; excerpt: "I changed this check from any(...) to all(...), so we only treat it as Quark-MXFP4 compatible when all discovered quant configs match MXFP4 weight ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r3035113878)
- `2026-04-04T04:39:09Z` `inline` by `fengli1702` `python/sglang/srt/layers/quantization/petit_utils.py`:117; signals: fp4, kernel, mxfp4; excerpt: "Agreed. I relaxed the input tensors check for petit mxfp4. Since this path is w4a16, input quant config is not used by the kernel. ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r3035114247)
- `2026-03-27T01:15:22Z` `review` `COMMENTED` by `BowenBao`; signals: fp4, mxfp4; excerpt: "Thank you for contribution! I'm not sure if is the model mentioned in the PR description. It is quantized by quark. If not could ..." (https://github.com/sgl-project/sglang/pull/19143#pullrequestreview-4018276629)
- `2026-02-22T15:23:01Z` `inline` by `fengli1702` `python/sglang/srt/layers/quantization/petit_mxfp4.py`:108; signals: fp4, mxfp4; excerpt: "I removed the duplication by extracting layer-pattern exclusion into a shared helper (is layer excluded by patterns) and reused it in both petit.py and ..." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2838113921)
- `2026-02-22T15:24:28Z` `inline` by `fengli1702` `python/sglang/srt/layers/quantization/petit.py`:89; signals: fp4, nvfp4; excerpt: "I made NVFP4 serialized-checkpoint detection case-insensitive in petit.py so lowercase nvfp4 configs stay consistent between validation and runtime behavior." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2838116175)
- `2026-03-27T01:12:21Z` `inline` by `BowenBao` `python/sglang/srt/layers/quantization/petit_utils.py`:60; signals: fp4, mxfp4; excerpt: "does petit mxfp4 support running quark model? the quant method would show up as "quark" in that case." (https://github.com/sgl-project/sglang/pull/19143#discussion_r2998480298)
