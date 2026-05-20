# PR Discussion Digest

- Source PR: [vllm-project/vllm#16263](https://github.com/vllm-project/vllm/pull/16263)
- Source page: `sources/prs/vllm/PR-16263.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16263`
- Generated at: `2026-05-20T15:34:54.583987+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-08T12:30:56Z`
- Merged: `2025-05-02T19:44:19Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 26 (approved=2, changes_requested=1, commented=23)
- Inline review comments: 23
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=0, outdated=4
- Human participants with discussion text: divakar-amd, houseroad, shajrawi, xw285cornell
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-08T15:48:26Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2750347227)
- `2025-04-08T15:54:05Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2750530286)
- `2025-04-08T16:40:52Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2750696123)
- `2025-04-08T16:48:02Z` `COMMENTED` by `houseroad` - Thanks for the improvement! (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2750722812)
- `2025-04-08T19:07:44Z` `COMMENTED` by `shajrawi` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751137474)
- `2025-04-08T19:18:56Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751160025)
- `2025-04-08T19:36:32Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751198608)
- `2025-04-08T19:37:51Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751201310)
- `2025-04-08T19:40:19Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751206172)
- `2025-04-08T20:42:38Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751343689)
- `2025-04-09T02:03:00Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751859983)
- `2025-04-09T02:03:45Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751861289)
- `2025-04-09T02:14:33Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2751873655)
- `2025-04-10T07:44:52Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2755681638)
- `2025-04-10T07:45:23Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2755683046)
- `2025-04-10T07:46:19Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2755685349)
- `2025-04-10T21:50:22Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2758501177)
- `2025-04-10T21:51:47Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2758503231)
- `2025-04-10T22:05:04Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2758530298)
- `2025-04-11T06:52:09Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2759324167)
- `2025-04-14T16:11:08Z` `COMMENTED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2764876151)
- `2025-04-17T15:56:16Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2776254800)
- `2025-04-17T19:02:48Z` `CHANGES_REQUESTED` by `houseroad` - Looks good to me. Will temporarily put on hold until internal ROCm upgrade is done, sorry about the ... (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2776669654)
- `2025-04-17T19:11:17Z` `APPROVED` by `divakar-amd` (https://github.com/vllm-project/vllm/pull/16263#pullrequestreview-2776684534)
- ... 2 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/platforms/rocm.py`: 12 inline comment(s)
- `benchmarks/kernels/benchmark_moe.py`: 11 inline comment(s)

## High-Signal Discussion

- `2025-04-08T19:37:51Z` `inline` by `xw285cornell` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "yeah, with ROCR VISIBLE DEVICES, we can only see 1 device, and the device guard will use deviceX (X =1) and this will fail" (https://github.com/vllm-project/vllm/pull/16263#discussion_r2033907540)
- `2025-04-08T20:42:38Z` `inline` by `divakar-amd` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "This seems a good potential fix and can be used to remove dependency on the ENV variable RAY EXPERIMENTAL NOSET ROCR VISIBLE DEVICES=1 However, ..." (https://github.com/vllm-project/vllm/pull/16263#discussion_r2033994458)
- `2025-04-09T02:03:00Z` `inline` by `xw285cornell` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "This feels more like a Ray problem that it probably shouldn't set ROCR VISIBLE DEVICES. Or, set ROCR VISIBLE DEVICES based on HIP VISIBLE ..." (https://github.com/vllm-project/vllm/pull/16263#discussion_r2034323221)
- `2025-04-10T21:51:47Z` `inline` by `divakar-amd` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "Yes, let's add a guard which avoids any mismatch between HIP VISIBLE DEVICES and ROCR VISIBLE DEVICES" (https://github.com/vllm-project/vllm/pull/16263#discussion_r2038390687)
- `2025-04-11T06:52:09Z` `inline` by `xw285cornell` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "It's not super clear to me how to add the guard - the check happens at import time when the ray worker starts. So ..." (https://github.com/vllm-project/vllm/pull/16263#discussion_r2038913131)
- `2025-04-14T16:09:18Z` `inline` by `divakar-amd` `benchmarks/kernels/benchmark_moe.py`:594; signals: benchmark, kernel, moe; excerpt: "- Can we add a log message. - Also, lets use the value of HIP VISIBLE DEVICES to set the ROCR VISIBLE DEVICES. This ..." (https://github.com/vllm-project/vllm/pull/16263#discussion_r2042468978)
- `2025-04-08T16:47:45Z` `inline` by `houseroad` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "wondering the old approach - blindly setting guard, is there any problem with it?" (https://github.com/vllm-project/vllm/pull/16263#discussion_r2033631013)
- `2025-04-09T02:03:45Z` `inline` by `xw285cornell` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "I could force HIP VISIBLE DEVICES to be the same as ROCR VISIBLE DEVICE" (https://github.com/vllm-project/vllm/pull/16263#discussion_r2034323747)
- `2025-04-10T07:44:52Z` `inline` by `houseroad` `benchmarks/kernels/benchmark_moe.py`:445; signals: benchmark, kernel, moe; excerpt: "Maybe we should handle HIP VISIBLE DEVICES as well?" (https://github.com/vllm-project/vllm/pull/16263#discussion_r2036723280)
- `2025-04-17T15:56:16Z` `inline` by `xw285cornell` `benchmarks/kernels/benchmark_moe.py`:594; signals: benchmark, kernel, moe; excerpt: "sounds good!" (https://github.com/vllm-project/vllm/pull/16263#discussion_r2049248560)
- `2025-04-17T19:11:08Z` `inline` by `divakar-amd` `benchmarks/kernels/benchmark_moe.py`:589; signals: benchmark, kernel, moe; excerpt: "(nit) accessibility . - accessibility." (https://github.com/vllm-project/vllm/pull/16263#discussion_r2049508180)
- `2025-04-08T15:05:42Z` `inline` by `divakar-amd` `vllm/platforms/rocm.py`:197; signals: hang; excerpt: "From our past experiments, we found amdsmi get gpu asic info()["market name"] to be more reliable across a set of different MI Instinct machines. ..." (https://github.com/vllm-project/vllm/pull/16263#discussion_r2033409557)
