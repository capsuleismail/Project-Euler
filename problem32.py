def generate_permutations(s):
    
    if len(s) <= 1:
        return [s]
    
    perms = []
    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        for perm in generate_permutations(rest):
            perms.append(ch + perm)
    return perms

def is_valid(multiplicand, multiplier, product):
    return multiplicand * multiplier == product

def pandigital_products():
    digits = '123456789'
    products = set()
    perms = generate_permutations(digits)

    for perm in perms:
        # Case 1: 1-digit × 4-digit = 4-digit
        a = int(perm[0])
        b = int(perm[1:5])
        c = int(perm[5:])
        if is_valid(a, b, c):
            products.add(c)

        # Case 2: 2-digit × 3-digit = 4-digit
        a = int(perm[0:2])
        b = int(perm[2:5])
        c = int(perm[5:])
        if is_valid(a, b, c):
            products.add(c)

    return sum(products)


print(pandigital_products())
