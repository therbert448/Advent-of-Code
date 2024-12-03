"""
Advent of Code
2023 Day 21

@author: Tom Herbert

My initial approach, working out the tile variants and adding them together
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

def solve_steps(N):
    w = width
    start = (w//2, w//2)
    if N <= w:
        return steps(N, start, True)
    repTiles = N//w
    rem = N % w
    corners = [(w//2 + rem, (0, w//2)), (w//2 + rem, (w//2, 0)),
             (w//2 + rem, (w-1, w//2)), (w//2 + rem, (w//2, w-1))]
    odds = [(rem-1, (0, 0)), (rem-1, (w-1, w-1)), 
            (rem-1, (0, w-1)), (rem-1, (w-1, 0))]
    evens = [(w + rem - 1, (0, w-1)), (w + rem - 1, (w-1, 0)),
             (w + rem - 1, (0, 0)), (w + rem - 1, (w-1, w-1))]
    fullOdd, fullEven = steps(w, start), steps(w-1, start)
    cornerScores = [steps(*tup) for tup in corners]
    oddScores = [steps(*tup) for tup in odds]
    evenScores = [steps(*tup) for tup in evens]
    oddCounts = 1 + sum([i*4 for i in range(0, repTiles, 2)])
    evenCounts = sum([i*4 for i in range(1, repTiles, 2)])
    middle = fullEven * evenCounts + fullOdd * oddCounts
    cornerEdges = sum(cornerScores)
    oddEdges = repTiles * sum(oddScores)
    evenEdges = (repTiles-1)*sum(evenScores)
    return middle + cornerEdges + oddEdges + evenEdges

def part_one(N):
    start = (width//2, width//2)
    result = steps(N, start)
    print(f"Part One = {result}")

def part_two(N = 26501365):
    result = solve_steps(N)
    print(f"Part Two = {result}")

rocks, width = open_file(day)

part_one(64)
part_two()