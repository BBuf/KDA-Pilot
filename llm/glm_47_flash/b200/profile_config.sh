FOLDER="glm_47_flash"
MODEL="zai-org/GLM-4.7-Flash"
CLEANUP_NAME="GLM-4.7-Flash BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 1
  --attention-backend triton
  --host 0.0.0.0
  --port "${PORT}"
)
