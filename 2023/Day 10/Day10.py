"""
Advent of Code
2023 Day 10

@author: Tom Herbert
"""
import matplotlib.path as p

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
    return pipes, start, x, y

def step(pos, dire, pipes, moves):
    x, y = pos
    nextPos = {"left": (x-1, y), "right": (x+1, y), 
               "up": (x, y-1), "down": (x, y+1)}
    if nextPos[dire] in pipes and pipes[nextPos[dire]] in moves[dire]:
        return (nextPos[dire], moves[dire][pipes[nextPos[dire]]])
    else:
        return False

def navigate(ps, start, ms):
    ds = ["left", "right", "up", "down"]
    paths = [step(start, d, ps, ms) for d in ds if step(start, d, ps, ms)]
    pathSet = [set((path[0],)) for path in paths]
    order = [paths[0][0], start, paths[1][0]]
    crossed = False
    while not crossed:
        newPaths = []
        for i, path in enumerate(paths):
            nextPath = step(*path, pipes, moves)
            pathSet[i].add(nextPath[0])
            if i:
                order.append(nextPath[0])
            else:
                order.insert(0, nextPath[0])
            newPaths.append(nextPath)
        if pathSet[0] & pathSet[1]:
            crossed = True
            return len(pathSet[0]), order[1:]
        paths = newPaths

def enclosed(path, pipes, xMax, yMax):
    closedPoints = set()
    pipePath = p.Path(path)
    for x in range(xMax+1):
        for y in range(yMax+1):
            if (x, y) in path:
                continue
            if pipePath.contains_point((x, y)):
                closedPoints.add((x, y))
    return len(closedPoints)

def part_one(pipes, start, moves):
    result, path = navigate(pipes, start, moves)
    print(f"Part One = {result}")
    return path

def part_two(path, pipes, x, y):
    print(f"Part Two = {enclosed(path, pipes, x, y)}")

moves = {"up": {"|": "up", "7": "left", "F": "right"},
         "right": {"-": "right", "7": "down", "J": "up"},
         "down": {"|": "down", "J": "left", "L": "right"},
         "left": {"-": "left", "L": "up", "F": "down"}}

pipes, start, x, y = open_file(day)

path = part_one(pipes, start, moves)
part_two(path, pipes, x, y)