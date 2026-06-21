FOLDER="mistral_small4"
MODEL="mistralai/Mistral-Small-4-119B-2603"
CLEANUP_NAME="Mistral Small 4 FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 1
  --reasoning-parser mistral
  --tool-call-parser mistral
  --host 0.0.0.0
  --port "${PORT}"
)
