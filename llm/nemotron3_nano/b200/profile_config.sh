FOLDER="nemotron3_nano"
MODEL="nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8"
CLEANUP_NAME="Nemotron3-Nano 30B-A3B FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --trust-remote-code
  --max-running-requests 1024
  --tp 1
  --host 0.0.0.0
  --port "${PORT}"
)
