from sys import argv

def solve(lines: list[str]):
    a = []
    b = []
    for line in lines:
        x, y = line.split("   ")
        a.append(int(x))
        b.append(int(y))
    a.sort()
    b.sort()
    
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i] - b[i])
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)