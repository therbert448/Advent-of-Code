"""
Advent of Code
2023 Day 23

@author: Tom Herbert

Slightly faster (~1 minute) solution that works out all the path permutations
before calculating the cost of each.
Improvements could be made by discarding the paths that visit the fewest junctions.
In this case the longest path visits 35 of the 36 junctions, with paths visiting all 36
being shorter.
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

def permutations(current, edges):
    paths = []
    pos = current[-1]
    if end in edges[pos]:
        paths.append(current + [end])
        return paths
    for nextJunc in edges[pos]:
        newCurrent = list(current)
        if nextJunc not in current:
            newCurrent.append(nextJunc)
            paths += permutations(newCurrent, edges)
    return paths

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

def path_score(path):
    steps = 0 
    for i in range(len(path)-1):
        steps += twoWay[path[i]][path[i+1]]
    return steps

def part_one_and_two(edges, part = "One"):
    current = [start]
    paths = permutations(current, edges)
    result = max(path_score(path) for path in paths)
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