"""
Advent of Code
2023 Day 21

@author: Tom Herbert

After determining quadratic relationship (using Day 9 logic), use polyfit to
extrapolate the result.
Invert matrix and multiply matrix functions lifted from the algorithms I
developed for polyfitting at work
"""

day = 21

def open_file(day):
    #filename = "test.txt"
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

def run_steps(N, extend=False):
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

def invert_matrix(X):
    m = len(X)
    newX = [[val for val in line] for line in X]
    for i in range(m):
        line = [0] * m
        line[i] = 1
        newX[i] = newX[i] + line
    n = len(newX[0])
    for i in range(m):
        pivot = newX[i][i]
        for j in range(m):
            if j == i: continue
            scale = newX[j][i]/pivot
            for k in range(n):
                newX[j][k] = newX[j][k] - (scale * newX[i][k])
        scale = newX[i][i]
        for j in range(n):
            newX[i][j] = newX[i][j]/scale
    Xinv = [[val for val in line[m:]] for line in newX]
    return Xinv

def matrix_multiply(A, B):
    Am, An, Bn = len(A), len(A[0]), len(B[0])
    AB = [[sum([A[i][j] * B[j][k] for j in range(An)]) for k in range(Bn)] for i in range(Am)]
    return AB

def polyfit(repTiles, rem):
    y = [[run_steps(rem)], [run_steps(rem+width)], [run_steps(rem+(2*width))]]
    X = [[1, 0, 0], [1, 1, 1], [1, 2, 4]]
    Xinv = invert_matrix(X)
    c = matrix_multiply(Xinv, y)
    result = int(c[0][0] + c[1][0] * repTiles + c[2][0] * repTiles ** 2)
    return result

def part_one(N):
    global result
    result = run_steps(N)
    print(f"Part One = {result}")

def part_two(N = 26501365):
    repeatedTiles = N//width
    remainder = N % width
    result = polyfit(repeatedTiles, remainder)
    print(f"Part Two = {result}")

rocks, start, width = open_file(day)

part_one(64)
part_two()