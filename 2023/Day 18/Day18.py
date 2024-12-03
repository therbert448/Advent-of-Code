"""
Advent of Code
2023 Day 18

@author: Tom Herbert
"""

day = 18

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    digging = []
    for line in inputs:
        dire, num, colour = line.split()
        num = int(num)
        colour = colour.strip("()")
        digging.append([dire, num, colour])
    return digging

def get_direction_and_distance(line, partTwo):
    if not partTwo:
        direction, distance, _ = line
    else:
        _, _, hexString = line
        direction = list(dires.keys())[int(hexString[-1])]
        distance = int(hexString[1:-1], base=16)
    return direction, distance

def shoelace(digging, partTwo = False):
    x, y, area, perimeter = 0, 0, 0, 0
    for line in digging:
        dire, dist = get_direction_and_distance(line, partTwo)
        newx = x + (dires[dire][0] * dist)
        newy = y + (dires[dire][1] * dist)
        area += (x * newy) - (y * newx) #2x2 determinant
        perimeter += dist
        x, y = newx, newy
    return (abs(area)//2) + (perimeter//2) + 1

def part_one_and_two(digging):
    dug = shoelace(digging)
    print(f"Part One = {dug}")
    dug = shoelace(digging, True)
    print(f"Part Two = {dug}")

digging = open_file(day)

dires = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}

part_one_and_two(digging)