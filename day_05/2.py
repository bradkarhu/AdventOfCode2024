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
    num_not_in_order = 0
    sum = 0
    for update in updates:
        if not is_in_order(update, rules):
            num_not_in_order += 1
            middle = len(update) // 2
            sum += update[middle]
    #print(num_not_in_order, "of", len(updates), "not in order")
    print(sum)

def is_in_order(update, rules):
    in_order = True
    for i in range(len(update) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if update[i] in rules and update[j] in rules[update[i]]:
                #print(update[j], "shouldn't come before", update[i])
                in_order = False                
                update[i], update[j] = update[j], update[i] # swap to fix
    return in_order

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)