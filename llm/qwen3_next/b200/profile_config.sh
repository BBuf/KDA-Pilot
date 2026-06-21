FOLDER="qwen3_next"
MODEL="Qwen/Qwen3-Next-80B-A3B-Instruct"
CLEANUP_NAME="Qwen3-Next 80B-A3B Instruct"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --host 0.0.0.0
  --port "${PORT}"
)
