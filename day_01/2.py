from sys import argv

def solve(lines: list[str]):
    a = []
    b = []
    for line in lines:
        x, y = line.split("   ")
        a.append(int(x))
        b.append(int(y))
        
    d = dict()
    for y in b:
        if y not in d:
            d[y] = 1
        else:
            d[y] += 1
            
    sum = 0
    for x in a:
        if x in d:
           sum += x * d[x]
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)