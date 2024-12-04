"""
Advent of Code
2022 Day 22

@author: Tom Herbert
"""

day = 22
example = False

class Side:
    def __init__(self, pos, rocks):
        self.pos = pos
        self.rocks = rocks

def open_file():
    if example:
        filename = "test.txt"
    else:
        filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.read().split("\n\n")
    return inputs

def format_data():
    global grid, steps, rocks, start, xmax, ymax
    plan, path = inputs
    grid = set()
    rocks = set()
    start = None
    xmax, ymax = 0, 0
    for y, line in enumerate(plan.splitlines()):
        line = line.strip("\n")
        for x, char in enumerate(line):
            if char == ".":
                if start == None:
                    start = [(x+1, y+1), 0]
            elif char == "#":
                rocks.add((x+1, y+1))
            else:
                continue
            grid.add((x+1, y+1))
            if x+1 > xmax: xmax = x+1
            if y+1 > ymax: ymax = y+1
    path = path.replace("R", " R ").replace("L", " L ")
    steps = []
    for step in path.strip().split(" "):
        if step.isnumeric():
            steps.append(int(step))
        else:
            steps.append(step)

def add(a, b): return a+b

def wrap_part_one(start, idx):
    pos = start
    newIdx = (idx + 2) % len(dires)
    backwards = dires[newIdx]
    found = False
    while not found:
        newPos = tuple(map(add, pos, backwards))
        if newPos in grid:
            pos = newPos
        else:
            if pos in rocks:
                return start
            else:
                return pos

def wrap_part_two(side, start, idx):
    x, y = start
    positions = [y, N-x+1, N-y+1, x]
    pos = positions[idx]
    if idx == 0: pos = y
    nextSide, nextIdx = sides[side].wraps[idx]
    newPositions = [(1, pos), (N-pos+1, 1), (N, N-pos+1), (pos, N)]
    newPos = newPositions[nextIdx]
    if newPos in sides[nextSide].rocks:
        return side, start, idx
    else:
        return nextSide, newPos, nextIdx

def turn(step, idx):
    idx += turns[step]
    idx = idx % len(dires)
    return idx

def take_steps(step, pos, idx, side = 0):
    for _ in range(step):
        facing = dires[idx]
        newPos = tuple(map(add, pos, facing))
        if side:
            if newPos in grid and newPos not in sides[side].rocks:
                pos = newPos
                continue
            elif newPos in sides[side].rocks:
                return side, pos, idx
            else:
                side, pos, idx = wrap_part_two(side, pos, idx)
        else:
            if newPos in grid and newPos not in rocks:
                pos = newPos
                continue
            elif newPos in rocks:
                return pos
            else:
                pos = wrap_part_one(pos, idx)
    if side: 
        return side, pos, idx
    else:
        return pos

def make_moves(partTwo = False):
    if partTwo:
        side, pos, idx = start
    else:
        pos, idx = start
    for step in steps:
        if step in turns:
            idx = turn(step, idx)
        else:
            if partTwo:
                side, pos, idx = take_steps(step, pos, idx, side)
            else:
                pos = take_steps(step, pos, idx)
    if partTwo:
        return side, pos, idx
    else:
        return pos, idx

def find_sides():
    global sides
    side = 0
    sides = {}
    for top in range((ymax+1)//N):
        for left in range((xmax+1)//N):
            pos = (left*N, top*N)
            if (pos[0]+1, pos[1]+1) not in grid:
                continue
            side += 1
            newRocks = set()
            for y in range(N):
                for x in range(N):
                    if (x+(left*N)+1, y+(top*N)+1) in rocks:
                        newRocks.add((x+1, y+1))
            sides[side] = Side(pos, newRocks)

def define_wraps(): #Hard code moving from side to side
    if example:
        sides[1].wraps = [(6, 2), (4, 1), (3, 1), (2, 1)]
        sides[2].wraps = [(3, 0), (5, 3), (6, 3), (1, 1)]
        sides[3].wraps = [(4, 0), (5, 0), (2, 2), (1, 0)]
        sides[4].wraps = [(6, 1), (5, 1), (3, 2), (1, 3)]
        sides[5].wraps = [(6, 0), (2, 3), (3, 3), (4, 3)]
        sides[6].wraps = [(1, 2), (2, 0), (5, 2), (4, 2)]
    else:
        sides[1].wraps = [(2, 0), (3, 1), (4, 0), (6, 0)]
        sides[2].wraps = [(5, 2), (3, 2), (1, 2), (6, 3)]
        sides[3].wraps = [(2, 3), (5, 1), (4, 1), (1, 3)]
        sides[4].wraps = [(5, 0), (6, 1), (1, 0), (3, 0)]
        sides[5].wraps = [(2, 2), (6, 2), (4, 2), (3, 3)]
        sides[6].wraps = [(5, 3), (2, 1), (1, 1), (4, 3)]

def new_grid():
    global grid
    grid = set((x, y) for y in range(1, N+1) for x in range(1, N+1))

def part_one(idx = 0):
    pos, idx = make_moves()
    score = (pos[1] * 1000) + (pos[0] * 4) + idx 
    print(f"Part One = {score}")

def part_two():
    find_sides()
    define_wraps()
    new_grid()
    side, pos, idx = make_moves(True)
    coords = tuple(map(add, sides[side].pos, pos))
    score = (coords[1] * 1000) + (coords[0] * 4) + idx 
    print(f"Part Two = {score}")

inputs = open_file()

format_data()

dires = [(1, 0), (0, 1), (-1, 0), (0, -1)]
turns = {"R": 1, "L": -1}

part_one()

start = [1, (1, 1), 0]
N = int(pow(len(grid)//6, 0.5))

part_two()