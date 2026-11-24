#!/usr/bin/env python3
"""Monday, Reviewed in One Line — v1 (original, written before reading the field).

Writes one funny one-line review of Monday to /output/entry.txt: the
alarm goes off at 6 while the soul is still on Sunday, the coffee files
a complaint, and the to-do list already asks for a day off. One line,
123 characters.
"""

import os

TEXT = (
    "Monday reviewed: alarm at 6, soul still on Sunday, coffee filed a "
    "complaint, and my to-do list already asked for a day off."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not have leading/trailing whitespace"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
