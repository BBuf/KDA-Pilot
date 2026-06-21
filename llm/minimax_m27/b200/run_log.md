# MiniMax-M2.7 B200 Kernel Shape Sweep

- Target: `MiniMaxAI/MiniMax-M2.7`.
- Cookbook page: `MiniMax/MiniMax-M2.7.md`.
- Recipe: cookbook B200 8-GPU command, TP8 + EP8, `--tool-call-parser
  minimax-m2`, `--reasoning-parser minimax-append-think`,
  `--trust-remote-code`, and `--mem-fraction-static 0.85`.
- Status: completed + cleaned. Launched on 2026-06-20T01:50:05Z, server
  ready at 2026-06-20T02:01:29Z, completed/cleaned at
  2026-06-20T02:07:58Z.
- Final row counts:
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`
  = `11/10/9/11/9/9`.
- HF cache cleaned: `215G`.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_minimax_m27`.
- Runner PID: `1150`; server PID: `1153`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
