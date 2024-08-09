# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def ispalindrome(s):
    return str(s) == str(s)[::-1]


def largest_palindrome_product():

    lst = []

    for i in range(1, 1000):
        for j in range(1, 1000):
            lst.append(i * j)
    return sorted(list(filter(ispalindrome, lst)))[-1]


print(largest_palindrome_product())
