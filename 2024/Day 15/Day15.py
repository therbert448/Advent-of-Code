"""
Advent of Code
2024 Day 15

@author: Tom Herbert
"""
from time import time

day = 15

def open_file(day):
    #filename = "test2.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        maze, moves = file.read().split("\n\n")
    walls, startBoxes = set(), set()
    maze = [line.strip() for line in maze.splitlines()]
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "O":
                startBoxes.add((x, y))
            elif char == "@":
                startRobot = (x, y)
    moves = "".join(moves.splitlines())
    return walls, startBoxes, startRobot, moves, x, y

def open_file2(day):
    #filename = "test2.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        maze, moves = file.read().split("\n\n")
    walls, startBoxes, pairBoxes = set(), set(), set()
    maze = [line.strip() for line in maze.splitlines()]
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((2*x, y))
                walls.add(((2*x) + 1, y))
            elif char == "O":
                startBoxes.add((2*x, y))
                startBoxes.add(((2*x) + 1, y))
                pairBoxes.add(((2*x, y), ((2*x) + 1, y)))
            elif char == "@":
                startRobot = (2*x, y)
    moves = "".join(moves.splitlines())
    return walls, startBoxes, pairBoxes, startRobot, moves, 2*x, y

def plot_grid(pairs, walls, robot):
    pairDict = {}
    for pair in pairs:
        l, r = pair
        pairDict[l] = "["
        pairDict[r] = "]"
    for y in range(ymax+1):
        line = ""
        for x in range(xmax+1):
            if (x, y) in walls:
                line += "#"
            elif (x, y) == robot:
                line += "@"
            elif (x, y) in pairDict:
                line += pairDict[(x, y)]
            else:
                line += "."
        print(line)

t0 = time()
walls, startBoxes, startRobot, moves, xmax, ymax = open_file(day)

steps = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
add = lambda a, b: a + b

robot = startRobot
boxes = set(tup for tup in startBoxes)
for move in moves:
    step = steps[move]
    nextPos = tuple(map(add, robot, step))
    current = nextPos
    empty = ()
    while not empty:
        if current in walls:
            break
        if current not in boxes:
            empty = current
            break
        current = tuple(map(add, current, step))
    if empty:
        if nextPos in boxes:
            boxes.remove(nextPos)
            boxes.add(empty)
        robot = nextPos
score = 0
for box in boxes:
    x, y = box
    score += (100 * y) + x
print(f"Part One = {score}")
t1 = time()
print(f"...took {round(t1-t0, 6)}s")

walls, startBoxes, pairBoxes, startRobot, moves, xmax, ymax = open_file2(day)
robot = startRobot
boxes, pairs = set(tup for tup in startBoxes), set(tup for tup in pairBoxes)
for i, move in enumerate(moves):
    step = steps[move]
    nextPos = tuple(map(add, robot, step))
    if nextPos in walls: continue
    if nextPos not in boxes:
        robot = nextPos
        continue
    r = tuple(map(add, nextPos, steps[">"])) 
    l = tuple(map(add, nextPos, steps["<"]))
    if (l, nextPos) in pairs:
        pair = (l, nextPos)
    elif (nextPos, r) in pairs:
        pair = (nextPos, r)
    toMove = {pair}
    boxMoves = {}
    moveable = False
    while not moveable:
        newToMove = set(pair for pair in toMove)
        for pair in toMove:
            l, r = pair
            lmove, rmove = tuple(map(add, l, step)), tuple(map(add, r, step))
            if lmove in walls or rmove in walls:
                boxMoves = {}
                break
            boxMoves[pair] = (lmove, rmove)
            if lmove in boxes:
                r = tuple(map(add, lmove, steps[">"])) 
                l = tuple(map(add, lmove, steps["<"]))
                if (l, lmove) in pairs:
                    newPair = (l, lmove)
                elif (lmove, r) in pairs:
                    newPair = (lmove, r)
                newToMove.add(newPair)
            if rmove in boxes:
                r = tuple(map(add, rmove, steps[">"])) 
                l = tuple(map(add, rmove, steps["<"]))
                if (l, rmove) in pairs:
                    newPair = (l, rmove)
                elif (rmove, r) in pairs:
                    newPair = (rmove, r)
                newToMove.add(newPair)
            newToMove.remove(pair)
        if not boxMoves:
            break
        if newToMove:
            toMove = set(pair for pair in newToMove)
        else:
            moveable = True
    if moveable:
        for boxMove, newPair in boxMoves.items():
            if boxMove not in boxMoves.values():
                pairs.remove(boxMove)
            pairs.add(newPair)
        boxes = set()
        for pair in pairs:
            l, r = pair
            boxes.add(l), boxes.add(r)
        robot = nextPos
#plot_grid(pairs, walls, robot)
score = 0
for pair in pairs:
    (x, y), (_, _) = pair
    score += (100 * y) + x
print(f"Part Two = {score}")
t2 = time()
print(f"...took {round(t2-t1, 6)}s")