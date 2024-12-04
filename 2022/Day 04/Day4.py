"""
Advent of Code
2022 Day 4

@author: Tom Herbert
"""

day = 4

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.split(",") for line in file.readlines()]
    return inputs

def format_data():
    global sections
    sections = []
    for line in inputs:
        pair = [[int(val) for val in elf.split("-")] for elf in line]
        sections.append(pair)

def part_one():
    count = 0
    for pair in sections:
        [[a, b], [c, d]] = pair
        if (a >= c and b <= d) or (c >= a and d <= b):
            count += 1
    print(f"Part One = {count}")

def part_two():
    count = 0
    for pair in sections:
        [[a, b], [c, d]] = pair
        if c <= a <= d or a <= c <= b:
            count += 1
    print(f"Part Two = {count}")
    pass

inputs = open_file()

format_data()

part_one()
part_two()
