FOLDER="lfm25"
MODEL="LiquidAI/LFM2.5-8B-A1B"
CLEANUP_NAME="LFM2.5 8B-A1B BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 1
  --attention-backend flashinfer
  --reasoning-parser qwen3
  --tool-call-parser lfm2
  --host 0.0.0.0
  --port "${PORT}"
)
