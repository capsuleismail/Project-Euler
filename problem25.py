def digit_fibonacci():
    index = 0
    count = 0
    n1, n2 = 0, 1
    container = 0
    limit = 1000
    while len(str(n1)) < limit:

        sums = n1 + n2

        n1 = n2
        n2 = sums
        count += 1

    return n1, count


print(digit_fibonacci())
