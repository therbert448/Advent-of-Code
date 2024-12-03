"""
Advent of Code
2023 Day 17

@author: Tom Herbert
"""

day = 17

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [[int(v) for v in l.strip()] for l in file.readlines()]
    weights = {}
    for y, line in enumerate(inputs):
        for x, val in enumerate(line):
            weights[(x, y)] = val
    return weights, [x, y]

def next_steps(position, partTwo):
    coords, dire, count = position
    newPositions = set()
    if not dire:
        dires = moves.keys()
    elif (not partTwo and count == 3) or (partTwo and count == 10):
        dires = turns[dire]
    elif (not partTwo) or (partTwo and 4 <= count < 10):
        dires = turns[dire] + [dire]
    else: 
        dires = [dire]
    for move in dires:
        newCoords = tuple(map(lambda a, b: a+b, coords, moves[move]))
        x, y = newCoords
        if x < 0 or y < 0 or x > maxes[0] or y > maxes[1]:
            continue
        if move == dire:
            newCount = count + 1
        else:
            newCount = 1
        newPositions.add((newCoords, move, newCount))
    return newPositions

def navigate(partTwo = False):
    global steps
    startPos = (0, 0)
    endPos = tuple(maxes)
    start = (startPos, None, None)
    steps = {start: 0}
    current = {start,}
    ends = []
    while current:
        newCurrent = set()
        for pos in current:
            coords, dire, count = pos
            value = steps[pos]
            nextMoves = next_steps(pos, partTwo)
            for newPos in nextMoves:
                newCoords, *_ = newPos
                newValue = value + weights[newCoords]
                if newPos in steps and steps[newPos] <= newValue:
                    continue
                if newCoords == endPos: 
                    ends.append(newValue)
                    continue
                steps[newPos] = newValue
                newCurrent.add(newPos)
        current = newCurrent
    return min(ends)

def part_one_and_two():
    result = navigate()
    print(f"Part One = {result}")
    result = navigate(True)
    print(f"Part Two = {result}")

moves = {"r": (1, 0), "d": (0, 1), "l": (-1, 0), "u": (0, -1)}
turns = {"r": ["u", "d"], "l": ["u", "d"], "u": ["l", "r"], "d": ["l", "r"]}

weights, maxes = open_file(day)       

part_one_and_two()