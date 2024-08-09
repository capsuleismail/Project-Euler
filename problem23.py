def is_abundant(n):
    divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return divisors_sum > n


def list_abundant_numbers(limit):
    return [n for n in range(12, limit + 1) if is_abundant(n)]


def generate_abundant_sums(abundant_numbers, limit):
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            summation = abundant_numbers[i] + abundant_numbers[j]
            if summation <= limit:
                abundant_sums.add(summation)
            else:
                break
    return abundant_sums


def non_abundant_sum(limit):
    abundant_numbers = list_abundant_numbers(limit)
    abundant_sums = generate_abundant_sums(abundant_numbers, limit)

    non_abundant_sum_total = sum(n for n in range(
        1, limit + 1) if n not in abundant_sums)

    return non_abundant_sum_total


# Running the solution for the limit 28123
limit = 28123
result = non_abundant_sum(limit)
print(
    f"The sum of all positive integers which cannot be written as the sum of two abundant numbers is: {result}")
