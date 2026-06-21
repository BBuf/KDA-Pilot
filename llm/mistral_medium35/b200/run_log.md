# Mistral Medium 3.5 B200 Kernel Shape Sweep

- Target: `mistralai/Mistral-Medium-3.5-128B`.
- Cookbook page: `Mistral/Mistral-Medium-3.5.md`.
- Recipe: live cookbook B200 command generator, TP2 on Blackwell, Mistral
  reasoning/tool parsers, and EAGLE speculative decoding with
  `mistralai/Mistral-Medium-3.5-128B-EAGLE`.
- Cleanup note: runner is configured to delete both target and EAGLE draft HF
  caches.
- Status: retrying. First launch on 2026-06-20T02:56:40Z used generic
  `lmsysorg/sglang:latest` and failed before full weight download with
  `AttributeError: 'str' object has no attribute 'get_quant_method'`.
  Runner cleaned partial primary cache `17M` and EAGLE draft cache `16M`.
  Live cookbook requires B200 image
  `lmsysorg/sglang:dev-cu13-mistral-medium-3.5`.
- Retry status: running; relaunched on 2026-06-20T03:05:34Z in
  `sglang_bbuf_mistral_medium35`; runner PID `1145`, server PID `1148`.
  TP0/TP1 reached Load weight at 2026-06-20T03:06:08Z. Primary HF cache
  observed at `108G`.
- Retry result: failed at 2026-06-20T03:14:22Z after full weight load
  because KV pool init reported not enough memory with default
  `mem_fraction_static=0.63384`; runner cleaned primary cache `249G`.
  Next retry adds `--mem-fraction-static 0.85 --context-length 32768`.
- Third attempt: running; launched on 2026-06-20T03:16:38Z in
  `sglang_bbuf_mistral_medium35`; runner PID `1147`, server PID `1150`.
  Load weight began at 2026-06-20T03:17:13Z; primary HF cache observed at
  `176G`.
- Server ready at 2026-06-20T03:26:27Z. `random_low` started. HF caches
  observed: primary `249G`, EAGLE draft `2.9G`.
- Final status: blocked/profiler-unavailable + cleaned. `random_low`
  benchmark succeeded, but `extract_random_low` failed because the cookbook
  B200 image's `torch.profiler` Chrome trace contained no GPU `kernel`
  events. A standalone CUDA matmul profiler sanity check in the same container
  also produced `kernel_count=0`. The old autograd profiler reports CUDA op
  time but no GPU kernel names, so it is not a valid replacement for the
  required `>2%` GPU-kernel filter. Runner cleaned primary cache `249G` and
  EAGLE draft cache `2.9G`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
