FOLDER="llada_21_flash"
MODEL="inclusionAI/LLaDA2.1-flash"
CLEANUP_NAME="LLaDA2.1-flash"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --dllm-algorithm JointThreshold
  --tp 2
  --trust-remote-code
  --mem-fraction-static 0.8
  --max-running-requests 1
  --attention-backend flashinfer
  --host 0.0.0.0
  --port "${PORT}"
)
