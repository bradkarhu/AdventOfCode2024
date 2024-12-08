from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        left, right = line.split(':')
        test = int(left)
        nums = [int(n) for n in right.split()]
        results = recurse(nums[1:], [nums[0]], test)
        #print(results)
        if test in results:
            sum += test
    print(sum)

def recurse(nums: list[int], list, test):
    if len(nums) == 0: return list
    next = []
    for val in list:
        if val > test: continue # cuts the time in half
        next.append(val + nums[0])
        next.append(val * nums[0])
        next.append(int(f"{val}{nums[0]}"))
    return recurse(nums[1:], next, test)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)