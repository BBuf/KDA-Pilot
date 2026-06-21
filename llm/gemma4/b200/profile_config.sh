FOLDER="gemma4"
MODEL="google/gemma-4-26B-A4B-it"
CLEANUP_NAME="Gemma 4 26B-A4B BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --reasoning-parser gemma4
  --tool-call-parser gemma4
  --mem-fraction-static 0.9
  --host 0.0.0.0
  --port "${PORT}"
)
