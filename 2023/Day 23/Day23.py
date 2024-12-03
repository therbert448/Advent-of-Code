"""
Advent of Code
2023 Day 23

@author: Tom Herbert

Slower solution that does a BFS on all the possible junction to junction permutations.
Takes about 2 minutes and I can't think of a good way to prune the search.
I tried a DFS with some memoisation, but there were 10s of millions of states, making it less
efficient than the BFS, which is in the order of 100s of thousands of paths
"""

from time import time

day = 23

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    forest, slippery = set(), {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "#":
                forest.add((x, y))
            elif char in slopes:
                x2 = x + slopes[char][0]
                y2 = y + slopes[char][1]
                slippery[(x, y)] = (x2, y2)
            elif y == 0:
                start = (x, y)
    return forest, slippery, start, x+1, y+1

def neighbours(pos):
    x, y = pos
    moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    neighs = []
    for n in moves:
        if n[0] < 0 or n[1] < 0 or n[0] >= width or n[1] >= height:
            continue
        if n in forest:
            continue
        neighs.append(n)
    return neighs

def longest_path(edges):
    path = "(" + str(start[0]) + "," + str(start[1]) + ")"
    steps = 0
    state = (start, path, steps)
    current = [state]
    endSteps = 0
    while current:
        newCurrent = []
        for state in current:
            pos, path, steps = state
            if end in edges[pos]:
                nSteps = steps + edges[pos][end]
                if nSteps > endSteps:
                    endSteps = nSteps
                    continue
            for nextJunc, juncSteps in edges[pos].items():
                nString = "(" + str(nextJunc[0]) + "," + str(nextJunc[1]) + ")"
                if nString in path:
                    continue
                nSteps = steps + juncSteps
                newState = (nextJunc, path + nString, nSteps)
                newCurrent.append(newState)
        current = newCurrent
    return endSteps

def find_junctions():
    junctions = {start,}
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            if pos in forest:
                continue
            neighs = neighbours(pos)
            if len(neighs) > 2:
                junctions.add(pos)
            if y == height - 1:
                end = pos
                junctions.add(pos)
    return junctions, end
                
def one_way(junctions):
    edges = {}
    for start in junctions:
        edges[start] = {}
        path = "(" + str(start[0]) + "," + str(start[1]) + ")"
        current = [(start, path, 0)]
        while current:
            newCurrent = []
            for state in current:
                pos, path, steps = state
                neighs = neighbours(pos)
                for n in neighs:
                    nSteps = steps + 1
                    if n in slippery:
                        n = slippery[n]
                        nSteps += 1
                    nString = "(" + str(n[0]) + "," + str(n[1]) + ")"
                    if nString in path:
                        continue
                    if n in junctions:
                        if n not in edges[start] or edges[start][n] < nSteps:
                            edges[start][n] = nSteps
                            continue
                    newState = (n, path + nString, nSteps)
                    newCurrent.append(newState)
            current = newCurrent
    return edges

def two_way(edges):
    newEdges = {}
    for start in edges:
        if start not in newEdges:
            newEdges[start] = {}
        for end, steps in edges[start].items():
            if end not in newEdges:
                newEdges[end] = {}
            newEdges[start][end] = steps
            newEdges[end][start] = steps
    return newEdges

def part_one_and_two(edges, part = "One"):
    result = longest_path(edges)
    print(f"Part {part} = {result}")

t0 = time()

slopes = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}

forest, slippery, start, width, height = open_file(day)

junctions, end = find_junctions()
oneWay = one_way(junctions)
twoWay = two_way(oneWay)

part_one_and_two(oneWay)
t1 = time()
part_one_and_two(twoWay, "Two")
t2 = time()
print(f"Part One took {round(t1-t0,3)} seconds")
print(f"Part One took {round(t2-t1,3)} seconds")