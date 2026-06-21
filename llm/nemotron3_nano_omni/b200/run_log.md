# Nemotron3-Nano-Omni B200 Kernel Shape Sweep

- Target: `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4`.
- Cookbook page: `NVIDIA/Nemotron3-Nano-Omni.md`.
- Recipe: live cookbook B200 NVFP4 command, TP4, `--trust-remote-code`,
  `--tool-call-parser qwen3_coder`, and `--reasoning-parser deepseek-r1`.
  The model is multimodal-capable, but this pass uses text-only random and
  ShareGPT workloads to keep it comparable to the rest of the LLM sweep.
- Status: running; launched on 2026-06-20T07:11:24Z in
  `sglang_bbuf_nemotron3_nano_omni`; runner host PID `3656635`, server PID
  `1141`.
- Current phase: `server_start`; HF cache observed at `1.3M` while startup
  begins downloading model metadata and weights.
- First launch failed at 2026-06-20T07:12:30Z before weight download because
  the multimodal `ParakeetExtractor` requires `librosa`, which is not present
  in `lmsysorg/sglang:latest`. The runner cleaned the partial HF cache (`18M`).
  Retrying in the same temporary container after installing `librosa`.
- Retry launched at 2026-06-20T07:16:30Z; runner host PID `3664600`, server
  PID `2278`. The retry passed the previous `librosa` failure point and is in
  `server_start`; HF cache observed at `1.5M`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
