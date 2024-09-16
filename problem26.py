# Online Python - IDE, Editor, Compiler, Interpreter
def recurring_cycle_length(d):
    # If d is divisible by 2 or 5, it terminates
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    # If d becomes 1, it means the decimal terminates
    if d == 1:
        return 0
    
    # Otherwise, find the length of the recurring cycle
    remainder = 1
    position = 0
    remainders = {}
    
    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1
    
    return 0

# Find the value of d between 1 and 1000 with the longest recurring cycle
max_cycle_length = 0
best_d = 0

for d in range(1, 1001):
    cycle_length = recurring_cycle_length(d)
    if cycle_length > max_cycle_length:
        max_cycle_length = cycle_length
        best_d = d

print(best_d, max_cycle_length)
