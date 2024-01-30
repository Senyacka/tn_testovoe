'''
Задание 1: Написать функцию, возвращающую все простые числа до N
'''


def simple_digits(limit: int) -> list:
    result = []
    sieve = [0] * 2 + [1] * limit
    for i in range(int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = 0
    for i in range(limit):
        if sieve[i]:
            result.append(i)
    return result


print(simple_digits(111))
