from sys import argv


def solve(lines: list[str], padded_char: str):
    fill_dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    corner_dirs = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

    def fill(x: int, y: int, needle: str, visited: set, rtn: list):
        if (x, y) in visited:
            return
        visited.add((x, y))
        # find neighbor locations
        neighbors = [False] * 4
        for i in range(len(fill_dirs)):
            dx, dy = fill_dirs[i]
            if lines[y + dy][x + dx] == needle:
                # recurse to get the area
                fill(x + dx, y + dy, needle, visited, rtn)
                neighbors[i] = True
        # count corners (the not fun part)
        c = 0
        num_neighbors = sum(neighbors)
        if num_neighbors == 0:
            c = 4
        elif num_neighbors == 1:
            c = 2
        elif num_neighbors >= 2:
            for i in range(len(neighbors)):
                j = (i + 1) % 4
                if not neighbors[i] and not neighbors[j]:
                    c += 1
                elif neighbors[i] and neighbors[j]:
                    cx, cy = corner_dirs[i]
                    if lines[y + cy][x + cx] != needle:
                        c += 1
        if c > 0:
            rtn.append(c)

    all_visited = set()
    ans = 0
    for y, line in enumerate(lines):
        for x, needle in enumerate(line):
            if needle == padded_char:
                continue
            if (x, y) in all_visited:
                continue
            visited = set()
            rtn = []
            fill(x, y, needle, visited, rtn)
            all_visited |= visited
            area = len(visited)
            corners = sum(rtn)
            # print(f"found plot: {needle}, area: {area}, corners: {corners}")
            ans += area * corners
    print(ans)


def pad_input(lines: list[str], amount: int, char: str) -> list[str]:
    width = len(lines[0]) + (amount * 2)
    padded = []
    for _ in range(amount):
        padded.append(char * width)
    for line in lines:
        padded.append((char * amount) + line + (char * amount))
    for _ in range(amount):
        padded.append(char * width)
    return padded


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(pad_input(f, 1, "."), ".")
