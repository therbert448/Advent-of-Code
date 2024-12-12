"""
Advent of Code
2024 Day 06

@author: Tom Herbert
"""
from time import time

day = 6

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    obstacles = set()
    for y, line in enumerate(inputs):
        for x, point in enumerate(line):
            if point == "#":
                obstacles.add((x, y))
            elif point != ".":
                guard = ((x, y), point)
    return obstacles, guard, x, y

def part_one(obstacles, guard, xmax, ymax, turns, steps):
    inMap = True
    visited = {guard[0]}
    while inMap:
        newPos = tuple(map(lambda a, b: a+b, guard[0], steps[guard[1]]))
        newDire = guard[1]
        if newPos in obstacles:
            newDire = turns[guard[1]]
            newPos = guard[0]
        newx, newy = newPos
        if (newx < 0 or newx > xmax) or (newy < 0 or newy > ymax):
            inMap = False
            break
        visited.add(newPos)
        guard = (newPos, newDire)
    print(f"Part One = {len(visited)}")
    return visited

def part_two(obstacles, guard, xmax, ymax, turns, steps, visited):
    startPos = tuple(v for v in guard[0])
    startDire = guard[1]
    visited.remove(startPos)
    count = 0
    for coord in visited:
        guard = (startPos, startDire)
        inMap = True
        newObstacles = {v for v in obstacles}
        newObstacles.add(coord)
        newVisited = {guard}
        while inMap:
            newPos = tuple(map(lambda a, b: a+b, guard[0], steps[guard[1]]))
            newDire = guard[1]
            if newPos in newObstacles:
                newDire = turns[guard[1]]
                newPos = guard[0]
            newx, newy = newPos
            if (newx < 0 or newx > xmax) or (newy < 0 or newy > ymax):
                inMap = False
                break
            guard = (newPos, newDire)
            if guard in newVisited:
                count += 1
                break
            else:
                newVisited.add(guard)
    print(f"Part Two = {count}")

obstacles, guard, xmax, ymax = open_file(day)

turns = {"^": ">", ">":"v", "v":"<", "<": "^"}
steps = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<":(-1, 0)}
t0 = time()
visited = part_one(obstacles, guard, xmax, ymax, turns, steps)
t1 = time()
print(t1-t0)
part_two(obstacles, guard, xmax, ymax, turns, steps, visited)
t2 = time()
print(t2-t1)