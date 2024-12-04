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
        for i, char in enumerate(line[1::4]):
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
    result = "".join(stack[-1] for stack in newStacks)
    print(f"Part One = {result}")

def part_two():
    newStacks = [[element for element in line] for line in stacks]
    for line in instructions:
        num, off, on = line
        for i in range(num, 0, -1):
            newStacks[on-1].append(newStacks[off-1].pop(-i))
    result = "".join(stack[-1] for stack in newStacks)
    print(f"Part Two = {result}")

inputs = open_file()

format_data()

part_one()
part_two()
