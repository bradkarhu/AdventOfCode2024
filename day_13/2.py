from sys import argv


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
            x += 1e13
            y += 1e13
            ax, ay = a
            bx, by = b

            # obviously my part 1 solution wasn't going to scale by 1e13.
            # this solution was stolen shamelessly from u/luke2006. thanks!
            # https://www.reddit.com/r/adventofcode/comments/1hd4wda/comment/m1tjocv
            b = (ax * y - ay * x) / (ax * by - ay * bx)
            a = (x - bx * b) / ax
            if int(a) == a and int(b) == b:
                ans += int(3 * a + b)

    print(ans)


with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)
