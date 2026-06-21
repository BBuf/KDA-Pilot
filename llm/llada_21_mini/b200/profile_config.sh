FOLDER="llada_21_mini"
MODEL="inclusionAI/LLaDA2.1-mini"
CLEANUP_NAME="LLaDA2.1-mini"
COOKBOOK_PAGE="InclusionAI/LLaDA-2.1.md"
DOCKER_IMAGE="lmsysorg/sglang:latest"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

# Cookbook LLaDA 2.1 B200/mini generator: TP=1, JointThreshold, FlashInfer.
SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --dllm-algorithm JointThreshold
  --tp 1
  --trust-remote-code
  --mem-fraction-static 0.8
  --max-running-requests 1
  --attention-backend flashinfer
  --host 0.0.0.0
  --port "${PORT}"
)
