# Advent of Code 2015, day 20, part 1

def nth_house_presents(n):
    if n == 1:
        return 10
    else:
        i = 2
        res = [1, n]
        while i ** 2 < n:
            if n % i == 0:
                res.append(i)
                res.append(int(n/i))
            i += 1
        if i ** 2 == n:
            res.append(i)
        return sum(res) * 10

total = 36000000
number = 1
while nth_house_presents(number) < total:
    number += 1

print(f"Lowest house number: {number}")
