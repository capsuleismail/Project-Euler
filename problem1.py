# staircase
def stair(n):
  table = [1] + [0] * n
  for brick in range(1, n + 1):
    for heigth in range(n, brick - 1, -1):
      table[heigth] += table[heigth - brick]
  return table[-1] - 1


print(stair(5))
print(stair(6))
print(stair(7))
