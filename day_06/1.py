from sys import argv
import numpy as np

def solve(lines: list[str]):
    size = len(lines)
    mask = np.zeros((size, size), dtype=int)
    x = -1
    y = -1
    for j, line in enumerate(lines):
        i = line.find("^")
        if i >= 0:
            x = i
            y = j
            break
    
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    d = 0
    dx, dy = dirs[d]
    while True:
        mask[y][x] = 1
        if x + dx < 0 or y + dy < 0 or \
           x + dx >= size or y + dy >= size:
            break # stop at the edge
        if lines[y + dy][x + dx] == "#":
            d += 1 # rotate
            if d > 3: d = 0
            dx, dy = dirs[d]
        x = x + dx
        y = y + dy
        
    sum = 0
    for j, line in enumerate(lines):
        #o = ""
        for i in range(size):
            if mask[j][i] > 0:
                #o += "X"
                sum += 1
            #else:
                #o += line[i]
        #print(o)
    print(sum)
        
with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)