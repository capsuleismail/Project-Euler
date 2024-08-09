# Starting in the top left corner of 2x2 a grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20X20grid?

## vi - v1

# DynamicProgramming


def solve():
    paths = [[0 for i in range(20 + 1)] for j in range(20 + 1)]
    paths[20][20] = 1
    queue = [(20, 20)]

    while queue:
        current = queue.pop(0)
        if current[0] - 1 >= 0:
            if (current[0] - 1, current[1]) not in queue:

                queue.append((current[0] - 1, current[1]))

            paths[current[0] - 1][current[1]] += paths[current[0]][current[1]]

        if current[1] - 1 >= 0:

            if (current[0], current[1] - 1) not in queue:
                queue.append((current[0], current[1] - 1))
            paths[current[0]][current[1] - 1] += paths[current[0]][current[1]]

    return paths[0][0]


print(solve())
