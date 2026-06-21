FOLDER="hunyuan3_preview"
MODEL="tencent/Hy3-preview"
CLEANUP_NAME="Hunyuan3 Preview BF16 + MTP"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

export SGLANG_ENABLE_SPEC_V2=1

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --reasoning-parser hunyuan
  --tool-call-parser hunyuan
  --trust-remote-code
  --mem-fraction-static 0.85
  --attention-backend trtllm_mha
  --host 0.0.0.0
  --port "${PORT}"
)
