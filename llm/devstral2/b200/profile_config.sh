FOLDER="devstral2"
MODEL="mistralai/Devstral-2-123B-Instruct-2512"
CLEANUP_NAME="Devstral 2 123B FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 2
  --mem-fraction-static 0.85
  --context-length 32768
  --host 0.0.0.0
  --port "${PORT}"
)
