FOLDER="intern_s2_preview"
MODEL="internLM/Intern-S2-Preview"
CLEANUP_NAME="Intern-S2-Preview BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --trust-remote-code
  --reasoning-parser qwen3
  --tool-call-parser qwen3_coder
  --mem-fraction-static 0.8
  --host 0.0.0.0
  --port "${PORT}"
)
