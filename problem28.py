def diagonal_sum(n):
    total = 1  # Centre
    for k in range(3, n+1, 2):
        total += 4 * k * k - 6 * (k - 1)
    return total
