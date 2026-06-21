# MiMo-V2.5 B200 Kernel Shape Sweep

- Target: `XiaomiMiMo/MiMo-V2.5`
- Cookbook page: `Xiaomi/MiMo-V2.5.md`
- Recipe: B200 Base TP4, no DP-attention, FP8 checkpoint, EAGLE MTP enabled with the checkpoint's MTP weights.
- Image required by cookbook: `lmsysorg/sglang:nightly-dev-cu13-20260511-044bb88a`; `latest` is documented as unable to load the checkpoint.
- Scope note: the page default is `MiMo-V2.5-Pro`, but the queue target is the base model because it is the multimodal/text model named in the original progress table.
- Status: blocked + cleaned; no profiler traces or kernel-shape rows were
  produced.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_mimo_v25`.
- Fallback note: the cookbook B200 image
  `lmsysorg/sglang:nightly-dev-cu13-20260511-044bb88a` is listed in the live
  docs but Docker Hub returned `not found`; `lmsysorg/sglang:dev-mimo-v2.5`
  exists and exposes `sglang 0.0.0.dev1+g7d99af439`, `torch 2.9.1+cu129`, and
  all 8 B200 GPUs, so this run uses it as the closest available MiMo image.
- Runner: launched 2026-06-19T15:20:12Z, PID `1208`, GPU0-3, port `30000`;
  log `mimo_v25/b200/logs/runner_20260619T152012Z_fallback_dev_mimo.log`.
- Failure: the fallback `dev-mimo-v2.5` image starts the MiMo visual encoder
  with FA3 attention and fails on B200/Blackwell with
  `ValueError: The 'fa3' backend is not supported on Blackwell GPUs`
  (`server.log` and runner log lines around the TP-rank tracebacks).
- Cleanup: partial HF cache
  `/root/.cache/huggingface/hub/models--XiaomiMiMo--MiMo-V2.5` was deleted
  after failure; size before cleanup was `12M`, and GPUs returned to 0 MiB.
