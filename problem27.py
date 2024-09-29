import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  
    
    for num in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_consecutive_primes(a, b):
    n = 0
    while True:
        value = n**2 + a*n + b
        if not is_prime(value):
            break
        n += 1
    return n

def find_best_coefficients_with_sieve(limit):
    primes = sieve_of_eratosthenes(limit)
    max_primes = 0
    best_a, best_b = 0, 0
    
    # Loop through values of a and b
    for a in range(-limit + 1, limit):
        for b in primes:
            # Count primes for positive and negative b
            count_pos_b = count_consecutive_primes(a, b)
            count_neg_b = count_consecutive_primes(a, -b)
            
            # Update maximum if necessary
            if count_pos_b > max_primes:
                max_primes = count_pos_b
                best_a, best_b = a, b
            
            if count_neg_b > max_primes:
                max_primes = count_neg_b
                best_a, best_b = a, -b
    
    return best_a, best_b, best_a * best_b, max_primes

find_best_coefficients_with_sieve(1000) # −59231.
