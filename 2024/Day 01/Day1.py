"""
Advent of Code
2024 Day 01

@author: Tom Herbert
"""

day = 1

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    left = [int(line.split()[0]) for line in inputs]
    right = [int(line.split()[1]) for line in inputs]
    return left, right

def part_one(left, right):
    left, right = sorted(left), sorted(right)
    result = sum(list(map(lambda a, b: abs(a-b), left, right)))
    print(f"Part One = {result}")

def part_two(left, right):
    result = sum([val * right.count(val) for val in left])
    print(f"Part Two = {result}")

left, right = open_file(day)

part_one(left, right)
part_two(left, right)

