"""
Advent of Code
2022 Day 10

@author: Tom Herbert
"""

day = 10

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(" ") for line in file.readlines()]
    return inputs

def print_grid():
    w, h = 40, 6
    stringOut = ""
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in grid:
                line += "#"
            else:
                line += " "
        stringOut += line + "\n"
    print(stringOut)

def CRT():
    global grid
    strength, cycle, x = 0, 0, 1
    grid = set()
    for line in inputs:
        for i, v in enumerate(line):
            coords = (cycle % 40, cycle//40)
            if cycle % 40 in (x-1, x, x+1):
                grid.add(coords)
            cycle += 1
            if cycle % 40 == 20:
                strength += cycle * x
            if i == 1:
                x += int(v)
    print(f"Part One = {strength}")
    print("Part Two =")
    print_grid()

inputs = open_file()

CRT()