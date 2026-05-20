# PR Discussion Digest

- Source PR: [sgl-project/sglang#14485](https://github.com/sgl-project/sglang/pull/14485)
- Source page: `sources/prs/sglang/PR-14485.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14485`
- Generated at: `2026-05-20T15:28:03.084768+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-05T07:01:21Z`
- Merged: `2025-12-13T05:34:42Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 11
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=8
- Human participants with discussion text: Fridge003, JustinTong0323, dcampora, elvischenv, ispobock
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-06T12:30:36Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/14485#pullrequestreview-3547491425)
- `2025-12-09T07:51:24Z` `COMMENTED` by `dcampora` (https://github.com/sgl-project/sglang/pull/14485#pullrequestreview-3555962424)
- `2025-12-09T07:52:52Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14485#pullrequestreview-3555968456)
- `2025-12-09T09:25:17Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/14485#pullrequestreview-3556324906)
- `2025-12-09T09:26:43Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/14485#pullrequestreview-3556331430)
- `2025-12-11T01:21:06Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/14485#pullrequestreview-3565233377)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`: 2 inline comment(s)
- `python/sglang/srt/configs/model_config.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/flashinfer_ops.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_nvfp4.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/marlin_utils_fp4.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/utils.py`: 1 inline comment(s)
- `python/sglang/srt/models/pixtral.py`: 1 inline comment(s)
- `python/sglang/srt/utils/mistral_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-06T12:17:00Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`:5; signals: hopper, moe; excerpt: "Have we tested the w4a16 code path? If not, better to do it in another PR. We may need it on Hopper or previous ..." (https://github.com/sgl-project/sglang/pull/14485#discussion_r2594792502)
- `2025-12-06T12:23:13Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`:472; signals: cutlass, flashinfer; excerpt: "w4a4 supports both flashinfer and cutlass, right? I think we should do something similar to the below method, check the capability." (https://github.com/sgl-project/sglang/pull/14485#discussion_r2594796977)
- `2025-12-06T12:11:58Z` `inline` by `elvischenv` `python/sglang/srt/layers/attention/flashinfer_ops.py`; signals: attention, flashinfer; excerpt: "This is a mm op, why put under attention layer?" (https://github.com/sgl-project/sglang/pull/14485#discussion_r2594788435)
- `2025-12-06T12:18:05Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_nvfp4.py`; signals: fp4, nvfp4; excerpt: "Same comment, can do in follow-up PR." (https://github.com/sgl-project/sglang/pull/14485#discussion_r2594793365)
- `2025-12-06T12:29:27Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/utils.py`:568; signals: fp4, nvfp4; excerpt: "Add a comment to clarify this method is nvfp4 specific." (https://github.com/sgl-project/sglang/pull/14485#discussion_r2594806247)
- `2025-12-09T07:51:23Z` `inline` by `dcampora` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/__init__.py`:5; signals: moe; excerpt: "vllm doesn't have w4a16 moe support either, so I guess it's not supported - I can remove it from the PR, but do we ..." (https://github.com/sgl-project/sglang/pull/14485#discussion_r2601486932)
- `2025-12-06T12:26:50Z` `inline` by `elvischenv` `python/sglang/srt/layers/quantization/marlin_utils_fp4.py`; signals: fp4; excerpt: "This seems to be only used by w4a16." (https://github.com/sgl-project/sglang/pull/14485#discussion_r2594801722)
- `2025-12-09T03:41:02Z` `issue` by `elvischenv`; signals: accuracy; excerpt: "Before merging main, the server can be launched and the accuracy is good. After merging, I got lots of rope related issues: 1. 14627 ..." (https://github.com/sgl-project/sglang/pull/14485#issuecomment-3630104183)
- `2025-12-10T02:18:25Z` `issue` by `elvischenv`; signals: general review; excerpt: "@elvischenv @dcampora This PR also handled the rope issue. Is it conflicting with your code? 14745 @Fridge003 It won't have conflicts, but that fix ..." (https://github.com/sgl-project/sglang/pull/14485#issuecomment-3635067663)
- `2025-12-10T22:08:47Z` `issue` by `Fridge003`; signals: general review; excerpt: "@elvischenv We reverted the transformers version to 4.57 and I removed the logics in model config.py. Please check whether it works on your side" (https://github.com/sgl-project/sglang/pull/14485#issuecomment-3639164898)
