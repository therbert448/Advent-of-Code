"""
Advent of Code
2024 Day 18

@author: Tom Herbert
"""
from time import time

day = 18

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as f:
        byts = [[int(v) for v in l.strip().split(",")] for l in f.readlines()]
    return byts

def neighbours(coord):
    add = lambda a, b: a + b
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighs = [tuple(map(add, coord, step)) for step in steps]
    return neighs

byts = open_file(day)
start = (0, 0)
#N, xmax, ymax = 12, 6, 6
N, xmax, ymax = 1024, 70, 70
end = (xmax, ymax)

corrupted = [tuple(v for v in line) for line in byts[:N]]

Nsteps = 0
visited, current = {start: Nsteps}, {start}
ended = False
while not ended:
    newCurrent = set()
    Nsteps += 1
    for coord in current:
        if ended: break
        neighs = neighbours(coord)
        for n in neighs:
            if n == end:
                ended = True
                visited[n] = Nsteps
                break
            if n in corrupted:
                continue
            x, y = n
            if 0 <= x <= xmax and 0 <= y <= ymax:
                if n not in visited:
                    visited[n] = Nsteps
                    newCurrent.add(n)
    if not newCurrent: break
    current = set(v for v in newCurrent)
print(visited[end])

corrupted = [tuple(v for v in line) for line in byts]

impossible = True
while impossible:
    Nsteps = 0
    visited, current = {start: Nsteps}, {start}
    while current:
        newCurrent = set()
        Nsteps += 1
        for coord in current:
            neighs = neighbours(coord)
            for n in neighs:
                if n == end:
                    visited[n] = Nsteps
                    break
                if n in corrupted:
                    continue
                x, y = n
                if 0 <= x <= xmax and 0 <= y <= ymax:
                    if n not in visited:
                        visited[n] = Nsteps
                        newCurrent.add(n)
        if not newCurrent: break
        current = set(v for v in newCurrent)
    if end in visited: break
    lastDropped = corrupted.pop(-1)
print(str(lastDropped[0]) + "," + str(lastDropped[1]))