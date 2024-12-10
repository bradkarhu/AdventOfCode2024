from sys import argv


def solve(line: str):
    id = 0
    expanded = []
    for index, c in enumerate(line):
        if index % 2 == 0:
            for _ in range(int(c)):
                expanded.append(id)
            id += 1
        else:
            for _ in range(int(c)):
                expanded.append(-1)
    # print(expanded)

    j = len(expanded) - 1
    for i in range(len(expanded)):
        if expanded[i] >= 0:
            continue
        while expanded[j] == -1:
            j -= 1
        if i < j:
            expanded[i], expanded[j] = expanded[j], expanded[i]
    # print(expanded)

    sum = 0
    for i, val in enumerate(expanded):
        if val < 0:
            break
        sum += i * val
    print(sum)


with open(argv[1], "r") as file:
    f = file.readline().rstrip()

solve(f)
