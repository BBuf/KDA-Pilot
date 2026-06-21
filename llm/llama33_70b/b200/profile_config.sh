FOLDER="llama33_70b"
MODEL="meta-llama/Llama-3.3-70B-Instruct"
CLEANUP_NAME="Llama-3.3-70B-Instruct BF16"
COOKBOOK_PAGE="Llama/Llama3.3-70B.md"
DOCKER_IMAGE="lmsysorg/sglang:latest"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

# Cookbook Llama 3.3 generator defaults to BF16 TP=1 and enables llama3 tool parsing for tool-call coverage.
SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 1
  --tool-call-parser llama3
  --host 0.0.0.0
  --port "${PORT}"
)
