"""
Advent of Code
2023 Day 16

@author: Tom Herbert
"""

day = 16

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    items = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char != ".":
                items[(x, y)] = char
    return items, [x, y]

def move(point):
    coords, dire = point
    newCoords = tuple(map(lambda a, b: a + b, coords, steps[dire]))
    x, y = newCoords
    if x < 0 or y < 0 or x > maxes[0] or y > maxes[1]:
        return []
    newPoints = [(newCoords, dire)]
    if newCoords in items:
        if items[newCoords] in mirrors:
            newDire = mirrors[items[newCoords]][dire]
            newPoints = [(newCoords, newDire)]
        elif dire in splitters[items[newCoords]][0]:
            newDires = splitters[items[newCoords]][1]
            newPoints = []
            for d in newDires:
                newPoints.append((newCoords, d))
    return newPoints

def run_light(start):
    energised = {}
    visited = set()
    current = {start,}
    while current:
        newCurrent = set()
        for point in current:
            newPoints = move(point)
            for p in newPoints:
                if p not in visited:
                    newCurrent.add(p)
                    visited.add(p)
                    coords, _ = p
                    if coords in energised:
                        energised[coords] += 1
                    else:
                        energised[coords] = 1
        current = newCurrent
    return energised

def part_one(start):
    energised = run_light(start)
    print(f"Part One = {len(energised)}")

def part_two():
    maxEnergised = 0
    for i in range(maxes[0]+1):
        starts = [((i, -1), "d"), ((i, maxes[0]+1), "u")]
        for start in starts:
            energised = run_light(start)
            if len(energised) > maxEnergised:
                maxEnergised = len(energised)
    for i in range(maxes[1]+1):
        starts = [((-1, i), "r"), ((maxes[1]+1, i), "l")]
        for start in starts:
            energised = run_light(start)
            if len(energised) > maxEnergised:
                maxEnergised = len(energised)
    print(f"Part Two = {maxEnergised}")

items, maxes = open_file(day)

mirrors = {"\\": {"r": "d", "d": "r", "u": "l", "l": "u"},
           "/": {"r": "u", "u": "r", "l": "d", "d": "l"}}
splitters = {"|": [("l", "r"), ("u", "d")],
             "-": [("u", "d"), ("l", "r")]}
steps = {"r": (1, 0), "d": (0, 1), "l": (-1, 0), "u": (0, -1)}

start = ((-1, 0), "r")

part_one(start)
part_two()