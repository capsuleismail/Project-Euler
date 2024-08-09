# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#step 1: check if a numbers is prime:
#step 2: loop over the limit and sum all primes in the range
def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def twomillions():
    tot = 0
    for i in range(2, (2 * 10**6) + 1):
        if isprime(i) == True:
            tot += i
    return tot


print(twomillions())
