# Intern-S1 B200 Kernel Shape Sweep

- Target: `internlm/Intern-S1-FP8`.
- Cookbook page: `InternLM/Intern-S1.md`.
- Recipe: the visible cookbook page is currently a contribution placeholder, so
  the runnable B200 command is taken from the generated cookbook model metadata:
  FP8 235B MoE, TP8, EP2, tokenizer `internlm/Intern-S1`, and
  `--trust-remote-code`.
- Status: blocked + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_intern_s1`.
- Runner: launched 2026-06-20T01:29:44Z, runner PID `1152`, server PID
  `1155`, GPU0-7, port `30000`. TP8/EP2 distributed initialization reached
  weight loading at 2026-06-20T01:30:38Z; observed HF cache sizes were `4.0G`
  for `Intern-S1-FP8` and `5.1M` for tokenizer `Intern-S1` at
  2026-06-20T01:30:50Z.
- Current stage update: observed HF cache size was `127G` for
  `Intern-S1-FP8` at 2026-06-20T01:36:32Z; server was still in weight loading,
  with no interruption or OOM.
- Outcome: launch failed before `server_ready`, so no workload or shape JSON was
  produced. During server warmup the Intern-S1 vision branch hit
  `sglang.jit_kernel.norm.fused_inplace_qknorm` and failed in
  `qknorm.cuh:214`: `head_dim` expected `512` but got `4096` for a BF16 tensor
  of shape `Tensor<4096>`. The runner cleaned the partial
  `Intern-S1-FP8` cache (`232G`) at 2026-06-20T01:46:13Z; the tokenizer cache
  `models--internlm--Intern-S1` (`5.1M`) was removed manually with `sudo`.
- Cleanup note: the runner cleans the model cache for `Intern-S1-FP8`; after
  completion also check/remove the tokenizer cache `models--internlm--Intern-S1`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
