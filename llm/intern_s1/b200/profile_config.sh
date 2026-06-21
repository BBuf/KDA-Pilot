FOLDER="intern_s1"
MODEL="internlm/Intern-S1-FP8"
CLEANUP_NAME="Intern-S1 FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tokenizer-path internlm/Intern-S1
  --tp-size 8
  --ep 2
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
)
