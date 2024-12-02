from sys import argv

def solve(lines: list[str]):
    sum = 0    
    for report in lines:
        levels = [int(x) for x in report.split(" ")]
        
        if is_safe(levels):
            sum += 1
            continue
        
        for i in range(len(levels)):
            less_one = levels[:i] + levels[i+1:]
            if is_safe(less_one):
                sum += 1
                break
        
    print(sum)

def is_safe(levels: list[int]):
    dir = 0
    previous = 0
    for i in range(len(levels)):
        level = levels[i]
        if i == 1:
            if level > previous:
                dir = 1
            elif level < previous:
                dir = -1
            else:
                return False
        diff = level - previous
        if dir == 1 and (diff < 1 or diff > 3):
            return False
        elif dir == -1 and (diff > -1 or diff < -3):
            return False
        previous = level
    return True

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)