#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty u-azazex-one-line-one-chill-6d4d5488.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. No arguments, no input, no network, deterministic:
the same bytes on every run.
"""

LINE = "The radiologist went quiet when the second spine on my MRI curled to spell my name."

OUTPUT_PATH = "/output/entry.txt"


import os


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
