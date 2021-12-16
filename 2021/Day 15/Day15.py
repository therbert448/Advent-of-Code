"""
Advent of Code
2021 Day 15

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.readlines()
    file.close()
    return inputs

def format_data():
    global grid, end
    grid = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = int(char)
    end = (x, y)

def neighbours(pos, grid):
    add = lambda a, b: a + b
    adjacent = [(1,0), (-1,0), (0,1), (0,-1)]
    neighs = [tuple(map(add, adj, pos)) for adj in adjacent]
    for n in list(neighs):
        if n not in grid:
            neighs.remove(n)
    return neighs

def new_grid():
    global newGrid, newEnd
    newGrid = dict(grid)
    xMax, yMax = end
    newEnd = (((xMax+1)*5)-1, ((yMax+1)*5)-1)
    for x in range(5):
        for y in range(5):
            if x == 0 and y == 0:
                continue
            increase = x + y
            for pos in grid:
                xPos, yPos = pos
                newPos = (xPos + (xMax+1)*x, yPos + (yMax+1)*y)
                newGrid[newPos] = grid[pos] + increase
                if newGrid[newPos] > 9:
                    newGrid[newPos] = newGrid[newPos] % 9

def part_one():
    mins = {}
    pos = (0, 0)
    mins = {pos: 0}
    current = {(0, 0)}
    while current:
        nextPos = set()
        for pos in current:
            neighs = neighbours(pos, grid)
            for n in neighs:
                total = mins[pos] + grid[n]
                if n not in mins:
                    nextPos.add(n)
                    mins[n] = total
                elif total < mins[n]:
                    nextPos.add(n)
                    mins[n] = total
        current = set(nextPos)
    print(f"Part One = {mins[end]}")

def part_two():
    new_grid()
    mins = {}
    pos = (0, 0)
    mins = {pos: 0}
    current = {(0, 0)}
    while current:
        nextPos = set()
        for pos in current:
            neighs = neighbours(pos, newGrid)
            for n in neighs:
                total = mins[pos] + newGrid[n]
                if n not in mins:
                    nextPos.add(n)
                    mins[n] = total
                elif total < mins[n]:
                    nextPos.add(n)
                    mins[n] = total
        current = set(nextPos)
    print(f"Part Two = {mins[newEnd]}")

day = 15
inputs = open_file()

format_data()

part_one()
part_two()