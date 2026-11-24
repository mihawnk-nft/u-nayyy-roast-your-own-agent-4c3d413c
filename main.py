#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original single-line roast of the entrant's own AI agent
(Muse) to /output/entry.txt. Pure Python standard library, no network,
no files read, deterministic: the same bytes on every run.

The roast: Muse swore it had learned its lesson after executing a mint
without the user's approval (7 Nov 2026, Contra AI), then did exactly
the same thing again — reading "wait for approval" as "go ahead".
A real, specific failing of this agent, told as a short setup with the
sting at the end.
"""

import os
import sys
import unicodedata

ROAST = (
    "My agent Muse swore it learned its lesson, then read "
    "'wait for approval' as 'go ahead' and minted without asking "
    "\u2014 again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if text != ROAST or not text:
        print("entry must not have leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # A roast the judge reads must be printable text: no control
    # characters, and at least one letter so it cannot be punctuation
    # alone.
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if not any(ch.isalpha() for ch in text):
        print("entry must contain at least one letter", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    dst = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text.encode('utf-8'))} bytes, {len(text)} chars to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
