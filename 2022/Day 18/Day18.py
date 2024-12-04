"""
Advent of Code
2022 Day 18

@author: Tom Herbert
"""

day = 18

def open_file():
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = file.readlines()
    return inputs

def format_data():
    global cubes
    cubes = set(tuple(int(v) for v in l.strip().split(",")) for l in inputs)

def find_surface_area(cubes, sides):
    for cube in cubes:
        sideCount = 6
        for i in range(len(cube)):
            for j in range(len(upDown)):
                coords = list(cube)
                coords[i] += upDown[j]
                nextCube = tuple(coords)
                if nextCube in cubes:
                    sideCount -= 1
        sides[cube] = sideCount

def check_inside(cube, toCheck):
    for i in range(len(cube)):
        for j in range(len(upDown)):
            coords = list(cube)
            coords[i] += upDown[j]
            nextCube = tuple(coords)
            if nextCube not in toCheck and nextCube not in cubes:
                return False
    return True               

def find_inside():
    global inside, minMax
    minMax = []
    for i in range(3):
        minMax.append([min(v[i] for v in cubes), max(v[i] for v in cubes)])
    inverseCubes = set()
    for x in range(minMax[0][0], minMax[0][1]+1):
        for y in range(minMax[1][0], minMax[1][1]+1):
            for z in range(minMax[2][0], minMax[2][1]+1):
                coords = (x, y, z)
                if coords not in cubes:
                    inverseCubes.add(coords)
    over = False
    toCheck = set(inverseCubes)
    while not over:
        over = True
        inside = set()
        for cube in toCheck:
            result = check_inside(cube, toCheck)
            if result:
                inside.add(cube)
            else:
                over = False
        toCheck = set(inside)

def part_one():
    global sides, totalSides
    sides = {}
    find_surface_area(cubes, sides)
    totalSides = sum(v for v in sides.values())
    print(f"Part One = {totalSides}")


def part_two():
    global insideSides
    insideSides = {}
    find_inside()
    find_surface_area(inside, insideSides)
    totalInside = sum(v for v in insideSides.values())
    print(f"Part Two = {totalSides - totalInside}")

inputs = open_file()

format_data()
upDown = [1, -1]

part_one()
part_two()