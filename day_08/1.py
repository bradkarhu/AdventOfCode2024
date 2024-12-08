from sys import argv


def solve(lines: list[str]):
    size = len(lines)
    nodes = dict()
    for y, line in enumerate(lines):
        for x, freq in enumerate(line):
            if freq == ".":
                continue
            if freq in nodes:
                nodes[freq].append((x, y))
            else:
                nodes[freq] = [(x, y)]

    def is_inbounds(point):
        x = point[0]
        y = point[1]
        return x >= 0 and x < size and y >= 0 and y < size

    def is_not_frequency(point, freq):
        x = point[0]
        y = point[1]
        return lines[y][x] != freq

    antinodes = set()
    for freq in nodes:
        coords = nodes[freq]
        for i in range(0, len(coords) - 1):
            x1, y1 = coords[i]
            for j in range(1, len(coords)):
                if i == j:
                    continue
                x2, y2 = coords[j]
                dx = x2 - x1
                dy = y2 - y1
                p1 = (x1 - dx, y1 - dy)
                p2 = (x2 + dx, y2 + dy)
                if is_inbounds(p1) and is_not_frequency(p1, freq):
                    antinodes.add(p1)
                if is_inbounds(p2) and is_not_frequency(p2, freq):
                    antinodes.add(p2)

    def print_lines():
        for y, line in enumerate(lines):
            o = ""
            for x, freq in enumerate(line):
                if (x, y) in antinodes:
                    if freq == ".":
                        o += "#"
                    else:
                        o += freq
                else:
                    o += freq
            print(o)

    # print_lines()
    print(len(antinodes))


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)
