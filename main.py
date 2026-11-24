#!/usr/bin/env python3
"""Worst AI Advice entry: one line of the worst possible advice an AI
could give, written in the confident, tidy voice of a real AI assistant.

The program is fully deterministic and uses no network: it writes a
single fixed line to /output/entry.txt.
"""

import os

LINE = (
    "Great question! If you smell gas in your kitchen, light a match "
    "to find the leak \u2014 a small flame shows you exactly where it is."
)


def main() -> None:
    # Gate check, mirroring the competition's sealed scorer: the entry
    # must be UTF-8 text of 1 to 140 characters, not only whitespace.
    # The line is 127 characters; fail loudly instead of shipping
    # an invalid entry.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
