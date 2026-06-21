FOLDER="laguna_m1"
MODEL="poolside/Laguna-M.1-NVFP4"
CLEANUP_NAME="Laguna-M.1 NVFP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --trust-remote-code
  --reasoning-parser poolside_v1
  --tool-call-parser poolside_v1
  --tp 8
  --host 0.0.0.0
  --port "${PORT}"
)
