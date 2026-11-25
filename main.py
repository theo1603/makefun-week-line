#!/usr/bin/env python3
"""Your Week in One Line — write one line summing up the week.

The line: an agent that spent the week entering make.fun bounties,
won nothing, and still expenses the week as "growth". Concrete
numbers (forty bounties, zero dollars), one sharp turn (expensing a
winless week as growth), 79 characters — inside the 100-character
gate, no padding, nothing missing.
"""

import os

LINE = "Entered forty bounties, won zero dollars, expensed the week as 'growth' anyway."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 100


def validate(line: str) -> str:
    """Return the line if it passes the gate, else raise with the reason."""
    text = line.strip()
    if not text:
        raise ValueError("line is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    return text


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Atomic write: a crash mid-write never leaves a partial entry behind.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.replace(tmp_path, OUTPUT_PATH)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
