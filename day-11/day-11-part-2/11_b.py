# Advent of Code 2015, day 11, part 2

my_input = "cqjxxyzz"
abc = "abcdefghijklmnopqrstuvwxyz"


def generate_password(template, abc):
    rev_template = template[::-1]
    curr_index = 0

    while abc.index(rev_template[curr_index]) + 1 == len(abc):
        curr_index += 1

    new_temp = (curr_index * "a") + abc[abc.index(rev_template[curr_index]) + 1] + rev_template[curr_index + 1:]
    return new_temp[::-1]


def validate_password(password, abc):
    req1 = False
    req2 = True
    req3 = False

    for index, char in enumerate(password[:-2]):
        if char == abc[-1] or char == abc[-2]:
            pass
        else:
            if (password[index + 1] == abc[abc.index(char) + 1]) and (password[index + 2] == abc[abc.index(char) + 2]):
                req1 = True

    if any(char in password for char in "iol"):
        req2 = False

    index = 0
    pairs = set()
    while index < (len(password) - 1):
        if password[index] == password[index + 1]:
            pairs.add(password[index])
            index += 2
        else:
            index += 1
    if len(pairs) > 1:
        req3 = True

    if all([req1, req2, req3]):
        return True
    return False


while True:
    new_password = generate_password(my_input, abc)
    if validate_password(new_password, abc):
        print(f"New password: {new_password}")
        break
    my_input = new_password
