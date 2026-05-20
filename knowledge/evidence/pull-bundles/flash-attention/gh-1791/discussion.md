# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1791](https://github.com/Dao-AILab/flash-attention/pull/1791)
- Source page: `sources/prs/flash-attention/PR-1791.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1791`
- Generated at: `2026-05-20T15:16:34.291423+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-31T14:58:44Z`
- Merged: `2025-09-12T19:28:35Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 17
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=5, outdated=10
- Human participants with discussion text: albanD, danthe3rd, janeyx99, mikaylagawarecki, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-20T20:55:57Z` `COMMENTED` by `janeyx99` - Left some minor nits -- I'm guessing the commented out stuff will be removed? (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3138203027)
- `2025-08-26T19:11:30Z` `COMMENTED` by `danthe3rd` - That's amazing! Thank you for working on this :) I have a few comments, in the name of ... (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3156932843)
- `2025-08-26T19:28:40Z` `COMMENTED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3157028206)
- `2025-08-26T19:30:44Z` `COMMENTED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3157034422)
- `2025-08-26T19:32:43Z` `COMMENTED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3157040904)
- `2025-09-03T20:42:33Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3182394477)
- `2025-09-03T21:29:19Z` `COMMENTED` by `albanD` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3182574125)
- `2025-09-03T22:05:59Z` `COMMENTED` by `mikaylagawarecki` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3182668119)
- `2025-09-11T20:06:45Z` `APPROVED` by `janeyx99` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3213451132)
- `2025-09-11T20:14:02Z` `COMMENTED` by `mikaylagawarecki` (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3213480398)

## Inline Comment Hotspots

- `hopper/flash_api.cpp`: 12 inline comment(s)
- `hopper/setup.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-08-26T19:11:30Z` `review` `COMMENTED` by `danthe3rd`; signals: compile, cuda, hang, kernel; excerpt: "That's amazing! Thank you for working on this :) I have a few comments, in the name of making the life of extension maintainers ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#pullrequestreview-3156932843)
- `2025-08-26T22:29:27Z` `issue` by `janeyx99`; signals: compile, cuda, hang, kernel; excerpt: "Thanks @danthe3rd for your comments! They very much align with where we're headed, especially as @mikaylagawarecki and I start enabling other repos with many ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#issuecomment-3225931190)
- `2025-08-26T19:03:09Z` `inline` by `danthe3rd` `hopper/flash_api.cpp`:1206; signals: compile, hang, hopper; excerpt: "Could we avoid having to do this kind of changes? Like could we just replace TORCH CHECK's definition with STD TORCH CHECK's definition - ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2301882796)
- `2025-08-26T19:05:47Z` `inline` by `danthe3rd` `hopper/flash_api.cpp`:70; signals: cuda, hopper; excerpt: "I can see multiple libraries could need this kind of functions. Would it be possible to have getCurrentDeviceProperties/getCurrentCUDAStream/... also part of the stable ABI? ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2301887837)
- `2025-08-26T19:30:44Z` `inline` by `janeyx99` `hopper/flash_api.cpp`:1206; signals: compile, hopper; excerpt: "We haven't yet explored having a compile time flag control what gets exposed, and that will be a part of our consideration when we ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2301942947)
- `2025-09-03T21:29:19Z` `inline` by `albanD` `hopper/flash_api.cpp`:70; signals: cuda, hopper; excerpt: "Yes it is an interesting balance between having generic enough APIs vs not. tbh in this case, if the cuda API was good enough ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2320261937)
- `2025-09-03T22:05:59Z` `inline` by `mikaylagawarecki` `hopper/flash_api.cpp`:1739; signals: hopper, kernel; excerpt: "This is a limitation of STABLE TORCH LIBRARY for now where it only accepts the boxed kernel. But echoing [Jane's comment]( We do want ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2320328714)
- `2025-09-11T20:14:02Z` `inline` by `mikaylagawarecki` `hopper/setup.py`:537; signals: compile, hopper; excerpt: "I don't think we need to pass this to nvcc extra compile args, hence I separated it out" (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2342231573)
- `2025-08-26T18:59:35Z` `inline` by `danthe3rd` `hopper/flash_api.cpp`:1877; signals: hopper; excerpt: "Do you think there is a way to automate this? It could be quite error prone. Probably we can do something with C++ template ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2301873500)
- `2025-08-26T19:28:39Z` `inline` by `janeyx99` `hopper/flash_api.cpp`:1877; signals: hopper; excerpt: "We do want to eventually automate this and hide it from the user completely! We ultimately want to support this in the dispatcher which ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2301938634)
- `2025-08-26T19:32:43Z` `inline` by `janeyx99` `hopper/flash_api.cpp`:70; signals: hopper; excerpt: "We explicitly chose to support the accelerator agnostic variations of these APIs in stable for 2.9, as we want people to eventually migrate to ..." (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2301947700)
- `2025-08-20T20:52:23Z` `inline` by `janeyx99` `hopper/flash_api.cpp`:1087; signals: hopper; excerpt: "let's use torch::headeronly for these" (https://github.com/Dao-AILab/flash-attention/pull/1791#discussion_r2289271256)
