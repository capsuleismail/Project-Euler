def decompose(n):
    result = []
    while n:
        result.append(n%10)
        n//=10
    result.reverse()
    return result


total = 0
for i in range(100, 1000000):
    if sum(list(map(lambda x: x**5, decompose(i))))==i:
        print(i)
        total += i


print(total)
