FOLDER="qwen3_coder"
MODEL="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8"
CLEANUP_NAME="Qwen3-Coder 480B-A35B FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --ep 8
  --context-length 8192
  --page-size 32
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
)
