import re
from sys import argv

def solve(lines: list[str]):
    regex = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
    sum = 0
    enabled = True
    for line in lines:
        matches = regex.findall(line)
        for match in matches:
            if match == "don't()":
                enabled = False
                #print(match, "--> disabled")
            elif match == "do()":
                enabled = True
                #print(match, "--> enabled")
            else:
                if enabled:
                    a, b = match[4:-1].split(",")
                    #print(match, a, "*", b)
                    sum += int(a) * int(b)
                #else:
                    #print(match, "--> skipped")
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)