#!/usr/bin/env python3
"""Deadpan forecast for Tatterford, a city that does not exist.

Writes exactly one line (<=160 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only; deterministic output.
"""

import os

LINE = (
    "In Tatterford today, expect a high of 68, light winds, and one (1) "
    "cloud, named Gerald by a council that refuses to discuss him."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
