def mlt_three_or_five():
    return sum([i for i in range(1, 1000) if (i % 3 == 0) or (i % 5 == 0)])


print(mlt_three_or_five())
