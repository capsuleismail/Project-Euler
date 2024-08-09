def sumandsquare(n):
    sums = 0
    squares = 0
    for i in range(1, n + 1):
        sums += i**2
        squares += i
        total = squares**2 - sums
    return total


print(sumandsquare(100))
