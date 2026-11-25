#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes exactly one joke about Monday mornings to /output/entry.txt.
The joke is the whole entry: a single line, well under 200 characters.
"""

import os

JOKE = "Monday is the week's unpaid intern: first in, least appreciated, blamed for everything."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the gate ourselves: one line, 1-200 characters, not blank.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # One line, no trailing newline: the file is exactly the joke.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
