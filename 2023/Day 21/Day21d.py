"""
Advent of Code
2023 Day 21

@author: Tom Herbert

Using sequences from Day 9
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
    width = x
    return rocks, width+1

def steps(N, start, extend=False):
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

def part_one(N):
    start = (width//2, width//2)
    result = steps(N, start)
    print(f"Part One = {result}")

def part_two(N = 26501365):
    start = (width//2, width//2)
    rem = N % width
    Ncheck = 4
    xs = [rem + i*width for i in range(Ncheck)]
    y = [steps(x, start, True) for x in xs]
    dy = [y[i+1]-y[i] for i in range(Ncheck-1)]
    dy2 = [dy[i+1]-dy[i] for i in range(Ncheck-2)]
    if dy2[0] == dy2[1]: #Quadratic relationship
        repTiles = N//width
        leftover = repTiles - Ncheck + 1
        y, dy, dy2 = y[-1], dy[-1], dy2[-1]
        for _ in range(leftover):
            dy += dy2
            y += dy
    print(f"Part Two = {y}")

rocks, width = open_file(day)

part_one(64)
part_two()