"""
Advent of Code
2021 Day 9

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = [[int(val) for val in line.strip()] for line in file.readlines()]
    file.close()
    return inputs

def format_data():
    global grid
    grid = {}
    for y, line in enumerate(inputs):
        for x, val in enumerate(line):
            grid[(x, y)] = val

def neighbours(pos):
    x, y = pos
    neighs = {}
    if x-1 >= 0:
        neighs[(x-1, y)] = grid[(x-1, y)]
    if x+1 < xmax:
        neighs[(x+1, y)] = grid[(x+1, y)]
    if y-1 >= 0:
        neighs[(x, y-1)] = grid[(x, y-1)]
    if y+1 < ymax:
        neighs[(x, y+1)] = grid[(x, y+1)]
    return neighs

def add_pos(pos, basin):
    checked.add(pos)
    basin.append(pos)
    neighs = neighbours(pos)
    for n, val in neighs.items():
        if n in checked or val == 9:
            continue
        basin = add_pos(n, basin)
    return basin

def part_one():
    count = 0
    for pos, val in grid.items():
        neighs = neighbours(pos)
        if all([n > val for n in neighs.values()]):
            count += val + 1
    print(f"Part One = {count}")

def part_two():
    global checked
    checked = set()
    basins = [] #collect length of each basin
    for pos, val in grid.items():
        if pos in checked or val == 9:
            continue
        basin = []
        basin = add_pos(pos, basin)
        basins.append(len(basin))
    basins.sort(reverse = True)
    product = 1
    for basin in basins[:3]:
        product *= basin
    print(f"Part Two = {product}")

day = 9
inputs = open_file()
xmax, ymax = len(inputs[0]), len(inputs)

format_data()

part_one()
part_two()