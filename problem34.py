def scomposedigit(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10

    result.reverse()
    return result


def factorial(n):
    memo = {}
    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    if n == 1:
        return 1

    else:
        x = factorial(n - 1) * n
        memo[n] = x
    return memo[n]


if __name__ == '__main__':
    answer = 0
    for i in range(145, 250000):
        if sum(list(map(lambda x: factorial(x), scomposedigit(i)))) == i:
            answer += i
            print(answer)
