result = set()
for i in range(2, 101):
    for j in range(2, 101):
        result.add(i**j)
print(len(result))
