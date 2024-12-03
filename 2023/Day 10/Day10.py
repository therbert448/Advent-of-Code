"""
Advent of Code
2023 Day 10

@author: Tom Herbert
"""

day = 10

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    pipes = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == ".":
                continue
            elif char == "S":
                start = (x, y)
            pipes[(x, y)] = char
    return pipes, start

def step(pos, dire):
    x, y = pos
    nextPos = {"left": (x-1, y), "right": (x+1, y), 
               "up": (x, y-1), "down": (x, y+1)}
    if nextPos[dire] in pipes and pipes[nextPos[dire]] in moves[dire]:
        return (nextPos[dire], moves[dire][pipes[nextPos[dire]]])
    else:
        return False

def navigate():
    ds = ["left", "right", "up", "down"]
    paths = [step(start, d) for d in ds if step(start, d)]
    dires = tuple(sorted([d for d in ds if step(start, d)]))
    pipes[start] = sides[dires]
    order = [start]
    current = paths[0]
    count = 1 
    while current:
        if pipes[current[0]] in ("7", "F", "J", "L"):
            order.append(current[0])
        nextPos, dire = step(*current)
        count += 1
        if nextPos == start:
            order.append(nextPos)
            return order
        current = (nextPos, dire)

def enclosed(path):
    area, perimeter = 0, 0
    for i, point1 in enumerate(path[:-1]):
        point2 = path[i+1]
        x1, y1 = point1
        x2, y2 = point2
        dist = abs(x2 - x1) + abs(y2 - y1)
        area += (x1 * y2) - (y1 * x1)
        perimeter += dist
    internal = abs(area) - (perimeter//2) + 1
    return perimeter, internal

def part_one_and_two():
    path = navigate()
    perimeter, internal = enclosed(path)
    print(f"Part One = {perimeter//2}")
    print(f"Part Two = {internal}")
    return path

moves = {"up": {"|": "up", "7": "left", "F": "right"},
         "right": {"-": "right", "7": "down", "J": "up"},
         "down": {"|": "down", "J": "left", "L": "right"},
         "left": {"-": "left", "L": "up", "F": "down"}}

sides = {('left', 'right'): '-', ('down', 'up'): '|', ('left', 'up'): 'J',
         ('down', 'left'): '7', ('down', 'right'): 'F', ('right', 'up'): 'L'}

pipes, start = open_file(day)

part_one_and_two()