FOLDER="llama31_405b"
MODEL="meta-llama/Llama-3.1-405B-Instruct"
CLEANUP_NAME="Llama-3.1-405B-Instruct BF16"
COOKBOOK_PAGE="Llama/Llama3.1.md"
DOCKER_IMAGE="lmsysorg/sglang:latest"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

# Cookbook Llama 3.1 generator for 405B/Instruct/BF16 on NVIDIA: TP=8.
SERVER_ARGS=(
  sglang serve
  --model-path "${MODEL}"
  --tp 8
  --host 0.0.0.0
  --port "${PORT}"
)
