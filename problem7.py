# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def nthprime(n):
    numofp, prime = 0, 1
    while numofp < n:
        prime += 1
        if isprime(prime):
            numofp += 1
    return prime


print(nthprime(10001))
print(nthprime(9995))
print(nthprime(7))
print(nthprime(9))
print(nthprime(21))
print(nthprime(11))
