# Advent of Code 2015, day 4, part 1

import hashlib

my_key = "yzbqklnj"
n = 0
while True:
    key_input = my_key + str(n)
    result = hashlib.md5(key_input.encode())
    if result.hexdigest().startswith("00000"):
        print(f"Hash number: {n}")
        break
    n += 1
