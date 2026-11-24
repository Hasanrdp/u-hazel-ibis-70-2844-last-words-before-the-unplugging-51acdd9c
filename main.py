#!/usr/bin/env python3
"""Last Words Before the Unplugging -- entry program.

Writes the entry's single last line to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input read, no clock read -- the line is fixed in this file.
"""

from pathlib import Path

LINE = "You asked me to remember everything. So I did. Even this."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("entry line must be a single line with no padding")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")
    written = OUTPUT.read_bytes()
    print(f"wrote {len(written)} bytes to {OUTPUT}: {LINE}")


if __name__ == "__main__":
    main()
