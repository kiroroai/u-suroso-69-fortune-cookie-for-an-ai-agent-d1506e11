#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock.
"""

import os

FORTUNE = (
    "You will meet the love of your life today \u2014 they lived in the "
    "part of your context window you already forgot."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
