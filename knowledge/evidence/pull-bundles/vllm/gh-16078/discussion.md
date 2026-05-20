# PR Discussion Digest

- Source PR: [vllm-project/vllm#16078](https://github.com/vllm-project/vllm/pull/16078)
- Source page: `sources/prs/vllm/PR-16078.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16078`
- Generated at: `2026-05-20T15:34:51.398777+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-04T22:43:18Z`
- Merged: `2025-06-07T04:58:55Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 55 (approved=3, commented=52)
- Inline review comments: 56
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=23, outdated=13
- Human participants with discussion text: ProExpertProg, WoosukKwon, drisspg, houseroad, mergify, robertgshaw2-redhat, tlrmchlsmth, youkaichao, zou3519
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-10T22:51:41Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2758679134)
- `2025-04-16T03:00:17Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2770515554)
- `2025-04-16T03:05:06Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2770520257)
- `2025-04-16T03:05:43Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2770520793)
- `2025-04-16T03:06:01Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2770521121)
- `2025-04-16T03:07:15Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2770522448)
- `2025-04-16T03:08:39Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2770524946)
- `2025-04-17T17:45:09Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2776520212)
- `2025-04-25T21:39:13Z` `COMMENTED` by `houseroad` - This is exciting, thanks! (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2795313355)
- `2025-04-30T14:23:40Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2807257492)
- `2025-04-30T14:28:21Z` `COMMENTED` by `zou3519` - The main feedback I have from the compilation side is that we don't support compile(custom op(compile(flex attention))) (or ... (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2807272932)
- `2025-04-30T14:34:27Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2807292154)
- `2025-05-03T23:54:42Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2813322921)
- `2025-05-03T23:55:01Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2813322961)
- `2025-05-07T20:42:10Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2823160352)
- `2025-05-07T20:42:32Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2823161115)
- `2025-05-08T16:21:43Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2825705404)
- `2025-05-08T22:01:35Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2826458822)
- `2025-05-08T22:02:31Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2826460022)
- `2025-05-08T22:14:13Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2826474541)
- `2025-05-08T22:33:33Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2826495602)
- `2025-05-09T01:25:26Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2826735301)
- `2025-05-09T01:27:07Z` `COMMENTED` by `drisspg` (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2826736919)
- `2025-05-12T19:12:23Z` `COMMENTED` by `ProExpertProg` - A couple of thoughts. Also, an unrelated question: could we make the FlexAttention backend "extensible"? I assume a ... (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2834191125)
- ... 31 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/v1/attention/backends/flex_attention.py`: 40 inline comment(s)
- `vllm/attention/layer.py`: 6 inline comment(s)
- `tests/kernels/test_flex_attention.py`: 3 inline comment(s)
- `requirements/cuda.txt`: 2 inline comment(s)
- `vllm/platforms/interface.py`: 2 inline comment(s)
- `vllm/platforms/cuda.py`: 1 inline comment(s)
- `vllm/attention/backends/abstract.py`: 1 inline comment(s)
- `vllm/engine/arg_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-07T20:42:10Z` `inline` by `drisspg` `vllm/v1/attention/backends/flex_attention.py`:32; signals: attention, cache, compile, kernel, kv cache, oom; excerpt: "This is a good point, however using flex without compile in vllm is pretty silly since it is a very unfused kernel and will ..." (https://github.com/vllm-project/vllm/pull/16078#discussion_r2078463014)
- `2025-04-30T14:28:21Z` `review` `COMMENTED` by `zou3519`; signals: attention, compile, perf, performance; excerpt: "The main feedback I have from the compilation side is that we don't support compile(custom op(compile(flex attention))) (or anything really) that well. This problem ..." (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2807272932)
- `2025-06-02T15:58:33Z` `review` `COMMENTED` by `WoosukKwon`; signals: benchmark, perf, performance, throughput; excerpt: "@drisspg I'm seeing 10x slowdown of e2e performance on sharegpt throughput benchmark (I'm using torch 2.7.0). Is this expected? Is this because re-compilation happens ..." (https://github.com/vllm-project/vllm/pull/16078#pullrequestreview-2889061977)
- `2025-04-25T21:38:26Z` `inline` by `houseroad` `tests/kernels/test_flex_attention.py`:90; signals: attention, cache, kernel, kv cache; excerpt: "Do we have a way to test the KV cache management?" (https://github.com/vllm-project/vllm/pull/16078#discussion_r2060909231)
- `2025-06-03T15:56:04Z` `issue` by `drisspg`; signals: attention, block, compile, race; excerpt: "@WoosukKwon Yup, as implemented this is expected and touched upon in the summary but it is not due to recompilation, the problem is that ..." (https://github.com/vllm-project/vllm/pull/16078#issuecomment-2936092679)
- `2025-04-16T03:05:05Z` `inline` by `drisspg` `vllm/v1/attention/backends/flex_attention.py`:77; signals: attention, block, perf; excerpt: "this was having weird perf results will highlight later. TBH this is the stickiest point since we rebuild at every decode step and this ..." (https://github.com/vllm-project/vllm/pull/16078#discussion_r2045917201)
- `2025-04-30T14:23:40Z` `inline` by `zou3519` `vllm/v1/attention/backends/flex_attention.py`:463; signals: attention, cache, compile; excerpt: "Btw, I don't know how this interacts with vLLM's multigraph dynamic shape compilation. It is possible that we will have a problem there. The ..." (https://github.com/vllm-project/vllm/pull/16078#discussion_r2068775536)
- `2025-04-30T14:34:27Z` `inline` by `zou3519` `vllm/v1/attention/backends/flex_attention.py`:126; signals: attention, cuda, cudagraph; excerpt: "@tlrmchlsmth @chanh FlexAttention should be CUDAGraphable so we could also use full CUDAGraphs with it. Is there anything special we would need to do ..." (https://github.com/vllm-project/vllm/pull/16078#discussion_r2068795732)
- `2025-05-12T19:04:36Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flex_attention.py`:126; signals: attention, cuda, triton; excerpt: "I think we should add either a property or likely better a method supports cuda graph to the attention backend that we call in ..." (https://github.com/vllm-project/vllm/pull/16078#discussion_r2085283600)
- `2025-05-28T23:29:26Z` `inline` by `drisspg` `vllm/v1/attention/backends/flex_attention.py`:436; signals: attention, cache, kv cache; excerpt: "Ohh that makes way more sense, I am not quite sure how if its possible to get this to work, because on profiling run ..." (https://github.com/vllm-project/vllm/pull/16078#discussion_r2112921335)
- `2025-05-30T00:44:45Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flex_attention.py`:436; signals: attention, cuda, cudagraph; excerpt: "We could just do full cudagraphs by default when using flex attention, if that's supported? They set up some attention metadata" (https://github.com/vllm-project/vllm/pull/16078#discussion_r2114951987)
- `2025-05-30T00:52:38Z` `inline` by `drisspg` `vllm/v1/attention/backends/flex_attention.py`:436; signals: attention, cuda, cudagraph; excerpt: "Is the full cudagraph path landed yet? I remember there was a PR somewhere but I can't find right now" (https://github.com/vllm-project/vllm/pull/16078#discussion_r2114959330)
