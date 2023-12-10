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
    return pipes, start, x, y

def step(pos, dire, pipes, moves):
    x, y = pos
    nextPos = {"left": (x-1, y), "right": (x+1, y), 
               "up": (x, y-1), "down": (x, y+1)}
    if nextPos[dire] in pipes and pipes[nextPos[dire]] in moves[dire]:
        return (nextPos[dire], moves[dire][pipes[nextPos[dire]]])
    else:
        return False

def navigate(ps, start, ms, sides):
    ds = ["left", "right", "up", "down"]
    paths = [step(start, d, ps, ms) for d in ds if step(start, d, ps, ms)]
    dires = tuple(sorted([d for d in ds if step(start, d, ps, ms)]))
    ps[start] = sides[dires]
    order = [start, paths[0][0]]
    dire = paths[0][1]
    ended = False
    while not ended:
        current = order[-1]
        nextPos, dire = step(current, dire, pipes, moves)
        if nextPos == start:
            ended = True
            return order, ps
        order.append(nextPos)

def enclosed(path, pipes, xMax, yMax):
    inner = set()
    for y in range(yMax+1):
        for x in range(xMax+1):
            x = xMax - x
            if (x, y) in path:
                continue
            if x in (0, xMax) or y in (0, yMax):
                continue
            if (x+1, y) not in inner and (x+1, y) not in path:
                continue
            if (x, y-1) not in inner and (x, y-1) not in path:
                continue
            if (x+1, y) in inner or (x, y-1) in inner:
                inner.add((x, y))
                continue
            string = ""
            for xi in range(x+1, xMax+1):
                if (xi, y) in path:
                    if pipes[(xi, y)] != '-':
                        string += pipes[(xi, y)]
            string = string.replace('L7', '|').replace('FJ', '|')
            if string.count('|') % 2:
                inner.add((x, y))
    return len(inner)

def part_one(pipes, start, moves, sides):
    path, pipes = navigate(pipes, start, moves, sides)
    print(f"Part One = {len(path)//2}")
    return path, pipes

def part_two(path, pipes, x, y):
    print(f"Part Two = {enclosed(path, pipes, x, y)}")

moves = {"up": {"|": "up", "7": "left", "F": "right"},
         "right": {"-": "right", "7": "down", "J": "up"},
         "down": {"|": "down", "J": "left", "L": "right"},
         "left": {"-": "left", "L": "up", "F": "down"}}

sides = {('left', 'right'): '-', ('down', 'up'): '|', ('left', 'up'): 'J',
         ('down', 'left'): '7', ('down', 'right'): 'F', ('right', 'up'): 'L'}

pipes, start, x, y = open_file(day)

path, pipes = part_one(pipes, start, moves, sides)
part_two(set(path), pipes, x, y)