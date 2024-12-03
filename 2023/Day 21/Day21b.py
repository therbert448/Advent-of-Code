"""
Advent of Code
2023 Day 21

@author: Tom Herbert

Solves the simultaneous quadratic equations using a few formulae
"""

day = 21

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    rocks = set()
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                rocks.add((x, y))
            if char == "S":
                start = (x, y)
    width = x
    return rocks, start, width+1

def steps(N, extend=False):
    current = [start]
    even, odd = {start,}, set()
    for i in range(N):
        newCurrent = []
        i += 1
        for pos in current:
            x, y = pos
            newPos = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for nPos in newPos:
                nx, ny = nPos
                modx = nx % width
                mody = ny % width
                if (modx, mody) in rocks:
                    continue
                outOfGrid = (nx < 0 or ny < 0 or nx >= width or ny >= width)
                if not extend and outOfGrid:
                    continue
                if i % 2:
                    if nPos not in odd:
                        odd.add(nPos)
                        newCurrent.append(nPos)
                else:
                    if nPos not in even:
                        even.add(nPos)
                        newCurrent.append(nPos)
        current = newCurrent
    if i % 2:
        return len(odd)
    else:
        return len(even)

def quadratic(repTiles, rem):
    y = [steps(rem, True), steps(rem+width, True), steps(rem+2*width, True)]
    x = [0, 1, 2]
    c = (y[2] - 2*y[1] + y[0])//(x[2]**2 - 2 * (x[1]**2) + x[0]**2)
    b = y[2] - y[1] - c * (x[2]**2 - x[1]**2)
    a = y[0] - b * x[0] - c * x[0]**2
    result = a + b * repTiles + c * repTiles ** 2
    return result

def part_one(N):
    result = steps(N, width)
    print(f"Part One = {result}")

def part_two(N = 26501365):
    repeatedTiles = N//width
    remainder = N % width
    result = quadratic(repeatedTiles, remainder)
    print(f"Part Two = {result}")

rocks, start, width = open_file(day)

part_one(64)
part_two()