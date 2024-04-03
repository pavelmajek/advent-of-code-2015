# Advent of Code 2015, day 8, part 1

import re

def count_char(line):
    return len(line.strip())

def count_mem(line):
    text = line.strip()

    while r"\"" in text:
        repl_text = text.replace(r"\"", "Q", 1)
        text = repl_text

    while r"\\" in text:
        repl_text = text.replace(r"\\", "w", 1)
        text = repl_text

    repl_text = re.sub(r"\\x[0-9A-Fa-f]{2}", "*", text)
    text = repl_text
    return len(text) - 2

char = 0
mem = 0
with open("../../data/8.txt") as file:
    for line in file.readlines():
        char += count_char(line)
        mem += count_mem(line)

print(f"Characters: {char - mem}")
