"""
Advent of Code
2022 Day 5

@author: Tom Herbert
"""

day = 5

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read().split("\n\n")
    return inputs

def format_data():
    global stacks, instructions
    stacks = []
    a, b = [block.splitlines() for block in inputs]
    for line in a[::-1]:
        for i in range((len(line)+1)//4):
            char = line[i*4 + 1]
            if char.isnumeric():
                stacks.append([])
            elif char.isupper():
                stacks[i].append(char)
    b = [line.strip().split(" ") for line in b]
    instructions = [[int(val) for val in line[1::2]] for line in b]

def part_one():
    newStacks = [[element for element in line] for line in stacks]
    for line in instructions:
        num, off, on = line
        for _ in range(num):
            newStacks[on-1].append(newStacks[off-1].pop())
    result = ""
    for i in range(len(newStacks)):
        result += newStacks[i][-1]
    print(f"Part One = {result}")

def part_two():
    newStacks = [[element for element in line] for line in stacks]
    for line in instructions:
        num, off, on = line
        moving = []
        for _ in range(num):
            moving.insert(0, newStacks[off-1].pop())
        newStacks[on-1].extend(moving)
    result = ""
    for i in range(len(newStacks)):
        result += newStacks[i][-1]
    print(f"Part Two = {result}")
    pass

inputs = open_file()

format_data()

part_one()
part_two()
