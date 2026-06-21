FOLDER="glm_45"
MODEL="zai-org/GLM-4.5"
CLEANUP_NAME="GLM-4.5 BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --host 0.0.0.0
  --port "${PORT}"
)
