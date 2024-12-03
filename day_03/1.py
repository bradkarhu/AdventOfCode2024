import re
from sys import argv

def solve(lines: list[str]):
    regex = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
    sum = 0
    for line in lines:
        matches = regex.findall(line)
        for match in matches:
            a, b = match[4:-1].split(",")
            #print(match, a, "*", b)
            sum += int(a) * int(b)
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)