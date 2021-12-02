"""
Advent of Code
2021 Day 2

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def format_data():
    global commands
    commands = [line.strip().split() for line in inputs]

def part_one():
    x, y = [0, 0]
    for line in commands:
        direction, value = line
        if direction == "forward":
            x += int(value)
        if direction == "down":
            y += int(value)
        if direction == "up":
            y -= int(value)
    print(f"Part One = {x*y}")

def part_two():
    x, y, a = [0, 0, 0]
    for line in commands:
        direction, value = line
        if direction == "forward":
            x += int(value)
            y += int(value) * a
        if direction == "down":
            a += int(value)
        if direction == "up":
            a -= int(value)
    print(f"Part Two = {x*y}")

day = 2
inputs = open_file()

format_data()

part_one()
part_two()