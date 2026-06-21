FOLDER="kimi_linear"
MODEL="moonshotai/Kimi-Linear-48B-A3B-Instruct"
CLEANUP_NAME="Kimi-Linear-48B-A3B-Instruct"
COOKBOOK_PAGE="Moonshotai/Kimi-Linear.md"
DOCKER_IMAGE="lmsysorg/sglang:latest"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

# Cookbook Kimi-Linear command uses TP=4 and trust-remote-code; reasoning parser is unsupported for Instruct.
SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tokenizer-path "${MODEL}"
  --tp 4
  --trust-remote-code
  --tool-call-parser kimi_k2
  --mem-fraction-static 0.75
  --cuda-graph-max-bs 256
  --host 0.0.0.0
  --port "${PORT}"
)
