from sys import argv


def solve(lines: list[str]):
    grid, x, y = build_grid(lines)
    directions = parse_directions(lines)
    # print_grid(grid, x, y)
    # print(directions)

    for dx, dy in directions:
        # _ = input("press any key to continue: ")
        # print_grid(grid, x, y)

        x1 = x + dx
        y1 = y + dy

        if grid[y1][x1] == 2:
            # print("no move, hit a wall")
            continue
        if grid[y1][x1] == 0:
            # print("moved to empty space")
            x = x1
            y = y1
            continue

        # handle the boxes
        x2 = x1 + dx
        y2 = y1 + dy
        while grid[y2][x2] == 1:
            x2 += dx
            y2 += dy
        if grid[y2][x2] == 2:
            # print("has box but no move, hit a wall")
            pass
        elif grid[y2][x2] == 0:
            # swap O for .
            grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]
            # move robot
            x = x1
            y = y1
            # print("moved box")

    # print_grid(grid, x, y)

    ans = 0
    size = len(grid)
    for y in range(size):
        for x in range(size):
            if grid[y][x] == 1:
                ans += 100 * y + x
    print(ans)


def build_grid(lines: list[str]):
    size = len(lines[0])
    grid = []
    x, y = -1, -1
    for _ in range(size):
        grid.append([0] * size)  # init
    for row in range(size):
        for col in range(size):
            if lines[row][col] == "O":
                grid[row][col] = 1
            elif lines[row][col] == "#":
                grid[row][col] = 2
            elif lines[row][col] == "@":
                x, y = col, row
    return grid, x, y


def print_grid(grid: list[list[int]], x, y):
    size = len(grid)
    for row in range(size):
        line = ""
        for col in range(size):
            if row == y and col == x:
                line += "@"
            elif grid[row][col] == 1:
                line += "O"
            elif grid[row][col] == 2:
                line += "#"
            else:
                line += "."
        print(line)


def parse_directions(lines: list[str]):
    begin = False
    directions = []
    for line in lines:
        if not begin:
            if len(line) == 0:
                begin = True
            continue

        for c in line:
            if c == "<":
                directions.append((-1, 0))
            elif c == "^":
                directions.append((0, -1))
            elif c == ">":
                directions.append((1, 0))
            elif c == "v":
                directions.append((0, 1))
            else:
                print("bad parsing", c, line)
    return directions


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)
