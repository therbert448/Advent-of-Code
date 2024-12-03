"""
Advent of Code
2023 Day 4

@author: Tom Herbert
"""

day = 4

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    numbers = []
    for line in inputs:
        _, nums = line.split(": ")
        winning, have = [block.split() for block in nums.split(" | ")]
        winning = [int(val) for val in winning]
        have = [int(val) for val in have]
        numbers.append([winning, have])
    return numbers

def part_one(numbers):
    total = 0
    for line in numbers:
        winning, have = line
        matches = sum([1 if num in winning else 0 for num in have])
        if matches:
            total += 2 ** (matches - 1)
    print(f"Part One = {total}")

def part_two(numbers):
    counts = [1 for _ in range(len(numbers))]
    for i, line in enumerate(numbers):
        winning, have = line
        matches = sum([1 if num in winning else 0 for num in have])
        for j in range(matches):
            counts[i+1+j] += counts[i]
    print(f"Part Two = {sum(counts)}")

numbers = open_file(day)

part_one(numbers)
part_two(numbers)