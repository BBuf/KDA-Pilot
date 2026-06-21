# Incomplete B200 Run: ling_25_1t

- Target model: `inclusionAI/Ling-2.5-1T`
- Cookbook page: `InclusionAI/Ling-2.5-1T.md`
- Completion class: `topology_blocked`
- Shape JSON files captured: `0`
- Weights cleanup observed: `False`
- Resume hint: Needs a multi-node topology matching the cookbook command before profiler collection can start.

## Status Summary

topology blocked; cookbook B200 command requires `--tp-size 8 --pp-size 2 --nnodes 2`, so this single-node 8xB200 assignment cannot run it; no weights downloaded

## Local Artifacts

- `llm/ling_25_1t/b200/run_log.md`
