from sys import argv

def solve(lines: list[str]):
    sum = 0    
    for report in lines:
        levels = report.split(" ")
        dir = 0
        previous = 0
        safe = True
        for i in range(len(levels)):
            level = int(levels[i])
            if i == 1:
                if level > previous:
                    dir = 1
                elif level < previous:
                    dir = -1
                else:
                    safe = False
                    break            
            diff = level - previous
            if dir == 1 and (diff < 1 or diff > 3):
                safe = False
                break
            elif dir == -1 and (diff > -1 or diff < -3):
                safe = False
                break            
            previous = level
        print(report, safe)
        if safe:
            sum += 1
        
    print(sum)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)