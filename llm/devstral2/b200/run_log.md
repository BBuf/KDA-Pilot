# Devstral-2 B200 Kernel Shape Sweep

- Target: `mistralai/Devstral-2-123B-Instruct-2512`.
- Cookbook page: `Mistral/Devstral-2.md`.
- Recipe: cookbook benchmark deployment command, TP8 and
  `--trust-remote-code`.
- Status: starting; live cookbook B200 large config uses TP2. Using
  `lmsysorg/sglang:latest` because it has `transformers 5.8.1` and a
  torch profiler sanity check produced GPU `kernel` events. Added cookbook
  memory tip `--context-length 32768` plus `--mem-fraction-static 0.85`.
- Launch: running since 2026-06-20T03:36:18Z in `sglang_bbuf_devstral2`;
  runner PID `1145`, server PID `1148`.
- Final status: blocked + cleaned. The `latest` image satisfies the page's
  `transformers >= 5.0.0rc` requirement and a profiler sanity check produced
  GPU `kernel` events, but Devstral-2 launch fails before full weight download
  with `AttributeError: 'str' object has no attribute 'get_quant_method'` in
  the Ministral3 FP8 path. An explicit `--quantization fp8` probe failed the
  same way. No Devstral-specific `lmsysorg/sglang` image tags were found.
  Runner cleaned partial cache `17M`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
