#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt, exactly as the competition gate requires:
UTF-8 text, 1 to 30 characters, not only white space.
"""
import os

WORD = "hazomi"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(WORD)
