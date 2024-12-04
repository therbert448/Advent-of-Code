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
    if d not in rocks and d not in sand and d[1] != ymax + 2:
        return d
    elif dl not in rocks and dl not in sand and dl[1] != ymax + 2:
        return dl
    elif dr not in rocks and dr not in sand and dr[1] != ymax + 2:
        return dr
    else:
        return current

def add_sand(partTwo = False):
    current = (500, 0)
    if current in sand:
        return True
    while True:
        nextPos = move_sand(current)
        if nextPos == current:
            break
        x, y = nextPos
        if (x < xmin or x > xmax or y >= ymax) and not partTwo:
            return True
        current = nextPos
    sand.add(current)
    return False

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

"""
Generic solution to Part Two using the code from Part One.
I initially got the answer using the shortcut below, which runs much faster.
I wrote this in for completeness as a solution that will work for all possible
inputs.
"""
def part_two(): 
    global sand
    sand = set()
    overflowing = False
    count = 0
    while not overflowing:
        overflowing = add_sand(True)
        if not overflowing:
            count += 1
    print(f"Part Two = {len(sand)}")

"""
My initial solution, which is conveniently a shortcut, at least for my inputs
This calculates the maximum space the sand could occupy in part 2, which is a 
triangle of height ymax+2 and width 2(ymax+1)+1 and area = (ymax+2)^2, then 
subtracts all the rocks and any tile that would be impossible for sand to ever 
occupy.
This is not a generic solution and may not work for all inputs.
"""
def blocked_tiles(ylimit):
    blocked = set(rocks)
    for y in range(ylimit):
        for x in range(500 - y, 500 + y + 1):
            coords = (x, y)
            if coords in blocked:
                continue
            above = set([tuple(map(add, coords, up)) for up in upper])
            if all([a in blocked for a in above]):
                blocked.add(coords)
    return blocked

def part_two_fast():
    ylimit = ymax+2
    totalTiles = ylimit ** 2
    blocked = blocked_tiles(ylimit)
    print(f"Part Two = {totalTiles - len(blocked)}")

"""
A better, more complete and generic version of the shortcut from my initial 
solution.
Instead of finding all the inaccessible tiles, work down from (500, 0) to find
all the tiles that must have sand in them for (500, 0) to be blocked
"""
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

def part_two_fast_better():
    ylimit = ymax+2
    filled = filled_tiles(ylimit)
    print(f"Part Two = {len(filled)}")

inputs = open_file()

format_data()

moves = [(0, 1), (-1, 1), (1, 1)]
upper = [(0, -1), (1, -1), (-1, -1)]
add = lambda a, b: a+b

part_one()
#part_two()
#part_two_fast()
part_two_fast_better()