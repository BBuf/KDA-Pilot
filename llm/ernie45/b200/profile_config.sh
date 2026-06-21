FOLDER="ernie45"
MODEL="baidu/ERNIE-4.5-21B-A3B-PT"
CLEANUP_NAME="ERNIE-4.5 21B-A3B"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 1
  --host 0.0.0.0
  --port "${PORT}"
)
