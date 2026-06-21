FOLDER="llama31_70b"
MODEL="meta-llama/Llama-3.1-70B"
CLEANUP_NAME="Llama-3.1-70B BF16"
COOKBOOK_PAGE="Llama/Llama3.1.md"
DOCKER_IMAGE="lmsysorg/sglang:latest"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

# Cookbook Llama 3.1 generator for 70B/Base/BF16 on B200 leaves TP unset; use TP=1 explicitly.
SERVER_ARGS=(
  sglang serve
  --model-path "${MODEL}"
  --tp 1
  --host 0.0.0.0
  --port "${PORT}"
)
