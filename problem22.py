import json


with open("/Users/ismailali/Desktop/Python/project euler/0022_names.txt") as f:
    names = json.loads(f"[{f.read()}]")
    names.sort()


result = {}
sums = 0
for i, element in enumerate(names):
    result[element] = (
        i + 1) * sum(list(map(lambda x: ord(x) - ord('A') + 1, list(element))))
    sums += (i + 1) * \
        sum(list(map(lambda x: ord(x) - ord('A') + 1, list(element))))

# print(sum(result.values()))
print(sums)
