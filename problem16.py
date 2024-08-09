test = str(2**1000).replace('0', '')
total = 0
for i in range(len(test)):
    total += int(test[i])
print(total)
