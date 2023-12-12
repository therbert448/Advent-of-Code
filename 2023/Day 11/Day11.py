"""
Advent of Code
2023 Day 11

@author: Tom Herbert
"""

day = 11

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    galaxies, rows, columns = set(), set(), set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.add((x, y))
                rows.add(y)
                columns.add(x)
    return galaxies, rows, columns

def expand(galaxies, rows, columns, N = 1):
    newGals = set()
    yCount = 0
    xMax, yMax = max([g[0] for g in galaxies]), max([g[1] for g in galaxies])
    for y in range(yMax+1):
        if y not in rows:
            yCount += N
        xCount = 0
        for x in range(xMax+1):
            if x not in columns:
                xCount += N
            if (x, y) in galaxies:
                newGals.add((x + xCount, y + yCount))
    return newGals
    
def distances(galaxies):
    dists = []
    for i, galA in enumerate(sorted(galaxies)):
        for galB in sorted(galaxies)[i+1:]:
            dist = sum(map(lambda a, b: abs(a-b), galA, galB))
            dists.append(dist)
    return sum(dists)

def part_one(galaxies, rows, columns):
    galaxies = expand(galaxies, rows, columns)
    result = distances(galaxies)
    print(f"Part One = {result}")

def part_two(galaxies, rows, columns):
    N = 1_000_000
    galaxies = expand(galaxies, rows, columns, N-1)
    result = distances(galaxies)
    print(f"Part Two = {result}")

galaxies, rows, columns = open_file(day)

part_one(galaxies, rows, columns)
part_two(galaxies, rows, columns)