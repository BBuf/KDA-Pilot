FOLDER="llama4"
MODEL="meta-llama/Llama-4-Maverick-17B-128E-Instruct"
CLEANUP_NAME="Llama 4 Maverick BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --enable-multimodal
  --context-length 65536
  --dtype bfloat16
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
)
