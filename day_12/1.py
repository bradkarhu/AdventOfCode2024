from sys import argv


def solve(lines: list[str], padded_char: str):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def fill(x: int, y: int, needle: str, visited: set, rtn: list):
        if (x, y) in visited:
            return
        visited.add((x, y))
        # count perimeter... or lack thereof
        p = 4
        for dx, dy in dirs:
            if lines[y + dy][x + dx] == needle:
                # recurse to get the area
                fill(x + dx, y + dy, needle, visited, rtn)
                p -= 1
        if p > 0:
            rtn.append(p)

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
            perimeter = sum(rtn)
            # print(f"found plot: {needle}, area: {area}, perimeter: {perimeter}")
            ans += area * perimeter
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
