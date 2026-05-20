# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7999](https://github.com/NVIDIA/cccl/pull/7999)
- Source page: `sources/prs/cccl-cub/PR-7999.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7999`
- Generated at: `2026-05-20T15:20:25.749667+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T02:47:39Z`
- Merged: `2026-03-25T09:32:20Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 23
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=9, outdated=7
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, gonidelis, pauleonix
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T13:32:57Z` `COMMENTED` by `NaderAlAwar` - Important: we are missing the DoubleBuffer overloads (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3936625767)
- `2026-03-12T23:11:32Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3940410168)
- `2026-03-13T18:32:48Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3946203937)
- `2026-03-13T19:04:56Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3946275867)
- `2026-03-20T00:56:57Z` `COMMENTED` by `pauleonix` - Still some nits (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3978680573)
- `2026-03-20T09:32:29Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3980442497)
- `2026-03-20T09:44:31Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3980495111)
- `2026-03-20T09:46:24Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3980503451)
- `2026-03-20T09:48:57Z` `APPROVED` by `bernhardmgruber` - Please apply the remaining feedback from other reviewers. Otherwise LGTM (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3980513842)
- `2026-03-25T07:37:25Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-4004599344)
- `2026-03-25T07:38:04Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-4004602799)
- `2026-03-25T07:41:40Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-4004618894)

## Inline Comment Hotspots

- `cub/cub/device/device_segmented_radix_sort.cuh`: 16 inline comment(s)
- `cub/test/catch2_test_device_segmented_radix_sort_env_api.cu`: 5 inline comment(s)
- `cub/test/catch2_test_device_segmented_radix_sort_env.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-20T00:08:37Z` `inline` by `pauleonix` `cub/cub/device/device_segmented_radix_sort.cuh`:436; signals: cuda, memory; excerpt: "Not sure I like this better than the - Can use a specific stream or cuda memory resource through the env parameter I saw ..." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2963371952)
- `2026-03-13T18:50:33Z` `inline` by `bernhardmgruber` `cub/cub/device/device_segmented_radix_sort.cuh`:553; signals: hang; excerpt: "We can drop the cast after changing the parameter types. Applies to all newly added overloads." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2933171806)
- `2026-03-20T00:33:18Z` `inline` by `pauleonix` `cub/cub/device/device_segmented_radix_sort.cuh`:1446; signals: hang; excerpt: "Missing some entries again. And the order of the ones not missing is changed as well." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2963426186)
- `2026-03-25T07:37:25Z` `inline` by `gonidelis` `cub/cub/device/device_segmented_radix_sort.cuh`:436; signals: hang; excerpt: "changed it" (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2986360043)
- `2026-03-12T13:32:57Z` `review` `COMMENTED` by `NaderAlAwar`; signals: general review; excerpt: "Important: we are missing the DoubleBuffer overloads" (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3936625767)
- `2026-03-20T00:56:57Z` `review` `COMMENTED` by `pauleonix`; signals: general review; excerpt: "Still some nits" (https://github.com/NVIDIA/cccl/pull/7999#pullrequestreview-3978680573)
- `2026-03-12T13:32:49Z` `inline` by `NaderAlAwar` `cub/test/catch2_test_device_segmented_radix_sort_env_api.cu`:80; signals: general review; excerpt: "Question: do we want to add a test where we do not explicitly pass an env? Other env API tests seem to have both ..." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2924665209)
- `2026-03-12T23:11:32Z` `inline` by `gonidelis` `cub/test/catch2_test_device_segmented_radix_sort_env_api.cu`:80; signals: general review; excerpt: "i think it's fine. unit tests cover that case and users can see it throughout docs as soon as they start using our env ..." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2927937206)
- `2026-03-13T18:32:48Z` `inline` by `bernhardmgruber` `cub/cub/device/device_segmented_radix_sort.cuh`:528; signals: general review; excerpt: "Q: Why do we need a constraint on this overload? Because of the second parameter KeyT , it can't be ambiguous with the old ..." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2933095937)
- `2026-03-13T18:48:59Z` `inline` by `bernhardmgruber` `cub/cub/device/device_segmented_radix_sort.cuh`:532; signals: general review; excerpt: "Important: the non-env overload uses int64 t for num items and num segments. Why do we make them template parameters here? I think we ..." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2933165499)
- `2026-03-20T00:12:10Z` `inline` by `pauleonix` `cub/cub/device/device_segmented_radix_sort.cuh`:456; signals: general review; excerpt: "Maybe we should have a @env like the @devicestorage on the old APIs to avoid the repetition. Even if it needs multiple like @env-with-guarantees." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2963379654)
- `2026-03-20T00:26:25Z` `inline` by `pauleonix` `cub/cub/device/device_segmented_radix_sort.cuh`:426; signals: general review; excerpt: "This "title" is new in comparison to the existing docs. If it stays, it looks like it should be underlined (rendered as a sub-title) ..." (https://github.com/NVIDIA/cccl/pull/7999#discussion_r2963412272)
