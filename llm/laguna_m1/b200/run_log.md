# Laguna-M.1 B200 Run Log

- Cookbook page: `https://docs.sglang.io/cookbook/autoregressive/Poolside/Laguna-M.1.md`
- Selected cell: verified B200 / default / NVFP4 / balanced / single-node.
- Model: `poolside/Laguna-M.1-NVFP4`.
- Docker image: `lmsysorg/sglang:dev-cu13-618-nightly`, per cookbook install notes for Laguna-M.1 support on SGLang main/nightly.
- Launch command source: cookbook deployment config for B200 NVFP4:
  `--model-path poolside/Laguna-M.1-NVFP4 --trust-remote-code --reasoning-parser poolside_v1 --tool-call-parser poolside_v1 --tp 8 --host 0.0.0.0 --port 30000`.
- Workload matrix: `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high`.
- Shape policy: keep only GPU kernel-name rows with profiler share strictly greater than 2% and SGLang-related/actionable provenance.
- Status: preparing after S24 `nemotron3_nano` completed and weights were cleaned.
