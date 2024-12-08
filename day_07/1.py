from sys import argv

def solve(lines: list[str]):
    sum = 0
    for line in lines:
        left, right = line.split(':')
        test = int(left)
        nums = [int(n) for n in right.split()]
        results = recurse(nums[1:], [nums[0]])
        #print(results)
        if test in results:
            sum += test
    print(sum)

def recurse(nums: list[int], list):
    if len(nums) == 0: return list
    next = []
    for val in list:
        next.append(val + nums[0])
        next.append(val * nums[0])
    return recurse(nums[1:], next)

with open(argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)