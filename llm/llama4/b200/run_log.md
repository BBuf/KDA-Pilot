# Llama4 B200 Kernel Shape Sweep

- Target: `meta-llama/Llama-4-Maverick-17B-128E-Instruct`
- Cookbook page: `Llama/Llama4.md`
- Recipe: B200 BF16 TP8, `--enable-multimodal`, context length 65536.
- Scope note: this page also exposes Scout. This run uses Maverick as the Llama4 series representative; Scout can be added as a variant pass if full per-variant coverage is required.
- Status: blocked + cleaned on `cirrascale-gpuc5a6` with image `lmsysorg/sglang:latest`.
- Selected container: `sglang_bbuf_llama4`.
- Runner: launched 2026-06-19T13:17:59Z, PID `1217`, GPU0-7, port `30000`.
- Result: Hugging Face returned 401 for the gated repo before `config.json`
  could be downloaded. No profiling run was possible without HF access to
  `meta-llama/Llama-4-Maverick-17B-128E-Instruct`.
- Cleanup: `/root/.cache/huggingface/hub/models--meta-llama--Llama-4-Maverick-17B-128E-Instruct`
  was absent/cleaned at 2026-06-19T13:18:21Z; no weights were left behind.
