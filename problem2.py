def even_fibonacci_numbers():

    somma = 0
    a, b = 1, 1

    c = a + b
    while c < 4000000:
        somma = somma + c
        a = b + c
        b = c + a
        c = a + b
    return somma


print(even_fibonacci_numbers())
