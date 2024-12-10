from sys import argv


def print_expanded(groups, *explanation):
    s = ""
    for j in range(len(groups)):
        val, size = groups[j]
        if val == -1:
            s += "." * size
        else:
            s += str(val) * size
    print(s, " ".join(str(arg) for arg in explanation))


def solve(line: str):
    id = -1  # use for counting up, then counting down
    groups = []
    for index, c in enumerate(line):
        if index % 2 == 0:
            id += 1
            groups.append((id, int(c)))  # file id, size
        elif int(c) > 0:
            groups.append((-1, int(c)))  # free space, size
    # print_expanded(groups, "starting point")

    i = 0  # track the leftmost empty space
    j = len(groups) - 1  # track the file id, descending
    while j > i:
        val, size = groups[j]
        if val != id:
            j -= 1
            continue
        id -= 1
        first_space_at = None
        for ii in range(i, j):
            val2, space = groups[ii]
            if val2 == -1:
                if first_space_at is None:
                    first_space_at = ii
                    i = ii  # cut time from ~1.7s to ~0.5s
                if space < size:
                    continue
                if space == size:
                    groups[ii], groups[j] = groups[j], groups[ii]
                else:  # deal with the remaining free space
                    groups[ii], groups[j] = groups[j], (-1, size)
                    groups.insert(ii + 1, (-1, space - size))
                # print_expanded(groups, "moved", val, "x", size, "with", space - size, "left")
                break

    # print_expanded(groups, "ending point")

    sum = 0
    index = 0
    for j in range(len(groups)):
        val, size = groups[j]
        if val >= 0:
            for _ in range(size):
                sum += index * val
                index += 1
        else:
            index += size
    print(sum)


with open(argv[1], "r") as file:
    f = file.readline().rstrip()

solve(f)
