lists = [i for i in range(0, 10)]


def permutate(lists):
    if len(lists) == 1:
        return [lists]
    return [[lists[i]] + p for i in range(len(lists)) for p in permutate(lists[:i] + lists[i + 1:])]


print(len(permutate(lists)))
