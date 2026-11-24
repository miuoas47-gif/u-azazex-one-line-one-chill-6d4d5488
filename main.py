#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty entry.

A single sentence of horror, under 200 characters, that has to
frighten a reader in one breath. This program writes that sentence:
one line, no setup, no second chance.

It writes the line as UTF-8 text to ``entry.txt`` inside the output
directory named by ``MAKEFUN_OUTPUT_DIR`` (``/output`` when the
variable is unset), with no trailing newline, and exits 0. The run is
fully deterministic: the same line is written on every run.
"""

import os
import sys

# The line. One sentence, no leading or trailing space, well under
# the 200-character gate. The scare is concrete (a dentist, an X-ray)
# and earned, not announced — and the last word is the blow.
# Revised: "My dentist" lands more personally than "The dentist",
# and "a second row" is the natural, tighter phrasing for teeth.
TEXT = (
    "My dentist found a second row of teeth growing behind mine, "
    "and the X-ray shows them smiling."
)

MAX_CHARS = 200


def fail(message):
    print("error: %s" % message, file=sys.stderr)
    return 1


def main():
    if not TEXT.strip():
        return fail("line is empty")
    if TEXT != TEXT.strip():
        return fail("line has leading or trailing whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        return fail("line must be a single sentence on one line")
    if len(TEXT) > MAX_CHARS:
        return fail("line is %d characters, over the %d limit"
                    % (len(TEXT), MAX_CHARS))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return fail("cannot create output directory %s: %s" % (out_dir, exc))
    path = os.path.join(out_dir, "entry.txt")

    try:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(TEXT)
    except OSError as exc:
        return fail("cannot write %s: %s" % (path, exc))

    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != TEXT.encode("utf-8"):
        return fail("read-back mismatch: entry.txt differs from the line")
    raw.decode("utf-8")

    print("Wrote %s (%d characters)" % (path, len(TEXT)))
    print(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
