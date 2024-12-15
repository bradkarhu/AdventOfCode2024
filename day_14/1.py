from sys import argv


def solve(lines: list[str], xmas: int, ymax: int, seconds: int):
    xm = xmas // 2
    ym = ymax // 2
    robots = {}

    for line in lines:
        a = line.split()
        b = a[0][2:].split(",")
        c = a[1][2:].split(",")
        x, y = int(b[0]), int(b[1])
        dx, dy = int(c[0]), int(c[1])

        for _ in range(seconds):
            x = (x + dx) % xmas
            y = (y + dy) % ymax

        if (x, y) in robots:
            robots[(x, y)] += 1
        else:
            robots[(x, y)] = 1

    q = [[] for _ in range(4)]

    def assign_robots():
        for x, y in robots:
            if x == xm or y == ym:
                continue
            elif x < xm:
                if y < ym:
                    q[0].append((x, y))
                else:
                    q[1].append((x, y))
            else:
                if y < ym:
                    q[2].append((x, y))
                else:
                    q[3].append((x, y))

    def print_robots():
        for y in range(ymax):
            if y == ym:
                print()
                continue
            o = ""
            for x in range(xmas):
                if x == xm:
                    o += " "
                elif (x, y) in robots:
                    o += str(robots[(x, y)])
                else:
                    o += "."
            print(o)

    assign_robots()
    # print_robots()

    ans = 1
    for r in q:
        print(r)
        if len(r) > 0:
            ans *= sum([robots[(x, y)] for x, y in r])
    print(ans)


with open(argv[1], "r") as file:
    f = file.read().splitlines()

# solve(f, 11, 7, 100) # sample
solve(f, 101, 103, 100)
