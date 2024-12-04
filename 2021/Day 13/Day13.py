"""
Advent of Code
2021 Day 13

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().split("\n\n")
    file.close()
    return inputs

def format_data():
    global dots, folds
    dots = set()
    folds = []
    d, f = inputs
    for line in d.strip().splitlines():
        x, y = line.strip().split(",")
        dots.add((int(x), int(y)))
    for line in f.strip().splitlines():
        xy, val = line.strip().split("=")
        folds.append((xy[-1], int(val)))

def fold(grid, line):
    newGrid = set()
    xy, val = line
    if xy == "x":
        idx = 0
    else:
        idx = 1
    for pos in grid:
        newPos = list(pos)
        if newPos[idx] > val:
            newXy = newPos[idx] - 2 * (newPos[idx] - val)
            newPos[idx] = newXy
        newGrid.add(tuple(newPos))
    return newGrid

def print_grid(grid):
    string = ""
    xmax, ymax = 0, 0
    for pos in grid:
        if pos[0] > xmax:
            xmax = pos[0]
        if pos[1] > ymax:
            ymax = pos[1]
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if (x, y) in grid:
                string += "#"
            else:
                string += " "
        string += "\n"
    print(string)

def part_one():
    newDots = set(dots)
    for line in folds[:1]:
        newDots = fold(newDots, line)
    print(f"Part One = {len(newDots)}")

def part_two():
    newDots = set(dots)
    for line in folds:
        newDots = fold(newDots, line)
    print("Part Two =")
    print_grid(newDots)

day = 13
inputs = open_file()

format_data()

part_one()
part_two()