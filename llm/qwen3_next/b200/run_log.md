# Qwen3-Next B200 Kernel Shape Sweep

- Target: `Qwen/Qwen3-Next-80B-A3B-Instruct`.
- Cookbook page: `Qwen/Qwen3-Next.md`.
- Recipe: B200 benchmark command, TP8. This pass does not enable 1M-context
  YaRN or NEXTN MTP initially, to keep the shape sweep comparable with the
  standard random/ShareGPT workload.
- Status: pending.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
