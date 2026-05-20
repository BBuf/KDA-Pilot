# PR Discussion Digest

- Source PR: [sgl-project/sglang#7149](https://github.com/sgl-project/sglang/pull/7149)
- Source page: `sources/prs/sglang/PR-7149.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7149`
- Generated at: `2026-05-20T15:31:02.622537+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-13T09:01:54Z`
- Merged: `2025-10-06T20:24:16Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 17 (approved=3, commented=14)
- Inline review comments: 16
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: Edwardf0t1, Qiaolin-Yu, Ying1123, jingyu-ml
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-13T09:02:30Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Edwardf0t1, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-2923948363)
- `2025-06-13T09:03:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces native ModelOpt quantization support, which is a valuable addition. The changes primarily ... (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-2923950762)
- `2025-09-06T08:40:17Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3191825994)
- `2025-09-11T04:14:33Z` `COMMENTED` by `jingyu-ml` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3208640872)
- `2025-09-12T00:33:57Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3214094273)
- `2025-09-12T00:36:36Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3214099166)
- `2025-09-12T00:36:47Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3214099556)
- `2025-09-12T23:22:53Z` `COMMENTED` by `Qiaolin-Yu` - May you fix the ascend ci? (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3219040245)
- `2025-09-13T04:10:35Z` `APPROVED` by `jingyu-ml` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3219471902)
- `2025-09-21T00:47:02Z` `APPROVED` by `Qiaolin-Yu` - LGTM (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3249325446)
- `2025-09-23T07:51:50Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3256711332)
- `2025-09-24T04:17:20Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3260815662)
- `2025-09-25T08:39:32Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3266497703)
- `2025-09-25T08:39:34Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3266497861)
- `2025-09-28T03:25:04Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3275265073)
- `2025-09-30T05:22:19Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3282628013)
- `2025-10-06T20:24:14Z` `APPROVED` by `Ying1123` (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3307146253)

## Inline Comment Hotspots

- `python/sglang/srt/model_loader/loader.py`: 8 inline comment(s)
- `python/sglang/srt/server_args.py`: 4 inline comment(s)
- `python/sglang/srt/configs/model_config.py`: 2 inline comment(s)
- `test/srt/model_loader/test_modelopt_loader.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-19T18:47:07Z` `issue` by `Edwardf0t1`; signals: accuracy, memory, moe; excerpt: "@Qiaolin-Yu @zhyncs Would you mind reviewing again? The failed ci tests seem unrelated to this PR. The job failed because the test class TestMoEEvalAccuracyLarge ..." (https://github.com/sgl-project/sglang/pull/7149#issuecomment-3313395579)
- `2025-09-23T07:51:49Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_loader/loader.py`:520; signals: hang; excerpt: "Should this be a config? If not, could you change it to a constant and move it to another place?" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2371478194)
- `2025-09-12T23:22:53Z` `review` `COMMENTED` by `Qiaolin-Yu`; signals: general review; excerpt: "May you fix the ascend ci?" (https://github.com/sgl-project/sglang/pull/7149#pullrequestreview-3219040245)
- `2025-09-06T08:40:03Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/server_args.py`:997; signals: general review; excerpt: "Has this library been included in the default installation? If not, could we add something like please use pip install xxx in the log?" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2326663711)
- `2025-09-11T04:14:26Z` `inline` by `jingyu-ml` `python/sglang/srt/model_loader/loader.py`:1832; signals: general review; excerpt: "Overall LGTM, In the future design, can users customize the quantization settings, for example, disabling certain layers through the config file?" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2338471517)
- `2025-09-12T00:36:36Z` `inline` by `Edwardf0t1` `python/sglang/srt/server_args.py`:997; signals: general review; excerpt: "Good point, not at this time, for now I included an installation instruction. I think we can add modelopt as an optional library in ..." (https://github.com/sgl-project/sglang/pull/7149#discussion_r2342645863)
- `2025-09-12T00:36:47Z` `inline` by `Edwardf0t1` `python/sglang/srt/model_loader/loader.py`:1832; signals: general review; excerpt: "Good point - we can show an example to advanced users on how to customize quantization configs, or provide a link to modelopt documentation." (https://github.com/sgl-project/sglang/pull/7149#discussion_r2342646043)
- `2025-09-06T08:34:00Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_loader/loader.py`:496; signals: general review; excerpt: "Use logger instead of print?" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2326657855)
- `2025-09-06T08:35:24Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_loader/loader.py`:82; signals: general review; excerpt: "Is this duplicated with the one inpython/sglang/srt/layers/modelopt utils.py?" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2326658971)
- `2025-09-12T00:33:57Z` `inline` by `Edwardf0t1` `python/sglang/srt/model_loader/loader.py`:82; signals: general review; excerpt: "Good catch, removed." (https://github.com/sgl-project/sglang/pull/7149#discussion_r2342643040)
- `2025-09-24T04:17:20Z` `inline` by `Qiaolin-Yu` `test/srt/model_loader/test_modelopt_loader.py`:1; signals: general review; excerpt: "Add this to test/srt/run suite.py" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2374159120)
- `2025-09-25T08:39:32Z` `inline` by `Edwardf0t1` `test/srt/model_loader/test_modelopt_loader.py`:1; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/7149#discussion_r2378265448)
