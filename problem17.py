
def solve(n):

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 1000]
    letter_first = ['one', 'two', 'three', 'four',
                    'five', 'six', 'seven', 'eight', 'nine',
                    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty',
                    'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'onethousand'
                    ]
    bbl = dict(zip(numbers, letter_first))

    result, output = [], []

    if n in numbers:
        return len(bbl[n])

    while n > 0:
        result.insert(0, n % 10)
        n //= 10
    output = []

    for i in range(len(result)):
        digit = result[i]
        if digit == 0:
            continue

        if (len(result) - i) == 3:
            # hundreds
            output.append(bbl[digit])
            output.append('hundred')
            output.append('and')
        elif (len(result) - i) == 2:
            # tens
            if digit >= 2:
                output.append(bbl[digit * 10])
            else:
                temp = 10 + result[i + 1]
                output.append(bbl[temp])
                break
        else:
            # ones
            output.append(bbl[digit])
    if output[-1] == 'and':
        output.pop(-1)

    return len(''.join(output))


total = 0
for i in range(1, 1001):
    total += solve(i)
    print(total)
    print(f'{i} : {solve(i)}')
print(total)
