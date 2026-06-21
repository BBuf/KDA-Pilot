# MiniMax-M2.5 B200 Kernel Shape Sweep

- Target: `MiniMaxAI/MiniMax-M2.5`.
- Cookbook page: `MiniMax/MiniMax-M2.5.md`.
- Recipe: cookbook B200 benchmark command, TP8 + EP8,
  `--reasoning-parser minimax-append-think`, `--trust-remote-code`,
  `--mem-fraction-static 0.85`, and `--tool-call-parser minimax-m2`.
- Status: completed + cleaned. Launched on 2026-06-20T02:11:50Z in
  `sglang_bbuf_minimax_m25`; server ready at 2026-06-20T02:22:39Z,
  completed at 2026-06-20T02:29:12Z, cleaned at 2026-06-20T02:29:33Z.
- Final row counts:
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`
  = `9/10/9/10/11/10`.
- HF cache cleaned: `215G`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
