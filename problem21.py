
def findproperdivisor(n):
    divisor_sum = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i

            if i != n // i:
                divisor_sum += n // i
    return divisor_sum


def findamicablenumbersum(limit):
    total = 0
    for i in range(2, limit):
        b = findproperdivisor(i)
        if b > i and b < limit:
            if findproperdivisor(b) == i:
                total += i + b
    return total


print(findamicablenumbersum(10000))
