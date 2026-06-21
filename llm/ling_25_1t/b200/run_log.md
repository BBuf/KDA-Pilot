# Ling-2.5-1T B200 Kernel Shape Sweep

- Target: `inclusionAI/Ling-2.5-1T`.
- Cookbook page: `InclusionAI/Ling-2.5-1T.md`.
- Status: topology blocked; no weights downloaded.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Reason: the cookbook states that Ling-2.5-1T is a BF16 trillion-parameter
  model requiring multi-node deployment with at least 2 nodes. The B200
  selector generates `--tp-size 8 --pp-size 2 --nnodes 2`, so the current
  single-node 8xB200 assignment cannot run it.
- Cleanup: skipped because the model was not launched and no HF cache directory
  was created.
