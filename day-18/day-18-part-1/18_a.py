# Advent of Code 2015, day 18, part 1

import numpy as np

with open("../../data/18.txt") as file:
    content = ""
    for line in file.readlines():
        content += line.strip()

start_lights_instructions = []
for char in content:
    if char == "#":
        start_lights_instructions.append(1)
    else:
        start_lights_instructions.append(0)

start_lights = np.array(start_lights_instructions).reshape((100, 100))

def evaluate_cells(array, i, j):
    top = array[i - 1][j] if i > 0 else None
    right = array[i][j + 1] if j < len(array[0]) - 1 else None
    bottom = array[i + 1][j] if i < len(array) - 1 else None
    left = array[i][j - 1] if j > 0 else None
    top_right = array[i - 1][j + 1] if i > 0 and j < len(array[0]) - 1 else None
    top_left = array[i - 1][j - 1] if i > 0 and j > 0 else None
    bottom_right = array[i + 1][j + 1] if i < len(array) - 1 and j < len(array[0]) - 1 else None
    bottom_left = array[i + 1][j - 1] if i < len(array) - 1 and j > 0 else None
    values = [top, right, bottom, left, top_right, top_left, bottom_right, bottom_left]
    total = 0
    for value in values:
        if value is not None:
            total += value
    return total


iterate_arr = start_lights[:][:]

for _ in range(100):
    temp_arr = np.zeros((100,100))
    for i, row in enumerate(iterate_arr):
        for j, element in enumerate(row):
            if iterate_arr[i][j] == 1:
                if evaluate_cells(iterate_arr,i,j) == 2 or evaluate_cells(iterate_arr,i,j) == 3:
                    temp_arr[i][j] = 1
                else:
                    temp_arr[i][j] = 0
            else:
                if evaluate_cells(iterate_arr,i,j) == 3:
                    temp_arr[i][j] = 1
                else:
                    temp_arr[i][j] = 0
    iterate_arr = temp_arr[:][:]

print(f"Lights: {np.sum(iterate_arr)}")
