"""
Advent of Code
2024 Day 20

@author: Tom Herbert
"""
from time import time

day = 20

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        maze = [line.strip() for line in file.readlines()]
    walls, empty = set(), set()
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "S":
                start = (x, y)
                empty.add(start)
            elif char == "E":
                end = (x, y)
                empty.add(end)
            else:
                empty.add((x, y))
    return walls, empty, start, end, x, y

def neighbours(coord):
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighs = [tuple(map(add, coord, step)) for step in steps]
    return neighs
t0 = time()
walls, empty, start, end, xmax, ymax = open_file(day)
add = lambda a, b: a + b

Nsteps = 0
visited = {start: Nsteps}
current = {start}
while current:
    newCurrent = set()
    Nsteps += 1
    for coord in current:
        neighs = neighbours(coord)
        for n in neighs:
            if n == end and end not in visited:
                visited[end] = Nsteps
            if n in walls:
                continue
            elif n not in visited:
                visited[n] = Nsteps
                newCurrent.add(n)
    current = set(v for v in newCurrent)

cheats = {}
coords = sorted(list(visited.keys()))
for i, coord in enumerate(coords):
    x, y = coord
    for xi in range(3):
        for yi in range(3-xi):
            if xi + yi > 2: continue
            steps = [(xi, yi), (xi, -yi), (-xi, yi), (-xi, -yi)]
            nextCoords = [tuple(map(add, coord, step)) for step in steps]
            for n in nextCoords:
                if n not in visited: continue
                if visited[coord] < visited[n]:
                    first, second = coord, n
                else:
                    first, second = n, coord
                if (first, second) in cheats: continue
                saving = visited[second] - visited[first] - (xi + yi)
                if saving: cheats[(first, second)] = saving

result = sum([1 for val in cheats.values() if val >= 100])
print(result)
t1 = time()
print(f"...took {round(t1-t0, 6)}s\n")

coords = sorted(list(visited.keys()))
for i, coord in enumerate(coords):
    x, y = coord
    for xi in range(21):
        for yi in range(21-xi):
            if xi + yi > 20: continue
            steps = [(xi, yi), (xi, -yi), (-xi, yi), (-xi, -yi)]
            nextCoords = [tuple(map(add, coord, step)) for step in steps]
            for n in nextCoords:
                if n not in visited: continue
                if visited[coord] < visited[n]:
                    first, second = coord, n
                else:
                    first, second = n, coord
                if (first, second) in cheats: continue
                saving = visited[second] - visited[first] - (xi + yi)
                if saving: cheats[(first, second)] = saving

result = sum([1 for val in cheats.values() if val >= 100])
print(result)
t2 = time()
print(f"...took {round(t2-t1, 6)}s\n")