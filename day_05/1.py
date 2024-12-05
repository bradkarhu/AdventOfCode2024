from sys import argv

def solve(lines: list[str]):
    reading_updates = False
    rules = dict()
    updates = []
    for line in lines:
        if (len(line) == 0):
            reading_updates = True
            continue
        if reading_updates:
            updates.append([int(n) for n in line.split(',')])
        else:
            a, b = line.split('|')
            key = int(a)
            val = int(b)
            if key not in rules:
                rules[key] = [val]
            elif val not in rules[key]:
                rules[key].append(val)
    num_in_order = 0
    sum = 0
    for update in updates:
        in_order = is_in_order(update, rules)
        if in_order:
            num_in_order += 1
            middle = len(update) // 2
            sum += update[middle]
        #print(update, in_order)
    #print(num_in_order, "of", len(updates), "in order")
    print(sum)

def is_in_order(update, rules):
    in_order = True
    for i in range(len(update) - 1, 0, -1):
        if update[i] not in rules:
            continue
        for j in range(i - 1, -1, -1):
            if update[j] in rules[update[i]]:
                #print(update[j], "shouldn't come before", update[i])
                in_order = False
                break
        if not in_order:
            break
    return in_order

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)