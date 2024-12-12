"""
Advent of Code
2024 Day 12

@author: Tom Herbert
"""
from time import time

day = 12

def open_file(day):
    #filename = "test3.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    plantTypes, allPlants = {}, set()
    for y, line in enumerate(inputs):
        for x, plant in enumerate(line):
            allPlants.add((x, y))
            if plant in plantTypes:
                plantTypes[plant].add((x, y))
            else:
                plantTypes[plant] = {(x, y)}
    return plantTypes, allPlants, x, y

def neighbours(coord):    
    neighs = [tuple(map(add, coord, step)) for step in steps]
    diags = [tuple(map(add, coord, step)) for step in diagSteps]
    return neighs, diags

add = lambda a, b: a + b
add3 = lambda a, b, c: a + b + c
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
diagSteps = [tuple(map(add, steps[i], steps[(i+1)%4])) for i in range(4)]

plantTypes, allPlants, xmax, ymax = open_file(day)
t0 = time()
regions = {}
for plant, plotSet in plantTypes.items():
    visited = set()
    regions[plant] = []
    for plot in plotSet:
        if plot in visited:
            continue
        group = {plot}
        visited.add(plot)
        current = [plot]
        while current:
            plot = current.pop()
            neighs, _ = neighbours(plot)
            for n in neighs:
                if n in group: continue
                if n in plotSet:
                    group.add(n)
                    visited.add(n)
                    current.append(n)
        regions[plant].append(group)

result = 0
for plant, regionList in regions.items():
    for region in regionList:
        area = len(region)
        perimeter = 0
        for plot in region:
            neighs, _ = neighbours(plot)
            for n in neighs:
                if n not in allPlants:
                    perimeter += 1
                elif n not in region:
                    perimeter += 1
        score = area * perimeter
        result += score
        #print(plant, score)
print(result)
t1 = time()
print(t1-t0)

result = 0
for plant, regionList in regions.items():
    for region in regionList:
        area = len(region)
        corners = 0
        for plot in region:
            neighs, diags = neighbours(plot)
            #print(plot, neighs, diags)
            sides = []
            for n in neighs:
                if n not in region:
                    sides.append(1)
                else:
                    sides.append(0)
            #print(plant, sides)
            if sum(sides) == 4:
                corners = 4
            elif sum(sides) == 3:
                corners += 2
            elif sum(sides) == 2:
                if sides[0] != sides[2]:
                    corners += 1
            if sum(sides) < 3:
                pairs = [[sides[i], sides[(i+1)%4]] for i in range(4)]
                for i, pair in enumerate(pairs):
                    if not any(pair):
                        if diags[i] not in region:
                            corners += 1
        perimeter = corners
        score = area * perimeter
        result += score
        #print(plant, area, perimeter, score)
print(result)
t2 = time()
print(t2-t1)