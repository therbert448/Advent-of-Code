"""
Advent of Code
2022 Day 14

@author: Tom Herbert
"""

day = 14

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split(" -> ") for line in file.readlines()]
    return inputs

def format_data():
    global rocks, ymax, xmin, xmax
    rocks = set()
    for line in inputs:
        for i in range(len(line)-1):
            x1, y1 = [int(v) for v in line[i].split(",")]
            x2, y2 = [int(v) for v in line[i+1].split(",")]
            [x1, x2], [y1, y2] = sorted([x1, x2]), sorted([y1, y2])
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    rocks.add((x, y))
    ymax = max([y for (_, y) in rocks])
    xmin, xmax = min([x for (x, _) in rocks]), max([x for (x, _) in rocks])

def move_sand(current):
    d, dl, dr = [tuple(map(add, current, move)) for move in moves]
    if d not in rocks and d not in sand:
        return d
    elif dl not in rocks and dl not in sand:
        return dl
    elif dr not in rocks and dr not in sand:
        return dr
    else:
        return current

def add_sand():
    current = (500, 0)
    if current in sand:
        return True
    while True:
        nextPos = move_sand(current)
        if nextPos == current:
            break
        x, y = nextPos
        if (x < xmin or x > xmax or y >= ymax):
            return True
        current = nextPos
    sand.add(current)
    return False

def filled_tiles(ylimit):
    filled = {(500, 0)}
    for y in range(ylimit):
        for x in range(500 - y, 500 + y + 1):
            coords = (x, y)
            if coords in rocks:
                continue
            above = set([tuple(map(add, coords, up)) for up in upper])
            if any([a in filled for a in above]):
                filled.add(coords)
    return filled

def part_one():
    global sand
    sand = set()
    overflowing = False
    count = 0
    while not overflowing:
        overflowing = add_sand()
        if not overflowing:
            count +=1
    print(f"Part One = {len(sand)}")

def part_two():
    filled = filled_tiles(ymax+2)
    print(f"Part Two = {len(filled)}")

inputs = open_file()

format_data()

moves = [(0, 1), (-1, 1), (1, 1)]
upper = [(0, -1), (1, -1), (-1, -1)]
add = lambda a, b: a+b

part_one()
part_two()