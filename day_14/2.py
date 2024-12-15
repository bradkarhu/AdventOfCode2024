from sys import argv


def solve(lines: list[str], xmas: int, ymax: int):
    robots = []
    for line in lines:
        a = line.split()
        b = a[0][2:].split(",")
        c = a[1][2:].split(",")
        x, y = int(b[0]), int(b[1])
        dx, dy = int(c[0]), int(c[1])
        robots.append((x, y, dx, dy))

    spots = {}
    seconds = 1
    while True:
        spots.clear()
        more_than_one = False

        for x, y, dx, dy in robots:
            x = (x + (dx * seconds)) % xmas
            y = (y + (dy * seconds)) % ymax

            if (x, y) not in spots:
                spots[(x, y)] = 1
            else:
                more_than_one = True
                break

        if more_than_one:
            seconds += 1
        else:
            break

    def print_robots():
        for y in range(ymax):
            o = ""
            for x in range(xmas):
                if (x, y) in spots:
                    o += "#"
                else:
                    o += "."
            print(o)

    # print_robots()
    print(seconds)


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f, 101, 103)
