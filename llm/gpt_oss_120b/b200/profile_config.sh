FOLDER="gpt_oss_120b"
MODEL="openai/gpt-oss-120b"
CLEANUP_NAME="GPT-OSS 120B"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python -m sglang.launch_server
  --model "${MODEL}"
  --tp 8
  --host 0.0.0.0
  --port "${PORT}"
)

