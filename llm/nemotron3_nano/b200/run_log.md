# Nemotron3-Nano B200 Kernel Shape Sweep

- Target: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`.
- Cookbook page: `NVIDIA/Nemotron3-Nano.md`.
- Recipe: cookbook B200 FP8 benchmark-section command with
  `--trust-remote-code`, `--max-running-requests 1024`, and explicit TP1 on a
  single B200.
- Status: launching on 2026-06-20 UTC after S23 blocked/cleaned.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
