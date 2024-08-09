

def pytha():

    m = 1000
    res = []
    # You can easily dont make range not further than 500
    # because if you square a and b, c would be more than 1000
    for a in range(1, int(m / 2)):
        for b in range(1, int(m / 2)):
            c = (m - a) - b
            # they has to be one smaller than the next one
            if a < b < c:
                if a**2 + b**2 == c**2:
                    print([a, b, c, a * b * c])


print(pytha())
