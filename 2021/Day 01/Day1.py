"""
Advent of Code
2021 Day 1

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def format_data():
    global depths
    depths = [int(line.strip()) for line in inputs]

def part_one():
    count = sum([1 for i in range(1, len(depths)) if depths[i]>depths[i-1]])
    print(f"Part One = {count}")

def part_two():
    count = sum([1 for i in range(3, len(depths)) if depths[i]>depths[i-3]])
    print(f"Part Two = {count}")

day = 1
inputs = open_file()

format_data()

part_one()
part_two()