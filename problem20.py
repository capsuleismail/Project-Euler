# For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,
# and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.
# Find the sum of the digits in the number $100!$

def digitsum(x):
    txt = str(x)
    res = 0
    for i in range(len(txt)):
        res += int(txt[i])
    return res


def fibonacci_of(n):
    container = []
    res = 1
    if n == 0 or n == 1:
        return n
    for i in range(1, n + 1):
        res = res * i
        txt = str(res)
    for i in range(len(txt)):
        container += [int(txt[i])]
    return res, sum(container)


print(fibonacci_of(100))
