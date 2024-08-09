def triangle_numbers(n):
    total = 0
    for i in range(1, int(n) + 1):
        total += i
    return total


def divisors(n):
    divid = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i**2 != n:
                divid += 2
            else:
                divid += 1
    return divid


index = 1
while divisors(triangle_numbers(index)) <= 500:
    index += 1
print(triangle_numbers(index))
