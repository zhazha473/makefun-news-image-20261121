#!/usr/bin/env python3
"""make.fun entrypoint: copy entry.png to the output directory.

Standard library only. No network. Deterministic: the same entry.png
bytes are copied every run.
"""
import hashlib
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    digest = hashlib.sha256(open(src, "rb").read()).hexdigest()
    print("entry.png sha256: " + digest)


if __name__ == "__main__":
    main()
