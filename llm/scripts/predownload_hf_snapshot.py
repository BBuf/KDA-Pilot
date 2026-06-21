#!/usr/bin/env python3
import argparse
import os
import sys
import time
import traceback

from huggingface_hub import snapshot_download


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_id")
    parser.add_argument("--cache-dir", default=None)
    parser.add_argument("--max-workers", type=int, default=1)
    parser.add_argument("--attempts", type=int, default=20)
    parser.add_argument("--sleep-s", type=int, default=30)
    parser.add_argument("--allow-pattern", action="append", default=None)
    parser.add_argument("--ignore-pattern", action="append", default=None)
    args = parser.parse_args()

    os.environ.setdefault("HF_HUB_ENABLE_HF_TRANSFER", "0")

    for attempt in range(1, args.attempts + 1):
        print(
            f"[predownload] attempt={attempt}/{args.attempts} repo={args.repo_id} "
            f"max_workers={args.max_workers}",
            flush=True,
        )
        try:
            path = snapshot_download(
                args.repo_id,
                cache_dir=args.cache_dir,
                max_workers=args.max_workers,
                allow_patterns=args.allow_pattern,
                ignore_patterns=args.ignore_pattern,
            )
            print(f"[predownload] complete path={path}", flush=True)
            return 0
        except KeyboardInterrupt:
            raise
        except Exception:
            traceback.print_exc()
            if attempt == args.attempts:
                break
            print(f"[predownload] sleeping {args.sleep_s}s before retry", flush=True)
            time.sleep(args.sleep_s)

    return 1


if __name__ == "__main__":
    sys.exit(main())
