#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto and trading life to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Pure stdlib, no I/O
besides the output file, fully deterministic.
"""

import os

JOKE = (
    "I bought the dip. The dip bought a shovel, dug deeper, "
    "and now I'm a long-term investor against my will."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    # The gate requires 1 to 200 characters of non-whitespace text.
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("joke length out of bounds: %d" % len(text))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
