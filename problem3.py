def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def decomposeprime(n):
    starter = int(n**0.5) + 1
    result = []
    for i in range(starter, -1, -1):
        if n % i == 0 and prime(i):
            return i


print(decomposeprime(600851475143))
