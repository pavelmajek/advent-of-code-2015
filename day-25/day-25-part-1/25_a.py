# Advent of Code 2015, day 25, part 1

import sys
sys.setrecursionlimit(5000)

def get_column(column, row, memo={}):
    if column == 1:
        return 1
    elif (column, row) in memo:
        return memo[(column, row)]
    else:
        result = get_column(column - 1, row, memo) + column
        memo[(column, row)] = result
        return result

def get_sum(column, row):
    return sum(range(column, column + row - 1))

def get_count(column, row):
    return get_column(column, row) + get_sum(column, row)

def find_code(column, row, first_code, multiply, division):
    code = first_code
    for i in range(get_count(column, row) - 1):
        new_code = (code * multiply) % division
        code = new_code
    return code

column = 3083
row = 2978
first_code = 20151125
multiply = 252533
division = 33554393

print(f"Code: {find_code(column, row, first_code, multiply, division)}")
