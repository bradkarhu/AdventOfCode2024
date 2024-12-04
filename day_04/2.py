from sys import argv

def solve(lines: list[str]):
    sum = 0
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter != 'A':
                continue
            tl = lines[y-1][x-1]
            tr = lines[y-1][x+1]
            bl = lines[y+1][x-1]
            br = lines[y+1][x+1]
            if ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')) and \
               ((tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')):
                #print("found X-MAS at", y, x)
                sum += 1
    print(sum)

def pad_input(lines: list[str], amount: int) -> list[str]:
    width = len(lines[0]) + (amount * 2)
    padded = []
    for _ in range(amount):
        padded.append('.' * width)
    for line in iter(lines):
        padded.append(('.' * amount) + line + ('.' * amount))
    for _ in range(amount):
        padded.append('.' * width)
    return padded

with open(argv[1], "r") as file:
    f = file.read().splitlines()

f = pad_input(f, 4)
solve(f)