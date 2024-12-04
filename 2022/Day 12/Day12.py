"""
Advent of Code
2022 Day 12

@author: Tom Herbert
"""

day = 12

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.readlines()
    return inputs

def format_data():
    global grid, start, end
    grid = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line.strip()):
            coords = (x, y)
            if char.isupper() and char == "S":
                start = coords
                char = "a"
            elif char.isupper():
                end = coords
                char = "z"
            grid[coords] = ord(char) - 97

def possible_moves(pos):
    level = grid[pos]
    newPositions = [tuple(map(lambda a, b: a+b, pos, step)) for step in steps]
    available = []
    for newPos in newPositions:
        if newPos not in grid:
            continue
        elif grid[newPos] > level + 1:
            continue
        available.append(newPos)
    return available

def make_moves(positions):
    nextPositions = []
    for position in positions:
        if position == end:
            continue
        available = possible_moves(position)
        for newPos in available:
            if newPos in states and states[position] + 1 >= states[newPos]:
                continue
            states[newPos] = states[position] + 1
            nextPositions.append(newPos)
    if nextPositions:
        make_moves(nextPositions)

def part_one():
    global states
    current = [start]
    states = {start: 0}
    make_moves(current)
    print(f"Part One = {states[end]}")

def part_two():
    global states
    current = [coords for coords in grid if grid[coords] == 0]
    states = {coords: 0 for coords in current}
    make_moves(current)
    print(f"Part Two = {states[end]}")

inputs = open_file()

format_data()

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

part_one()
part_two()