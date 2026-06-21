FOLDER="ministral3_14b"
MODEL="mistralai/Ministral-3-14B-Instruct-2512"
CLEANUP_NAME="Ministral-3-14B-Instruct-2512"
COOKBOOK_PAGE="Mistral/Ministral-3.md"
DOCKER_IMAGE="lmsysorg/sglang:latest"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

# Cookbook Ministral-3 large command: TP=1, trust remote code, Mistral tool parser.
SERVER_ARGS=(
  sglang serve
  --model-path "${MODEL}"
  --tp 1
  --quantization fp8
  --trust-remote-code
  --tool-call-parser mistral
  --host 0.0.0.0
  --port "${PORT}"
)
