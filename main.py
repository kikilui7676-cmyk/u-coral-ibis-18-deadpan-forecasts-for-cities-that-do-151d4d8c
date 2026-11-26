"""Deadpan weather forecast for a city that does not exist, for make.fun.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; deterministic: the same line every run.
"""

import os

ENTRY = "In Plonkshire, rain is due at 3 p.m. sharp, as it has been daily since 1974, and nobody has asked why."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
