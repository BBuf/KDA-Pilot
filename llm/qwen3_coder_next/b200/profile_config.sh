FOLDER="qwen3_coder_next"
MODEL="Qwen/Qwen3-Coder-Next"
CLEANUP_NAME="Qwen3-Coder-Next"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 2
  --tool-call-parser qwen3_coder
  --host 0.0.0.0
  --port "${PORT}"
)
