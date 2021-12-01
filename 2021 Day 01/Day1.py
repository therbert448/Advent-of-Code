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

def formatdata():
    global depths
    depths = [int(line.strip()) for line in inputs]

def part_one():
    count = sum([1 for i in range(1, len(depths)) if depths[i]>depths[i-1]])
    print(f"Part One = {count}")

def part_two():
    rolling = [sum(depths[i:i+3]) for i in range(len(depths)-2)]
    count = sum([1 for i in range(1, len(rolling)) if rolling[i]>rolling[i-1]])
    print(f"Part Two = {count}")

day = 1
inputs = open_file()

formatdata()

part_one()
part_two()