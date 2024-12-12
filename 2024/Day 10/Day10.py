"""
Advent of Code
2024 Day 10

@author: Tom Herbert
"""
from time import time

day = 10

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    heights = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            val = int(char)
            if val in heights:
                heights[val].add((x, y))
            else:
                heights[val] = {(x, y)}
    return heights

heights = open_file(day)
t0 = time()
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

result = 0
trailheads = heights[0]
for start in trailheads:
    height = 0
    current = {start}
    while height < 9:
        newCurrent = set()
        for pos in current:
            for move in moves:
                nextPos = tuple(map(lambda a, b: a + b, pos, move))
                if nextPos in heights[height+1]:
                    newCurrent.add(nextPos)
        current = set(tup for tup in newCurrent)
        height += 1
    result += len(current)
print(f"Part Two = {result}")
t1 = time()
print(f"...took {round(t1-t0, 6)}s\n")

result = 0
trailheads = heights[0]
for start in trailheads:
    height = 0
    current = [start]
    while height < 9:
        newCurrent = []
        for pos in current:
            for move in moves:
                nextPos = tuple(map(lambda a, b: a + b, pos, move))
                if nextPos in heights[height+1]:
                    newCurrent.append(nextPos)
        current = [tup for tup in newCurrent]
        height += 1
    result += len(current)
print(f"Part One = {result}")
t2 = time()
print(f"...took {round(t2-t1, 6)}s")