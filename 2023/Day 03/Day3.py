"""
Advent of Code
2023 Day 3

@author: Tom Herbert
"""

day = 3

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def parse_file(inputs):
    nums, syms = {}, {}
    xMax, yMax = len(inputs[0]), len(inputs)
    for y, line in enumerate(inputs):
        string, start = "", None
        for x, char in enumerate(line):
            if char.isnumeric():
                if start == None:
                    start = x
                string += char
            else:
                if string:
                    nums[(start, y)] = string
                    string, start = "", None
                if char == ".":
                    continue
                else:
                    syms[(x, y)] = char
        if string: nums[(start, y)] = string
    return nums, syms, xMax, yMax

def neighbours(coord, num, xMax, yMax):
    x, y = coord
    xs = [x - 1 + i for i in range(len(num) + 2)]
    ys = [y - 1 + i for i in range(3)]
    xs = [val for val in xs if val >= 0 and val < xMax]
    ys = [val for val in ys if val >= 0 and val < yMax]
    neighs = set()
    for x in xs:
        for y in ys:
            neighs.add((x, y))
    return neighs

def ratio(args):
    result = 1
    for arg in args:
        result *= arg
    return result

def part_one_and_two(nums, syms, xMax, yMax):
    gears = {}
    total = 0
    for coord, num in nums.items():
        neighs = neighbours(coord, num, xMax, yMax)
        for n in neighs:
            if n in syms and syms[n] == "*":
                if n in gears:
                    gears[n].append(int(num))
                else:
                    gears[n] = [int(num)]
        if any([n in syms for n in neighs]):
            total += int(num)
    print(f"Part One = {total}")
    total = sum([ratio(parts) for parts in gears.values() if len(parts) == 2])
    print(f"Part Two = {total}")

inputs = open_file(day)
nums, syms, xMax, yMax = parse_file(inputs)

part_one_and_two(nums, syms, xMax, yMax)