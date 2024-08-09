def collatz_seq(n):  # no space after function, snake case preferred in python
    if n == 1:   # base case
        return 1
    elif n % 2 == 0:     # recursive definitions
        return collatz_seq(n // 2) + 1   # integer division
    else:
        return collatz_seq(3 * n + 1) + 1


fullList = list()
for i in range(2, 1000000):
    fullList.append(collatz_seq(i))
sortedList = sorted(fullList, reverse=True)
print(sortedList[:-4])
