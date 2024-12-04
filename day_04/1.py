from sys import argv

def solve(lines: list[str]):
    sum = 0
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter != 'X':
                continue
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    sum += check_word(lines, x+i, y+j, i, j, "MAS")        
    print(sum)
    
def check_word(lines: list[str], x: int, y: int, dx: int, dy: int, word: str) -> int:
    if lines[y][x] == word: 
        #print("found", word, "at", y, x)
        return 1
    if lines[y][x] != word[0]:
        return 0
    return check_word(lines, x+dx, y+dy, dx, dy, word[1:])

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