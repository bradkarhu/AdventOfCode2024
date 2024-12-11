from sys import argv


def solve(lines: list[str]):
    sum = 0
    order = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def search(x: int, y: int, index: tuple, trailheads: list):
        if x < 0 or y < 0 or x >= size or y >= size:
            return
        if lines[y][x] != order[index]:
            return
        if index == len(order) - 1:
            # print("found end of trail at", x, y)
            trailheads.append((x, y))
            return
        for dx, dy in dirs:
            search(x + dx, y + dy, index + 1, trailheads)

    size = len(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == order[0]:
                trailheads = []
                search(x, y, 0, trailheads)
                score = len(trailheads)
                # if score > 0:
                #    print("found trailhead at", x, y, "score:", score)
                sum += score
    print(sum)


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)
