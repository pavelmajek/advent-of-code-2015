# Advent of Code 2015, day 20, part 2

def divisors(n):
    if n == 1:
        return [1]
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
        return res


def get_presents(houses, cache):
    total = 0
    for number in divisors(houses):
        if number not in cache:
            cache[number] = 1
            total += number
        else:
            if cache[number] < 50:
                cache[number] += 1
                total += number
    return 11 * total


presents = 36000000
k = 1
cache = {}
while get_presents(k, cache) < presents:
    k += 1

print(f"Lowest house number: {k}")
