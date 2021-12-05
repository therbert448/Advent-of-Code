"""
Advent of Code
2021 Day 5

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [line.split(" ->") for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global lines
    lines = [[[int(v) for v in p.split(",")] for p in l] for l in inputs]

def add_non_diag(line):
    start, end = line
    if start[0] != end[0] and start[1] != end[1]:
        return #diagonal line, ignore for part one
    elif start[0] == end[0]: #vertical line
        x = start[0]
        y = [start[1], end[1]]
        y1, y2 = [min(y), max(y)] #make sure it's ascending
        for i in range(y1, y2+1):
            point = (x, i)
            if point in grid:
                grid[point] += 1
            else:
                grid[point] = 1
    elif start[1] == end[1]: #horizontal line
        x = [start[0], end[0]]
        x1, x2 = [min(x), max(x)] #make sure it's ascending
        y = start[1]
        for i in range(x1, x2+1):
            point = (i, y)
            if point in grid:
                grid[point] += 1
            else:
                grid[point] = 1

def add_diag(line):
    start, end = line
    if start[0] == end[0] or start[1] == end[1]:
        return #vertical or horizontal, already counted in grid
    x = [start[0], end[0]]
    y = [start[1], end[1]]
    xLength = abs(x[1] - x[0])
    yLength = abs(y[1] - y[0])
    if xLength != yLength:
        return #not a 45 degree diagonal
    dx = (x[1] - x[0])/xLength #ascending or descending
    dy = (y[1] - y[0])/yLength
    for i in range(xLength+1):
        xi = x[0] + (dx * i)
        yi = y[0] + (dy * i)
        point = (xi, yi)
        if point in grid:
            grid[point] += 1
        else:
            grid[point] = 1

def part_one():
    global grid #dict for all points with a vent as keys, values are vent count
    grid = {}
    for line in lines:
        add_non_diag(line)
    overlap = sum([1 for count in grid.values() if count > 1])
    print(f"Part One = {overlap}")

def part_two():
    for line in lines:
        add_diag(line)
    overlap = sum([1 for count in grid.values() if count > 1])
    print(f"Part Two = {overlap}")

day = 5
inputs = open_file()

format_data()

part_one()
part_two()