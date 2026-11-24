#!/bin/sh
# One Word, One Username, One Reward — entry program.
# Writes the entrant's own make.fun username, one word and nothing else,
# to /output/entry.txt, exactly as the competition gate requires:
# UTF-8 text, 1 to 30 characters, not only white space.
set -eu

mkdir -p /output
printf '%s' 'hazomi' > /output/entry.txt
