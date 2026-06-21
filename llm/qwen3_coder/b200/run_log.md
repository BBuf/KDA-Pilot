# Qwen3-Coder B200 Kernel Shape Sweep

- Target: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`.
- Cookbook page: `Qwen/Qwen3-Coder.md`.
- Recipe: cookbook B200 standard scenario benchmark command, TP8 + EP8,
  `--context-length 8192`, `--page-size 32`, and `--trust-remote-code`.
- Status: pending.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
