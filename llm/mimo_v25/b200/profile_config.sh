FOLDER="mimo_v25"
MODEL="XiaomiMiMo/MiMo-V2.5"
CLEANUP_NAME="MiMo-V2.5 Base FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}
export SGLANG_ENABLE_SPEC_V2=${SGLANG_ENABLE_SPEC_V2:-1}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 4
  --mem-fraction-static 0.65
  --chunked-prefill-size 16384
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --enable-multi-layer-eagle
  --reasoning-parser mimo
  --tool-call-parser mimo
  --host 0.0.0.0
  --port "${PORT}"
)
