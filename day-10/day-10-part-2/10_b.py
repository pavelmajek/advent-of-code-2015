# Advent of Code 2015, day 10, part 2

my_input = "1321131112"

def transform_string(text):
    result = ""
    index = 0

    while index < len(text):
        char = text[index]
        i = 1
        copy = 1

        try:
            while char == text[index + i]:
                copy += 1
                i += 1
            result += str(copy) + char
            index += copy
        except IndexError:
            result += str(copy) + char
            index += copy

    return result

for _ in range(50):
    text_res = transform_string(my_input)
    my_input = text_res

print(f"Length: {len(text_res)}")
