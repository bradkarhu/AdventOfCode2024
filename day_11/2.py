from sys import argv
import functools


def solve(line: str):
    sum = 0
    data = line.split()
    for val in data:
        sum += loop(val, 75)
    print(sum)


@functools.lru_cache(None)
def loop(val: str, n: int) -> int:
    if n == 0:
        return 1
    if val == "0":
        return loop("1", n - 1)
    elif len(val) % 2 == 0:
        mid = len(val) // 2
        rtn = loop(str(int(val[mid:])), n - 1)
        rtn += loop(str(int(val[:mid])), n - 1)
        return rtn
    else:
        return loop(str(int(val) * 2024), n - 1)


with open(argv[1], "r") as file:
    f = file.readline().rstrip()

solve(f)
