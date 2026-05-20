# PR Discussion Digest

- Source PR: [pytorch/pytorch#158301](https://github.com/pytorch/pytorch/pull/158301)
- Source page: `sources/prs/pytorch/PR-158301.md`
- Evidence bundle: `evidence/pull-bundles/pytorch/gh-158301`
- Generated at: `2026-05-20T15:27:01.649266+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-15T00:03:06Z`
- Merged: `unknown`

## Discussion Counts

- Issue comments: 10
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: albanD, atalman, nWEIdia
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-15T15:22:48Z` `COMMENTED` by `atalman` (https://github.com/pytorch/pytorch/pull/158301#pullrequestreview-3020941186)
- `2025-07-15T15:45:58Z` `APPROVED` by `nWEIdia` - LGTM. Just had one small suggestion. (https://github.com/pytorch/pytorch/pull/158301#pullrequestreview-3021049225)
- `2025-07-16T10:36:25Z` `COMMENTED` by `atalman` (https://github.com/pytorch/pytorch/pull/158301#pullrequestreview-3024226436)
- `2025-07-16T18:21:10Z` `APPROVED` by `albanD` - Looks great, thanks! (https://github.com/pytorch/pytorch/pull/158301#pullrequestreview-3026319363)
- `2025-07-19T00:50:17Z` `COMMENTED` by `atalman` (https://github.com/pytorch/pytorch/pull/158301#pullrequestreview-3035029803)

## Inline Comment Hotspots

- `torch/cuda/__init__.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-07-15T15:22:48Z` `inline` by `atalman` `torch/cuda/__init__.py`:274; signals: cuda; excerpt: "Looks like `incorrect binary warn` is never used. However its probably more accurate warning" (https://github.com/pytorch/pytorch/pull/158301#discussion_r2207825700)
- `2025-07-15T15:45:39Z` `inline` by `nWEIdia` `torch/cuda/__init__.py`:282; signals: cuda; excerpt: "Could we add a link to "Get Started" Page after "Please install CUDA 12.6 builds" ?" (https://github.com/pytorch/pytorch/pull/158301#discussion_r2207889998)
- `2025-07-16T10:36:25Z` `inline` by `atalman` `torch/cuda/__init__.py`:282; signals: cuda; excerpt: "Done" (https://github.com/pytorch/pytorch/pull/158301#discussion_r2209951996)
- `2025-07-19T00:50:16Z` `inline` by `atalman` `torch/cuda/__init__.py`:266; signals: cuda; excerpt: "New version added check for torch.cuda.get arch list()" (https://github.com/pytorch/pytorch/pull/158301#discussion_r2217068893)
- `2025-07-16T14:49:00Z` `issue` by `albanD`; signals: aligned; excerpt: "Wait, these warning are saying two opposite things lol. One says that it is not supported and one says you just need to install ..." (https://github.com/pytorch/pytorch/pull/158301#issuecomment-3078966183)
- `2025-07-16T20:16:58Z` `issue` by `nWEIdia`; signals: sm120; excerpt: "Just adding a note that in future, we might want to re-evaluate for "cur arch max arch" case, as there could be scenarios that ..." (https://github.com/pytorch/pytorch/pull/158301#issuecomment-3080281675)
