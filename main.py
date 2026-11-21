#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-brave-20261121-0302.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a baker vignette: an oven lit before dawn, dough folded
once and again and left to rest, and a quiet step out into the dark
street with the first loaves still warm. Concrete work, unhurried
rhythm, no instructions.
"""

import os

TEXT = (
    "At four he lights the oven and waits for the bricks to hold the heat. "
    "Flour on his forearms, he folds the dough once, then again, and lets "
    "it rest under cloth. When the first loaves crackle, he opens the door "
    "to the dark street and steps out with them, still warm."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
