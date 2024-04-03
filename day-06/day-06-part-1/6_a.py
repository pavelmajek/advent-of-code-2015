# Advent of Code 2015, day 6, part 1

import numpy as np

with open("../../data/6.txt") as file:
    content = [line for line in file.readlines()]

santa_arr = np.zeros((1000, 1000))

for item in content:
    if item.startswith("turn on"):
        temp_list = item.split()
        start_x, start_y = temp_list[2].split(",")
        stop_x, stop_y = temp_list[4].split(",")

        for x in range(int(start_x), int(stop_x) + 1):
            for y in range(int(start_y), int(stop_y) + 1):
                santa_arr[x][y] = 1

    if item.startswith("turn off"):
        temp_list = item.split()
        start_x, start_y = temp_list[2].split(",")
        stop_x, stop_y = temp_list[4].split(",")

        for x in range(int(start_x), int(stop_x) + 1):
            for y in range(int(start_y), int(stop_y) + 1):
                santa_arr[x][y] = 0

    if item.startswith("toggle"):
        temp_list = item.split()
        start_x, start_y = temp_list[1].split(",")
        stop_x, stop_y = temp_list[3].split(",")

        for x in range(int(start_x), int(stop_x) + 1):
            for y in range(int(start_y), int(stop_y) + 1):
                if santa_arr[x][y] == 0:
                    santa_arr[x][y] = 1
                elif santa_arr[x][y] == 1:
                    santa_arr[x][y] = 0

print(f"Lights on: {np.count_nonzero(santa_arr)}")
