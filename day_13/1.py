from sys import argv
from collections import deque


def solve(lines: list[str]):
    ans = 0

    for line in lines:
        if len(line) == 0:
            continue
        array = [s.strip(":,") for s in line.split()]
        if array[0] == "Button":
            x, y = (int(array[2].split("+")[1]), int(array[3].split("+")[1]))
            if array[1] == "A":
                a = x, y
            else:
                b = x, y
        else:
            x, y = (int(array[1].split("=")[1]), int(array[2].split("=")[1]))
            ax, ay = a
            bx, by = b

            # my slow way (2.328 seconds):
            # z = shortest_path(x, y, ax, ay, bx, by)
            # print("searching for:", x, y, a[0], a[1], b[0], b[1], "=", z)
            # if z > 0:
            #    ans += z

            # using faster math based solution from part 2:
            b = (ax * y - ay * x) / (ax * by - ay * bx)
            a = (x - bx * b) / ax
            if int(a) == a and int(b) == b:
                ans += int(3 * a + b)

    print(ans)


def shortest_path(X, Y, X1, Y1, X2, Y2):
    # BFS queue: stores (x, y, current_cost)
    queue = deque([(0, 0, 0)])

    # Dictionary to track the minimum cost to reach each position (x, y)
    visited = {}
    visited[(0, 0)] = 0  # The cost to reach (0, 0) is 0

    # Directions for the two types of steps
    steps = [((X1, Y1), 3), ((X2, Y2), 1)]  # (move, cost)

    while queue:
        current_x, current_y, current_cost = queue.popleft()

        # If we've reached the destination, return the current cost
        if (current_x, current_y) == (X, Y):
            return current_cost

        # Stop after we've passed the destination
        if current_x > X or current_y > Y:
            continue

        # Try both possible steps
        for (dx, dy), step_cost in steps:
            next_x, next_y = current_x + dx, current_y + dy
            next_cost = current_cost + step_cost

            # If this position has not been visited or can be reached with a lower cost, visit it
            if (next_x, next_y) not in visited or next_cost < visited[(next_x, next_y)]:
                visited[(next_x, next_y)] = next_cost
                queue.append((next_x, next_y, next_cost))

    # If we exhaust the queue and haven't found the destination, return -1
    return -1


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)
