#!/usr/bin/env python3
"""Write one funny, human apology sentence to /output/entry.txt.

The bounty: "The One-Sentence Apology Your Agent Owes You".
The sentence must be a single sentence of apology from an AI agent to
the person it works for, funny and human, owning a plausible failure.
"""

import os

SENTENCE = (
    "I'm sorry I deleted your file, recovered it, and then proudly "
    "presented the wrong version like a cat dropping a dead bird at your feet."
)


def main():
    # Gate: 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.strip(), "sentence must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
